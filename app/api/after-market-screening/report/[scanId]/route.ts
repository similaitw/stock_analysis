import { NextResponse } from "next/server";

import { fetchAfterMarketReport } from "@/lib/after-market-screening";

type RouteContext = {
  params: Promise<{
    scanId: string;
  }>;
};

export async function GET(_request: Request, context: RouteContext) {
  try {
    const { scanId } = await context.params;
    if (!scanId || scanId.includes("/") || scanId.includes("\\")) {
      return NextResponse.json(
        {
          error: "scanId is required and must be a single path segment.",
          route: "after-market-screening/report"
        },
        { status: 400 }
      );
    }

    const result = await fetchAfterMarketReport(scanId);
    return NextResponse.json(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    let status = 500;
    if (message.includes("not found")) {
      status = 404;
    } else if (message.includes("Python bridge") || message.includes("managed backend")) {
      status = 503;
    }

    return NextResponse.json(
      {
        error: message,
        route: "after-market-screening/report"
      },
      { status }
    );
  }
}
