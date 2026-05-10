"use client";

import { useMemo, useState } from "react";

type MarketType = "TEST" | "Tw50" | "All" | "Custom";
type ScreeningProfile = "conservative" | "balanced" | "aggressive";
type ResultSection = "aList" | "bList" | "avoidList";

type ScreeningStock = {
  stockId: string;
  stockName?: string;
  score: number;
  riskScore: number;
  rank?: number;
  technicalScore?: number;
  chipScore?: number;
  volumeScore?: number;
  relativeStrengthScore?: number;
  reasons?: string[];
  risks?: string[];
  nextDayPlan?: string;
};

type ScreeningResponse = {
  scanId?: string;
  id?: string;
  executedAt?: string;
  executed_at?: string;
  date?: string;
  marketType?: string;
  market_scope?: string;
  profile?: string;
  counts?: {
    requested?: number;
    scanned?: number;
    aList?: number;
    bList?: number;
    avoidList?: number;
    skipped?: number;
  };
  aList?: ScreeningStock[];
  a_list?: ScreeningStock[];
  bList?: ScreeningStock[];
  b_list?: ScreeningStock[];
  avoidList?: ScreeningStock[];
  avoid_list?: ScreeningStock[];
  rawResults?: ScreeningStock[];
  raw_results?: ScreeningStock[];
  skipped?: Array<{ stockId?: string; stockName?: string; reason?: string; skipReason?: string }>;
  nextDayWatchlistId?: string;
  next_day_watchlist_id?: string;
  request_payload?: {
    stockList?: string[];
    maxStocks?: number;
  };
};

export type RecentAfterMarketScan = {
  id: string;
  date?: string;
  executedAt?: string;
  marketScope?: string;
  profile?: string;
  scanned?: number;
  aList?: number;
  bList?: number;
  avoidList?: number;
};

const MARKET_LABELS: Record<MarketType, string> = {
  TEST: "TEST 測試池",
  Tw50: "台灣 50",
  All: "全市場",
  Custom: "自訂清單"
};

const PROFILE_LABELS: Record<ScreeningProfile, string> = {
  conservative: "保守",
  balanced: "均衡",
  aggressive: "積極"
};

const SECTION_COPY: Record<ResultSection, { title: string; empty: string; tone: string }> = {
  aList: {
    title: "A 級觀察",
    empty: "目前沒有 A 級觀察標的。",
    tone: "strong"
  },
  bList: {
    title: "B 級觀察",
    empty: "目前沒有 B 級觀察標的。",
    tone: "watch"
  },
  avoidList: {
    title: "避開名單",
    empty: "本次沒有需要避開的風險標的。",
    tone: "risk"
  }
};

function todayInTaipei() {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Taipei",
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  }).format(new Date());
}

function parseStocks(value: string) {
  return value
    .split(/[\s,，、]+/)
    .map((item) => item.trim())
    .filter(Boolean);
}

function countTopFactors(items: ScreeningStock[], key: "reasons" | "risks") {
  const counts = new Map<string, number>();
  items.forEach((item) => {
    item[key]?.forEach((factor) => {
      counts.set(factor, (counts.get(factor) ?? 0) + 1);
    });
  });
  return Array.from(counts.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5);
}

function formatNumber(value: number | undefined) {
  return typeof value === "number" && Number.isFinite(value) ? value.toLocaleString("zh-TW") : "-";
}

function formatDateTime(value: string | undefined) {
  if (!value) {
    return "尚未執行";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return new Intl.DateTimeFormat("zh-TW", {
    dateStyle: "medium",
    timeStyle: "short"
  }).format(date);
}

function getScanId(value: ScreeningResponse | null) {
  return value?.scanId ?? value?.id ?? "";
}

function getExecutedAt(value: ScreeningResponse | null) {
  return value?.executedAt ?? value?.executed_at;
}

function getMarketType(value: ScreeningResponse | null) {
  return value?.marketType ?? value?.market_scope;
}

function getList(value: ScreeningResponse | null, key: ResultSection) {
  if (!value) {
    return [];
  }
  if (key === "aList") {
    return value.aList ?? value.a_list ?? [];
  }
  if (key === "bList") {
    return value.bList ?? value.b_list ?? [];
  }
  return value.avoidList ?? value.avoid_list ?? [];
}

function ResultTable({
  title,
  items,
  section,
  includeRiskList
}: {
  title: string;
  items: ScreeningStock[];
  section: ResultSection;
  includeRiskList: boolean;
}) {
  const copy = SECTION_COPY[section];

  return (
    <article className={`after-market-result after-market-result-${copy.tone}`}>
      <div className="after-market-result-header">
        <h3>{title}</h3>
        <span>{items.length} 檔</span>
      </div>

      {items.length > 0 ? (
        <div className="after-market-table-shell">
          <table className="after-market-table">
            <thead>
              <tr>
                <th>Rank</th>
                <th>股票</th>
                <th>總分</th>
                <th>技術</th>
                <th>籌碼</th>
                <th>量能</th>
                <th>相對強弱</th>
                <th>風險</th>
                <th>命中原因</th>
                <th>避開原因</th>
                <th>隔日計畫</th>
              </tr>
            </thead>
            <tbody>
              {items.map((item, index) => (
                <tr key={`${section}-${item.stockId}-${item.rank ?? index}`}>
                  <td>{item.rank ?? index + 1}</td>
                  <td>
                    <strong>{item.stockId}</strong>
                    <span>{item.stockName ?? "未命名"}</span>
                  </td>
                  <td>
                    <span className="score-chip">{formatNumber(item.score)}</span>
                  </td>
                  <td>{formatNumber(item.technicalScore)}</td>
                  <td>{formatNumber(item.chipScore)}</td>
                  <td>{formatNumber(item.volumeScore)}</td>
                  <td>{formatNumber(item.relativeStrengthScore)}</td>
                  <td>
                    <span className={item.riskScore <= -30 ? "risk-chip high" : "risk-chip"}>
                      {formatNumber(item.riskScore)}
                    </span>
                  </td>
                  <td>
                    <div className="factor-list">
                      {(item.reasons?.length ? item.reasons : ["尚無命中原因"]).map((reason) => (
                        <span key={reason}>{reason}</span>
                      ))}
                    </div>
                  </td>
                  <td>
                    <div className="factor-list risk">
                      {(item.risks?.length ? item.risks : ["無明顯風險"]).map((risk) => (
                        <span key={risk}>{risk}</span>
                      ))}
                    </div>
                  </td>
                  <td>{item.nextDayPlan ?? "等待盤中確認"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <p className="empty-state">
          {section === "avoidList" && !includeRiskList ? "目前設定不輸出避開名單。" : copy.empty}
        </p>
      )}
    </article>
  );
}

export function AfterMarketScreeningWorkbench({
  recentScans = []
}: {
  recentScans?: RecentAfterMarketScan[];
}) {
  const [date, setDate] = useState(todayInTaipei);
  const [marketType, setMarketType] = useState<MarketType>("TEST");
  const [profile, setProfile] = useState<ScreeningProfile>("balanced");
  const [maxStocks, setMaxStocks] = useState(80);
  const [includeRiskList, setIncludeRiskList] = useState(true);
  const [stockText, setStockText] = useState("2330, 2317, 2454, 2303, 2603");
  const [result, setResult] = useState<ScreeningResponse | null>(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [reportError, setReportError] = useState("");
  const [loadingReportId, setLoadingReportId] = useState("");

  const allResults = useMemo(() => {
    return [
      ...getList(result, "aList"),
      ...getList(result, "bList"),
      ...getList(result, "avoidList")
    ];
  }, [result]);

  const topReasons = useMemo(() => countTopFactors(allResults, "reasons"), [allResults]);
  const topRisks = useMemo(() => countTopFactors(allResults, "risks"), [allResults]);
  const scanId = getScanId(result);
  const scannedCount = result?.counts?.scanned ?? result?.rawResults?.length ?? result?.raw_results?.length;
  const visibleCandidateCount = allResults.length;
  const rawResultCount = result?.rawResults?.length ?? result?.raw_results?.length;
  const hasScanOutput = Boolean(result);
  const hasNoCandidates = hasScanOutput && visibleCandidateCount === 0;
  const latestRecentScan = recentScans[0];

  async function runScan() {
    setError("");
    setReportError("");
    setResult(null);
    setIsLoading(true);

    const stockList = parseStocks(stockText);
    const safeMaxStocks = Math.max(1, Math.min(2000, Math.floor(maxStocks || 1)));

    try {
      const response = await fetch("/api/after-market-screening/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          date,
          marketType,
          stockList,
          profile,
          maxStocks: safeMaxStocks,
          includeRiskList,
          weights: {
            technical: 40,
            chip: 30,
            volume: 15,
            relativeStrength: 15
          }
        })
      });

      const payload = await response.json().catch(() => null);
      if (!response.ok) {
        throw new Error(payload?.error ?? `盤後篩選 API 回應 ${response.status}`);
      }
      setResult(payload as ScreeningResponse);
    } catch (scanError) {
      setError(scanError instanceof Error ? scanError.message : "盤後篩選失敗，請稍後再試。");
    } finally {
      setIsLoading(false);
    }
  }

  async function loadReport(nextScanId: string) {
    if (!nextScanId) {
      return;
    }

    setError("");
    setReportError("");
    setLoadingReportId(nextScanId);

    try {
      const response = await fetch(`/api/after-market-screening/report/${encodeURIComponent(nextScanId)}`);
      const payload = await response.json().catch(() => null);
      if (!response.ok) {
        throw new Error(payload?.error ?? `讀取報告 API 回應 ${response.status}`);
      }
      setResult(payload as ScreeningResponse);
    } catch (reportLoadError) {
      setReportError(reportLoadError instanceof Error ? reportLoadError.message : "讀取盤後報告失敗。");
    } finally {
      setLoadingReportId("");
    }
  }

  return (
    <section className="after-market-workbench" aria-labelledby="after-market-title">
      <div className="panel after-market-settings">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Daily Screening</p>
            <h2 id="after-market-title">每日盤後篩選</h2>
          </div>
          <div className="status-pill">{PROFILE_LABELS[profile]}</div>
        </div>

        <div className="after-market-control-grid">
          <label>
            掃描日期
            <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
          </label>

          <label>
            股票池
            <select value={marketType} onChange={(event) => setMarketType(event.target.value as MarketType)}>
              {Object.entries(MARKET_LABELS).map(([value, label]) => (
                <option key={value} value={value}>
                  {label}
                </option>
              ))}
            </select>
          </label>

          <label>
            模式
            <select value={profile} onChange={(event) => setProfile(event.target.value as ScreeningProfile)}>
              {Object.entries(PROFILE_LABELS).map(([value, label]) => (
                <option key={value} value={value}>
                  {label}
                </option>
              ))}
            </select>
          </label>

          <label>
            最大掃描數
            <input
              min={1}
              max={2000}
              type="number"
              value={maxStocks}
              onChange={(event) => setMaxStocks(Number(event.target.value))}
            />
          </label>
        </div>

        <label>
          自訂標的
          <textarea
            rows={3}
            value={stockText}
            onChange={(event) => setStockText(event.target.value)}
            placeholder="例：2330, 2317, 2454"
          />
        </label>

          <div className="after-market-actions">
          <label className="after-market-checkbox">
            <input
              type="checkbox"
              checked={includeRiskList}
              onChange={(event) => setIncludeRiskList(event.target.checked)}
            />
            輸出避開名單
          </label>

          <button type="button" onClick={runScan} disabled={isLoading}>
            {isLoading ? "掃描中..." : "執行盤後掃描"}
          </button>
        </div>

        {error ? <p className="feedback-message error">{error}</p> : null}
      </div>

      <div className="panel after-market-summary">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Score Board</p>
            <h2>分數摘要</h2>
          </div>
          <div className="status-pill">{formatDateTime(getExecutedAt(result) ?? latestRecentScan?.executedAt)}</div>
        </div>

        <div className="after-market-report-strip" aria-label="最近盤後報告">
          <div>
            <span>目前報告</span>
            <strong>{scanId || latestRecentScan?.id || "尚未載入"}</strong>
          </div>
          <div>
            <span>市場 / 模式</span>
            <strong>
              {getMarketType(result) ?? latestRecentScan?.marketScope ?? marketType}
              {" · "}
              {result?.profile ?? latestRecentScan?.profile ?? profile}
            </strong>
          </div>
          <button
            type="button"
            className="secondary-button"
            disabled={Boolean(!scanId || loadingReportId)}
            onClick={() => loadReport(scanId)}
          >
            {loadingReportId === scanId ? "讀取中..." : "重新讀取報告"}
          </button>
        </div>

        {recentScans.length > 0 ? (
          <div className="after-market-recent-runs">
            <div className="after-market-recent-runs-header">
              <h3>最近盤後掃描</h3>
              <span>{recentScans.length} 筆</span>
            </div>
            <div className="after-market-run-list">
              {recentScans.map((scan) => (
                <button
                  key={scan.id}
                  type="button"
                  className={scan.id === scanId ? "after-market-run active" : "after-market-run"}
                  disabled={Boolean(loadingReportId)}
                  onClick={() => loadReport(scan.id)}
                >
                  <span>{formatDateTime(scan.executedAt)}</span>
                  <strong>{scan.id}</strong>
                  <small>
                    {scan.marketScope ?? "-"} · 掃描 {formatNumber(scan.scanned)} · A/B/避{" "}
                    {formatNumber(scan.aList)}/{formatNumber(scan.bList)}/{formatNumber(scan.avoidList)}
                  </small>
                </button>
              ))}
            </div>
          </div>
        ) : null}

        {reportError ? <p className="feedback-message error">{reportError}</p> : null}

        {isLoading ? (
          <div className="after-market-loading" role="status">
            <span />
            <p>正在送出盤後掃描，等待 Python bridge / API 回傳結果。</p>
          </div>
        ) : result ? (
          <>
            <div className="after-market-metric-grid">
              <div>
                <span>掃描股票</span>
                <strong>{formatNumber(scannedCount)}</strong>
              </div>
              <div>
                <span>A 級</span>
                <strong>{formatNumber(result.counts?.aList ?? getList(result, "aList").length)}</strong>
              </div>
              <div>
                <span>B 級</span>
                <strong>{formatNumber(result.counts?.bList ?? getList(result, "bList").length)}</strong>
              </div>
              <div>
                <span>避開</span>
                <strong>{formatNumber(result.counts?.avoidList ?? getList(result, "avoidList").length)}</strong>
              </div>
              <div>
                <span>未入榜</span>
                <strong>{formatNumber(Math.max(0, (rawResultCount ?? scannedCount ?? 0) - visibleCandidateCount))}</strong>
              </div>
            </div>

            {hasNoCandidates ? (
              <div className="after-market-empty-report">
                <h3>這次沒有符合 A / B / 避開名單的標的</h3>
                <p>
                  掃描已完成，代表資料與報告流程可用；可改用積極模式、提高最大掃描數，或從最近報告重新載入原始掃描紀錄。
                </p>
              </div>
            ) : null}

            <div className="after-market-factor-grid">
              <div>
                <h3>前 5 大加分因子</h3>
                {topReasons.length > 0 ? (
                  <ol>
                    {topReasons.map(([factor, count]) => (
                      <li key={factor}>
                        <span>{factor}</span>
                        <strong>{count}</strong>
                      </li>
                    ))}
                  </ol>
                ) : (
                  <p className="empty-state">尚無加分因子。</p>
                )}
              </div>
              <div>
                <h3>前 5 大風險因子</h3>
                {topRisks.length > 0 ? (
                  <ol>
                    {topRisks.map(([factor, count]) => (
                      <li key={factor}>
                        <span>{factor}</span>
                        <strong>{count}</strong>
                      </li>
                    ))}
                  </ol>
                ) : (
                  <p className="empty-state">尚無風險因子。</p>
                )}
              </div>
            </div>
          </>
        ) : (
          <p className="empty-state">尚未執行每日盤後篩選。設定股票池、模式與掃描數後即可送出。</p>
        )}
      </div>

      <div className="after-market-results-grid">
        <ResultTable
          title={SECTION_COPY.aList.title}
          items={getList(result, "aList")}
          section="aList"
          includeRiskList={includeRiskList}
        />
        <ResultTable
          title={SECTION_COPY.bList.title}
          items={getList(result, "bList")}
          section="bList"
          includeRiskList={includeRiskList}
        />
        <ResultTable
          title={SECTION_COPY.avoidList.title}
          items={getList(result, "avoidList")}
          section="avoidList"
          includeRiskList={includeRiskList}
        />
      </div>
    </section>
  );
}
