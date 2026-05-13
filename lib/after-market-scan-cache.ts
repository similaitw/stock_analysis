import { createHash, randomUUID } from "crypto";
import { promises as fs } from "fs";
import path from "path";

import postgres from "postgres";

import { getAnalysisStorageMode } from "@/lib/analysis-results";
import type { AfterMarketScanRequest } from "@/lib/after-market-screening";

type CachedScanRow = {
  cache_key: string;
  scan_id: string;
  scan_date: string;
  market_type: string;
  profile: string;
  stock_count: number;
  request: Record<string, unknown> | string;
  result: Record<string, unknown> | string;
  created_at: Date | string;
  updated_at: Date | string;
};

export type DailyScanCacheEntry = {
  cacheKey: string;
  scanId: string;
  scanDate: string;
  marketType: string;
  profile: string;
  stockCount: number;
  result: Record<string, unknown>;
  createdAt: string;
  updatedAt: string;
  storageMode: "managed-database" | "local-file";
};

export type DailyScanCacheSummary = {
  scanId: string;
  scanDate: string;
  marketType: string;
  profile: string;
  stockCount: number;
  scanned: number;
  aList: number;
  bList: number;
  avoidList: number;
  skipped: number;
  createdAt: string;
  updatedAt: string;
  storageMode: DailyScanCacheEntry["storageMode"];
};

let schemaReady = false;
let cacheSqlUrl = "";
let cacheSql: ReturnType<typeof postgres> | null = null;

function todayInTaipei() {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Taipei",
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  }).format(new Date());
}

function getDatabaseUrl() {
  return process.env.DATABASE_URL ?? "";
}

function getSql() {
  const databaseUrl = getDatabaseUrl();
  if (getAnalysisStorageMode() !== "managed-database" || !databaseUrl || databaseUrl.startsWith("file:")) {
    throw new Error("Daily scan cache requires a managed DATABASE_URL.");
  }
  if (!cacheSql || cacheSqlUrl !== databaseUrl) {
    cacheSql = postgres(databaseUrl, {
      max: 1,
      prepare: false
    });
    cacheSqlUrl = databaseUrl;
    schemaReady = false;
  }
  return cacheSql;
}

async function ensureSchema() {
  if (schemaReady) {
    return;
  }

  const sql = getSql();
  await sql`
    CREATE TABLE IF NOT EXISTS after_market_scan_cache (
      cache_key TEXT PRIMARY KEY,
      scan_id TEXT NOT NULL,
      scan_date DATE NOT NULL,
      market_type TEXT NOT NULL,
      profile TEXT NOT NULL,
      stock_count INTEGER NOT NULL,
      request JSONB NOT NULL,
      result JSONB NOT NULL,
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    )
  `;
  await sql`
    CREATE INDEX IF NOT EXISTS after_market_scan_cache_scan_id_idx
    ON after_market_scan_cache (scan_id)
  `;
  await sql`
    CREATE INDEX IF NOT EXISTS after_market_scan_cache_scan_date_idx
    ON after_market_scan_cache (scan_date)
  `;
  schemaReady = true;
}

function normalizeStockIds(stockList?: string[]) {
  return Array.from(
    new Set(
      (stockList ?? [])
        .map((item) => item.trim().toUpperCase().replace(/\.(TW|TWO)$/, ""))
        .filter((item) => /^\d{4,6}$/.test(item))
    )
  ).sort((left, right) => left.localeCompare(right, "en-US"));
}

function normalizeWeights(weights: AfterMarketScanRequest["weights"]) {
  return {
    technical: weights?.technical ?? 40,
    chip: weights?.chip ?? 30,
    volume: weights?.volume ?? 15,
    relativeStrength: weights?.relativeStrength ?? 15
  };
}

export function buildDailyScanCacheDescriptor(request: AfterMarketScanRequest) {
  const stockIds = normalizeStockIds(request.stockList);
  const scanDate = request.date ?? todayInTaipei();
  const descriptor = {
    date: scanDate,
    marketType: request.marketType,
    profile: request.profile,
    maxStocks: Math.max(1, Math.min(2000, Math.floor(request.maxStocks ?? 80))),
    includeRiskList: request.includeRiskList !== false,
    weights: normalizeWeights(request.weights),
    stockIds
  };
  const cacheKey = createHash("sha256").update(JSON.stringify(descriptor)).digest("hex");
  return {
    cacheKey,
    scanDate,
    stockIds,
    descriptor
  };
}

function parseRecord(value: Record<string, unknown> | string | null): Record<string, unknown> {
  if (!value) {
    return {};
  }
  if (typeof value !== "string") {
    return value;
  }
  try {
    const parsed = JSON.parse(value);
    return parsed && typeof parsed === "object" && !Array.isArray(parsed) ? parsed as Record<string, unknown> : {};
  } catch {
    return {};
  }
}

function toIso(value: Date | string) {
  return value instanceof Date ? value.toISOString() : new Date(value).toISOString();
}

function toDateOnly(value: Date | string) {
  return value instanceof Date ? value.toISOString().slice(0, 10) : String(value).slice(0, 10);
}

function mapRow(row: CachedScanRow, storageMode: DailyScanCacheEntry["storageMode"]): DailyScanCacheEntry {
  return {
    cacheKey: row.cache_key,
    scanId: row.scan_id,
    scanDate: toDateOnly(row.scan_date),
    marketType: row.market_type,
    profile: row.profile,
    stockCount: row.stock_count,
    result: parseRecord(row.result),
    createdAt: toIso(row.created_at),
    updatedAt: toIso(row.updated_at),
    storageMode
  };
}

function getArrayCount(result: Record<string, unknown>, camelKey: string, snakeKey: string) {
  const value = result[camelKey] ?? result[snakeKey];
  return Array.isArray(value) ? value.length : 0;
}

function getCounts(result: Record<string, unknown>) {
  const counts = parseRecord(result.counts as Record<string, unknown> | string | null);
  return {
    scanned: Number(counts.scanned ?? getArrayCount(result, "rawResults", "raw_results") ?? 0),
    aList: Number(counts.aList ?? getArrayCount(result, "aList", "a_list") ?? 0),
    bList: Number(counts.bList ?? getArrayCount(result, "bList", "b_list") ?? 0),
    avoidList: Number(counts.avoidList ?? getArrayCount(result, "avoidList", "avoid_list") ?? 0),
    skipped: Number(counts.skipped ?? (Array.isArray(result.skipped) ? result.skipped.length : 0))
  };
}

function toSummary(entry: DailyScanCacheEntry): DailyScanCacheSummary {
  const counts = getCounts(entry.result);
  return {
    scanId: entry.scanId,
    scanDate: entry.scanDate,
    marketType: entry.marketType,
    profile: entry.profile,
    stockCount: entry.stockCount,
    scanned: Number.isFinite(counts.scanned) ? counts.scanned : 0,
    aList: Number.isFinite(counts.aList) ? counts.aList : 0,
    bList: Number.isFinite(counts.bList) ? counts.bList : 0,
    avoidList: Number.isFinite(counts.avoidList) ? counts.avoidList : 0,
    skipped: Number.isFinite(counts.skipped) ? counts.skipped : 0,
    createdAt: entry.createdAt,
    updatedAt: entry.updatedAt,
    storageMode: entry.storageMode
  };
}

function getLocalCacheDir() {
  return path.join(process.cwd(), "data", "workspace", "after_market_scan_cache");
}

function getLocalCachePath(cacheKey: string) {
  return path.join(getLocalCacheDir(), `${cacheKey}.json`);
}

async function readLocalCache(cacheKey: string): Promise<DailyScanCacheEntry | null> {
  try {
    const raw = await fs.readFile(getLocalCachePath(cacheKey), "utf-8");
    const parsed = JSON.parse(raw) as DailyScanCacheEntry;
    return {
      ...parsed,
      storageMode: "local-file"
    };
  } catch {
    return null;
  }
}

async function writeLocalCache(
  request: AfterMarketScanRequest,
  result: Record<string, unknown>
): Promise<DailyScanCacheEntry> {
  const { cacheKey, scanDate, stockIds, descriptor } = buildDailyScanCacheDescriptor(request);
  const now = new Date().toISOString();
  const entry: DailyScanCacheEntry = {
    cacheKey,
    scanId: String(result.scanId ?? `local_cache_${scanDate}_${randomUUID()}`),
    scanDate,
    marketType: request.marketType,
    profile: request.profile,
    stockCount: stockIds.length || Math.max(1, Math.min(2000, Math.floor(request.maxStocks ?? 80))),
    result: {
      ...result,
      request_payload: descriptor
    },
    createdAt: now,
    updatedAt: now,
    storageMode: "local-file"
  };

  await fs.mkdir(getLocalCacheDir(), { recursive: true });
  await fs.writeFile(getLocalCachePath(cacheKey), JSON.stringify(entry, null, 2), "utf-8");
  return entry;
}

export async function getCachedDailyAfterMarketScan(
  request: AfterMarketScanRequest
): Promise<DailyScanCacheEntry | null> {
  const { cacheKey } = buildDailyScanCacheDescriptor(request);

  if (getAnalysisStorageMode() === "managed-database") {
    await ensureSchema();
    const sql = getSql();
    const rows = await sql`
      SELECT *
      FROM after_market_scan_cache
      WHERE cache_key = ${cacheKey}
      LIMIT 1
    ` as CachedScanRow[];
    return rows[0] ? mapRow(rows[0], "managed-database") : null;
  }

  if (getAnalysisStorageMode() === "readonly-fallback") {
    return null;
  }

  return readLocalCache(cacheKey);
}

export async function getCachedDailyAfterMarketReport(scanId: string): Promise<DailyScanCacheEntry | null> {
  if (!scanId || scanId.includes("/") || scanId.includes("\\")) {
    return null;
  }

  if (getAnalysisStorageMode() === "managed-database") {
    await ensureSchema();
    const sql = getSql();
    const rows = await sql`
      SELECT *
      FROM after_market_scan_cache
      WHERE scan_id = ${scanId}
      ORDER BY updated_at DESC
      LIMIT 1
    ` as CachedScanRow[];
    return rows[0] ? mapRow(rows[0], "managed-database") : null;
  }

  if (getAnalysisStorageMode() === "readonly-fallback") {
    return null;
  }

  try {
    const files = await fs.readdir(getLocalCacheDir());
    for (const file of files.filter((item) => item.endsWith(".json"))) {
      const raw = await fs.readFile(path.join(getLocalCacheDir(), file), "utf-8");
      const parsed = JSON.parse(raw) as DailyScanCacheEntry;
      if (parsed.scanId === scanId) {
        return {
          ...parsed,
          storageMode: "local-file"
        };
      }
    }
  } catch {
    return null;
  }

  return null;
}

export async function listDailyAfterMarketScanCache(
  scanDate = todayInTaipei(),
  limit = 100
): Promise<DailyScanCacheSummary[]> {
  const safeLimit = Math.max(1, Math.min(200, Math.floor(limit || 100)));

  if (getAnalysisStorageMode() === "managed-database") {
    await ensureSchema();
    const sql = getSql();
    const rows = await sql`
      SELECT *
      FROM after_market_scan_cache
      WHERE scan_date = ${scanDate}
      ORDER BY updated_at DESC
      LIMIT ${safeLimit}
    ` as CachedScanRow[];
    return rows.map((row) => toSummary(mapRow(row, "managed-database")));
  }

  if (getAnalysisStorageMode() === "readonly-fallback") {
    return [];
  }

  try {
    const files = await fs.readdir(getLocalCacheDir());
    const entries = await Promise.all(
      files
        .filter((item) => item.endsWith(".json"))
        .map(async (file) => {
          const raw = await fs.readFile(path.join(getLocalCacheDir(), file), "utf-8");
          return JSON.parse(raw) as DailyScanCacheEntry;
        })
    );
    return entries
      .filter((entry) => entry.scanDate === scanDate)
      .map((entry) => toSummary({ ...entry, storageMode: "local-file" }))
      .sort((left, right) => right.updatedAt.localeCompare(left.updatedAt))
      .slice(0, safeLimit);
  } catch {
    return [];
  }
}

export async function rememberDailyAfterMarketScan(
  request: AfterMarketScanRequest,
  result: Record<string, unknown>
): Promise<DailyScanCacheEntry | null> {
  const { cacheKey, scanDate, stockIds, descriptor } = buildDailyScanCacheDescriptor(request);

  if (getAnalysisStorageMode() === "managed-database") {
    await ensureSchema();
    const sql = getSql();
    const scanId = String(result.scanId ?? `db_cache_${scanDate}_${randomUUID()}`);
    const stockCount = stockIds.length || Number((result.counts as Record<string, unknown> | undefined)?.scanned ?? 0);
    const cachedResult = {
      ...result,
      scanId,
      request_payload: descriptor
    };
    const rows = await sql`
      INSERT INTO after_market_scan_cache (
        cache_key,
        scan_id,
        scan_date,
        market_type,
        profile,
        stock_count,
        request,
        result
      )
      VALUES (
        ${cacheKey},
        ${scanId},
        ${scanDate},
        ${request.marketType},
        ${request.profile},
        ${stockCount},
        ${JSON.stringify(descriptor)}::jsonb,
        ${JSON.stringify(cachedResult)}::jsonb
      )
      ON CONFLICT (cache_key)
      DO UPDATE SET
        scan_id = EXCLUDED.scan_id,
        stock_count = EXCLUDED.stock_count,
        request = EXCLUDED.request,
        result = EXCLUDED.result,
        updated_at = NOW()
      RETURNING *
    ` as CachedScanRow[];
    return mapRow(rows[0], "managed-database");
  }

  if (getAnalysisStorageMode() === "readonly-fallback") {
    return null;
  }

  return writeLocalCache(request, result);
}
