import {
  average,
  fetchCloudStock,
  latestBar,
  mapWithConcurrency,
  movingAverage,
  previousMovingAverage,
  resolveCloudStockPool,
  type CloudPriceBar
} from "@/lib/cloud-market-scanner";
import type {
  AfterMarketReportResult,
  AfterMarketScanRequest,
  AfterMarketScanResult,
  AfterMarketScreeningItem
} from "@/lib/after-market-screening";
import { getTaiwanStockDisplayName } from "@/lib/taiwan-stock-names";

type ScoredItem = AfterMarketScreeningItem & {
  bucket: "A" | "B" | "avoid" | "hidden";
};

type CachedCloudReport = AfterMarketReportResult & {
  cachedAt: number;
};

const CLOUD_REPORT_CACHE_TTL_MS = 1000 * 60 * 60;
const CLOUD_REPORT_CACHE_LIMIT = 20;
const cloudReportCache = new Map<string, CachedCloudReport>();

function makeScanId(date: string) {
  return `cloud_after_market_${date.replaceAll("-", "")}_${Math.random().toString(16).slice(2, 10)}`;
}

function rememberCloudReport(report: AfterMarketScanResult) {
  const cached = {
    ...report,
    rawResults: {
      source: "cloud-cache",
      cachedAt: new Date().toISOString()
    },
    nextDayWatchlist: [
      ...report.aList,
      ...(report.bList ?? [])
    ].slice(0, 20),
    cachedAt: Date.now()
  };

  cloudReportCache.set(report.scanId, cached);

  if (cloudReportCache.size > CLOUD_REPORT_CACHE_LIMIT) {
    const oldestKey = cloudReportCache.keys().next().value as string | undefined;
    if (oldestKey) {
      cloudReportCache.delete(oldestKey);
    }
  }
}

export function getCachedCloudAfterMarketReport(scanId: string): AfterMarketReportResult | null {
  const report = cloudReportCache.get(scanId);
  if (!report) {
    return null;
  }
  if (Date.now() - report.cachedAt > CLOUD_REPORT_CACHE_TTL_MS) {
    cloudReportCache.delete(scanId);
    return null;
  }

  const { cachedAt, ...payload } = report;
  void cachedAt;
  return payload;
}

function pctChange(values: number[], days: number) {
  if (values.length <= days) {
    return 0;
  }
  const start = values[values.length - 1 - days];
  const end = values[values.length - 1];
  return start ? (end / start) - 1 : 0;
}

function ema(values: number[], period: number) {
  const multiplier = 2 / (period + 1);
  const result: number[] = [];
  for (const value of values) {
    if (result.length === 0) {
      result.push(value);
    } else {
      result.push((value - result[result.length - 1]) * multiplier + result[result.length - 1]);
    }
  }
  return result;
}

function rsi(values: number[], period = 14) {
  if (values.length <= period) {
    return Number.NaN;
  }
  const changes = values.slice(1).map((value, index) => value - values[index]);
  const recent = changes.slice(-period);
  const gains = recent.map((value) => Math.max(value, 0));
  const losses = recent.map((value) => Math.abs(Math.min(value, 0)));
  const avgGain = average(gains);
  const avgLoss = average(losses);
  if (avgLoss === 0) {
    return 100;
  }
  return 100 - (100 / (1 + (avgGain / avgLoss)));
}

function stochasticK(bars: CloudPriceBar[], period = 9) {
  if (bars.length < period) {
    return Number.NaN;
  }
  const recent = bars.slice(-period);
  const high = Math.max(...recent.map((bar) => bar.high));
  const low = Math.min(...recent.map((bar) => bar.low));
  const close = latestBar(bars).close;
  return high === low ? 50 : ((close - low) / (high - low)) * 100;
}

function validateBars(bars: CloudPriceBar[]) {
  if (bars.length < 45) {
    return "insufficient history: need at least 45 rows";
  }

  const latest = latestBar(bars);
  const avgVolume20 = average(bars.slice(-20).map((bar) => bar.volume));
  const volumeThresholds = avgVolume20 > 100_000
    ? { average: 500_000, latest: 300_000 }
    : { average: 500, latest: 300 };

  if (latest.close < 10) {
    return "price below 10";
  }
  if (avgVolume20 < volumeThresholds.average) {
    return "20-day average volume below liquidity threshold";
  }
  if (latest.volume < volumeThresholds.latest) {
    return "latest volume below liquidity threshold";
  }
  return "";
}

function scoreBars(stockId: string, stockName: string, bars: CloudPriceBar[], marketBars?: CloudPriceBar[]): ScoredItem {
  const closes = bars.map((bar) => bar.close);
  const highs = bars.map((bar) => bar.high);
  const volumes = bars.map((bar) => bar.volume);
  const latest = latestBar(bars);
  const previous = bars[bars.length - 2];
  const ma5 = movingAverage(closes, 5);
  const ma20 = movingAverage(closes, 20);
  const ma60 = movingAverage(closes, 60);
  const previousMa5 = previousMovingAverage(closes, 5);
  const previousMa20 = previousMovingAverage(closes, 20);
  const avgVolume20 = average(volumes.slice(-20));

  let technicalScore = 0;
  let volumeScore = 0;
  let relativeStrengthScore = 0;
  let riskScore = 0;
  const reasons: string[] = [];
  const risks: string[] = [];

  if (latest.close > ma5 && ma5 > ma20 && ma20 > ma60) {
    technicalScore += 10;
    reasons.push("均線多頭排列");
  }
  if (latest.close > Math.max(...highs.slice(-21, -1))) {
    technicalScore += 10;
    reasons.push("突破 20 日高");
  }
  if (ma5 > ma20 && previousMa5 <= previousMa20) {
    technicalScore += 6;
    reasons.push("均線黃金交叉");
  }

  const ema12 = ema(closes, 12);
  const ema26 = ema(closes, 26);
  const dif = ema12.map((value, index) => value - (ema26[index] ?? value));
  const signal = ema(dif, 9);
  if (dif.at(-1)! > signal.at(-1)! && dif.at(-2)! <= signal.at(-2)!) {
    technicalScore += 6;
    reasons.push("MACD 黃金交叉");
  }

  const currentK = stochasticK(bars);
  const previousK = stochasticK(bars.slice(0, -1));
  if (currentK > 50 && previousK <= 50) {
    technicalScore += 4;
    reasons.push("KD 轉強");
  }

  const currentRsi = rsi(closes);
  const previousRsi = rsi(closes.slice(0, -1));
  if (currentRsi > 30 && previousRsi <= 30) {
    technicalScore += 4;
    reasons.push("RSI 低檔轉強");
  }

  const bollingerUpper = ma20 + (Math.sqrt(average(closes.slice(-20).map((value) => (value - ma20) ** 2))) * 2);
  if (latest.close > bollingerUpper) {
    technicalScore += 4;
    reasons.push("布林上軌突破");
  }

  if (latest.volume >= avgVolume20 * 1.5) {
    volumeScore += 8;
    reasons.push("成交量放大");
  }
  if (latest.close >= Math.max(...closes.slice(-20)) && latest.volume >= Math.max(...volumes.slice(-20))) {
    volumeScore += 5;
    reasons.push("價量同步創高");
  }
  if (volumes.slice(-5).every((value, index, source) => index === 0 || value >= source[index - 1] * 0.85)) {
    volumeScore += 4;
    reasons.push("量能維持");
  }

  if (marketBars && marketBars.length >= 21) {
    const marketReturn = pctChange(marketBars.map((bar) => bar.close), 20);
    const stockReturn = pctChange(closes, 20);
    if (stockReturn > marketReturn) {
      relativeStrengthScore += 6;
      reasons.push("強於大盤");
    }
    if (marketReturn < 0 && latest.close > ma20) {
      relativeStrengthScore += 3;
      reasons.push("大盤弱勢仍守月線");
    }
  } else if (latest.close > ma20) {
    relativeStrengthScore += 3;
    reasons.push("守住月線");
  }

  const range = Math.max(latest.high - latest.low, 0.01);
  const upperShadow = latest.high - Math.max(latest.open, latest.close);
  if (latest.volume >= avgVolume20 * 2 && upperShadow / range >= 0.45) {
    riskScore -= 20;
    risks.push("爆量長上影");
  }
  if (latest.open > previous.close && latest.close <= latest.low + range * 0.25) {
    riskScore -= 12;
    risks.push("開高走低");
  }
  if (latest.close < ma20) {
    riskScore -= 12;
    risks.push("跌破 MA20");
  }
  if (latest.close < ma60) {
    riskScore -= 20;
    risks.push("跌破 MA60");
  }

  technicalScore = Math.min(40, technicalScore);
  volumeScore = Math.min(15, volumeScore);
  relativeStrengthScore = Math.min(15, relativeStrengthScore);
  const chipScore = 0;
  const score = Math.max(0, Math.round(technicalScore + chipScore + volumeScore + relativeStrengthScore + riskScore));
  const bucket = riskScore <= -30 ? "avoid" : score >= 62 ? "A" : score >= 45 ? "B" : "hidden";

  return {
    stockId,
    stockName,
    score,
    riskScore,
    technicalScore,
    chipScore,
    volumeScore,
    relativeStrengthScore,
    reasons,
    risks,
    nextDayPlan: "觀察是否守住昨高與開盤低點",
    bucket
  };
}

function rank(items: ScoredItem[]) {
  return items
    .sort((left, right) => (right.score - left.score) || (right.riskScore - left.riskScore))
    .map((item, index) => ({ ...item, rank: index + 1 }));
}

export async function runCloudAfterMarketScan(request: AfterMarketScanRequest): Promise<AfterMarketScanResult> {
  const date = request.date ?? new Intl.DateTimeFormat("en-CA", { timeZone: "Asia/Taipei" }).format(new Date());
  const marketType = request.marketType;
  const stockPool = resolveCloudStockPool(marketType, request.stockList, request.maxStocks ?? 80);
  const executedAt = new Date().toISOString();
  const skipped: NonNullable<AfterMarketScanResult["skipped"]> = [];
  const marketPayload = await fetchCloudStock("^TWII").catch(() => null);

  const scanResults = await mapWithConcurrency(stockPool, 6, async (stockId) => {
    try {
      const payload = await fetchCloudStock(stockId);
      const skipReason = validateBars(payload.bars);
      if (skipReason) {
        return { skipped: { stockId, stockName: payload.stockName, skipReason } };
      }
      return { scored: scoreBars(stockId, payload.stockName, payload.bars, marketPayload?.bars) };
    } catch (error) {
      return {
        skipped: {
          stockId,
          stockName: getTaiwanStockDisplayName(stockId),
          skipReason: error instanceof Error ? error.message : "cloud fetch failed"
        }
      };
    }
  });

  const rawResults: ScoredItem[] = [];
  for (const item of scanResults) {
    if (item.scored) {
      rawResults.push(item.scored);
    }
    if (item.skipped) {
      skipped.push(item.skipped);
    }
  }

  const aList = rank(rawResults.filter((item) => item.bucket === "A"));
  const bList = rank(rawResults.filter((item) => item.bucket === "B"));
  const avoidList = request.includeRiskList === false
    ? []
    : rank(rawResults.filter((item) => item.bucket === "avoid"));

  const result = {
    scanId: makeScanId(date),
    executedAt,
    marketType,
    counts: {
      scanned: rawResults.length,
      aList: aList.length,
      bList: bList.length,
      avoidList: avoidList.length,
      skipped: skipped.length
    },
    aList,
    bList,
    avoidList,
    skipped,
    summary: {
      engine: "vercel-node-yahoo-finance",
      note: "Cloud fallback uses Yahoo daily OHLCV and omits chip-data scoring until a managed worker/data source is connected."
    }
  };

  rememberCloudReport(result);
  return result;
}
