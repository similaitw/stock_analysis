import { NextResponse } from "next/server";

import { hasSettingsAccess } from "@/lib/settings-auth";
import { createTradePlan, validateTradePlanInput } from "@/lib/trade-plans";

export async function POST(request: Request) {
  if (!(await hasSettingsAccess())) {
    return NextResponse.json({ error: "Unauthorized." }, { status: 401 });
  }

  try {
    const input = validateTradePlanInput(await request.json());
    const tradePlan = await createTradePlan(input);
    return NextResponse.json({ message: "TradePlan draft created.", tradePlan }, { status: 201 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unknown error";
    const status = message.includes("required")
      || message.includes("must be")
      || message.includes("Request body")
        ? 400
        : 500;

    return NextResponse.json({ error: message }, { status });
  }
}
