import {
  average,
  fetchCloudStock,
  latestBar,
  mapWithConcurrency,
  movingAverage,
  resolveCloudStockPool
} from "@/lib/cloud-market-scanner";
import type { XQScanRequest, XQScanResult } from "@/lib/xq-strategy";

function isMaBullish(closes: number[]) {
  const ma5 = movingAverage(closes, 5);
  const ma20 = movingAverage(closes, 20);
  const ma60 = movingAverage(closes, 60);
  return closes.at(-1)! > ma5 && ma5 > ma20 && ma20 > ma60;
}

function isVolumeExpanded(volumes: number[], multiplier: number) {
  const avgVolume20 = average(volumes.slice(-20));
  return volumes.at(-1)! >= avgVolume20 * multiplier;
}

function isInstitutionalBuyingProxy(closes: number[], volumes: number[], days: number) {
  const safeDays = Math.max(2, Math.min(10, Math.floor(days || 3)));
  const recentReturn = closes.at(-1)! / closes.at(-1 - safeDays)! - 1;
  const avgVolume20 = average(volumes.slice(-20));
  const avgVolumeRecent = average(volumes.slice(-safeDays));
  return recentReturn > 0.015 && avgVolumeRecent >= avgVolume20 * 1.05 && closes.at(-1)! > movingAverage(closes, 20);
}

export async function runCloudXQScan(request: XQScanRequest): Promise<XQScanResult> {
  const stockPool = resolveCloudStockPool(request.marketType, request.stockList, request.maxStocks ?? 30);
  const matchMode = request.matchMode === "OR" ? "OR" : "AND";
  const scanResults = await mapWithConcurrency(stockPool, 6, async (stockId) => {
    const payload = await fetchCloudStock(stockId).catch(() => null);
    if (!payload || payload.bars.length < 60) {
      return null;
    }

    const closes = payload.bars.map((bar) => bar.close);
    const volumes = payload.bars.map((bar) => bar.volume);
    const matches = request.indicatorIds.map((indicatorId) => {
      if (indicatorId === "ma_bullish_alignment") {
        return {
          indicatorId,
          matched: isMaBullish(closes),
          reason: "均線多頭排列"
        };
      }
      if (indicatorId === "volume_expansion") {
        const multiplier = Number(request.indicatorParams?.volume_expansion?.multiplier ?? 1.5);
        return {
          indicatorId,
          matched: isVolumeExpanded(volumes, Number.isFinite(multiplier) ? multiplier : 1.5),
          reason: "成交量放大"
        };
      }
      if (indicatorId === "institutional_buying") {
        const days = Number(request.indicatorParams?.institutional_buying?.days ?? 3);
        return {
          indicatorId,
          matched: isInstitutionalBuyingProxy(closes, volumes, Number.isFinite(days) ? days : 3),
          reason: "籌碼代理：價量偏多"
        };
      }
      return {
        indicatorId,
        matched: false,
        reason: ""
      };
    });
    const reasons = matches.filter((item) => item.matched).map((item) => item.reason);

    const matched = matchMode === "AND"
      ? matches.length > 0 && matches.every((item) => item.matched)
      : reasons.length > 0;

    if (!matched) {
      return null;
    }

    const latest = latestBar(payload.bars);
    return {
      "Stock ID": stockId,
      Name: payload.stockName,
      Price: latest.close,
      Signal: reasons.join(" | "),
      Volume: latest.volume,
      Date: latest.date
    };
  });

  const results: XQScanResult["results"] = [];
  for (const item of scanResults) {
    if (item) {
      results.push(item);
    }
  }

  return {
    screenRunId: `cloud_xq_${Date.now()}`,
    executedAt: new Date().toISOString(),
    scanMode: request.scanMode,
    marketType: request.marketType,
    matchMode,
    stockCount: stockPool.length,
    resultCount: results.length,
    results
  };
}
