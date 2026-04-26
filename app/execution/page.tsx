import { DataTable } from "@/components/data-table";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export default async function ExecutionPage() {
  const snapshot = await getWorkspaceDashboardSnapshot();

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Execution</p>
        <h2>模擬執行</h2>
        <p>TradePlan 與 PaperOrder 已經能被 Next UI 讀取，後續可以把狀態操作逐步搬到 API routes。</p>
      </section>

      <section className="grid-two">
        <DataTable
          title="Trade Plans"
          rows={snapshot.tradePlans.map((item) => ({
            股票: item.stock_id,
            策略: item.strategy_name,
            狀態: item.status,
            更新時間: item.updated_at
          }))}
          emptyMessage="目前沒有 trade plans。"
        />
        <DataTable
          title="Paper Orders"
          rows={snapshot.paperOrders.map((item) => ({
            股票: item.stock_id,
            方向: item.side,
            狀態: item.status,
            數量: item.quantity,
            更新時間: item.updated_at
          }))}
          emptyMessage="目前沒有 paper orders。"
        />
      </section>
    </main>
  );
}
