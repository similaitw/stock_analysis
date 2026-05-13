import { NextResponse } from "next/server";

import { listDailyAfterMarketScanCache } from "@/lib/after-market-scan-cache";

function todayInTaipei() {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Taipei",
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  }).format(new Date());
}

function normalizeDate(value: string | null) {
  if (!value) {
    return todayInTaipei();
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    throw new Error("date must use YYYY-MM-DD.");
  }
  return value;
}

function normalizeLimit(value: string | null) {
  if (!value) {
    return 100;
  }
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    throw new Error("limit must be a number.");
  }
  return Math.max(1, Math.min(200, Math.floor(parsed)));
}

export async function GET(request: Request) {
  try {
    const url = new URL(request.url);
    const date = normalizeDate(url.searchParams.get("date"));
    const limit = normalizeLimit(url.searchParams.get("limit"));
    const entries = await listDailyAfterMarketScanCache(date, limit);

    return NextResponse.json({
      date,
      entries
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    return NextResponse.json(
      {
        error: message,
        route: "after-market-screening/cache"
      },
      { status: message.includes("must") ? 400 : 500 }
    );
  }
}
