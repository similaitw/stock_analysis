"use client";

import { useCallback, useDeferredValue, useMemo, useState } from "react";

import type { AfterMarketStockCategory, AfterMarketStockOption } from "@/lib/stock-universe";

type MarketType = "TEST" | "Tw50" | "All" | "Custom";
type ScreeningProfile = "conservative" | "balanced" | "aggressive";
type ResultSection = "aList" | "bList" | "avoidList";
type WorkflowMode = "known-stock" | "strategy-scan";
type WeightConfig = {
  technical: number;
  chip: number;
  volume: number;
  relativeStrength: number;
};

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
  cache?: {
    status?: "hit" | "miss";
    storageMode?: string;
    cachedAt?: string;
  };
  request_payload?: {
    stockList?: string[];
    maxStocks?: number;
  };
};

type BatchRunState = {
  batchIndex: number;
  totalBatches: number;
  scanId: string;
  cacheStatus: string;
  scanned: number;
};

type DailyCacheSummary = {
  scanId: string;
  scanDate: string;
  marketType: string;
  profile: string;
  stockCount: number;
  scanned: number;
  aList: number;
  bList: number;
  avoidList: number;
  skipped: number;
  updatedAt: string;
  storageMode: string;
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

const STRATEGY_PRESETS: Array<{
  id: string;
  label: string;
  description: string;
  profile: ScreeningProfile;
  weights: WeightConfig;
}> = [
  {
    id: "steady",
    label: "穩健轉強",
    description: "技術與籌碼平均，適合新手先看趨勢是否乾淨。",
    profile: "balanced",
    weights: { technical: 40, chip: 30, volume: 15, relativeStrength: 15 }
  },
  {
    id: "chip",
    label: "籌碼優先",
    description: "提高法人/籌碼權重，適合檢查是否有資金集中。",
    profile: "conservative",
    weights: { technical: 30, chip: 45, volume: 10, relativeStrength: 15 }
  },
  {
    id: "breakout",
    label: "量價突破",
    description: "提高技術與量能，適合找隔日可能延續的強勢股。",
    profile: "aggressive",
    weights: { technical: 45, chip: 20, volume: 25, relativeStrength: 10 }
  },
  {
    id: "rs",
    label: "相對強勢",
    description: "提高相對強弱，適合從分類裡找領先族群。",
    profile: "balanced",
    weights: { technical: 32, chip: 23, volume: 15, relativeStrength: 30 }
  }
];

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

function getDecision(stock: ScreeningStock, section: ResultSection) {
  if (section === "aList") {
    return {
      label: "值得進入個股分析",
      tone: "go",
      detail: "先檢查進場價、停損與隔日量價確認。"
    };
  }
  if (section === "bList") {
    return {
      label: "列入觀察",
      tone: "watch",
      detail: stock.riskScore <= -20 ? "有風險扣分，等盤中確認再動。" : "條件未完整，先看是否補量或轉強。"
    };
  }
  return {
    label: "暫不分析",
    tone: "avoid",
    detail: "風險名單先排除，避免把時間花在低品質標的。"
  };
}

function chunkStockIds(stockIds: string[], size: number) {
  const safeSize = Math.max(1, Math.min(500, Math.floor(size || 80)));
  const chunks: string[][] = [];
  for (let index = 0; index < stockIds.length; index += safeSize) {
    chunks.push(stockIds.slice(index, index + safeSize));
  }
  return chunks;
}

function mergeBatchResponses(responses: ScreeningResponse[], date: string, profile: ScreeningProfile): ScreeningResponse {
  const aList = responses.flatMap((response) => getList(response, "aList"));
  const bList = responses.flatMap((response) => getList(response, "bList"));
  const avoidList = responses.flatMap((response) => getList(response, "avoidList"));
  const rawResults = responses.flatMap((response) => response.rawResults ?? response.raw_results ?? []);
  const skipped = responses.flatMap((response) => response.skipped ?? []);
  const cacheHits = responses.filter((response) => response.cache?.status === "hit").length;

  return {
    scanId: `batch_${date.replaceAll("-", "")}_${responses.length}`,
    executedAt: new Date().toISOString(),
    date,
    marketType: "Custom",
    profile,
    counts: {
      scanned: rawResults.length,
      aList: aList.length,
      bList: bList.length,
      avoidList: avoidList.length,
      skipped: skipped.length
    },
    aList: aList
      .sort((left, right) => right.score - left.score)
      .map((item, index) => ({ ...item, rank: index + 1 })),
    bList: bList
      .sort((left, right) => right.score - left.score)
      .map((item, index) => ({ ...item, rank: index + 1 })),
    avoidList: avoidList
      .sort((left, right) => left.riskScore - right.riskScore)
      .map((item, index) => ({ ...item, rank: index + 1 })),
    rawResults,
    skipped,
    cache: {
      status: cacheHits === responses.length ? "hit" : "miss",
      storageMode: `batch ${cacheHits}/${responses.length} cache hits`
    }
  };
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
  recentScans = [],
  stockCategories = [],
  stockOptions = [],
  initialCacheEntries = []
}: {
  recentScans?: RecentAfterMarketScan[];
  stockCategories?: AfterMarketStockCategory[];
  stockOptions?: AfterMarketStockOption[];
  initialCacheEntries?: DailyCacheSummary[];
}) {
  const [workflowMode, setWorkflowMode] = useState<WorkflowMode>("known-stock");
  const [date, setDate] = useState(todayInTaipei);
  const [marketType, setMarketType] = useState<MarketType>("TEST");
  const [profile, setProfile] = useState<ScreeningProfile>("balanced");
  const [strategyPresetId, setStrategyPresetId] = useState("steady");
  const [weights, setWeights] = useState<WeightConfig>(STRATEGY_PRESETS[0].weights);
  const [maxStocks, setMaxStocks] = useState(80);
  const [includeRiskList, setIncludeRiskList] = useState(true);
  const [stockText, setStockText] = useState("2330, 2317, 2454, 2303, 2603");
  const [selectedCategoryIds, setSelectedCategoryIds] = useState<string[]>([]);
  const [selectedStockIds, setSelectedStockIds] = useState<string[]>([]);
  const [stockQuery, setStockQuery] = useState("");
  const [batchSize, setBatchSize] = useState(80);
  const [batchRuns, setBatchRuns] = useState<BatchRunState[]>([]);
  const [result, setResult] = useState<ScreeningResponse | null>(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [reportError, setReportError] = useState("");
  const [loadingReportId, setLoadingReportId] = useState("");
  const [cacheEntries, setCacheEntries] = useState<DailyCacheSummary[]>(initialCacheEntries);
  const [cacheError, setCacheError] = useState("");
  const [isCacheLoading, setIsCacheLoading] = useState(false);

  const allResults = useMemo(() => {
    return [
      ...getList(result, "aList"),
      ...getList(result, "bList"),
      ...getList(result, "avoidList")
    ];
  }, [result]);

  const topReasons = useMemo(() => countTopFactors(allResults, "reasons"), [allResults]);
  const topRisks = useMemo(() => countTopFactors(allResults, "risks"), [allResults]);
  const deferredStockQuery = useDeferredValue(stockQuery.trim().toLowerCase());
  const marketCategories = useMemo(
    () => stockCategories.filter((category) => category.group === "市場"),
    [stockCategories]
  );
  const industryCategories = useMemo(
    () => stockCategories.filter((category) => category.group === "產業"),
    [stockCategories]
  );
  const selectedCategories = useMemo(() => {
    const selectedIds = new Set(selectedCategoryIds);
    return stockCategories.filter((category) => selectedIds.has(category.id));
  }, [selectedCategoryIds, stockCategories]);
  const selectedCategoryStockIds = useMemo(() => {
    return Array.from(
      new Set(selectedCategories.flatMap((category) => category.stockIds))
    ).sort((left, right) => left.localeCompare(right, "en-US"));
  }, [selectedCategories]);
  const filteredStockOptions = useMemo(() => {
    if (!deferredStockQuery) {
      return stockOptions.slice(0, 24);
    }

    return stockOptions
      .filter((stock) => stock.searchText.includes(deferredStockQuery))
      .slice(0, 40);
  }, [deferredStockQuery, stockOptions]);
  const selectedStockSet = useMemo(() => new Set(selectedStockIds), [selectedStockIds]);
  const effectiveStockList = selectedStockIds.length > 0
    ? selectedStockIds
    : selectedCategoryStockIds.length > 0
    ? selectedCategoryStockIds
    : parseStocks(stockText);
  const effectiveMarketType = selectedStockIds.length > 0 || selectedCategoryStockIds.length > 0 ? "Custom" : marketType;
  const batchCount = chunkStockIds(effectiveStockList, batchSize).length;
  const scanId = getScanId(result);
  const scannedCount = result?.counts?.scanned ?? result?.rawResults?.length ?? result?.raw_results?.length;
  const visibleCandidateCount = allResults.length;
  const rawResultCount = result?.rawResults?.length ?? result?.raw_results?.length;
  const hasScanOutput = Boolean(result);
  const hasNoCandidates = hasScanOutput && visibleCandidateCount === 0;
  const latestRecentScan = recentScans[0];
  const cacheStatus = result?.cache?.status;
  const aList = getList(result, "aList");
  const bList = getList(result, "bList");
  const avoidList = getList(result, "avoidList");
  const decisionCandidates = [
    ...aList.map((item) => ({ item, section: "aList" as ResultSection })),
    ...bList.map((item) => ({ item, section: "bList" as ResultSection })),
    ...avoidList.slice(0, 2).map((item) => ({ item, section: "avoidList" as ResultSection }))
  ].slice(0, 8);
  const scopeLabel = selectedStockIds.length > 0
    ? `手選 ${formatNumber(selectedStockIds.length)} 檔`
    : selectedCategories.length > 0
    ? `${selectedCategories.slice(0, 2).map((category) => category.label).join("、")}${selectedCategories.length > 2 ? " 等" : ""}`
    : MARKET_LABELS[marketType];
  const plannedSingleScanCount = Math.min(effectiveStockList.length || maxStocks, maxStocks);
  const latestCacheEntry = cacheEntries[0];

  const loadTodayCache = useCallback(async () => {
    setCacheError("");
    setIsCacheLoading(true);

    try {
      const response = await fetch(`/api/after-market-screening/cache?date=${encodeURIComponent(date)}&limit=100`);
      const payload = await response.json().catch(() => null);
      if (!response.ok) {
        throw new Error(payload?.error ?? `讀取當日快取 API 回應 ${response.status}`);
      }
      setCacheEntries(Array.isArray(payload?.entries) ? payload.entries as DailyCacheSummary[] : []);
    } catch (cacheLoadError) {
      setCacheError(cacheLoadError instanceof Error ? cacheLoadError.message : "讀取當日快取失敗。");
    } finally {
      setIsCacheLoading(false);
    }
  }, [date]);

  function toggleCategory(categoryId: string) {
    setSelectedCategoryIds((currentIds) =>
      currentIds.includes(categoryId)
        ? currentIds.filter((id) => id !== categoryId)
        : [...currentIds, categoryId]
    );
  }

  function toggleStock(stockId: string) {
    setSelectedStockIds((currentIds) =>
      currentIds.includes(stockId)
        ? currentIds.filter((id) => id !== stockId)
        : [...currentIds, stockId].sort((left, right) => left.localeCompare(right, "en-US"))
    );
  }

  function addFilteredStocks() {
    const nextIds = new Set(selectedStockIds);
    filteredStockOptions.forEach((stock) => nextIds.add(stock.code));
    setSelectedStockIds(Array.from(nextIds).sort((left, right) => left.localeCompare(right, "en-US")));
  }

  function selectAllStocks() {
    setSelectedCategoryIds([]);
    setSelectedStockIds(stockOptions.map((stock) => stock.code));
    setStockQuery("");
  }

  function selectPresetMarket(nextMarketType: MarketType) {
    setSelectedCategoryIds([]);
    setSelectedStockIds([]);
    setMarketType(nextMarketType);
  }

  function applyStrategyPreset(presetId: string) {
    const preset = STRATEGY_PRESETS.find((item) => item.id === presetId);
    if (!preset) {
      return;
    }
    setStrategyPresetId(preset.id);
    setProfile(preset.profile);
    setWeights(preset.weights);
  }

  function updateWeight(key: keyof WeightConfig, value: number) {
    setStrategyPresetId("custom");
    setWeights((currentWeights) => ({
      ...currentWeights,
      [key]: Math.max(0, Math.min(100, Math.floor(value || 0)))
    }));
  }

  function selectCategoryGroup(group: "市場" | "產業") {
    const categoryIds = stockCategories
      .filter((category) => category.group === group)
      .map((category) => category.id);
    setSelectedCategoryIds(categoryIds);
  }

  async function requestScan(stockList: string[]) {
    const safeMaxStocks = Math.max(1, Math.min(2000, Math.floor(stockList.length || maxStocks || 1)));
    const requestStockList = stockList.length > 0 ? stockList : undefined;
    const response = await fetch("/api/after-market-screening/scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        date,
        marketType: effectiveMarketType,
        stockList: requestStockList,
        profile,
        maxStocks: safeMaxStocks,
        includeRiskList,
        weights
      })
    });

    const payload = await response.json().catch(() => null);
    if (!response.ok) {
      throw new Error(payload?.error ?? `盤後篩選 API 回應 ${response.status}`);
    }

    return payload as ScreeningResponse;
  }

  async function runScan() {
    setError("");
    setReportError("");
    setBatchRuns([]);
    setResult(null);
    setIsLoading(true);

    try {
      setResult(await requestScan(effectiveStockList.slice(0, Math.max(1, Math.min(2000, Math.floor(maxStocks || 1))))));
      await loadTodayCache();
    } catch (scanError) {
      setError(scanError instanceof Error ? scanError.message : "盤後篩選失敗，請稍後再試。");
    } finally {
      setIsLoading(false);
    }
  }

  async function runBatchScan() {
    setError("");
    setReportError("");
    setBatchRuns([]);
    setResult(null);
    setIsLoading(true);

    const chunks = chunkStockIds(effectiveStockList, batchSize);
    const responses: ScreeningResponse[] = [];

    try {
      for (let index = 0; index < chunks.length; index += 1) {
        const payload = await requestScan(chunks[index]);
        responses.push(payload);
        setBatchRuns((currentRuns) => [
          ...currentRuns,
          {
            batchIndex: index + 1,
            totalBatches: chunks.length,
            scanId: getScanId(payload),
            cacheStatus: payload.cache?.status ?? "unknown",
            scanned: payload.counts?.scanned ?? 0
          }
        ]);
      }
      setResult(mergeBatchResponses(responses, date, profile));
      await loadTodayCache();
    } catch (scanError) {
      setError(scanError instanceof Error ? scanError.message : "分批掃描失敗，已完成的批次仍保留在當日 cache。");
      if (responses.length > 0) {
        setResult(mergeBatchResponses(responses, date, profile));
        await loadTodayCache();
      }
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
      <div className="panel after-market-command-center">
        <div className="after-market-command-title">
          <div>
            <p className="eyebrow">Daily Workflow</p>
            <h2 id="after-market-title">盤後選股操作台</h2>
          </div>
          <div className="after-market-command-meta">
            <label>
              日期
              <input type="date" value={date} onChange={(event) => setDate(event.target.value)} />
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
          </div>
        </div>

        <div className="after-market-mode-switch" aria-label="功能分類">
          <button
            type="button"
            className={workflowMode === "known-stock" ? "active" : ""}
            onClick={() => setWorkflowMode("known-stock")}
          >
            <strong>已知股票全面分析</strong>
            <span>輸入代碼或名稱，檢查策略、風險與操作選擇</span>
          </button>
          <button
            type="button"
            className={workflowMode === "strategy-scan" ? "active" : ""}
            onClick={() => setWorkflowMode("strategy-scan")}
          >
            <strong>分類策略組合掃描</strong>
            <span>選分類與策略組合，分批掃描並使用當日 cache</span>
          </button>
        </div>

        <div className="after-market-workflow-cards" aria-label="盤後篩選流程">
          <article>
            <span>1</span>
            <div>
              <strong>{scopeLabel}</strong>
              <small>有效股票池 {formatNumber(effectiveStockList.length)} 檔</small>
            </div>
          </article>
          <article>
            <span>2</span>
            <div>
              <strong>{cacheEntries.length > 0 ? `${formatNumber(cacheEntries.length)} 批已掃` : "尚無當日快取"}</strong>
              <small>
                {latestCacheEntry
                  ? `${formatDateTime(latestCacheEntry.updatedAt)} · B ${formatNumber(latestCacheEntry.bList)} / 避 ${formatNumber(latestCacheEntry.avoidList)}`
                  : "刷新後可載入終端機或網頁掃描"}
              </small>
            </div>
          </article>
          <article>
            <span>3</span>
            <div>
              <strong>{batchCount > 1 ? `${formatNumber(batchCount)} 批` : "單批掃描"}</strong>
              <small>每批 {formatNumber(batchSize)} 檔，重跑會優先讀 cache</small>
            </div>
          </article>
        </div>

        <div className="after-market-quick-actions">
          {workflowMode === "strategy-scan" ? (
            <>
              <button type="button" className="secondary-button" onClick={() => selectPresetMarket("TEST")}>
                測試池
              </button>
              <button type="button" className="secondary-button" onClick={() => selectPresetMarket("Tw50")}>
                台灣50
              </button>
              <button type="button" className="secondary-button" onClick={selectAllStocks}>
                全部股票
              </button>
            </>
          ) : null}
          <button type="button" className="secondary-button" onClick={loadTodayCache} disabled={isCacheLoading}>
            {isCacheLoading ? "讀取中..." : "刷新今日快取"}
          </button>
          <button type="button" onClick={runScan} disabled={isLoading}>
            {isLoading ? "掃描中..." : `掃描 ${formatNumber(plannedSingleScanCount)} 檔`}
          </button>
          <button type="button" onClick={runBatchScan} disabled={isLoading || effectiveStockList.length === 0}>
            {isLoading ? "分批中..." : "分批掃描全部"}
          </button>
        </div>
      </div>

      <div className="panel after-market-settings">
        <div className="panel-header">
          <div>
            <p className="eyebrow">{workflowMode === "known-stock" ? "Known Stock" : "Strategy Scan"}</p>
            <h2>{workflowMode === "known-stock" ? "已知股票全面分析" : "分類與策略組合"}</h2>
          </div>
          <div className="status-pill">{formatNumber(effectiveStockList.length)} 檔</div>
        </div>

        <div className="after-market-strategy-presets">
          {STRATEGY_PRESETS.map((preset) => (
            <button
              key={preset.id}
              type="button"
              className={strategyPresetId === preset.id ? "active" : ""}
              onClick={() => applyStrategyPreset(preset.id)}
            >
              <strong>{preset.label}</strong>
              <span>{preset.description}</span>
            </button>
          ))}
        </div>

        <div className="after-market-weight-grid">
          <label>
            技術
            <input
              type="number"
              min={0}
              max={100}
              value={weights.technical}
              onChange={(event) => updateWeight("technical", Number(event.target.value))}
            />
          </label>
          <label>
            籌碼
            <input
              type="number"
              min={0}
              max={100}
              value={weights.chip}
              onChange={(event) => updateWeight("chip", Number(event.target.value))}
            />
          </label>
          <label>
            量能
            <input
              type="number"
              min={0}
              max={100}
              value={weights.volume}
              onChange={(event) => updateWeight("volume", Number(event.target.value))}
            />
          </label>
          <label>
            相對強弱
            <input
              type="number"
              min={0}
              max={100}
              value={weights.relativeStrength}
              onChange={(event) => updateWeight("relativeStrength", Number(event.target.value))}
            />
          </label>
        </div>

        <div className="after-market-control-grid">
          {workflowMode === "strategy-scan" ? (
            <label>
              快速股票池
              <select value={marketType} onChange={(event) => setMarketType(event.target.value as MarketType)}>
                {Object.entries(MARKET_LABELS).map(([value, label]) => (
                  <option key={value} value={value}>
                    {label}
                  </option>
                ))}
              </select>
            </label>
          ) : null}

          <label>
            單次掃描上限
            <input
              min={1}
              max={2000}
              type="number"
              value={maxStocks}
              onChange={(event) => setMaxStocks(Number(event.target.value))}
            />
          </label>

          <label>
            每批檔數
            <input
              type="number"
              min={1}
              max={500}
              value={batchSize}
              onChange={(event) => setBatchSize(Number(event.target.value))}
            />
          </label>
        </div>

        {workflowMode === "known-stock" ? (
          <div className="after-market-known-stock-panel">
            <div>
              <h3>輸入已知股票</h3>
              <p>輸入代碼、名稱或產業關鍵字，可一次勾多檔做全面分析與策略檢查。</p>
            </div>
            <div className="after-market-stock-search">
              <input
                value={stockQuery}
                onChange={(event) => setStockQuery(event.target.value)}
                placeholder="例：2330、台積電、半導體"
              />
              <button type="button" className="secondary-button" onClick={addFilteredStocks}>
                加入搜尋結果
              </button>
            </div>
            <div className="after-market-stock-list">
              {filteredStockOptions.map((stock) => (
                <label key={stock.code} className="after-market-stock-option">
                  <input
                    type="checkbox"
                    checked={selectedStockSet.has(stock.code)}
                    onChange={() => toggleStock(stock.code)}
                  />
                  <strong>{stock.code} {stock.name}</strong>
                  <small>{stock.market} / {stock.industry}</small>
                </label>
              ))}
            </div>
          </div>
        ) : null}

        {workflowMode === "strategy-scan" && stockCategories.length > 0 ? (
          <div className="after-market-category-panel">
            <div className="after-market-category-header">
              <div>
                <h3>股票池選擇器</h3>
                <p>
                  已選 {selectedCategories.length} 類、手選 {selectedStockIds.length} 檔；有效股票池 {effectiveStockList.length} 檔。
                  同一天同批次重跑會先讀資料庫快取。
                </p>
              </div>
              <div className="after-market-category-actions">
                <button type="button" className="secondary-button" onClick={() => selectCategoryGroup("市場")}>
                  全市場類
                </button>
                <button type="button" className="secondary-button" onClick={selectAllStocks}>
                  全部股票
                </button>
                <button type="button" className="secondary-button" onClick={() => {
                  setSelectedCategoryIds([]);
                  setSelectedStockIds([]);
                }}>
                  清除
                </button>
              </div>
            </div>

            <div className="after-market-category-group">
              <span>市場</span>
              <div className="after-market-category-list">
                {marketCategories.map((category) => (
                  <label key={category.id} className="after-market-category-option">
                    <input
                      type="checkbox"
                      checked={selectedCategoryIds.includes(category.id)}
                      onChange={() => toggleCategory(category.id)}
                    />
                    <strong>{category.label}</strong>
                    <small>{formatNumber(category.count)} 檔</small>
                  </label>
                ))}
              </div>
            </div>

            <div className="after-market-category-group">
              <span>產業</span>
              <div className="after-market-category-list compact">
                {industryCategories.map((category) => (
                  <label key={category.id} className="after-market-category-option">
                    <input
                      type="checkbox"
                      checked={selectedCategoryIds.includes(category.id)}
                      onChange={() => toggleCategory(category.id)}
                    />
                    <strong>{category.label}</strong>
                    <small>{formatNumber(category.count)}</small>
                  </label>
                ))}
              </div>
            </div>

            <div className="after-market-category-group">
              <span>搜尋代碼 / 名稱 / 產業</span>
              <div className="after-market-stock-search">
                <input
                  value={stockQuery}
                  onChange={(event) => setStockQuery(event.target.value)}
                  placeholder="例：2330、台積電、半導體"
                />
                <button type="button" className="secondary-button" onClick={addFilteredStocks}>
                  加入搜尋結果
                </button>
              </div>
              <div className="after-market-stock-list">
                {filteredStockOptions.map((stock) => (
                  <label key={stock.code} className="after-market-stock-option">
                    <input
                      type="checkbox"
                      checked={selectedStockSet.has(stock.code)}
                      onChange={() => toggleStock(stock.code)}
                    />
                    <strong>{stock.code} {stock.name}</strong>
                    <small>{stock.market} / {stock.industry}</small>
                  </label>
                ))}
              </div>
            </div>

            {selectedStockIds.length > 0 ? (
              <div className="after-market-selected-strip">
                <span>手選清單</span>
                <strong>{selectedStockIds.slice(0, 16).join(", ")}{selectedStockIds.length > 16 ? " ..." : ""}</strong>
                <button type="button" className="secondary-button" onClick={() => setSelectedStockIds([])}>
                  清除手選
                </button>
              </div>
            ) : null}
          </div>
        ) : null}

        <label className="after-market-custom-list">
          自訂標的
          <textarea
            rows={3}
            value={stockText}
            disabled={selectedCategoryStockIds.length > 0}
            onChange={(event) => setStockText(event.target.value)}
            placeholder={selectedCategoryStockIds.length > 0 ? "已使用上方分類股票池" : "例：2330, 2317, 2454"}
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
        </div>

        <div className="after-market-batch-panel">
          <div>
            <strong>批次狀態</strong>
            <p>
              目前 {formatNumber(effectiveStockList.length)} 檔，批次大小 {formatNumber(batchSize)}，
              預估 {formatNumber(batchCount)} 批；每批完成會寫入當天 cache。
            </p>
          </div>
        </div>

        {batchRuns.length > 0 ? (
          <div className="after-market-batch-log">
            {batchRuns.map((run) => (
              <div key={`${run.batchIndex}-${run.scanId}`}>
                <span>{run.batchIndex}/{run.totalBatches}</span>
                <strong>{run.cacheStatus}</strong>
                <small>{run.scanId} · 掃描 {formatNumber(run.scanned)}</small>
              </div>
            ))}
          </div>
        ) : null}

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
          <div>
            <span>當日快取</span>
            <strong>
              {cacheStatus === "hit"
                ? `命中 · ${result?.cache?.storageMode ?? "cache"}`
                : cacheStatus === "miss"
                  ? `已寫入 · ${result?.cache?.storageMode ?? "cache"}`
                  : "尚未檢查"}
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

        <div className="after-market-cache-panel">
          <div className="after-market-recent-runs-header">
            <h3>今日已掃批次</h3>
            <button type="button" className="secondary-button" onClick={loadTodayCache} disabled={isCacheLoading}>
              {isCacheLoading ? "讀取中..." : "刷新"}
            </button>
          </div>
          {cacheError ? <p className="feedback-message error">{cacheError}</p> : null}
          {cacheEntries.length > 0 ? (
            <div className="after-market-cache-list">
              {cacheEntries.map((entry) => (
                <button
                  key={`${entry.scanId}-${entry.updatedAt}`}
                  type="button"
                  className={entry.scanId === scanId ? "after-market-cache-entry active" : "after-market-cache-entry"}
                  disabled={Boolean(loadingReportId)}
                  onClick={() => loadReport(entry.scanId)}
                >
                  <span>{formatDateTime(entry.updatedAt)}</span>
                  <strong>{entry.scanId}</strong>
                  <small>
                    {entry.marketType} · {entry.profile} · 掃描 {formatNumber(entry.scanned || entry.stockCount)} · A/B/避{" "}
                    {formatNumber(entry.aList)}/{formatNumber(entry.bList)}/{formatNumber(entry.avoidList)}
                  </small>
                  <em>{entry.storageMode}</em>
                </button>
              ))}
            </div>
          ) : (
            <p className="empty-state">
              {isCacheLoading ? "正在讀取當日資料庫 cache。" : "這個日期目前沒有已掃批次。"}
            </p>
          )}
        </div>

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

            {decisionCandidates.length > 0 ? (
              <div className="after-market-decision-panel">
                <div className="after-market-recent-runs-header">
                  <h3>一眼判斷：要不要進入個股分析</h3>
                  <span>{decisionCandidates.length} 檔重點</span>
                </div>
                <div className="after-market-decision-grid">
                  {decisionCandidates.map(({ item, section }) => {
                    const decision = getDecision(item, section);
                    return (
                      <article key={`${section}-${item.stockId}`} className={`after-market-decision-card ${decision.tone}`}>
                        <div>
                          <span>{section === "aList" ? "A 級" : section === "bList" ? "B 級" : "避開"}</span>
                          <strong>{item.stockId} {item.stockName ?? ""}</strong>
                        </div>
                        <b>{formatNumber(item.score)}</b>
                        <p>{decision.label}</p>
                        <small>{decision.detail}</small>
                        <a href={`/research?ticker=${encodeURIComponent(item.stockId)}`}>進入個股分析</a>
                      </article>
                    );
                  })}
                </div>
              </div>
            ) : null}

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
