import { Prisma } from "@prisma/client";

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

export async function listAnalysisResults(limit = 50): Promise<AnalysisResultDto[]> {
  if (getAnalysisStorageMode() === "readonly-fallback") {
    return [];
  }

  try {
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
