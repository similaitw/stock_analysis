import { randomUUID } from "crypto";

import postgres from "postgres";

import { runAfterMarketScan, type AfterMarketScanRequest } from "@/lib/after-market-screening";
import { getAnalysisStorageMode } from "@/lib/analysis-results";
import { runXQScan, type XQScanRequest } from "@/lib/xq-strategy";

export type ScanJobType = "after-market" | "xq";
export type ScanJobStatus = "queued" | "running" | "completed" | "failed";

export type CreateScanJobInput = {
  type: ScanJobType;
  request: AfterMarketScanRequest | XQScanRequest;
};

export type ScanJobDto = {
  id: string;
  type: ScanJobType;
  status: ScanJobStatus;
  request: Record<string, unknown>;
  result: Record<string, unknown> | null;
  error: string | null;
  createdAt: string;
  startedAt: string | null;
  finishedAt: string | null;
};

type ScanJobRow = {
  id: string;
  type: ScanJobType;
  status: ScanJobStatus;
  request: string | Record<string, unknown>;
  result: string | Record<string, unknown> | null;
  error: string | null;
  created_at: Date | string;
  started_at: Date | string | null;
  finished_at: Date | string | null;
};

let scanJobsSchemaReady = false;
let scanJobsSqlUrl = "";
let scanJobsSql: ReturnType<typeof postgres> | null = null;

function getDatabaseUrl() {
  return process.env.DATABASE_URL ?? "";
}

function getScanJobsSql() {
  const databaseUrl = getDatabaseUrl();
  if (getAnalysisStorageMode() !== "managed-database" || !databaseUrl || databaseUrl.startsWith("file:")) {
    throw new Error("Scan jobs require a managed DATABASE_URL.");
  }
  if (!scanJobsSql || scanJobsSqlUrl !== databaseUrl) {
    scanJobsSql = postgres(databaseUrl, {
      max: 1,
      prepare: false
    });
    scanJobsSqlUrl = databaseUrl;
    scanJobsSchemaReady = false;
  }
  return scanJobsSql;
}

async function ensureScanJobsSchema() {
  if (scanJobsSchemaReady) {
    return;
  }

  const sql = getScanJobsSql();
  await sql`
    CREATE TABLE IF NOT EXISTS scan_jobs (
      id TEXT PRIMARY KEY,
      type TEXT NOT NULL,
      status TEXT NOT NULL,
      request JSONB NOT NULL,
      result JSONB,
      error TEXT,
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      started_at TIMESTAMPTZ,
      finished_at TIMESTAMPTZ
    )
  `;
  await sql`
    CREATE INDEX IF NOT EXISTS scan_jobs_status_created_at_idx
    ON scan_jobs (status, created_at)
  `;
  scanJobsSchemaReady = true;
}

function parseJsonObject(value: string | Record<string, unknown> | null): Record<string, unknown> | null {
  if (!value) {
    return null;
  }
  if (typeof value !== "string") {
    return !Array.isArray(value) ? value : null;
  }
  try {
    const parsed = JSON.parse(value);
    return parsed && typeof parsed === "object" && !Array.isArray(parsed) ? parsed as Record<string, unknown> : null;
  } catch {
    return { raw: value };
  }
}

function toIso(value: Date | string | null) {
  return value ? (value instanceof Date ? value.toISOString() : new Date(value).toISOString()) : null;
}

function mapScanJob(row: ScanJobRow): ScanJobDto {
  return {
    id: row.id,
    type: row.type,
    status: row.status,
    request: parseJsonObject(row.request) ?? {},
    result: parseJsonObject(row.result),
    error: row.error,
    createdAt: toIso(row.created_at)!,
    startedAt: toIso(row.started_at),
    finishedAt: toIso(row.finished_at)
  };
}

export async function createScanJob(input: CreateScanJobInput): Promise<ScanJobDto> {
  await ensureScanJobsSchema();
  const sql = getScanJobsSql();
  const rows = await sql`
    INSERT INTO scan_jobs (id, type, status, request)
    VALUES (${randomUUID()}, ${input.type}, 'queued', ${JSON.stringify(input.request)}::jsonb)
    RETURNING *
  ` as ScanJobRow[];
  return mapScanJob(rows[0]);
}

export async function listScanJobs(limit = 20): Promise<ScanJobDto[]> {
  await ensureScanJobsSchema();
  const sql = getScanJobsSql();
  const safeLimit = Math.max(1, Math.min(100, Math.floor(limit || 20)));
  const rows = await sql`
    SELECT *
    FROM scan_jobs
    ORDER BY created_at DESC
    LIMIT ${safeLimit}
  ` as ScanJobRow[];
  return rows.map(mapScanJob);
}

export async function getScanJob(jobId: string): Promise<ScanJobDto | null> {
  await ensureScanJobsSchema();
  const sql = getScanJobsSql();
  const rows = await sql`
    SELECT *
    FROM scan_jobs
    WHERE id = ${jobId}
    LIMIT 1
  ` as ScanJobRow[];
  return rows[0] ? mapScanJob(rows[0]) : null;
}

async function claimNextQueuedJob(): Promise<ScanJobDto | null> {
  await ensureScanJobsSchema();
  const sql = getScanJobsSql();
  const rows = await sql`
    UPDATE scan_jobs
    SET status = 'running', started_at = NOW(), error = NULL
    WHERE id = (
      SELECT id
      FROM scan_jobs
      WHERE status = 'queued'
      ORDER BY created_at ASC
      LIMIT 1
    )
    RETURNING *
  ` as ScanJobRow[];
  return rows[0] ? mapScanJob(rows[0]) : null;
}

async function completeScanJob(jobId: string, result: Record<string, unknown>) {
  const sql = getScanJobsSql();
  const rows = await sql`
    UPDATE scan_jobs
    SET status = 'completed', result = ${JSON.stringify(result)}::jsonb, finished_at = NOW()
    WHERE id = ${jobId}
    RETURNING *
  ` as ScanJobRow[];
  return mapScanJob(rows[0]);
}

async function failScanJob(jobId: string, error: string) {
  const sql = getScanJobsSql();
  const rows = await sql`
    UPDATE scan_jobs
    SET status = 'failed', error = ${error}, finished_at = NOW()
    WHERE id = ${jobId}
    RETURNING *
  ` as ScanJobRow[];
  return mapScanJob(rows[0]);
}

async function runJob(job: ScanJobDto): Promise<Record<string, unknown>> {
  if (job.type === "after-market") {
    return await runAfterMarketScan(job.request as AfterMarketScanRequest) as unknown as Record<string, unknown>;
  }
  if (job.type === "xq") {
    return await runXQScan(job.request as XQScanRequest) as unknown as Record<string, unknown>;
  }
  throw new Error(`Unsupported scan job type: ${job.type}`);
}

export async function processNextScanJob(): Promise<ScanJobDto | null> {
  const job = await claimNextQueuedJob();
  if (!job) {
    return null;
  }

  try {
    const result = await runJob(job);
    return completeScanJob(job.id, result);
  } catch (error) {
    return failScanJob(job.id, error instanceof Error ? error.message : "Unknown scan job failure");
  }
}
