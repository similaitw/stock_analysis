import { DataTable } from "@/components/data-table";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export default async function StrategyPage() {
  const snapshot = await getWorkspaceDashboardSnapshot();

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Strategy</p>
        <h2>策略工作流視圖</h2>
        <p>這個頁面先讀取既有 workspace JSON，讓 Next 前端能接手策略工作台的結果展示與交接。</p>
      </section>

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
