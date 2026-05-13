"use client";

import { useMemo, useState } from "react";

type CandidateOption = {
  stockId: string;
  stockName: string;
  strategyName: string;
  thesis: string;
  entryIdea: string;
  stopLoss: string;
  tags: string[];
  riskChecks: string[];
};

type TradePlanDraftFormProps = {
  candidates: CandidateOption[];
};

const EMPTY_CANDIDATE: CandidateOption = {
  stockId: "",
  stockName: "",
  strategyName: "manual-decision",
  thesis: "",
  entryIdea: "",
  stopLoss: "",
  tags: [],
  riskChecks: []
};

export function TradePlanDraftForm({ candidates }: TradePlanDraftFormProps) {
  const [selectedStockId, setSelectedStockId] = useState(candidates[0]?.stockId ?? "");
  const selectedCandidate = useMemo(
    () => candidates.find((candidate) => candidate.stockId === selectedStockId) ?? EMPTY_CANDIDATE,
    [candidates, selectedStockId]
  );
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function submitTradePlan(formData: FormData) {
    setMessage("");
    setError("");
    setIsSubmitting(true);

    try {
      const response = await fetch("/api/trade-plans", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          stockId: String(formData.get("stockId") ?? ""),
          stockName: String(formData.get("stockName") ?? ""),
          strategyName: String(formData.get("strategyName") ?? ""),
          intendedAction: String(formData.get("intendedAction") ?? "BUY"),
          thesis: String(formData.get("thesis") ?? ""),
          entryIdea: String(formData.get("entryIdea") ?? ""),
          stopLoss: String(formData.get("stopLoss") ?? ""),
          takeProfit: String(formData.get("takeProfit") ?? ""),
          sizeNote: String(formData.get("sizeNote") ?? ""),
          riskChecks: String(formData.get("riskChecks") ?? ""),
          tags: String(formData.get("tags") ?? "")
        })
      });
      const payload = await response.json().catch(() => null) as { message?: string; error?: string } | null;
      if (!response.ok) {
        throw new Error(payload?.error ?? `TradePlan API 回應 ${response.status}`);
      }
      setMessage(payload?.message ?? "TradePlan draft created.");
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : "建立 TradePlan 失敗。");
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section className="panel trade-plan-builder">
      <div className="panel-header">
        <div>
          <p className="eyebrow">Execution Intake</p>
          <h2>候選轉 TradePlan 草稿</h2>
        </div>
        <span>{candidates.length} 檔候選</span>
      </div>

      <form key={selectedStockId || "manual"} action={submitTradePlan} className="stack-form">
        <div className="form-grid">
          <label>
            候選股票
            <select
              value={selectedStockId}
              onChange={(event) => setSelectedStockId(event.target.value)}
            >
              <option value="">手動輸入</option>
              {candidates.map((candidate) => (
                <option key={candidate.stockId} value={candidate.stockId}>
                  {candidate.stockId} {candidate.stockName}
                </option>
              ))}
            </select>
          </label>
          <label>
            股票名稱
            <input name="stockName" defaultValue={selectedCandidate.stockName} placeholder="例：台積電" />
          </label>
          <label>
            策略名稱
            <input name="strategyName" defaultValue={selectedCandidate.strategyName} />
          </label>
          <label>
            動作
            <select name="intendedAction" defaultValue="BUY">
              <option value="BUY">BUY</option>
              <option value="WATCH">WATCH</option>
              <option value="SELL">SELL</option>
            </select>
          </label>
        </div>

        {selectedStockId ? (
          <input type="hidden" name="stockId" value={selectedStockId} />
        ) : (
          <label>
            手動股票代碼
            <input name="stockId" placeholder="例：2330" required />
          </label>
        )}

        <label>
          投資論點
          <textarea name="thesis" rows={3} defaultValue={selectedCandidate.thesis} required />
        </label>
        <div className="form-grid">
          <label>
            進場想法
            <input name="entryIdea" defaultValue={selectedCandidate.entryIdea} required />
          </label>
          <label>
            停損條件
            <input name="stopLoss" defaultValue={selectedCandidate.stopLoss} required />
          </label>
          <label>
            停利想法
            <input name="takeProfit" placeholder="例：分批停利或壓力區減碼" />
          </label>
          <label>
            部位控管
            <input name="sizeNote" placeholder="例：單筆風險不超過 1%" required />
          </label>
        </div>
        <div className="form-grid">
          <label>
            風險檢查
            <input name="riskChecks" defaultValue={selectedCandidate.riskChecks.join("，")} />
          </label>
          <label>
            標籤
            <input name="tags" defaultValue={selectedCandidate.tags.join("，")} />
          </label>
        </div>

        <div className="button-row">
          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "建立中..." : "建立 TradePlan 草稿"}
          </button>
        </div>
        {message ? <p className="feedback-message">{message}</p> : null}
        {error ? <p className="feedback-message error">{error}</p> : null}
      </form>
    </section>
  );
}
