import { NextResponse } from "next/server";

import { createScanJob, listScanJobs, type CreateScanJobInput } from "@/lib/scan-jobs";

function isPlainObject(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function validatePayload(payload: unknown): CreateScanJobInput {
  if (!isPlainObject(payload)) {
    throw new Error("Request body must be a JSON object.");
  }

  const type = payload.type;
  if (type !== "after-market" && type !== "xq") {
    throw new Error("type must be after-market or xq.");
  }

  if (!isPlainObject(payload.request)) {
    throw new Error("request must be a JSON object.");
  }

  return {
    type,
    request: payload.request as CreateScanJobInput["request"]
  };
}

export async function GET(request: Request) {
  try {
    const url = new URL(request.url);
    const limit = Number(url.searchParams.get("limit") ?? 20);
    const jobs = await listScanJobs(limit);
    return NextResponse.json({ jobs });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  try {
    const job = await createScanJob(validatePayload(await request.json()));
    return NextResponse.json({ message: "Scan job queued.", job }, { status: 201 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    const status = message.includes("must be") || message.includes("Request body") ? 400 : 500;
    return NextResponse.json({ error: message }, { status });
  }
}
