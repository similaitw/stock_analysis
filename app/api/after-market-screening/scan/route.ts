import { NextResponse } from "next/server";

import {
  getCachedDailyAfterMarketScan,
  rememberDailyAfterMarketScan
} from "@/lib/after-market-scan-cache";
import { runAfterMarketScan, type AfterMarketScanRequest } from "@/lib/after-market-screening";

function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function normalizeStockList(value: unknown): string[] | undefined {
  if (value === undefined) {
    return undefined;
  }
  if (!Array.isArray(value)) {
    throw new Error("stockList must be an array of stock ids.");
  }

  const stockList = Array.from(
    new Set(
      value
        .map((item) => String(item).trim().toUpperCase().replace(/\.(TW|TWO)$/, ""))
        .filter((item) => /^\d{4,6}$/.test(item))
    )
  );
  if (stockList.length === 0) {
    throw new Error("stockList must include at least one valid stock id.");
  }
  if (stockList.length > 2000) {
    throw new Error("stockList cannot exceed 2000 stocks.");
  }
  return stockList;
}

function normalizeMaxStocks(value: unknown) {
  if (value === undefined) {
    return undefined;
  }
  if (typeof value !== "number" || !Number.isFinite(value)) {
    throw new Error("maxStocks must be a number.");
  }
  return Math.max(1, Math.min(2000, Math.floor(value)));
}

function validatePayload(payload: unknown): AfterMarketScanRequest {
  if (!isPlainObject(payload)) {
    throw new Error("Request body must be a JSON object.");
  }

  const marketType = payload.marketType;
  if (!["TEST", "Tw50", "All", "TSE", "OTC", "Custom"].includes(String(marketType))) {
    throw new Error("marketType must be TEST, Tw50, All, TSE, OTC, or Custom.");
  }

  const profile = payload.profile ?? "balanced";
  if (!["conservative", "balanced", "aggressive"].includes(String(profile))) {
    throw new Error("profile must be conservative, balanced, or aggressive.");
  }

  const stockList = normalizeStockList(payload.stockList);
  const maxStocks = normalizeMaxStocks(payload.maxStocks);

  return {
    ...(payload as AfterMarketScanRequest),
    marketType: marketType as AfterMarketScanRequest["marketType"],
    profile: profile as AfterMarketScanRequest["profile"],
    stockList,
    maxStocks
  };
}

export async function POST(request: Request) {
  try {
    const payload = validatePayload(await request.json());
    const cached = await getCachedDailyAfterMarketScan(payload);
    if (cached) {
      return NextResponse.json({
        ...cached.result,
        cache: {
          status: "hit",
          storageMode: cached.storageMode,
          cachedAt: cached.updatedAt,
          key: cached.cacheKey
        }
      });
    }

    const result = await runAfterMarketScan(payload);
    const stored = await rememberDailyAfterMarketScan(payload, result as unknown as Record<string, unknown>);
    return NextResponse.json({
      ...result,
      cache: {
        status: "miss",
        storageMode: stored?.storageMode ?? "unavailable",
        cachedAt: stored?.updatedAt,
        key: stored?.cacheKey
      }
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    let status = 500;
    if (message.includes("Request body") || message.includes("required") || message.includes("must be")) {
      status = 400;
    } else if (message.includes("Python bridge") || message.includes("managed backend")) {
      status = 503;
    }

    return NextResponse.json(
      {
        error: message,
        route: "after-market-screening/scan"
      },
      { status }
    );
  }
}
