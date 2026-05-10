import YahooFinance from "yahoo-finance2";

import { getTaiwanStockDisplayName, getTaiwanStockInfo } from "@/lib/taiwan-stock-names";

export type ResearchSnapshot = {
  ticker: string;
  name: string;
  industry: string;
  description: string;
  currentPrice: number | null;
  fundamentals: Record<string, number | string>;
  history: Array<{ date: string; close: number | null; volume: number | null }>;
};

const yahooFinance = new YahooFinance({
  suppressNotices: ["yahooSurvey", "ripHistorical"]
});

function toNumber(value: unknown): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function toPercent(value: unknown): number | null {
  const numericValue = toNumber(value);
  if (numericValue === null) {
    return null;
  }

  return Number((numericValue * 100).toFixed(2));
}

function compactFundamentals(
  entries: Array<[string, number | string | null]>
): Record<string, number | string> {
  const result: Record<string, number | string> = {};

  for (const [key, value] of entries) {
    if (value !== null && value !== "") {
      result[key] = value;
    }
  }

  return result;
}

function buildTickerCandidates(ticker: string): string[] {
  const normalizedTicker = ticker.trim().toUpperCase();

  if (!normalizedTicker) {
    return [];
  }

  if (normalizedTicker.endsWith(".TW") || normalizedTicker.endsWith(".TWO")) {
    return [normalizedTicker];
  }

  if (/^\d+$/.test(normalizedTicker)) {
    return [`${normalizedTicker}.TW`, `${normalizedTicker}.TWO`];
  }

  return [normalizedTicker];
}

async function fetchSymbolSnapshot(ticker: string, symbol: string): Promise<ResearchSnapshot> {
  const [quote, summary, chart] = await Promise.all([
    yahooFinance.quote(symbol),
    yahooFinance.quoteSummary(symbol, {
      modules: ["price", "summaryProfile", "financialData", "defaultKeyStatistics", "summaryDetail"]
    }),
    yahooFinance.chart(symbol, {
      period1: new Date(Date.now() - 1000 * 60 * 60 * 24 * 180),
      period2: new Date(),
      interval: "1d"
    })
  ]);

  const fundamentals = compactFundamentals([
    ["Revenue YoY", toPercent(summary.financialData?.revenueGrowth)],
    ["ROE", toPercent(summary.financialData?.returnOnEquity)],
    ["PER", toNumber(summary.summaryDetail?.trailingPE ?? summary.defaultKeyStatistics?.forwardPE)],
    ["PBR", toNumber(summary.defaultKeyStatistics?.priceToBook)],
    ["EPS", toNumber(summary.defaultKeyStatistics?.trailingEps)],
    ["Margin", toPercent(summary.financialData?.profitMargins)],
    ["Yield", toPercent(summary.summaryDetail?.dividendYield)]
  ]);

  const localInfo = getTaiwanStockInfo(ticker);

  return {
    ticker,
    name: getTaiwanStockDisplayName(ticker, quote.shortName ?? quote.longName ?? symbol),
    industry: localInfo?.industry ?? summary.summaryProfile?.industry ?? "-",
    description: summary.summaryProfile?.longBusinessSummary ?? "",
    currentPrice: toNumber(summary.price?.regularMarketPrice ?? quote.regularMarketPrice),
    fundamentals,
    history: (chart.quotes ?? []).slice(-60).map((item) => ({
      date: item.date.toISOString().slice(0, 10),
      close: toNumber(item.close),
      volume: toNumber(item.volume)
    }))
  };
}

export async function fetchResearchSnapshot(ticker: string): Promise<ResearchSnapshot> {
  const normalizedTicker = ticker.trim();
  const candidates = buildTickerCandidates(normalizedTicker);

  if (candidates.length === 0) {
    throw new Error("Ticker is required.");
  }

  let lastError: unknown;

  for (const candidate of candidates) {
    try {
      return await fetchSymbolSnapshot(normalizedTicker, candidate);
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError instanceof Error ? lastError : new Error(`Unable to fetch research data for ${ticker}.`);
}
