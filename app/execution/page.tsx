import { DataTable } from "@/components/data-table";
import { TradePlanDraftForm } from "@/components/trade-plan-draft-form";
import { getWorkspaceDashboardSnapshot } from "@/lib/workspace";

type WorkspaceRecord = Record<string, unknown>;

function asRecord(value: unknown): WorkspaceRecord | null {
  return value && typeof value === "object" && !Array.isArray(value) ? value as WorkspaceRecord : null;
}

function asRecordArray(value: unknown): WorkspaceRecord[] {
  return Array.isArray(value) ? value.map(asRecord).filter((item): item is WorkspaceRecord => Boolean(item)) : [];
}

function asString(value: unknown, fallback = "") {
  return value === null || value === undefined || value === "" ? fallback : String(value);
}

function asStringArray(value: unknown) {
  return Array.isArray(value) ? value.map((item) => String(item)).filter(Boolean) : [];
}

function buildTradePlanCandidates(snapshot: Awaited<ReturnType<typeof getWorkspaceDashboardSnapshot>>) {
  const latestScan = snapshot.afterMarketScans[0];
  const scanCandidates = latestScan
    ? [
        ...asRecordArray(latestScan.a_list),
        ...asRecordArray(latestScan.b_list),
        ...asRecordArray(latestScan.raw_results).slice(0, 6)
      ]
    : [];
  const existingPlanStocks = new Set(snapshot.tradePlans.map((plan) => asString(plan.stock_id)));
  const byStock = new Map<string, WorkspaceRecord>();

  for (const candidate of scanCandidates) {
    const stockId = asString(candidate.stockId ?? candidate.stock_id);
    if (!stockId || existingPlanStocks.has(stockId) || byStock.has(stockId)) {
      continue;
    }
    byStock.set(stockId, candidate);
  }

  return Array.from(byStock.entries()).slice(0, 8).map(([stockId, candidate]) => {
    const reasons = asStringArray(candidate.reasons).slice(0, 3);
    const risks = asStringArray(candidate.risks).slice(0, 3);
    return {
      stockId,
      stockName: asString(candidate.stockName ?? candidate.stock_name),
      strategyName: `after-market-${asString(latestScan?.profile, "balanced")}`,
      thesis: reasons.length > 0
        ? reasons.join("，")
        : "盤後掃描列入候選，需補研究與回測確認。",
      entryIdea: asString(candidate.nextDayPlan ?? candidate.next_day_plan, "觀察是否守住昨高與開盤低點。"),
      stopLoss: risks.length > 0 ? risks.join("，") : "跌破開盤低點或關鍵均線時取消。",
      tags: ["after-market", asString(latestScan?.profile, "balanced")].filter(Boolean),
      riskChecks: risks
    };
  });
}

export default async function ExecutionPage() {
  const snapshot = await getWorkspaceDashboardSnapshot();
  const tradePlanCandidates = buildTradePlanCandidates(snapshot);

  return (
    <main className="page-shell">
      <section className="page-hero">
        <p className="eyebrow">Execution</p>
        <h2>模擬執行</h2>
        <p>TradePlan 與 PaperOrder 已經能被 Next UI 讀取，後續可以把狀態操作逐步搬到 API routes。</p>
      </section>

      <TradePlanDraftForm candidates={tradePlanCandidates} />

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
