import { NextResponse } from "next/server";

import { listXQIndicators } from "@/lib/xq-strategy";

export async function GET() {
  try {
    const indicators = await listXQIndicators();
    return NextResponse.json({ indicators });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
}
