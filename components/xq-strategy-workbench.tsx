"use client";

import { useMemo, useState, useTransition } from "react";

import type { XQIndicator, XQScanResult } from "@/lib/xq-strategy";

type Props = {
  indicators: XQIndicator[];
};

type FilterCategory = "all" | "technical" | "chip";
type ScanMode = "after_market" | "intraday";
type MarketType = "TEST" | "Tw50" | "All";
type MatchMode = "AND" | "OR";

const CATEGORY_LABELS: Record<FilterCategory, string> = {
  all: "全部",
  technical: "技術",
  chip: "籌碼"
};

const SCAN_MODE_LABELS: Record<ScanMode, string> = {
  after_market: "盤後",
  intraday: "盤中"
};

function defaultParams(indicator: XQIndicator) {
  return Object.fromEntries(
    Object.entries(indicator.params).map(([key, value]) => [key, value])
  ) as Record<string, number | string | boolean>;
}

function parseParamValue(value: string, fallback: number | string | boolean) {
  if (typeof fallback === "number") {
    const numeric = Number(value);
    return Number.isFinite(numeric) ? numeric : fallback;
  }
  if (typeof fallback === "boolean") {
    return value === "true";
  }
  return value;
}

export function XQStrategyWorkbench({ indicators }: Props) {
  const [category, setCategory] = useState<FilterCategory>("all");
  const [group, setGroup] = useState("全部");
  const [selectedIds, setSelectedIds] = useState<string[]>(() =>
    indicators.slice(0, 3).map((indicator) => indicator.id)
  );
  const [params, setParams] = useState<Record<string, Record<string, number | string | boolean>>>(() =>
    Object.fromEntries(indicators.map((indicator) => [indicator.id, defaultParams(indicator)]))
  );
  const [scanMode, setScanMode] = useState<ScanMode>("after_market");
  const [marketType, setMarketType] = useState<MarketType>("TEST");
  const [matchMode, setMatchMode] = useState<MatchMode>("AND");
  const [stockText, setStockText] = useState("2330, 2317, 2454, 2303, 2603");
  const [result, setResult] = useState<XQScanResult | null>(null);
  const [error, setError] = useState("");
  const [isPending, startTransition] = useTransition();

  const groups = useMemo(() => {
    const source = category === "all" ? indicators : indicators.filter((item) => item.category === category);
    return ["全部", ...Array.from(new Set(source.map((item) => item.group))).sort()];
  }, [category, indicators]);

  const filteredIndicators = useMemo(() => {
    return indicators.filter((indicator) => {
      const categoryMatch = category === "all" || indicator.category === category;
      const groupMatch = group === "全部" || indicator.group === group;
      return categoryMatch && groupMatch;
    });
  }, [category, group, indicators]);

  const selectedIndicators = useMemo(() => {
    const selectedSet = new Set(selectedIds);
    return indicators.filter((indicator) => selectedSet.has(indicator.id));
  }, [indicators, selectedIds]);

  function toggleIndicator(indicator: XQIndicator) {
    setSelectedIds((current) => {
      if (current.includes(indicator.id)) {
        return current.filter((id) => id !== indicator.id);
      }
      return [...current, indicator.id];
    });
    setParams((current) => ({
      ...current,
      [indicator.id]: current[indicator.id] ?? defaultParams(indicator)
    }));
  }

  function updateParam(indicator: XQIndicator, key: string, value: string) {
    const fallback = indicator.params[key];
    setParams((current) => ({
      ...current,
      [indicator.id]: {
        ...(current[indicator.id] ?? defaultParams(indicator)),
        [key]: parseParamValue(value, fallback)
      }
    }));
  }

  function runScan() {
    setError("");
    setResult(null);
    const stocks = stockText
      .split(/[\s,，]+/)
      .map((item) => item.trim())
      .filter(Boolean);

    startTransition(async () => {
      try {
        const response = await fetch("/api/xq-strategy/scan", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: `${SCAN_MODE_LABELS[scanMode]} XQ 條件掃描`,
            scanMode,
            marketType,
            matchMode,
            indicatorIds: selectedIds,
            indicatorParams: params,
            stockList: stocks,
            maxStocks: marketType === "All" ? 80 : 30
          })
        });
        const payload = await response.json();
        if (!response.ok) {
          throw new Error(payload.error ?? "Scan failed.");
        }
        setResult(payload);
      } catch (scanError) {
        setError(scanError instanceof Error ? scanError.message : "Scan failed.");
      }
    });
  }

  return (
    <section className="xq-workbench">
      <div className="panel xq-builder">
        <div className="panel-header">
          <div>
            <p className="eyebrow">XQ Module</p>
            <h2>策略條件組合器</h2>
          </div>
          <div className="status-pill">{selectedIds.length} 條件</div>
        </div>

        <div className="xq-toolbar">
          <div className="segmented-control" aria-label="指標類型">
            {(["all", "technical", "chip"] as FilterCategory[]).map((item) => (
              <button
                key={item}
                className={category === item ? "active" : ""}
                type="button"
                onClick={() => {
                  setCategory(item);
                  setGroup("全部");
                }}
              >
                {CATEGORY_LABELS[item]}
              </button>
            ))}
          </div>

          <label>
            群組
            <select value={group} onChange={(event) => setGroup(event.target.value)}>
              {groups.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </label>
        </div>

        <div className="indicator-grid">
          {filteredIndicators.map((indicator) => {
            const selected = selectedIds.includes(indicator.id);
            return (
              <button
                key={indicator.id}
                type="button"
                className={`indicator-tile${selected ? " selected" : ""}`}
                onClick={() => toggleIndicator(indicator)}
              >
                <span>{indicator.name}</span>
                <small>
                  {indicator.group} · {indicator.category === "technical" ? "技術" : "籌碼"}
                </small>
              </button>
            );
          })}
        </div>
      </div>

      <div className="panel xq-runner">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Screening</p>
            <h2>盤中 / 盤後篩選</h2>
          </div>
        </div>

        <div className="form-grid">
          <label>
            時段
            <select value={scanMode} onChange={(event) => setScanMode(event.target.value as ScanMode)}>
              <option value="after_market">盤後日線</option>
              <option value="intraday">盤中 5 分線</option>
            </select>
          </label>
          <label>
            股票池
            <select value={marketType} onChange={(event) => setMarketType(event.target.value as MarketType)}>
              <option value="TEST">測試清單</option>
              <option value="Tw50">大型權值</option>
              <option value="All">完整清單</option>
            </select>
          </label>
          <label>
            組合邏輯
            <select value={matchMode} onChange={(event) => setMatchMode(event.target.value as MatchMode)}>
              <option value="AND">全部符合</option>
              <option value="OR">任一符合</option>
            </select>
          </label>
        </div>

        <label>
          自訂標的
          <textarea
            rows={3}
            value={stockText}
            onChange={(event) => setStockText(event.target.value)}
          />
        </label>

        <div className="selected-stack">
          {selectedIndicators.map((indicator) => (
            <div className="condition-row" key={indicator.id}>
              <div>
                <strong>{indicator.name}</strong>
                <p>{indicator.description}</p>
              </div>
              <div className="param-grid">
                {Object.entries(indicator.params).map(([key, value]) => (
                  <label key={key}>
                    {key}
                    <input
                      value={String((params[indicator.id] ?? defaultParams(indicator))[key] ?? value)}
                      onChange={(event) => updateParam(indicator, key, event.target.value)}
                    />
                  </label>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="button-row">
          <button type="button" onClick={runScan} disabled={isPending || selectedIds.length === 0}>
            {isPending ? "掃描中..." : "執行篩選"}
          </button>
          <button type="button" className="secondary-button" onClick={() => setSelectedIds([])}>
            清空條件
          </button>
        </div>

        {error ? <p className="feedback-message error">{error}</p> : null}
      </div>

      <div className="panel xq-results">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Results</p>
            <h2>命中標的</h2>
          </div>
          {result ? <div className="status-pill">{result.resultCount} / {result.stockCount}</div> : null}
        </div>

        {result && result.results.length > 0 ? (
          <div className="table-shell">
            <table>
              <thead>
                <tr>
                  <th>股票</th>
                  <th>名稱</th>
                  <th>價格</th>
                  <th>條件</th>
                  <th>日期</th>
                </tr>
              </thead>
              <tbody>
                {result.results.map((row) => (
                  <tr key={`${row["Stock ID"]}-${row.Date}`}>
                    <td>{row["Stock ID"]}</td>
                    <td>{row.Name}</td>
                    <td>{row.Price}</td>
                    <td>{row.Signal}</td>
                    <td>{row.Date}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <p className="empty-state">
            {result ? "本次條件沒有命中標的。" : "尚未執行新的條件掃描。"}
          </p>
        )}
      </div>
    </section>
  );
}
