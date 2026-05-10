import YahooFinance from "yahoo-finance2";

type MarketType = "TEST" | "Tw50" | "All" | "TSE" | "OTC" | "Custom";

export type CloudPriceBar = {
  date: string;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
};

export type CloudStockPayload = {
  stockId: string;
  stockName: string;
  bars: CloudPriceBar[];
};

const yahooFinance = new YahooFinance({
  suppressNotices: ["yahooSurvey", "ripHistorical"]
});

const TEST_STOCKS = ["2330", "2317", "2454", "2303", "2603"];

const TW50_STOCKS = [
  "2330",
  "2317",
  "2454",
  "2308",
  "2382",
  "2412",
  "2881",
  "2882",
  "2891",
  "3711",
  "2303",
  "2886",
  "1216",
  "1303",
  "1301",
  "2002",
  "2603",
  "5871",
  "5880",
  "3045"
];

const ALL_FALLBACK_STOCKS = Array.from(new Set([...TW50_STOCKS, "2357", "2379", "3034", "3661", "6669"]));

function toNumber(value: unknown): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

function symbolCandidates(stockId: string) {
  const normalized = stockId.trim().toUpperCase();
  if (!normalized) {
    return [];
  }
  if (normalized.endsWith(".TW") || normalized.endsWith(".TWO")) {
    return [normalized];
  }
  if (/^\d+$/.test(normalized)) {
    return [`${normalized}.TW`, `${normalized}.TWO`];
  }
  return [normalized];
}

export function resolveCloudStockPool(marketType: MarketType, stockList?: string[], maxStocks = 80) {
  const custom = (stockList ?? []).map((item) => item.trim()).filter(Boolean);
  const pool = custom.length > 0
    ? custom
    : marketType === "Tw50"
      ? TW50_STOCKS
      : marketType === "All" || marketType === "TSE" || marketType === "OTC"
        ? ALL_FALLBACK_STOCKS
        : TEST_STOCKS;

  return Array.from(new Set(pool)).slice(0, Math.max(1, Math.min(2000, Math.floor(maxStocks || 1))));
}

export async function mapWithConcurrency<T, R>(
  items: T[],
  concurrency: number,
  worker: (item: T, index: number) => Promise<R>
) {
  const results = new Array<R>(items.length);
  const safeConcurrency = Math.max(1, Math.min(items.length || 1, Math.floor(concurrency || 1)));
  let cursor = 0;

  async function runWorker() {
    while (cursor < items.length) {
      const index = cursor;
      cursor += 1;
      results[index] = await worker(items[index], index);
    }
  }

  await Promise.all(Array.from({ length: safeConcurrency }, runWorker));
  return results;
}

export async function fetchCloudStock(stockId: string): Promise<CloudStockPayload> {
  let lastError: unknown;

  for (const symbol of symbolCandidates(stockId)) {
    try {
      const [quote, chart] = await Promise.all([
        yahooFinance.quote(symbol),
        yahooFinance.chart(symbol, {
          period1: new Date(Date.now() - 1000 * 60 * 60 * 24 * 220),
          period2: new Date(),
          interval: "1d"
        })
      ]);

      const bars = (chart.quotes ?? [])
        .map((item) => {
          const open = toNumber(item.open);
          const high = toNumber(item.high);
          const low = toNumber(item.low);
          const close = toNumber(item.close);
          const volume = toNumber(item.volume);
          if (open === null || high === null || low === null || close === null || volume === null) {
            return null;
          }
          return {
            date: item.date.toISOString().slice(0, 10),
            open,
            high,
            low,
            close,
            volume
          };
        })
        .filter((item): item is CloudPriceBar => Boolean(item));

      return {
        stockId,
        stockName: quote.shortName ?? quote.longName ?? stockId,
        bars
      };
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError instanceof Error ? lastError : new Error(`Unable to fetch ${stockId}`);
}

export function average(values: number[]) {
  if (values.length === 0) {
    return 0;
  }
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

export function movingAverage(values: number[], window: number) {
  if (values.length < window) {
    return Number.NaN;
  }
  return average(values.slice(-window));
}

export function previousMovingAverage(values: number[], window: number) {
  if (values.length <= window) {
    return Number.NaN;
  }
  return average(values.slice(-(window + 1), -1));
}

export function latestBar(bars: CloudPriceBar[]) {
  return bars[bars.length - 1];
}
