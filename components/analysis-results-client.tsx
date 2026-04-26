"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

type AnalysisResultsClientProps = {
  initialCount: number;
};

export function AnalysisResultsClient({ initialCount }: AnalysisResultsClientProps) {
  const router = useRouter();
  const [message, setMessage] = useState<string>("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleCreate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsSubmitting(true);
    setMessage("");

    const formData = new FormData(event.currentTarget);
    const payload = {
      kind: "MANUAL_NOTE",
      stockId: String(formData.get("stockId") ?? ""),
      stockName: String(formData.get("stockName") ?? ""),
      strategyName: String(formData.get("strategyName") ?? ""),
      title: String(formData.get("title") ?? ""),
      summary: String(formData.get("summary") ?? ""),
      tags: String(formData.get("tags") ?? "")
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean),
      payload: {
        sourcePage: "analysis-results",
        noteType: "manual-entry"
      }
    };

    const response = await fetch("/api/analysis-results", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const result = (await response.json()) as { message?: string; error?: string };
    setIsSubmitting(false);

    if (!response.ok) {
      setMessage(result.error ?? "建立分析結果失敗。");
      return;
    }

    setMessage(result.message ?? "分析結果已保存。");
    event.currentTarget.reset();
    router.refresh();
  }

  async function handleImport() {
    setIsSubmitting(true);
    setMessage("");

    const response = await fetch("/api/analysis-results/import-workspace", {
      method: "POST"
    });
    const result = (await response.json()) as {
      imported?: number;
      skipped?: number;
      error?: string;
    };

    setIsSubmitting(false);

    if (!response.ok) {
      setMessage(result.error ?? "匯入 workspace 結果失敗。");
      return;
    }

    setMessage(`已匯入 ${result.imported ?? 0} 筆，略過 ${result.skipped ?? 0} 筆。`);
    router.refresh();
  }

  return (
    <section className="panel">
      <div className="panel-header">
        <h2>新增 / 匯入分析結果</h2>
        <span>目前 {initialCount} 筆</span>
      </div>
      <form className="stack-form" onSubmit={handleCreate}>
        <div className="form-grid">
          <label>
            股票代碼
            <input name="stockId" defaultValue="2330" required />
          </label>
          <label>
            股票名稱
            <input name="stockName" defaultValue="TSMC" />
          </label>
          <label>
            策略名稱
            <input name="strategyName" defaultValue="MA Crossover" />
          </label>
          <label>
            標題
            <input name="title" defaultValue="手動分析紀錄" required />
          </label>
        </div>
        <label>
          摘要
          <textarea
            name="summary"
            rows={4}
            defaultValue="記錄對股票與策略的觀察，作為後續驗證與決策依據。"
            required
          />
        </label>
        <label>
          標籤
          <input name="tags" defaultValue="manual,next-ui" />
        </label>
        <div className="button-row">
          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "儲存中..." : "儲存分析結果"}
          </button>
          <button type="button" className="secondary-button" onClick={handleImport} disabled={isSubmitting}>
            從 workspace 匯入回測結果
          </button>
        </div>
      </form>
      {message ? <p className="feedback-message">{message}</p> : null}
    </section>
  );
}
