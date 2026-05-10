import { execFile } from "child_process";
import { existsSync } from "fs";
import path from "path";
import { promisify } from "util";

import { getCachedCloudAfterMarketReport, runCloudAfterMarketScan } from "@/lib/after-market-cloud";

const execFileAsync = promisify(execFile);

export type AfterMarketProfile = "conservative" | "balanced" | "aggressive";
export type AfterMarketMarketType = "TEST" | "Tw50" | "All" | "TSE" | "OTC" | "Custom";

export type AfterMarketWeights = {
  technical: number;
  chip: number;
  volume: number;
  relativeStrength: number;
};

export type AfterMarketScanRequest = {
  date?: string;
  marketType: AfterMarketMarketType;
  stockList?: string[];
  profile: AfterMarketProfile;
  maxStocks?: number;
  includeRiskList?: boolean;
  weights?: Partial<AfterMarketWeights>;
};

export type AfterMarketScreeningItem = {
  stockId: string;
  stockName: string;
  score: number;
  riskScore: number;
  rank?: number;
  technicalScore?: number;
  chipScore?: number;
  volumeScore?: number;
  relativeStrengthScore?: number;
  reasons: string[];
  risks: string[];
  nextDayPlan?: string;
  skipReason?: string;
};

export type AfterMarketScanResult = {
  scanId: string;
  executedAt: string;
  marketType: string;
  counts: {
    scanned: number;
    aList: number;
    bList: number;
    avoidList: number;
    skipped?: number;
  };
  aList: AfterMarketScreeningItem[];
  bList?: AfterMarketScreeningItem[];
  avoidList: AfterMarketScreeningItem[];
  skipped?: Array<Pick<AfterMarketScreeningItem, "stockId" | "stockName" | "skipReason">>;
  summary?: Record<string, unknown>;
};

export type AfterMarketReportResult = AfterMarketScanResult & {
  rawResults?: unknown;
  nextDayWatchlist?: unknown;
};

type BridgeErrorPayload = {
  error?: string;
};

function getPythonPath() {
  return path.join(process.cwd(), ".venv", "Scripts", "python.exe");
}

function getBridgeScriptPath() {
  return path.join(process.cwd(), "dev_tools", "next_bridge.py");
}

function isPythonBridgeAvailable() {
  if (process.env.STOCK_ANALYSIS_FORCE_CLOUD_SCANNER === "1") {
    return false;
  }
  return existsSync(getPythonPath()) && existsSync(getBridgeScriptPath());
}

function parseBridgeJson<T>(stdout: string): T {
  const lines = stdout
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const jsonLine = lines.at(-1);

  if (!jsonLine) {
    throw new Error("Python bridge returned no JSON payload.");
  }

  const parsed = JSON.parse(jsonLine) as T & BridgeErrorPayload;
  if (parsed.error) {
    throw new Error(parsed.error);
  }
  return parsed;
}

async function runBridge<T>(command: string, payload?: unknown): Promise<T> {
  const args = [getBridgeScriptPath(), command];
  if (payload !== undefined) {
    args.push(typeof payload === "string" ? payload : JSON.stringify(payload));
  }

  try {
    const { stdout, stderr } = await execFileAsync(getPythonPath(), args, {
      cwd: process.cwd(),
      timeout: 240000,
      maxBuffer: 30 * 1024 * 1024
    });

    if (stderr.trim()) {
      console.warn(stderr.trim());
    }

    return parseBridgeJson<T>(stdout);
  } catch (error) {
    const bridgeError = error as Error & { stdout?: string; stderr?: string };
    if (bridgeError.stderr?.trim()) {
      console.warn(bridgeError.stderr.trim());
    }
    if (bridgeError.stdout) {
      return parseBridgeJson<T>(bridgeError.stdout);
    }
    throw error;
  }
}

export async function runAfterMarketScan(
  request: AfterMarketScanRequest
): Promise<AfterMarketScanResult> {
  if (!isPythonBridgeAvailable()) {
    return runCloudAfterMarketScan(request);
  }

  return runBridge<AfterMarketScanResult>("after_market_scan", request);
}

export async function fetchAfterMarketReport(scanId: string): Promise<AfterMarketReportResult> {
  if (!isPythonBridgeAvailable()) {
    const report = getCachedCloudAfterMarketReport(scanId);
    if (report) {
      return report;
    }
    throw new Error("Cloud after-market report not found. Run a new scan to refresh the report cache.");
  }

  return runBridge<AfterMarketReportResult>("after_market_report", scanId);
}
