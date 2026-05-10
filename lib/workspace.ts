import { promises as fs } from "fs";
import path from "path";

type WorkspaceCollection =
  | "screen_runs"
  | "signal_events"
  | "backtest_runs"
  | "trade_plans"
  | "paper_orders"
  | "watchlists"
  | "research_notes"
  | "after_market_scans"
  | "next_day_watchlists";

type WorkspaceRecord = Record<string, unknown>;

const WORKSPACE_ROOT = path.join(process.cwd(), "data", "workspace");

const SORT_KEYS: Record<WorkspaceCollection, string> = {
  screen_runs: "executed_at",
  signal_events: "detected_at",
  backtest_runs: "executed_at",
  trade_plans: "updated_at",
  paper_orders: "updated_at",
  watchlists: "updated_at",
  research_notes: "updated_at",
  after_market_scans: "executed_at",
  next_day_watchlists: "created_at"
};

function normalizeRecord(value: unknown): WorkspaceRecord | null {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return null;
  }
  return value as WorkspaceRecord;
}

async function readJsonFile(filePath: string): Promise<WorkspaceRecord | null> {
  try {
    const raw = await fs.readFile(filePath, "utf-8");
    return normalizeRecord(JSON.parse(raw));
  } catch {
    return null;
  }
}

function compareDescending(left: WorkspaceRecord, right: WorkspaceRecord, key: string): number {
  const leftValue = String(left[key] ?? "");
  const rightValue = String(right[key] ?? "");
  return rightValue.localeCompare(leftValue);
}

export async function readWorkspaceCollection(
  collection: WorkspaceCollection,
  limit?: number
): Promise<WorkspaceRecord[]> {
  const dir = path.join(WORKSPACE_ROOT, collection);

  try {
    const entries = await fs.readdir(dir);
    const records = (
      await Promise.all(
        entries
          .filter((entry) => entry.endsWith(".json"))
          .map((entry) => readJsonFile(path.join(dir, entry)))
      )
    ).filter((record): record is WorkspaceRecord => Boolean(record));

    records.sort((left, right) => compareDescending(left, right, SORT_KEYS[collection]));
    return typeof limit === "number" ? records.slice(0, limit) : records;
  } catch {
    return [];
  }
}

export async function getWorkspaceDashboardSnapshot() {
  const [
    screenRuns,
    signalEvents,
    backtestRuns,
    tradePlans,
    paperOrders,
    watchlists,
    researchNotes,
    afterMarketScans,
    nextDayWatchlists
  ] = await Promise.all([
    readWorkspaceCollection("screen_runs"),
    readWorkspaceCollection("signal_events"),
    readWorkspaceCollection("backtest_runs"),
    readWorkspaceCollection("trade_plans"),
    readWorkspaceCollection("paper_orders"),
    readWorkspaceCollection("watchlists"),
    readWorkspaceCollection("research_notes"),
    readWorkspaceCollection("after_market_scans"),
    readWorkspaceCollection("next_day_watchlists")
  ]);

  const pendingOrders = paperOrders.filter((order) =>
    ["planned", "submitted"].includes(String(order.status ?? ""))
  ).length;

  return {
    counts: {
      screenRuns: screenRuns.length,
      signalEvents: signalEvents.length,
      backtestRuns: backtestRuns.length,
      tradePlans: tradePlans.length,
      paperOrders: paperOrders.length,
      pendingOrders,
      watchlists: watchlists.length,
      researchNotes: researchNotes.length,
      afterMarketScans: afterMarketScans.length,
      nextDayWatchlists: nextDayWatchlists.length
    },
    screenRuns: screenRuns.slice(0, 5),
    signalEvents: signalEvents.slice(0, 10),
    backtestRuns: backtestRuns.slice(0, 5),
    tradePlans: tradePlans.slice(0, 5),
    paperOrders: paperOrders.slice(0, 5),
    watchlists: watchlists.slice(0, 5),
    researchNotes: researchNotes.slice(0, 5),
    afterMarketScans: afterMarketScans.slice(0, 5),
    nextDayWatchlists: nextDayWatchlists.slice(0, 5)
  };
}
