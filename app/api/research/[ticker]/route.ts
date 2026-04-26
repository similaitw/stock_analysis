import { NextResponse } from "next/server";

import { fetchResearchSnapshot } from "@/lib/research-data";

type RouteContext = {
  params: Promise<{
    ticker: string;
  }>;
};

export async function GET(_request: Request, context: RouteContext) {
  try {
    const { ticker } = await context.params;
    const payload = await fetchResearchSnapshot(ticker);
    return NextResponse.json(payload);
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
