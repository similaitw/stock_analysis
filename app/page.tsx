import { AnalysisResultsClient } from "@/components/analysis-results-client";
import { DataTable } from "@/components/data-table";
import { MetricCard } from "@/components/metric-card";
import { listAnalysisResults } from "@/lib/analysis-results";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export default async function HomePage() {
  const [snapshot, analysisResults] = await Promise.all([
    getWorkspaceDashboardSnapshot(),
    listAnalysisResults(5)
  ]);

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Migration Overview</p>
        <h2>Next.js front-end 已接管主 UI 殼層</h2>
        <p>
          目前前端已改成 App Router。Python 分析核心與 workspace JSON 仍保留，並額外加入
          Prisma + SQLite 來保存分析結果。
        </p>
      </section>

      <section className="metric-grid">
        <MetricCard label="Screen Runs" value={snapshot.counts.screenRuns} />
        <MetricCard label="Signals" value={snapshot.counts.signalEvents} />
        <MetricCard label="Backtests" value={snapshot.counts.backtestRuns} />
        <MetricCard label="After-Market Scans" value={snapshot.counts.afterMarketScans} />
        <MetricCard label="Trade Plans" value={snapshot.counts.tradePlans} />
        <MetricCard label="Pending Orders" value={snapshot.counts.pendingOrders} />
        <MetricCard label="DB Analysis Results" value={analysisResults.length} />
      </section>

      <section className="grid-two">
        <DataTable
          title="最近 Screen Runs"
          rows={snapshot.screenRuns.map((item) => ({
            名稱: item.name,
            市場: item.market_scope,
            命中數: item.result_count,
            時間: item.executed_at
          }))}
          emptyMessage="目前沒有 screen runs。"
        />
        <DataTable
          title="最近每日盤後篩選"
          rows={snapshot.afterMarketScans.map((item) => ({
            日期: item.date,
            股票池: item.market_scope,
            掃描: (item.counts as Record<string, unknown> | undefined)?.scanned ?? 0,
            A級: (item.counts as Record<string, unknown> | undefined)?.aList ?? 0,
            B級: (item.counts as Record<string, unknown> | undefined)?.bList ?? 0,
            避開: (item.counts as Record<string, unknown> | undefined)?.avoidList ?? 0,
            時間: item.executed_at
          }))}
          emptyMessage="目前沒有每日盤後篩選紀錄。"
        />
        <DataTable
          title="最近 Backtests"
          rows={snapshot.backtestRuns.map((item) => ({
            股票: item.stock_id,
            策略: item.strategy_name,
            總報酬: item.total_return_pct,
            時間: item.executed_at
          }))}
          emptyMessage="目前沒有 backtest runs。"
        />
      </section>

      <AnalysisResultsClient initialCount={analysisResults.length} />

      <DataTable
        title="資料庫中的分析結果"
        rows={analysisResults.map((item) => ({
          類型: item.kind,
          股票: item.stockId,
          標題: item.title,
          來源: item.source,
          時間: item.createdAt
        }))}
        emptyMessage="資料庫裡還沒有分析結果。"
      />
    </main>
  );
}
