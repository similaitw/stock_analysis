import { NextResponse } from "next/server";

import { processNextScanJob } from "@/lib/scan-jobs";

function isAuthorized(request: Request) {
  const secret = process.env.SCAN_JOBS_SECRET ?? process.env.CRON_SECRET ?? "";
  if (!secret) {
    return true;
  }

  const header = request.headers.get("authorization") ?? "";
  return header === `Bearer ${secret}`;
}

export async function POST(request: Request) {
  if (!isAuthorized(request)) {
    return NextResponse.json({ error: "Unauthorized." }, { status: 401 });
  }

  try {
    const job = await processNextScanJob();
    if (!job) {
      return NextResponse.json({ message: "No queued scan jobs.", job: null });
    }
    return NextResponse.json({ message: "Scan job processed.", job });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
