from __future__ import annotations

import contextlib
import datetime as _datetime
import importlib
import json
import os
import sys
from typing import Any

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from data.fetcher import DataFetcher
from data.workspace_models import ScreenRun
from data.workspace_store import WorkspaceStore
from scanner.engine import ScannerEngine
from strategies.indicator_library import (
    evaluate_indicator_set,
    get_indicator_catalog,
    uses_chip_data,
)


def _safe_float(value: Any) -> float | None:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def _history_payload(ticker: str) -> dict[str, Any]:
    # Keep stdout reserved for the final JSON payload so the Next.js bridge can
    # safely parse the response. Existing data-layer logs are redirected to stderr.
    with contextlib.redirect_stdout(sys.stderr):
        name, industry, description = DataFetcher.get_stock_info(ticker)
        current_price = DataFetcher.fetch_current_price(ticker)
        fundamentals = DataFetcher.fetch_fundamentals(ticker)
        history = DataFetcher.fetch_history(ticker, period="6mo")

    candles: list[dict[str, Any]] = []
    if not history.empty:
        tail = history.tail(60).reset_index()
        date_key = tail.columns[0]
        for _, row in tail.iterrows():
            date_value = row[date_key]
            candles.append(
                {
                    "date": getattr(date_value, "strftime", lambda fmt: str(date_value))("%Y-%m-%d"),
                    "close": _safe_float(row.get("Close")),
                    "volume": _safe_float(row.get("Volume")),
                }
            )

    return {
        "ticker": ticker,
        "name": name,
        "industry": industry,
        "description": description,
        "currentPrice": _safe_float(current_price),
        "fundamentals": fundamentals,
        "history": candles,
    }


def _chip_cache(stock_id: str, indicator_ids: list[str]) -> dict[str, Any]:
    if not uses_chip_data(indicator_ids):
        return {}
    return {
        "institutional": DataFetcher.fetch_institutional_investors(stock_id, 90),
        "margin": DataFetcher.fetch_margin_trading(stock_id, 90),
        "sbl": DataFetcher.fetch_borrowing_sell(stock_id, 90),
    }


def _scan_period(scan_mode: str) -> tuple[str, str]:
    if scan_mode == "intraday":
        return "5d", "5m"
    return "6mo", "1d"


def _normalize_stock_list(payload: dict[str, Any]) -> list[str]:
    raw_stocks = payload.get("stockList") or []
    if isinstance(raw_stocks, str):
        raw_stocks = [item.strip() for item in raw_stocks.replace("\n", ",").split(",")]
    stocks = [str(item).strip() for item in raw_stocks if str(item).strip()]
    if stocks:
        return stocks
    return ScannerEngine.get_stock_list(str(payload.get("marketType") or "Tw50"))


def _xq_scan_payload(payload: dict[str, Any]) -> dict[str, Any]:
    indicator_ids = [str(item) for item in payload.get("indicatorIds", []) if str(item)]
    if not indicator_ids:
        raise ValueError("至少需要選一個指標條件。")

    match_mode = str(payload.get("matchMode") or "AND").upper()
    if match_mode not in {"AND", "OR"}:
        match_mode = "AND"

    scan_mode = str(payload.get("scanMode") or "after_market")
    period, interval = _scan_period(scan_mode)
    stock_list = _normalize_stock_list(payload)
    indicator_params = payload.get("indicatorParams") or {}
    max_stocks = int(payload.get("maxStocks") or len(stock_list))
    stock_list = stock_list[:max_stocks]

    results: list[dict[str, Any]] = []
    with contextlib.redirect_stdout(sys.stderr):
        for stock_id in stock_list:
            history = DataFetcher.fetch_history(stock_id, period=period, interval=interval)
            if history.empty or len(history) < 5:
                continue
            chips = _chip_cache(stock_id, indicator_ids)
            matched, reasons = evaluate_indicator_set(
                history,
                indicator_ids,
                match_mode=match_mode,
                indicator_params=indicator_params,
                chip_cache=chips,
            )
            if not matched:
                continue
            stock_name, _industry, _description = DataFetcher.get_stock_info(stock_id)
            latest = history.iloc[-1]
            results.append(
                {
                    "Stock ID": stock_id,
                    "Name": stock_name,
                    "Price": _safe_float(latest.get("Close")),
                    "Signal": " | ".join(reasons),
                    "Volume": _safe_float(latest.get("Volume")),
                    "Date": getattr(history.index[-1], "strftime", lambda fmt: str(history.index[-1]))("%Y-%m-%d"),
                }
            )

    screen_run = ScreenRun.from_scan_results(
        name=str(payload.get("name") or "XQ 模組化條件掃描"),
        market_scope=f"{payload.get('marketType') or 'Tw50'}:{scan_mode}",
        stock_pool=stock_list,
        strategy_names=indicator_ids,
        match_mode=match_mode,
        results=results,
        strategy_params=indicator_params,
        source_page="xq_strategy_workspace",
        notes="Composable technical/chip indicator scan from Next.js strategy page.",
    )
    with contextlib.redirect_stdout(sys.stderr):
        WorkspaceStore().save_screen_run(screen_run)

    return {
        "screenRunId": screen_run.id,
        "executedAt": screen_run.executed_at,
        "scanMode": scan_mode,
        "marketType": payload.get("marketType") or "Tw50",
        "matchMode": match_mode,
        "stockCount": len(stock_list),
        "resultCount": len(results),
        "results": results,
    }


def _json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_ready(item) for item in value]
    if isinstance(value, (_datetime.datetime, _datetime.date)):
        return value.isoformat()
    if hasattr(value, "model_dump"):
        return _json_ready(value.model_dump())
    if hasattr(value, "to_dict"):
        return _json_ready(value.to_dict())
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    return value


def _load_after_market_module() -> Any:
    try:
        return importlib.import_module("scanner.daily_after_market")
    except ModuleNotFoundError as error:
        if error.name == "scanner.daily_after_market":
            raise ValueError(
                "scanner.daily_after_market is not available yet. "
                "Merge the scanner implementation before running the after-market scan."
            ) from error
        raise


def _call_module_function(module: Any, function_names: list[str], *args: Any) -> Any:
    for function_name in function_names:
        candidate = getattr(module, function_name, None)
        if callable(candidate):
            return candidate(*args)
    return None


def _call_scanner_instance(module: Any, method_names: list[str], *args: Any) -> Any:
    for class_name in ("DailyAfterMarketScanner", "AfterMarketScanner"):
        scanner_class = getattr(module, class_name, None)
        if scanner_class is None:
            continue
        scanner = scanner_class()
        for method_name in method_names:
            candidate = getattr(scanner, method_name, None)
            if callable(candidate):
                return candidate(*args)
    return None


def _after_market_scan_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("after_market_scan payload must be a JSON object.")

    with contextlib.redirect_stdout(sys.stderr):
        module = _load_after_market_module()
        result = _call_module_function(
            module,
            ["after_market_scan", "run_after_market_scan", "scan_after_market", "run_scan", "scan"],
            payload,
        )
        if result is None:
            result = _call_scanner_instance(module, ["after_market_scan", "run_scan", "scan"], payload)

    if result is None:
        raise ValueError(
            "scanner.daily_after_market does not expose a supported scan function "
            "(after_market_scan/run_after_market_scan/scan_after_market/run_scan/scan)."
        )

    return _json_ready(result)


def _normalize_after_market_report_payload(result: Any) -> dict[str, Any]:
    data = _json_ready(result)
    if not isinstance(data, dict):
        return data

    scan_id = data.get("scanId") or data.get("id")
    normalized = {
        "scanId": scan_id,
        "executedAt": data.get("executedAt") or data.get("executed_at"),
        "date": data.get("date"),
        "marketType": data.get("marketType") or data.get("market_scope"),
        "profile": data.get("profile"),
        "weights": data.get("weights") or {},
        "counts": data.get("counts") or {},
        "aList": data.get("aList") or data.get("a_list") or [],
        "bList": data.get("bList") or data.get("b_list") or [],
        "avoidList": data.get("avoidList") or data.get("avoid_list") or [],
        "skipped": data.get("skipped") or [],
        "rawResults": data.get("rawResults") or data.get("raw_results") or [],
        "requestPayload": data.get("requestPayload") or data.get("request_payload") or {},
    }
    return {key: value for key, value in normalized.items() if value is not None}


def _read_after_market_report_file(scan_id: str) -> dict[str, Any] | None:
    safe_scan_id = os.path.basename(scan_id)
    if safe_scan_id != scan_id or not safe_scan_id:
        raise ValueError("Invalid scan_id.")

    candidate_paths = [
        os.path.join(PROJECT_ROOT, "data", "workspace", "after_market_scans", f"{safe_scan_id}.json"),
        os.path.join(PROJECT_ROOT, "data", "workspace", "after_market_scans", safe_scan_id),
    ]
    for candidate_path in candidate_paths:
        if os.path.isfile(candidate_path):
            with open(candidate_path, "r", encoding="utf-8") as handle:
                return json.load(handle)
    return None


def _after_market_report_payload(scan_id: str) -> dict[str, Any]:
    if not scan_id:
        raise ValueError("scan_id is required.")

    result = None
    with contextlib.redirect_stdout(sys.stderr):
        try:
            module = _load_after_market_module()
        except ValueError:
            module = None
        if module is not None:
            result = _call_module_function(
                module,
                ["after_market_report", "get_after_market_report", "load_after_market_report", "load_report", "get_report"],
                scan_id,
            )
            if result is None:
                result = _call_scanner_instance(module, ["after_market_report", "get_report", "load_report"], scan_id)

    if result is None:
        result = _read_after_market_report_file(scan_id)

    if result is None:
        raise ValueError(f"After-market report not found: {scan_id}")

    return _normalize_after_market_report_payload(result)


def main() -> int:
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: next_bridge.py <command> [payload]"}))
        return 1

    command = sys.argv[1]

    try:
        if command == "research":
            if len(sys.argv) < 3:
                raise ValueError("Usage: next_bridge.py research <ticker>")
            payload = _history_payload(sys.argv[2])
        elif command == "xq_catalog":
            payload = {"indicators": get_indicator_catalog()}
        elif command == "xq_scan":
            if len(sys.argv) < 3:
                raise ValueError("Usage: next_bridge.py xq_scan <json-payload>")
            payload = _xq_scan_payload(json.loads(sys.argv[2]))
        elif command == "after_market_scan":
            if len(sys.argv) < 3:
                raise ValueError("Usage: next_bridge.py after_market_scan <json-payload>")
            payload = _after_market_scan_payload(json.loads(sys.argv[2]))
        elif command == "after_market_report":
            if len(sys.argv) < 3:
                raise ValueError("Usage: next_bridge.py after_market_report <scan_id>")
            payload = _after_market_report_payload(sys.argv[2])
        else:
            raise ValueError(f"Unknown command: {command}")
    except Exception as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 1

    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
