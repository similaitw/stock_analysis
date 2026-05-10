import { NextResponse } from "next/server";

import { runXQScan, type XQScanRequest } from "@/lib/xq-strategy";

export async function POST(request: Request) {
  try {
    const payload = (await request.json()) as XQScanRequest;
    const result = await runXQScan(payload);
    return NextResponse.json(result);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
