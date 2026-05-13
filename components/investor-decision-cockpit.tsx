import type { AnalysisResultDto } from "@/lib/analysis-results";

type WorkspaceRecord = Record<string, unknown>;

type DashboardSnapshot = {
  counts: Record<string, number>;
  screenRuns: WorkspaceRecord[];
  signalEvents: WorkspaceRecord[];
  backtestRuns: WorkspaceRecord[];
  tradePlans: WorkspaceRecord[];
  paperOrders: WorkspaceRecord[];
  watchlists: WorkspaceRecord[];
  researchNotes: WorkspaceRecord[];
  afterMarketScans: WorkspaceRecord[];
  nextDayWatchlists: WorkspaceRecord[];
};

type InvestorDecisionCockpitProps = {
  snapshot: DashboardSnapshot;
  analysisResults: AnalysisResultDto[];
};

type Candidate = {
  stockId: string;
  stockName: string;
  score: number | null;
  riskScore: number | null;
  decisionScore: number;
  supportScore: number;
  freshnessScore: number;
  bucket: string;
  source: string;
  plan: string;
  reasons: string[];
  risks: string[];
  supportCount: number;
};

function asRecord(value: unknown): WorkspaceRecord | null {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return null;
  }
  return value as WorkspaceRecord;
}

function asRecordArray(value: unknown): WorkspaceRecord[] {
  return Array.isArray(value) ? value.map(asRecord).filter((item): item is WorkspaceRecord => Boolean(item)) : [];
}

function asString(value: unknown, fallback = "-") {
  return value === null || value === undefined || value === "" ? fallback : String(value);
}

function asNumber(value: unknown): number | null {
  if (typeof value === "number" && Number.isFinite(value)) {
    return value;
  }
  if (typeof value === "string" && value.trim() !== "") {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? parsed : null;
  }
  return null;
}

function asStringArray(value: unknown): string[] {
  return Array.isArray(value) ? value.map((item) => String(item)).filter(Boolean) : [];
}

function formatScore(value: number | null) {
  return value === null ? "-" : value.toFixed(value % 1 === 0 ? 0 : 1);
}

function formatDateTime(value: unknown) {
  const raw = asString(value, "");
  if (!raw) {
    return "-";
  }

  const parsed = new Date(raw);
  if (Number.isNaN(parsed.getTime())) {
    return raw;
  }

  return parsed.toLocaleString("zh-TW", {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function formatMetric(value: unknown, suffix = "") {
  const numericValue = asNumber(value);
  return numericValue === null ? "-" : `${numericValue}${suffix}`;
}

function getLatestAfterMarketScan(snapshot: DashboardSnapshot) {
  return snapshot.afterMarketScans[0] ?? null;
}

function clampScore(value: number) {
  return Math.max(0, Math.min(100, Math.round(value)));
}

function calculateFreshnessScore(value: unknown) {
  const raw = asString(value, "");
  const timestamp = raw ? new Date(raw).getTime() : Number.NaN;
  if (Number.isNaN(timestamp)) {
    return 20;
  }
  const ageHours = Math.max(0, (Date.now() - timestamp) / 1000 / 60 / 60);
  if (ageHours <= 24) {
    return 100;
  }
  if (ageHours <= 72) {
    return 75;
  }
  if (ageHours <= 168) {
    return 45;
  }
  return 20;
}

function calculateDecisionScore({
  score,
  riskScore,
  supportCount,
  freshnessScore,
  bucket
}: {
  score: number | null;
  riskScore: number | null;
  supportCount: number;
  freshnessScore: number;
  bucket: string;
}) {
  const baseScore = score ?? (bucket.includes("backtest") ? 58 : 45);
  const riskPenalty = Math.min(35, Math.abs(Math.min(0, riskScore ?? 0)));
  const supportScore = Math.min(20, supportCount * 8);
  const bucketBonus = bucket.includes("A") ? 10 : bucket.includes("B") ? 5 : 0;
  return clampScore((baseScore * 0.55) + supportScore + (freshnessScore * 0.15) + bucketBonus - riskPenalty);
}

function buildCandidates(snapshot: DashboardSnapshot, analysisResults: AnalysisResultDto[]) {
  const latestScan = getLatestAfterMarketScan(snapshot);
  const latestExecutedAt = latestScan?.executed_at;
  const scanCandidates: WorkspaceRecord[] = latestScan
    ? [
        ...asRecordArray(latestScan.a_list).map((item) => ({ ...item, bucket: "A級候選" })),
        ...asRecordArray(latestScan.b_list).map((item) => ({ ...item, bucket: "B級觀察" })),
        ...asRecordArray(latestScan.raw_results).map((item) => ({
          ...item,
          bucket: asString(item.bucket, "盤後掃描")
        }))
      ]
    : [];

  const byStock = new Map<string, Candidate>();
  const supportCounts = new Map<string, number>();
  for (const result of analysisResults) {
    supportCounts.set(result.stockId, (supportCounts.get(result.stockId) ?? 0) + 1);
  }

  for (const item of scanCandidates) {
    const stockId = asString(item.stockId ?? item.stock_id, "");
    if (!stockId || byStock.has(stockId)) {
      continue;
    }

    const supportCount = supportCounts.get(stockId) ?? 0;
    const score = asNumber(item.score);
    const riskScore = asNumber(item.riskScore ?? item.risk_score);
    const bucket = asString(item.bucket, "盤後掃描");
    const freshnessScore = calculateFreshnessScore(latestExecutedAt);

    byStock.set(stockId, {
      stockId,
      stockName: asString(item.stockName ?? item.stock_name, ""),
      score,
      riskScore,
      decisionScore: calculateDecisionScore({ score, riskScore, supportCount, freshnessScore, bucket }),
      supportScore: Math.min(20, supportCount * 8),
      freshnessScore,
      bucket,
      source: asString(latestScan?.id, "after_market_scan"),
      plan: asString(item.nextDayPlan ?? item.next_day_plan, "等待明確進出場條件後再列入交易計畫。"),
      reasons: asStringArray(item.reasons).slice(0, 4),
      risks: asStringArray(item.risks).slice(0, 4),
      supportCount
    });
  }

  for (const result of analysisResults) {
    if (!result.stockId || byStock.has(result.stockId)) {
      continue;
    }

    const supportCount = supportCounts.get(result.stockId) ?? 1;
    const freshnessScore = calculateFreshnessScore(result.createdAt);
    const bucket = result.kind;

    byStock.set(result.stockId, {
      stockId: result.stockId,
      stockName: result.stockName ?? "",
      score: null,
      riskScore: null,
      decisionScore: calculateDecisionScore({
        score: null,
        riskScore: null,
        supportCount,
        freshnessScore,
        bucket
      }),
      supportScore: Math.min(20, supportCount * 8),
      freshnessScore,
      bucket,
      source: result.source,
      plan: result.summary || "先閱讀分析結果，再補盤後掃描或回測支持度。",
      reasons: result.tags.slice(0, 4),
      risks: [],
      supportCount
    });
  }

  return [...byStock.values()]
    .sort((left, right) => {
      return right.decisionScore - left.decisionScore || right.supportCount - left.supportCount;
    })
    .slice(0, 6);
}

function buildRiskItems(snapshot: DashboardSnapshot, candidates: Candidate[]) {
  const latestScan = getLatestAfterMarketScan(snapshot);
  const avoidList = latestScan ? asRecordArray(latestScan.avoid_list) : [];
  const candidateRisks = candidates
    .filter((candidate) => (candidate.riskScore ?? 0) !== 0 || candidate.risks.length > 0)
    .map((candidate) => {
      const riskScore = candidate.riskScore ?? 0;
      const riskMagnitude = Math.abs(riskScore);

      return {
        title: `${candidate.stockId} ${candidate.stockName}`.trim(),
        detail: candidate.risks.join("、") || `風險分數 ${formatScore(candidate.riskScore)}`,
        level: riskMagnitude >= 60 || riskScore <= -30 ? "高" : "觀察"
      };
    });

  const scanRisks = avoidList.map((item) => ({
    title: `${asString(item.stockId ?? item.stock_id)} ${asString(item.stockName ?? item.stock_name, "")}`.trim(),
    detail: asStringArray(item.risks).join("、") || asString(item.reason, "列入避開清單"),
    level: "避開"
  }));

  return [...scanRisks, ...candidateRisks].slice(0, 5);
}

function buildValidationRows(snapshot: DashboardSnapshot, analysisResults: AnalysisResultDto[]) {
  const backtestRows = snapshot.backtestRuns.map((item) => ({
    stockId: asString(item.stock_id),
    source: "Workspace Backtest",
    strategy: asString(item.strategy_name),
    result: `期間 ${asString(item.period)} / 總報酬 ${formatMetric(item.total_return_pct, "%")} / 最終資產 ${formatMetric(item.final_value)} / 交易 ${asStringArray(item.trades).length} 筆`,
    updatedAt: asString(item.executed_at)
  }));

  const analysisRows = analysisResults
    .filter((item) => item.kind.toLowerCase().includes("backtest") || item.tags.includes("backtest"))
    .map((item) => {
      const metrics = asRecord(item.payload?.backtestMetrics);
      const result = metrics
        ? [
            metrics.period ? `期間 ${metrics.period}` : null,
            `總報酬 ${formatMetric(metrics.totalReturnPct, "%")}`,
            `最大回撤 ${formatMetric(metrics.maxDrawdownPct, "%")}`,
            `勝率 ${formatMetric(metrics.winRatePct, "%")}`,
            `交易 ${formatMetric(metrics.tradeCount)} 筆`
          ].filter(Boolean).join(" / ")
        : item.summary;

      return {
        stockId: item.stockId,
        source: item.source,
        strategy: item.strategyName ?? item.kind,
        result,
        updatedAt: item.createdAt
      };
    });

  return [...backtestRows, ...analysisRows].slice(0, 5);
}

function buildFreshnessRows(snapshot: DashboardSnapshot, analysisResults: AnalysisResultDto[]) {
  const latestAnalysis = analysisResults[0];

  return [
    {
      label: "盤後掃描",
      count: snapshot.counts.afterMarketScans,
      updatedAt: snapshot.afterMarketScans[0]?.executed_at,
      state: snapshot.counts.afterMarketScans > 0 ? "可用" : "待補"
    },
    {
      label: "次日觀察清單",
      count: snapshot.counts.nextDayWatchlists,
      updatedAt: snapshot.nextDayWatchlists[0]?.created_at,
      state: snapshot.counts.nextDayWatchlists > 0 ? "可用" : "待補"
    },
    {
      label: "分析結果 DB",
      count: analysisResults.length,
      updatedAt: latestAnalysis?.createdAt,
      state: analysisResults.length > 0 ? "可用" : "待補"
    },
    {
      label: "交易計畫",
      count: snapshot.counts.tradePlans,
      updatedAt: snapshot.tradePlans[0]?.updated_at,
      state: snapshot.counts.tradePlans > 0 ? "可用" : "待建立"
    },
    {
      label: "回測驗證",
      count: snapshot.counts.backtestRuns,
      updatedAt: snapshot.backtestRuns[0]?.executed_at,
      state: snapshot.counts.backtestRuns > 0 ? "可用" : "待補"
    }
  ];
}

export function InvestorDecisionCockpit({ snapshot, analysisResults }: InvestorDecisionCockpitProps) {
  const latestScan = getLatestAfterMarketScan(snapshot);
  const latestWatchlist = snapshot.nextDayWatchlists[0];
  const candidates = buildCandidates(snapshot, analysisResults);
  const risks = buildRiskItems(snapshot, candidates);
  const validationRows = buildValidationRows(snapshot, analysisResults);
  const freshnessRows = buildFreshnessRows(snapshot, analysisResults);
  const watchlistRules = asStringArray(latestWatchlist?.monitoring_rules);
  const pendingOrders = snapshot.counts.pendingOrders ?? 0;

  return (
    <div className="investor-cockpit">
      <section className="investor-brief panel">
        <div>
          <p className="eyebrow">Investor Decision Cockpit</p>
          <h2>今日投資決策中控台</h2>
          <p>
            只整合目前 workspace snapshot 與 analysis results，協助投資人把「候選、風險、驗證、交易計畫、資料新鮮度」
            放在同一個決策畫面檢查。
          </p>
        </div>
        <dl className="investor-brief-stats">
          <div>
            <dt>最新盤後資料</dt>
            <dd>{formatDateTime(latestScan?.executed_at)}</dd>
          </div>
          <div>
            <dt>候選清單</dt>
            <dd>{candidates.length} 檔</dd>
          </div>
          <div>
            <dt>待執行/送出單</dt>
            <dd>{pendingOrders} 筆</dd>
          </div>
        </dl>
      </section>

      <section className="investor-grid">
        <div className="panel investor-panel">
          <div className="panel-header">
            <h2>今日可研究候選</h2>
            <span>{candidates.length} 檔</span>
          </div>
          {candidates.length === 0 ? (
            <p className="empty-state">目前沒有候選。先執行盤後掃描或匯入分析結果，這裡才會產生研究排序。</p>
          ) : (
            <div className="investor-candidate-list">
              {candidates.map((candidate) => (
                <article className="investor-candidate" key={`${candidate.source}-${candidate.stockId}`}>
                  <div className="investor-candidate-top">
                    <div>
                      <strong>{candidate.stockId} {candidate.stockName}</strong>
                      <span>{candidate.bucket}</span>
                    </div>
                    <div className="investor-score">
                      <small>決策分</small>
                      <b>{candidate.decisionScore}</b>
                    </div>
                  </div>
                  <p>{candidate.plan}</p>
                  <div className="investor-score-line">
                    <span>掃描 {formatScore(candidate.score)}</span>
                    <span>支持 {candidate.supportScore}</span>
                    <span>新鮮 {candidate.freshnessScore}</span>
                    <span>風險 {formatScore(candidate.riskScore)}</span>
                  </div>
                  <div className="investor-tags">
                    {candidate.reasons.length > 0 ? (
                      candidate.reasons.map((reason) => <span key={`${candidate.stockId}-${reason}`}>{reason}</span>)
                    ) : (
                      <span>等待更多理由</span>
                    )}
                  </div>
                  <small>分析/回測支持：{candidate.supportCount} 筆</small>
                </article>
              ))}
            </div>
          )}
        </div>

        <div className="panel investor-panel investor-risk-panel">
          <div className="panel-header">
            <h2>風險觀察</h2>
            <span>{risks.length} 項</span>
          </div>
          {risks.length === 0 ? (
            <p className="empty-state">最新資料沒有明確風險項。仍需觀察大盤轉弱、破均線與隔日開盤低點。</p>
          ) : (
            <div className="investor-risk-list">
              {risks.map((risk) => (
                <article key={`${risk.title}-${risk.detail}`}>
                  <span>{risk.level}</span>
                  <div>
                    <strong>{risk.title}</strong>
                    <p>{risk.detail}</p>
                  </div>
                </article>
              ))}
            </div>
          )}
        </div>
      </section>

      <section className="investor-grid">
        <div className="panel investor-panel">
          <div className="panel-header">
            <h2>驗證/回測支持度</h2>
            <span>{validationRows.length} 筆</span>
          </div>
          {validationRows.length === 0 ? (
            <p className="empty-state">目前沒有可用回測或 backtest analysis。交易前應補上策略期間、報酬、最大回撤與樣本數。</p>
          ) : (
            <div className="investor-validation-list">
              {validationRows.map((row) => (
                <article key={`${row.source}-${row.stockId}-${row.updatedAt}`}>
                  <strong>{row.stockId} / {row.strategy}</strong>
                  <p>{row.result}</p>
                  <span>{row.source} · {formatDateTime(row.updatedAt)}</span>
                </article>
              ))}
            </div>
          )}
        </div>

        <div className="panel investor-panel">
          <div className="panel-header">
            <h2>下一步交易計畫</h2>
            <span>{snapshot.tradePlans.length} 筆計畫</span>
          </div>
          {snapshot.tradePlans.length > 0 ? (
            <div className="investor-plan-list">
              {snapshot.tradePlans.map((plan) => (
                <article key={asString(plan.id ?? `${plan.stock_id}-${plan.updated_at}`)}>
                  <strong>{asString(plan.stock_id)} {asString(plan.strategy_name, "")}</strong>
                  <p>狀態：{asString(plan.status)} · 更新：{formatDateTime(plan.updated_at)}</p>
                </article>
              ))}
            </div>
          ) : (
            <div className="investor-plan-list">
              <article>
                <strong>盤前確認條件</strong>
                <p>{watchlistRules[0] ?? "確認候選是否守住關鍵價位，未達條件不進場。"}</p>
              </article>
              <article>
                <strong>失敗條件</strong>
                <p>{watchlistRules[1] ?? "開盤後跌破開盤低點或盤勢轉弱時，先降級為觀察。"}</p>
              </article>
              <article>
                <strong>補強動作</strong>
                <p>把候選股轉成 TradePlan 前，補上進場價、停損價、部位大小與回測依據。</p>
              </article>
            </div>
          )}
        </div>
      </section>

      <section className="panel investor-panel">
        <div className="panel-header">
          <h2>資料新鮮度</h2>
          <span>只顯示安全摘要</span>
        </div>
        <div className="investor-freshness-grid">
          {freshnessRows.map((row) => (
            <div key={row.label}>
              <span className={`investor-state ${row.state === "可用" ? "ready" : "warning"}`}>{row.state}</span>
              <strong>{row.label}</strong>
              <p>{row.count} 筆 · 最新 {formatDateTime(row.updatedAt)}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
