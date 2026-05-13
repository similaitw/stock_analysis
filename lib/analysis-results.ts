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

export type BacktestMetrics = {
  period: string | null;
  totalReturnPct: number | null;
  benchmarkReturnPct: number | null;
  maxDrawdownPct: number | null;
  winRatePct: number | null;
  tradeCount: number;
  finalValue: number | null;
  startingCash: number | null;
  commissionRate: number | null;
};

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

function toNumber(value: unknown): number | null {
  if (typeof value === "number" && Number.isFinite(value)) {
    return value;
  }
  if (typeof value === "string" && value.trim() !== "") {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }
  return null;
}

function toRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : {};
}

function toArray(value: unknown): unknown[] {
  return Array.isArray(value) ? value : [];
}

function calculateMaxDrawdownPct(trades: unknown[]): number | null {
  const equityValues = trades
    .map((trade) => {
      const record = toRecord(trade);
      return toNumber(record.equity ?? record.portfolio_value ?? record.value ?? record.final_value);
    })
    .filter((value): value is number => value !== null);

  if (equityValues.length === 0) {
    return null;
  }

  let peak = equityValues[0];
  let maxDrawdown = 0;
  for (const value of equityValues) {
    peak = Math.max(peak, value);
    if (peak > 0) {
      maxDrawdown = Math.min(maxDrawdown, (value - peak) / peak);
    }
  }
  return Number((maxDrawdown * 100).toFixed(2));
}

function calculateWinRatePct(trades: unknown[]): number | null {
  const closedTrades = trades
    .map((trade) => toRecord(trade))
    .map((trade) => toNumber(trade.pnl ?? trade.profit ?? trade.return_pct ?? trade.returnPct))
    .filter((value): value is number => value !== null);

  if (closedTrades.length === 0) {
    return null;
  }

  const wins = closedTrades.filter((value) => value > 0).length;
  return Number(((wins / closedTrades.length) * 100).toFixed(2));
}

export function normalizeBacktestMetrics(record: Record<string, unknown>): BacktestMetrics {
  const trades = toArray(record.trades);

  return {
    period: record.period ? String(record.period) : null,
    totalReturnPct: toNumber(record.total_return_pct ?? record.totalReturnPct),
    benchmarkReturnPct: toNumber(record.benchmark_return_pct ?? record.benchmarkReturnPct),
    maxDrawdownPct: toNumber(record.max_drawdown_pct ?? record.maxDrawdownPct) ?? calculateMaxDrawdownPct(trades),
    winRatePct: toNumber(record.win_rate_pct ?? record.winRatePct) ?? calculateWinRatePct(trades),
    tradeCount: Math.max(0, Math.floor(toNumber(record.trade_count ?? record.tradeCount) ?? trades.length)),
    finalValue: toNumber(record.final_value ?? record.finalValue),
    startingCash: toNumber(record.starting_cash ?? record.startingCash),
    commissionRate: toNumber(record.commission_rate ?? record.commissionRate)
  };
}

function normalizeAnalysisPayload(input: CreateAnalysisResultInput) {
  const payload = input.payload ? { ...input.payload } : null;
  if (!payload) {
    return null;
  }

  if (input.kind.toLowerCase().includes("backtest") || input.tags?.includes("backtest")) {
    return {
      ...payload,
      backtestMetrics: normalizeBacktestMetrics(payload)
    };
  }

  return payload;
}

function buildBacktestSummary(metrics: BacktestMetrics, fallbackId: string) {
  const parts = [
    metrics.period ? `期間 ${metrics.period}` : null,
    metrics.totalReturnPct !== null ? `總報酬 ${metrics.totalReturnPct}%` : null,
    metrics.maxDrawdownPct !== null ? `最大回撤 ${metrics.maxDrawdownPct}%` : null,
    metrics.winRatePct !== null ? `勝率 ${metrics.winRatePct}%` : null,
    `交易 ${metrics.tradeCount} 筆`
  ].filter(Boolean);

  return parts.length > 0 ? parts.join(" / ") : `Imported from workspace backtest run ${fallbackId}`;
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
  const normalizedPayload = normalizeAnalysisPayload(input);
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
      ${normalizedPayload ? JSON.stringify(normalizedPayload) : null},
      ${serializeTags(input.tags)},
      ${input.source ?? "next-ui"}
    )
    RETURNING *
  ` as ManagedAnalysisRow[];
  return mapManagedAnalysisResult(records[0]);
}

async function findManagedAnalysisResultBySourceKey(sourceKey: string): Promise<AnalysisResultDto | null> {
  await ensureManagedSchema();
  const sql = getManagedSql();
  const records = await sql`
    SELECT *
    FROM analysis_results
    WHERE source_key = ${sourceKey}
    LIMIT 1
  ` as ManagedAnalysisRow[];
  return records[0] ? mapManagedAnalysisResult(records[0]) : null;
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

  const normalizedPayload = normalizeAnalysisPayload(input);
  const record = await prisma.analysisResult.create({
    data: {
      sourceKey: input.sourceKey,
      kind: input.kind,
      stockId: input.stockId,
      stockName: input.stockName,
      strategyName: input.strategyName,
      title: input.title,
      summary: input.summary,
      payload: normalizedPayload ? JSON.stringify(normalizedPayload) : null,
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

  const backtests = await readWorkspaceCollection("backtest_runs");
  let imported = 0;
  let skipped = 0;

  for (const record of backtests) {
    const sourceKey = `workspace:backtest:${String(record.id ?? "")}`;
    if (!String(record.id ?? "")) {
      skipped += 1;
      continue;
    }

    const existing = getAnalysisStorageMode() === "managed-database"
      ? await findManagedAnalysisResultBySourceKey(sourceKey)
      : await prisma.analysisResult.findUnique({ where: { sourceKey } });
    if (existing) {
      skipped += 1;
      continue;
    }

    const metrics = normalizeBacktestMetrics(record);
    await createAnalysisResult({
      sourceKey,
      kind: "BACKTEST",
      stockId: String(record.stock_id ?? ""),
      stockName: record.stock_name ? String(record.stock_name) : undefined,
      strategyName: record.strategy_name ? String(record.strategy_name) : undefined,
      title: `${String(record.stock_id ?? "")} ${String(record.strategy_name ?? "Backtest")}`,
      summary: buildBacktestSummary(metrics, String(record.id)),
      payload: {
        ...record,
        backtestMetrics: metrics
      },
      tags: ["workspace", "backtest"],
      source: "workspace-import"
    });
    imported += 1;
  }

  return { imported, skipped };
}
