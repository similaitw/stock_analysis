import { DataTable } from "@/components/data-table";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

export default async function CollaborationPage() {
  const snapshot = await getWorkspaceDashboardSnapshot();

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Collaboration</p>
        <h2>協作與交接</h2>
        <p>共享 watchlist、研究筆記與 workspace 歷史都可以直接在 Next UI 讀取，方便之後接多人或資料庫化。</p>
      </section>

      <section className="grid-two">
        <DataTable
          title="Watchlists"
          rows={snapshot.watchlists.map((item) => ({
            名稱: item.name,
            持有人: item.owner,
            股票數: Array.isArray(item.stocks) ? item.stocks.length : 0,
            更新時間: item.updated_at
          }))}
          emptyMessage="目前沒有 watchlists。"
        />
        <DataTable
          title="Research Notes"
          rows={snapshot.researchNotes.map((item) => ({
            標題: item.title,
            股票: item.stock_id,
            作者: item.author,
            更新時間: item.updated_at
          }))}
          emptyMessage="目前沒有研究筆記。"
        />
      </section>
    </main>
  );
}
