import { AnalysisResultsClient } from "@/components/analysis-results-client";
import { DataTable } from "@/components/data-table";
import { listAnalysisResults } from "@/lib/analysis-results";

function asRecord(value: unknown): Record<string, unknown> | null {
  return value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;
}

export default async function AnalysisResultsPage() {
  const analysisResults = await listAnalysisResults(50);

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Database</p>
        <h2>分析結果資料庫</h2>
        <p>這裡使用 Prisma + SQLite 保存整理過的分析結果，讓原本的 workspace JSON 能逐步過渡到資料庫。</p>
      </section>

      <AnalysisResultsClient initialCount={analysisResults.length} />

      <DataTable
        title="Analysis Results"
        rows={analysisResults.map((item) => {
          const metrics = asRecord(item.payload?.backtestMetrics);
          return {
            類型: item.kind,
            股票: item.stockId,
            股票名稱: item.stockName,
            策略: item.strategyName,
            標題: item.title,
            總報酬: metrics?.totalReturnPct ?? "-",
            最大回撤: metrics?.maxDrawdownPct ?? "-",
            勝率: metrics?.winRatePct ?? "-",
            交易數: metrics?.tradeCount ?? "-",
            標籤: item.tags.join(", "),
            建立時間: item.createdAt
          };
        })}
        emptyMessage="資料庫中尚無分析結果。"
      />
    </main>
  );
}
