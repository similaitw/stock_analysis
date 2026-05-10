import { NextResponse } from "next/server";

import { runXQScan, type XQScanRequest } from "@/lib/xq-strategy";

export async function POST(request: Request) {
  try {
    const payload = (await request.json()) as XQScanRequest;
    const result = await runXQScan(payload);
    return NextResponse.json(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    const status = message.includes("Python bridge") || message.includes("managed backend") ? 503 : 500;

    return NextResponse.json(
      { error: message },
      { status }
    );
  }
}
