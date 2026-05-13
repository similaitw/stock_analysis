import { promises as fs } from "fs";
import path from "path";

import { DataTable } from "@/components/data-table";
import {
  AfterMarketScreeningWorkbench,
  type RecentAfterMarketScan
} from "@/components/after-market-screening-workbench";
import { XQStrategyWorkbench } from "@/components/xq-strategy-workbench";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";
import { listXQIndicators } from "@/lib/xq-strategy";
import { getAfterMarketStockCategories, getAfterMarketStockOptions } from "@/lib/stock-universe";
import { listDailyAfterMarketScanCache } from "@/lib/after-market-scan-cache";

export const dynamic = "force-dynamic";

const AFTER_MARKET_SCAN_DIR = path.join(process.cwd(), "data", "workspace", "after_market_scans");

type StoredAfterMarketScan = {
  id?: string;
  date?: string;
  executed_at?: string;
  market_scope?: string;
  profile?: string;
  counts?: {
    scanned?: number;
    aList?: number;
    bList?: number;
    avoidList?: number;
  };
};

function normalizeRecentAfterMarketScan(value: unknown): RecentAfterMarketScan | null {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return null;
  }

  const scan = value as StoredAfterMarketScan;
  if (!scan.id) {
    return null;
  }

  return {
    id: scan.id,
    date: scan.date,
    executedAt: scan.executed_at,
    marketScope: scan.market_scope,
    profile: scan.profile,
    scanned: scan.counts?.scanned,
    aList: scan.counts?.aList,
    bList: scan.counts?.bList,
    avoidList: scan.counts?.avoidList
  };
}

async function getRecentAfterMarketScans(): Promise<RecentAfterMarketScan[]> {
  try {
    const files = await fs.readdir(AFTER_MARKET_SCAN_DIR);
    const scans = await Promise.all(
      files
        .filter((file) => file.endsWith(".json"))
        .map(async (file) => {
          try {
            const raw = await fs.readFile(path.join(AFTER_MARKET_SCAN_DIR, file), "utf-8");
            return normalizeRecentAfterMarketScan(JSON.parse(raw));
          } catch {
            return null;
          }
        })
    );

    return scans
      .filter((scan): scan is RecentAfterMarketScan => Boolean(scan))
      .sort((left, right) => String(right.executedAt ?? "").localeCompare(String(left.executedAt ?? "")))
      .slice(0, 5);
  } catch {
    return [];
  }
}

export default async function StrategyPage() {
  const [snapshot, indicators, recentAfterMarketScans, stockCategories, stockOptions, dailyCacheEntries] = await Promise.all([
    getWorkspaceDashboardSnapshot(),
    listXQIndicators(),
    getRecentAfterMarketScans(),
    getAfterMarketStockCategories(),
    getAfterMarketStockOptions(),
    listDailyAfterMarketScanCache()
  ]);

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Strategy</p>
        <h2>XQ 模組化策略工作台</h2>
        <p>技術指標、籌碼指標與既有掃描紀錄整合在同一個策略頁，支援盤中與盤後條件組合。</p>
      </section>

      <XQStrategyWorkbench indicators={indicators} />

      <AfterMarketScreeningWorkbench
        recentScans={recentAfterMarketScans}
        stockCategories={stockCategories}
        stockOptions={stockOptions}
        initialCacheEntries={dailyCacheEntries}
      />

      <DataTable
        title="最近每日盤後篩選"
        rows={snapshot.afterMarketScans.map((item) => ({
          ScanID: item.id,
          日期: item.date,
          股票池: item.market_scope,
          模式: item.profile,
          掃描: (item.counts as Record<string, unknown> | undefined)?.scanned ?? 0,
          A級: (item.counts as Record<string, unknown> | undefined)?.aList ?? 0,
          B級: (item.counts as Record<string, unknown> | undefined)?.bList ?? 0,
          避開: (item.counts as Record<string, unknown> | undefined)?.avoidList ?? 0,
          時間: item.executed_at
        }))}
        emptyMessage="目前沒有每日盤後篩選紀錄。"
      />

      <DataTable
        title="最近隔日監控名單"
        rows={snapshot.nextDayWatchlists.map((item) => ({
          名單ID: item.id,
          來源Scan: item.source_scan_id,
          交易日: item.trade_date,
          股票數: Array.isArray(item.stocks) ? item.stocks.length : 0,
          建立時間: item.created_at
        }))}
        emptyMessage="目前沒有隔日監控名單。"
      />

      <DataTable
        title="最近 Screen Runs"
        rows={snapshot.screenRuns.map((item) => ({
          名稱: item.name,
          市場: item.market_scope,
          模式: item.match_mode,
          命中數: item.result_count,
          時間: item.executed_at
        }))}
        emptyMessage="目前沒有保存的 screen runs。"
      />

      <DataTable
        title="最近 Signal Events"
        rows={snapshot.signalEvents.map((item) => ({
          股票: item.stock_id,
          名稱: item.stock_name,
          原因: item.reason,
          時間: item.detected_at
        }))}
        emptyMessage="目前沒有 signal events。"
      />
    </main>
  );
}
