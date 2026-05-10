import { execFile } from "child_process";
import { existsSync } from "fs";
import path from "path";
import { promisify } from "util";

const execFileAsync = promisify(execFile);

export type XQIndicator = {
  id: string;
  name: string;
  category: "technical" | "chip";
  group: string;
  session: string;
  description: string;
  params: Record<string, number | string | boolean>;
  data_requirements: string[];
};

export type XQScanRequest = {
  name?: string;
  scanMode: "intraday" | "after_market";
  marketType: "TEST" | "Tw50" | "All";
  matchMode: "AND" | "OR";
  indicatorIds: string[];
  indicatorParams: Record<string, Record<string, number | string | boolean>>;
  stockList?: string[];
  maxStocks?: number;
};

export type XQScanResult = {
  screenRunId: string;
  executedAt: string;
  scanMode: string;
  marketType: string;
  matchMode: string;
  stockCount: number;
  resultCount: number;
  results: Array<Record<string, string | number | null>>;
};

const FALLBACK_INDICATORS: XQIndicator[] = [
  {
    id: "ma_bullish_alignment",
    name: "均線多頭排列",
    category: "technical",
    group: "趨勢",
    session: "after_market",
    description: "Close > MA5 > MA20 > MA60 的多頭排列條件。",
    params: {},
    data_requirements: ["OHLCV"]
  },
  {
    id: "volume_expansion",
    name: "成交量放大",
    category: "technical",
    group: "量能",
    session: "after_market",
    description: "今日量大於近 20 日均量倍數。",
    params: { multiplier: 1.5 },
    data_requirements: ["OHLCV"]
  },
  {
    id: "institutional_buying",
    name: "法人買超",
    category: "chip",
    group: "籌碼",
    session: "after_market",
    description: "法人籌碼偏多的基本條件。",
    params: { days: 3 },
    data_requirements: ["institutional"]
  }
];

function getPythonPath() {
  return path.join(process.cwd(), ".venv", "Scripts", "python.exe");
}

function getBridgeScriptPath() {
  return path.join(process.cwd(), "dev_tools", "next_bridge.py");
}

function isPythonBridgeAvailable() {
  return existsSync(getPythonPath()) && existsSync(getBridgeScriptPath());
}

function pythonBridgeUnavailableError() {
  return new Error(
    "XQ 條件掃描目前需要本機 Python bridge。雲端部署尚未接上可執行的掃描 worker，請先在本機執行，或部署前改接 managed backend。"
  );
}

async function runBridge<T>(command: string, payload?: unknown): Promise<T> {
  if (!isPythonBridgeAvailable()) {
    throw pythonBridgeUnavailableError();
  }

  const args = [getBridgeScriptPath(), command];
  if (payload !== undefined) {
    args.push(JSON.stringify(payload));
  }

  const { stdout, stderr } = await execFileAsync(getPythonPath(), args, {
    cwd: process.cwd(),
    timeout: 180000,
    maxBuffer: 20 * 1024 * 1024
  });

  if (stderr.trim()) {
    console.warn(stderr.trim());
  }

  const lines = stdout
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const jsonLine = lines.at(-1);

  if (!jsonLine) {
    throw new Error("Python bridge returned no JSON payload.");
  }

  const parsed = JSON.parse(jsonLine) as T & { error?: string };
  if (parsed.error) {
    throw new Error(parsed.error);
  }
  return parsed;
}

export async function listXQIndicators(): Promise<XQIndicator[]> {
  if (!isPythonBridgeAvailable()) {
    return FALLBACK_INDICATORS;
  }

  const payload = await runBridge<{ indicators: XQIndicator[] }>("xq_catalog");
  return payload.indicators;
}

export async function runXQScan(request: XQScanRequest): Promise<XQScanResult> {
  return runBridge<XQScanResult>("xq_scan", request);
}
