import { NextResponse } from "next/server";

import { getScanJob } from "@/lib/scan-jobs";

type RouteContext = {
  params: Promise<{
    jobId: string;
  }>;
};

export async function GET(_request: Request, context: RouteContext) {
  try {
    const { jobId } = await context.params;
    if (!jobId || jobId.includes("/") || jobId.includes("\\")) {
      return NextResponse.json({ error: "jobId must be a single path segment." }, { status: 400 });
    }

    const job = await getScanJob(jobId);
    if (!job) {
      return NextResponse.json({ error: "Scan job not found." }, { status: 404 });
    }

    return NextResponse.json({ job });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
