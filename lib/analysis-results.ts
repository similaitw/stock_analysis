import { randomUUID } from "crypto";

import { Prisma } from "@prisma/client";
import postgres from "postgres";

import { prisma } from "@/lib/prisma";
import { readWorkspaceCollection } from "@/lib/workspace";

export type AnalysisResultDto = {
  id: string;
  kind: string;
  stockId: string;
  stockName: string | null;
  strategyName: string | null;
  title: string;
  summary: string;
  payload: Record<string, unknown> | null;
  tags: string[];
  source: string;
  createdAt: string;
  updatedAt: string;
  sourceKey: string | null;
};

export type CreateAnalysisResultInput = {
  kind: string;
  stockId: string;
  title: string;
  summary: string;
  stockName?: string;
  strategyName?: string;
  tags?: string[];
  payload?: Record<string, unknown> | null;
  source?: string;
  sourceKey?: string;
};

export type AnalysisStorageMode = "managed-database" | "local-file" | "readonly-fallback";

function getDatabaseUrl() {
  return process.env.DATABASE_URL ?? "";
}

export function getAnalysisStorageMode(): AnalysisStorageMode {
  const databaseUrl = getDatabaseUrl();

  if (!databaseUrl || databaseUrl.startsWith("file:")) {
    return process.env.VERCEL ? "readonly-fallback" : "local-file";
  }

  return "managed-database";
}

export function canWriteAnalysisResults() {
  return getAnalysisStorageMode() !== "readonly-fallback";
}

function buildStorageUnavailableError() {
  return new Error(
    "Analysis result storage is read-only in this deployment. Set a managed DATABASE_URL on Vercel to enable writes."
  );
}

function parsePayload(value: string | null): Record<string, unknown> | null {
  if (!value) {
    return null;
  }

  try {
    return JSON.parse(value) as Record<string, unknown>;
  } catch {
    return { raw: value };
  }
}

function parseTags(value: string | null): string[] {
  if (!value) {
    return [];
  }

  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function serializeTags(tags?: string[]) {
  return tags && tags.length > 0 ? tags.join(",") : null;
}

function mapAnalysisResult(
  record: Prisma.AnalysisResultGetPayload<Record<string, never>>
): AnalysisResultDto {
  return {
    id: record.id,
    kind: record.kind,
    stockId: record.stockId,
    stockName: record.stockName,
    strategyName: record.strategyName,
    title: record.title,
    summary: record.summary,
    payload: parsePayload(record.payload),
    tags: parseTags(record.tags),
    source: record.source,
    createdAt: record.createdAt.toISOString(),
    updatedAt: record.updatedAt.toISOString(),
    sourceKey: record.sourceKey
  };
}

type ManagedAnalysisRow = {
  id: string;
  kind: string;
  stock_id: string;
  stock_name: string | null;
  strategy_name: string | null;
  title: string;
  summary: string;
  payload: string | null;
  tags: string | null;
  source: string;
  created_at: Date | string;
  updated_at: Date | string;
  source_key: string | null;
};

let managedSchemaReady = false;
let managedSqlUrl = "";
let managedSql: ReturnType<typeof postgres> | null = null;

function getManagedSql() {
  const databaseUrl = getDatabaseUrl();
  if (!databaseUrl || databaseUrl.startsWith("file:")) {
    throw buildStorageUnavailableError();
  }
  if (!managedSql || managedSqlUrl !== databaseUrl) {
    managedSql = postgres(databaseUrl, {
      max: 1,
      prepare: false
    });
    managedSqlUrl = databaseUrl;
    managedSchemaReady = false;
  }
  return managedSql;
}

async function ensureManagedSchema() {
  if (managedSchemaReady) {
    return;
  }

  const sql = getManagedSql();
  await sql`
    CREATE TABLE IF NOT EXISTS analysis_results (
      id TEXT PRIMARY KEY,
      source_key TEXT UNIQUE,
      kind TEXT NOT NULL,
      stock_id TEXT NOT NULL,
      stock_name TEXT,
      strategy_name TEXT,
      title TEXT NOT NULL,
      summary TEXT NOT NULL,
      payload TEXT,
      tags TEXT,
      source TEXT NOT NULL DEFAULT 'next-ui',
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  managedSchemaReady = true;
}

function toIso(value: Date | string) {
  return value instanceof Date ? value.toISOString() : new Date(value).toISOString();
}

function mapManagedAnalysisResult(row: ManagedAnalysisRow): AnalysisResultDto {
  return {
    id: row.id,
    kind: row.kind,
    stockId: row.stock_id,
    stockName: row.stock_name,
    strategyName: row.strategy_name,
    title: row.title,
    summary: row.summary,
    payload: parsePayload(row.payload),
    tags: parseTags(row.tags),
    source: row.source,
    createdAt: toIso(row.created_at),
    updatedAt: toIso(row.updated_at),
    sourceKey: row.source_key
  };
}

async function listManagedAnalysisResults(limit: number): Promise<AnalysisResultDto[]> {
  await ensureManagedSchema();
  const sql = getManagedSql();
  const safeLimit = Math.max(1, Math.min(100, Math.floor(limit || 50)));
  const records = await sql`
    SELECT *
    FROM analysis_results
    ORDER BY created_at DESC
    LIMIT ${safeLimit}
  ` as ManagedAnalysisRow[];
  return records.map(mapManagedAnalysisResult);
}

async function createManagedAnalysisResult(input: CreateAnalysisResultInput): Promise<AnalysisResultDto> {
  await ensureManagedSchema();
  const sql = getManagedSql();
  const records = await sql`
    INSERT INTO analysis_results (
      id,
      source_key,
      kind,
      stock_id,
      stock_name,
      strategy_name,
      title,
      summary,
      payload,
      tags,
      source
    )
    VALUES (
      ${randomUUID()},
      ${input.sourceKey ?? null},
      ${input.kind},
      ${input.stockId},
      ${input.stockName ?? null},
      ${input.strategyName ?? null},
      ${input.title},
      ${input.summary},
      ${input.payload ? JSON.stringify(input.payload) : null},
      ${serializeTags(input.tags)},
      ${input.source ?? "next-ui"}
    )
    RETURNING *
  ` as ManagedAnalysisRow[];
  return mapManagedAnalysisResult(records[0]);
}

export async function listAnalysisResults(limit = 50): Promise<AnalysisResultDto[]> {
  if (getAnalysisStorageMode() === "readonly-fallback") {
    return [];
  }

  try {
    if (getAnalysisStorageMode() === "managed-database") {
      return listManagedAnalysisResults(limit);
    }

    const records = await prisma.analysisResult.findMany({
      orderBy: { createdAt: "desc" },
      take: limit
    });

    return records.map(mapAnalysisResult);
  } catch (error) {
    console.warn("Failed to list analysis results:", error);
    return [];
  }
}

export async function createAnalysisResult(
  input: CreateAnalysisResultInput
): Promise<AnalysisResultDto> {
  if (!canWriteAnalysisResults()) {
    throw buildStorageUnavailableError();
  }

  if (getAnalysisStorageMode() === "managed-database") {
    return createManagedAnalysisResult(input);
  }

  const record = await prisma.analysisResult.create({
    data: {
      sourceKey: input.sourceKey,
      kind: input.kind,
      stockId: input.stockId,
      stockName: input.stockName,
      strategyName: input.strategyName,
      title: input.title,
      summary: input.summary,
      payload: input.payload ? JSON.stringify(input.payload) : null,
      tags: serializeTags(input.tags),
      source: input.source ?? "next-ui"
    }
  });

  return mapAnalysisResult(record);
}

export async function importWorkspaceBacktests(): Promise<{
  imported: number;
  skipped: number;
}> {
  if (!canWriteAnalysisResults()) {
    throw buildStorageUnavailableError();
  }

  if (getAnalysisStorageMode() === "managed-database") {
    return { imported: 0, skipped: 0 };
  }

  const backtests = await readWorkspaceCollection("backtest_runs");
  let imported = 0;
  let skipped = 0;

  for (const record of backtests) {
    const sourceKey = `workspace:backtest:${String(record.id ?? "")}`;
    if (!String(record.id ?? "")) {
      skipped += 1;
      continue;
    }

    const existing = await prisma.analysisResult.findUnique({ where: { sourceKey } });
    if (existing) {
      skipped += 1;
      continue;
    }

    await prisma.analysisResult.create({
      data: {
        sourceKey,
        kind: "BACKTEST",
        stockId: String(record.stock_id ?? ""),
        stockName: record.stock_name ? String(record.stock_name) : null,
        strategyName: record.strategy_name ? String(record.strategy_name) : null,
        title: `${String(record.stock_id ?? "")} ${String(record.strategy_name ?? "Backtest")}`,
        summary: `Imported from workspace backtest run ${String(record.id)}`,
        payload: JSON.stringify(record),
        tags: serializeTags(["workspace", "backtest"]),
        source: "workspace-import"
      }
    });
    imported += 1;
  }

  return { imported, skipped };
}
