import { NextResponse } from "next/server";

import { runAfterMarketScan, type AfterMarketScanRequest } from "@/lib/after-market-screening";

function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function validatePayload(payload: unknown): AfterMarketScanRequest {
  if (!isPlainObject(payload)) {
    throw new Error("Request body must be a JSON object.");
  }

  const marketType = payload.marketType;
  if (typeof marketType !== "string" || !marketType.trim()) {
    throw new Error("marketType is required.");
  }

  const profile = payload.profile ?? "balanced";
  if (typeof profile !== "string" || !profile.trim()) {
    throw new Error("profile must be a string.");
  }

  if (payload.stockList !== undefined && !Array.isArray(payload.stockList)) {
    throw new Error("stockList must be an array of stock ids.");
  }

  if (payload.maxStocks !== undefined && typeof payload.maxStocks !== "number") {
    throw new Error("maxStocks must be a number.");
  }

  return {
    ...(payload as AfterMarketScanRequest),
    marketType: marketType as AfterMarketScanRequest["marketType"],
    profile: profile as AfterMarketScanRequest["profile"]
  };
}

export async function POST(request: Request) {
  try {
    const payload = validatePayload(await request.json());
    const result = await runAfterMarketScan(payload);
    return NextResponse.json(result);
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
