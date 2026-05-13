import { randomUUID } from "crypto";
import { promises as fs } from "fs";
import path from "path";

import { normalizeTaiwanStockCode } from "@/lib/taiwan-stock-names";

export type CreateTradePlanInput = {
  stockId: string;
  stockName?: string;
  strategyName?: string;
  intendedAction?: "BUY" | "SELL" | "WATCH";
  thesis: string;
  entryIdea: string;
  stopLoss: string;
  takeProfit?: string;
  sizeNote: string;
  riskChecks?: string[];
  tags?: string[];
};

export type TradePlanDto = {
  id: string;
  stock_id: string;
  stock_name: string;
  strategy_name: string;
  intended_action: string;
  thesis: string;
  entry_idea: string;
  stop_loss: string;
  take_profit: string;
  size_note: string;
  risk_checks: string[];
  tags: string[];
  status: string;
  created_at: string;
  updated_at: string;
};

const TRADE_PLAN_DIR = path.join(process.cwd(), "data", "workspace", "trade_plans");
const MAX_TEXT_LENGTH = 800;

function nowIso() {
  return new Date().toISOString();
}

function cleanText(value: unknown, maxLength = MAX_TEXT_LENGTH) {
  return String(value ?? "").trim().slice(0, maxLength);
}

function cleanList(value: unknown, maxItems = 8) {
  if (Array.isArray(value)) {
    return value.map((item) => cleanText(item, 80)).filter(Boolean).slice(0, maxItems);
  }
  return cleanText(value)
    .split(/[\n,，、]+/)
    .map((item) => item.trim())
    .filter(Boolean)
    .slice(0, maxItems);
}

export function validateTradePlanInput(payload: unknown): CreateTradePlanInput {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    throw new Error("Request body must be a JSON object.");
  }

  const record = payload as Record<string, unknown>;
  const stockId = normalizeTaiwanStockCode(cleanText(record.stockId));
  if (!/^\d{4,6}$/.test(stockId)) {
    throw new Error("stockId must be a Taiwan stock code.");
  }

  const intendedAction = cleanText(record.intendedAction || "BUY").toUpperCase();
  if (!["BUY", "SELL", "WATCH"].includes(intendedAction)) {
    throw new Error("intendedAction must be BUY, SELL, or WATCH.");
  }

  const thesis = cleanText(record.thesis);
  const entryIdea = cleanText(record.entryIdea);
  const stopLoss = cleanText(record.stopLoss);
  const sizeNote = cleanText(record.sizeNote);
  if (!thesis || !entryIdea || !stopLoss || !sizeNote) {
    throw new Error("thesis, entryIdea, stopLoss, and sizeNote are required.");
  }

  return {
    stockId,
    stockName: cleanText(record.stockName, 80),
    strategyName: cleanText(record.strategyName || "manual-decision", 120),
    intendedAction: intendedAction as CreateTradePlanInput["intendedAction"],
    thesis,
    entryIdea,
    stopLoss,
    takeProfit: cleanText(record.takeProfit),
    sizeNote,
    riskChecks: cleanList(record.riskChecks),
    tags: cleanList(record.tags)
  };
}

export async function createTradePlan(input: CreateTradePlanInput): Promise<TradePlanDto> {
  if (process.env.VERCEL) {
    throw new Error("TradePlan writes require a managed database on Vercel. Local workspace writes are disabled.");
  }

  const timestamp = nowIso();
  const id = `trade_plan_${timestamp.slice(0, 10).replaceAll("-", "")}_${randomUUID().slice(0, 8)}`;
  const tradePlan: TradePlanDto = {
    id,
    stock_id: input.stockId,
    stock_name: input.stockName ?? "",
    strategy_name: input.strategyName ?? "manual-decision",
    intended_action: input.intendedAction ?? "BUY",
    thesis: input.thesis,
    entry_idea: input.entryIdea,
    stop_loss: input.stopLoss,
    take_profit: input.takeProfit ?? "",
    size_note: input.sizeNote,
    risk_checks: input.riskChecks ?? [],
    tags: input.tags ?? [],
    status: "draft",
    created_at: timestamp,
    updated_at: timestamp
  };

  await fs.mkdir(TRADE_PLAN_DIR, { recursive: true });
  await fs.writeFile(
    path.join(TRADE_PLAN_DIR, `${id}.json`),
    JSON.stringify(tradePlan, null, 2),
    "utf-8"
  );
  return tradePlan;
}
