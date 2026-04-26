import { NextResponse } from "next/server";

import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export async function GET() {
  const snapshot = await getWorkspaceDashboardSnapshot();
  return NextResponse.json(snapshot);
}
