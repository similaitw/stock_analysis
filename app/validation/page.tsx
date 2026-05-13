import { DataTable } from "@/components/data-table";
import { MetricCard } from "@/components/metric-card";
import { listAnalysisResults } from "@/lib/analysis-results";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

function asRecord(value: unknown): Record<string, unknown> | null {
  return value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;
}

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

      <DataTable
        title="已匯入 DB 的標準化回測"
        rows={analysisResults
          .filter((item) => item.kind.toLowerCase().includes("backtest") || item.tags.includes("backtest"))
          .map((item) => {
            const metrics = asRecord(item.payload?.backtestMetrics);
            return {
              股票: item.stockId,
              策略: item.strategyName,
              期間: metrics?.period ?? "-",
              總報酬: metrics?.totalReturnPct ?? "-",
              最大回撤: metrics?.maxDrawdownPct ?? "-",
              勝率: metrics?.winRatePct ?? "-",
              交易數: metrics?.tradeCount ?? "-",
              最終資產: metrics?.finalValue ?? "-",
              建立時間: item.createdAt
            };
          })}
        emptyMessage="目前沒有標準化回測資料。可到分析結果頁匯入 workspace backtests。"
      />
    </main>
  );
}
