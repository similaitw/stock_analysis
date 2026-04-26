import { DataTable } from "@/components/data-table";
import { MetricCard } from "@/components/metric-card";
import { listAnalysisResults } from "@/lib/analysis-results";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export default async function ValidationPage() {
  const [snapshot, analysisResults] = await Promise.all([
    getWorkspaceDashboardSnapshot(),
    listAnalysisResults(10)
  ]);

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Validation</p>
        <h2>回測與驗證中心</h2>
        <p>BacktestRun 仍由 Python engine 產生，Next 版本目前負責瀏覽、匯入和後續資料庫保存。</p>
      </section>

      <section className="metric-grid">
        <MetricCard label="Workspace Backtests" value={snapshot.counts.backtestRuns} />
        <MetricCard label="Imported Analysis Results" value={analysisResults.length} />
      </section>

      <DataTable
        title="最近 Backtest Runs"
        rows={snapshot.backtestRuns.map((item) => ({
          股票: item.stock_id,
          策略: item.strategy_name,
          期間: item.period,
          最終資產: item.final_value,
          總報酬: item.total_return_pct,
          時間: item.executed_at
        }))}
        emptyMessage="目前沒有 backtest runs。"
      />
    </main>
  );
}
