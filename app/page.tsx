import Link from "next/link";

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
        <p className="eyebrow">Start Here</p>
        <h2>今天要看什麼股票，從這裡開始</h2>
        <p>
          這個網站會幫你先找候選、再檢查風險，最後整理是否值得進入個股分析。新手先照三步驟操作，不需要先懂所有專有名詞。
        </p>
      </section>

      <section className="home-guide-panel">
        <div className="home-guide-title">
          <p className="eyebrow">Beginner Flow</p>
          <h2>新手操作流程</h2>
        </div>
        <div className="home-guide-steps">
          <Link href="/beginner-guide">
            <span>1</span>
            <strong>先看新手教學</strong>
            <small>理解 A 級、B 級、避開名單代表什麼。</small>
          </Link>
          <Link href="/strategy">
            <span>2</span>
            <strong>做策略掃描</strong>
            <small>用台灣50或分類策略掃描，掃完會自動 cache。</small>
          </Link>
          <Link href="/investor">
            <span>3</span>
            <strong>看投資決策</strong>
            <small>確認今天要研究、觀察或避開哪些股票。</small>
          </Link>
        </div>
      </section>

      <section className="metric-grid">
        <MetricCard label="策略掃描紀錄" value={snapshot.counts.screenRuns} />
        <MetricCard label="訊號事件" value={snapshot.counts.signalEvents} />
        <MetricCard label="回測紀錄" value={snapshot.counts.backtestRuns} />
        <MetricCard label="盤後篩選" value={snapshot.counts.afterMarketScans} />
        <MetricCard label="交易計畫" value={snapshot.counts.tradePlans} />
        <MetricCard label="待處理委託" value={snapshot.counts.pendingOrders} />
        <MetricCard label="分析結果" value={analysisResults.length} />
      </section>

      <section className="grid-two">
        <DataTable
          title="最近策略掃描"
          rows={snapshot.screenRuns.map((item) => ({
            名稱: item.name,
            市場: item.market_scope,
            命中數: item.result_count,
            時間: item.executed_at
          }))}
          emptyMessage="目前沒有策略掃描。先到策略頁執行「分類策略組合掃描」。"
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
          emptyMessage="目前沒有每日盤後篩選紀錄。先到策略頁按「台灣50」或「全部股票」開始。"
        />
        <DataTable
          title="最近回測"
          rows={snapshot.backtestRuns.map((item) => ({
            股票: item.stock_id,
            策略: item.strategy_name,
            總報酬: item.total_return_pct,
            時間: item.executed_at
          }))}
          emptyMessage="目前沒有回測。先有候選股後，再補回測檢查風險。"
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
