import { existsSync, readFileSync } from "fs";
import path from "path";

export type TaiwanStockInfo = {
  code: string;
  name: string;
  market?: string;
  industry?: string;
};

const FALLBACK_STOCK_INFO: Record<string, TaiwanStockInfo> = {
  "1216": { code: "1216", name: "統一", market: "TSE", industry: "食品工業" },
  "1301": { code: "1301", name: "台塑", market: "TSE", industry: "塑膠工業" },
  "1303": { code: "1303", name: "南亞", market: "TSE", industry: "塑膠工業" },
  "2002": { code: "2002", name: "中鋼", market: "TSE", industry: "鋼鐵工業" },
  "2303": { code: "2303", name: "聯電", market: "TSE", industry: "半導體業" },
  "2308": { code: "2308", name: "台達電", market: "TSE", industry: "電子零組件業" },
  "2317": { code: "2317", name: "鴻海", market: "TSE", industry: "其他電子業" },
  "2330": { code: "2330", name: "台積電", market: "TSE", industry: "半導體業" },
  "2357": { code: "2357", name: "華碩", market: "TSE", industry: "電腦及週邊設備業" },
  "2379": { code: "2379", name: "瑞昱", market: "TSE", industry: "半導體業" },
  "2382": { code: "2382", name: "廣達", market: "TSE", industry: "電腦及週邊設備業" },
  "2412": { code: "2412", name: "中華電", market: "TSE", industry: "通信網路業" },
  "2454": { code: "2454", name: "聯發科", market: "TSE", industry: "半導體業" },
  "2603": { code: "2603", name: "長榮", market: "TSE", industry: "航運業" },
  "2881": { code: "2881", name: "富邦金", market: "TSE", industry: "金融保險業" },
  "2882": { code: "2882", name: "國泰金", market: "TSE", industry: "金融保險業" },
  "2886": { code: "2886", name: "兆豐金", market: "TSE", industry: "金融保險業" },
  "2891": { code: "2891", name: "中信金", market: "TSE", industry: "金融保險業" },
  "3034": { code: "3034", name: "聯詠", market: "TSE", industry: "半導體業" },
  "3045": { code: "3045", name: "台灣大", market: "TSE", industry: "通信網路業" },
  "3661": { code: "3661", name: "世芯-KY", market: "TSE", industry: "半導體業" },
  "3711": { code: "3711", name: "日月光投控", market: "TSE", industry: "半導體業" },
  "5871": { code: "5871", name: "中租-KY", market: "TSE", industry: "其他業" },
  "5880": { code: "5880", name: "合庫金", market: "TSE", industry: "金融保險業" },
  "6669": { code: "6669", name: "緯穎", market: "TSE", industry: "電腦及週邊設備業" }
};

let cachedStockInfo: Map<string, TaiwanStockInfo> | null = null;

export function normalizeTaiwanStockCode(value: string) {
  return value.trim().toUpperCase().replace(/\.(TW|TWO)$/, "");
}

function loadStockInfo() {
  const info = new Map<string, TaiwanStockInfo>(
    Object.entries(FALLBACK_STOCK_INFO).map(([code, item]) => [code, item])
  );
  const filePath = path.join(process.cwd(), "data", "stock_list.csv");

  if (!existsSync(filePath)) {
    return info;
  }

  const rows = readFileSync(filePath, "utf-8").split(/\r?\n/).slice(1);
  for (const row of rows) {
    const [code, name, market, industry] = row.split(",").map((item) => item.trim());
    if (!code || !name) {
      continue;
    }
    info.set(normalizeTaiwanStockCode(code), {
      code: normalizeTaiwanStockCode(code),
      name,
      market,
      industry
    });
  }

  return info;
}

export function getTaiwanStockInfo(stockId: string): TaiwanStockInfo | null {
  if (!cachedStockInfo) {
    cachedStockInfo = loadStockInfo();
  }
  return cachedStockInfo.get(normalizeTaiwanStockCode(stockId)) ?? null;
}

export function getTaiwanStockDisplayName(stockId: string, fallback?: string | null) {
  return getTaiwanStockInfo(stockId)?.name ?? fallback ?? normalizeTaiwanStockCode(stockId);
}
