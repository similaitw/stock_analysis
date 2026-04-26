import { NextRequest, NextResponse } from "next/server";

import {
  canWriteAnalysisResults,
  createAnalysisResult,
  listAnalysisResults
} from "@/lib/analysis-results";

export async function GET() {
  const results = await listAnalysisResults();
  return NextResponse.json(results);
}

export async function POST(request: NextRequest) {
  if (!canWriteAnalysisResults()) {
    return NextResponse.json(
      { error: "This deployment is read-only until a managed DATABASE_URL is configured." },
      { status: 503 }
    );
  }

  try {
    const body = (await request.json()) as {
      kind?: string;
      stockId?: string;
      stockName?: string;
      strategyName?: string;
      title?: string;
      summary?: string;
      tags?: string[];
      payload?: Record<string, unknown>;
    };

    if (!body.kind || !body.stockId || !body.title || !body.summary) {
      return NextResponse.json(
        { error: "kind, stockId, title, summary are required." },
        { status: 400 }
      );
    }

    const created = await createAnalysisResult({
      kind: body.kind,
      stockId: body.stockId,
      stockName: body.stockName,
      strategyName: body.strategyName,
      title: body.title,
      summary: body.summary,
      tags: body.tags,
      payload: body.payload ?? null,
      source: "next-ui"
    });

    return NextResponse.json({ message: "Analysis result created.", result: created }, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
