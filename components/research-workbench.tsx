"use client";

import { useEffect, useState } from "react";

type ResearchPayload = {
  ticker: string;
  name: string;
  industry: string;
  description: string;
  currentPrice: number | null;
  fundamentals: Record<string, number | string>;
  history: Array<{ date: string; close: number | null; volume: number | null }>;
};

export function ResearchWorkbench() {
  const [ticker, setTicker] = useState("2330");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [data, setData] = useState<ResearchPayload | null>(null);

  async function fetchResearch(targetTicker: string) {
    const response = await fetch(`/api/research/${targetTicker}`);
    const payload = (await response.json()) as ResearchPayload & { error?: string };
    if (!response.ok) {
      throw new Error(payload.error ?? "研究資料讀取失敗。");
    }

    return payload;
  }

  async function loadResearch(targetTicker: string) {
    setLoading(true);
    setError("");

    try {
      const payload = await fetchResearch(targetTicker);
      setData(payload);
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : "未知錯誤");
      setData(null);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    let isActive = true;

    async function bootstrap() {
      try {
        const payload = await fetchResearch("2330");
        if (!isActive) {
          return;
        }
        setData(payload);
      } catch (caughtError) {
        if (!isActive) {
          return;
        }
        setError(caughtError instanceof Error ? caughtError.message : "未知錯誤");
      } finally {
        if (isActive) {
          setLoading(false);
        }
      }
    }

    void bootstrap();

    return () => {
      isActive = false;
    };
  }, []);

  return (
    <div className="stack-layout">
      <section className="panel">
        <div className="panel-header">
          <h2>研究輸入</h2>
          <span>呼叫 Next.js market data service</span>
        </div>
        <div className="inline-form">
          <input value={ticker} onChange={(event) => setTicker(event.target.value)} placeholder="輸入台股代碼" />
          <button type="button" onClick={() => void loadResearch(ticker)} disabled={loading}>
            {loading ? "查詢中..." : "執行研究"}
          </button>
        </div>
        <p className="helper-text">這個頁面透過 Next API route 直接抓取市場資料，部署到 Vercel 時不再依賴本機 Python。</p>
      </section>

      {error ? <section className="panel"><p className="feedback-message">{error}</p></section> : null}

      {data ? (
        <>
          <section className="panel">
            <div className="panel-header">
              <h2>
                {data.ticker} {data.name}
              </h2>
              <span>{data.industry}</span>
            </div>
            <div className="metric-grid">
              <article className="metric-card">
                <p className="metric-label">目前價格</p>
                <p className="metric-value">{data.currentPrice ?? "-"}</p>
              </article>
              {Object.entries(data.fundamentals).slice(0, 4).map(([key, value]) => (
                <article key={key} className="metric-card">
                  <p className="metric-label">{key}</p>
                  <p className="metric-value">{String(value)}</p>
                </article>
              ))}
            </div>
            <p className="body-copy">{data.description || "目前沒有額外描述。"}</p>
          </section>

          <section className="panel">
            <div className="panel-header">
              <h2>近 60 筆價格</h2>
              <span>{data.history.length} 根</span>
            </div>
            <div className="table-shell">
              <table>
                <thead>
                  <tr>
                    <th>日期</th>
                    <th>收盤</th>
                    <th>成交量</th>
                  </tr>
                </thead>
                <tbody>
                  {data.history.slice(-15).reverse().map((item) => (
                    <tr key={item.date}>
                      <td>{item.date}</td>
                      <td>{item.close ?? "-"}</td>
                      <td>{item.volume ?? "-"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        </>
      ) : null}
    </div>
  );
}
