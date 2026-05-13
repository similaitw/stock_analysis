import { promises as fs } from "fs";
import path from "path";

import { normalizeTaiwanStockCode } from "@/lib/taiwan-stock-names";

export type AfterMarketStockCategory = {
  id: string;
  group: "市場" | "產業";
  label: string;
  description: string;
  stockIds: string[];
  count: number;
};

export type AfterMarketStockOption = {
  code: string;
  name: string;
  market: string;
  industry: string;
  searchText: string;
};

type StockUniverseRow = {
  code: string;
  name: string;
  market: string;
  industry: string;
};

const STOCK_LIST_PATH = path.join(process.cwd(), "data", "stock_list.csv");

function parseCsvLine(line: string) {
  return line.split(",").map((item) => item.trim());
}

function toCategoryId(group: string, value: string) {
  return `${group}:${encodeURIComponent(value)}`;
}

async function readStockUniverseRows(): Promise<StockUniverseRow[]> {
  try {
    const raw = await fs.readFile(STOCK_LIST_PATH, "utf-8");
    return raw
      .split(/\r?\n/)
      .slice(1)
      .map(parseCsvLine)
      .map(([code, name, market, industry]) => ({
        code: normalizeTaiwanStockCode(code ?? ""),
        name: name ?? "",
        market: market || "未分類",
        industry: industry || "未分類"
      }))
      .filter((row) => /^\d{4,6}$/.test(row.code) && row.name);
  } catch {
    return [];
  }
}

function pushIntoMap(map: Map<string, string[]>, key: string, stockId: string) {
  const list = map.get(key) ?? [];
  list.push(stockId);
  map.set(key, list);
}

function uniqueSortedStockIds(stockIds: string[]) {
  return Array.from(new Set(stockIds)).sort((left, right) => left.localeCompare(right, "en-US"));
}

export async function getAfterMarketStockCategories(): Promise<AfterMarketStockCategory[]> {
  const rows = await readStockUniverseRows();
  const marketMap = new Map<string, string[]>();
  const industryMap = new Map<string, string[]>();

  for (const row of rows) {
    pushIntoMap(marketMap, row.market, row.code);
    pushIntoMap(industryMap, row.industry, row.code);
  }

  const marketCategories = Array.from(marketMap.entries())
    .sort(([left], [right]) => left.localeCompare(right, "zh-TW"))
    .map(([market, stockIds]) => {
      const uniqueStockIds = uniqueSortedStockIds(stockIds);
      return {
        id: toCategoryId("market", market),
        group: "市場" as const,
        label: market,
        description: `${market} 股票池`,
        stockIds: uniqueStockIds,
        count: uniqueStockIds.length
      };
    });

  const industryCategories = Array.from(industryMap.entries())
    .sort(([, leftIds], [, rightIds]) => rightIds.length - leftIds.length)
    .map(([industry, stockIds]) => {
      const uniqueStockIds = uniqueSortedStockIds(stockIds);
      return {
        id: toCategoryId("industry", industry),
        group: "產業" as const,
        label: industry,
        description: `${industry} 產業股票池`,
        stockIds: uniqueStockIds,
        count: uniqueStockIds.length
      };
    });

  return [...marketCategories, ...industryCategories];
}

export async function getAfterMarketStockOptions(): Promise<AfterMarketStockOption[]> {
  const rows = await readStockUniverseRows();
  return rows
    .map((row) => ({
      code: row.code,
      name: row.name,
      market: row.market,
      industry: row.industry,
      searchText: `${row.code} ${row.name} ${row.market} ${row.industry}`.toLowerCase()
    }))
    .sort((left, right) => left.code.localeCompare(right.code, "en-US"));
}
