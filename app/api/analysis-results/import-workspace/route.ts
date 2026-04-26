import { NextResponse } from "next/server";

import { canWriteAnalysisResults, importWorkspaceBacktests } from "@/lib/analysis-results";

export async function POST() {
  if (!canWriteAnalysisResults()) {
    return NextResponse.json(
      { error: "This deployment is read-only until a managed DATABASE_URL is configured." },
      { status: 503 }
    );
  }

  try {
    const result = await importWorkspaceBacktests();
    return NextResponse.json(result);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
