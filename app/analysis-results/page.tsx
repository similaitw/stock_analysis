import { AnalysisResultsClient } from "@/components/analysis-results-client";
import { DataTable } from "@/components/data-table";
import { listAnalysisResults } from "@/lib/analysis-results";

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
        rows={analysisResults.map((item) => ({
          類型: item.kind,
          股票: item.stockId,
          股票名稱: item.stockName,
          策略: item.strategyName,
          標題: item.title,
          標籤: item.tags.join(", "),
          建立時間: item.createdAt
        }))}
        emptyMessage="資料庫中尚無分析結果。"
      />
    </main>
  );
}
