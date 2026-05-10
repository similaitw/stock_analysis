from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any, Callable, Optional

import pandas as pd

from data.fetcher import DataFetcher
from data.workspace_models import (
    AfterMarketScan,
    NextDayWatchlist,
    make_after_market_scan_id,
    now_iso,
    sanitize_for_json,
)
from data.workspace_store import WorkspaceStore
from scanner.engine import ScannerEngine


DEFAULT_WEIGHTS = {
    "technical": 40,
    "chip": 30,
    "volume": 15,
    "relativeStrength": 15,
}

DEFAULT_MONITORING_RULES = [
    "開高後守住昨高",
    "開高跌破開盤低點時降級",
    "量能延續且價格站穩時升級",
    "大盤轉弱且個股破均線時移入避開",
    "同族群同步轉強時加強信號",
]

score_stock: Optional[Callable[..., Any]] = None


def run_after_market_scan(
    payload: dict[str, Any],
    data_fetcher: Any = DataFetcher,
    store: WorkspaceStore = WorkspaceStore(),
) -> dict[str, Any]:
    scan_date = str(payload.get("date") or date.today().isoformat())
    market_type = str(payload.get("marketType") or payload.get("market_scope") or "All")
    profile = str(payload.get("profile") or "balanced")
    weights = _normalize_weights(payload.get("weights"))
    include_risk_list = bool(payload.get("includeRiskList", True))
    stock_pool = _resolve_stock_pool(payload, market_type)

    max_stocks = _safe_positive_int(payload.get("maxStocks"), len(stock_pool))
    stock_pool = stock_pool[:max_stocks]

    executed_at = now_iso()
    a_list: list[dict[str, Any]] = []
    b_list: list[dict[str, Any]] = []
    avoid_list: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    raw_results: list[dict[str, Any]] = []

    market_data = _fetch_market_data(data_fetcher)

    for stock_id in stock_pool:
        try:
            stock_payload = _fetch_stock_payload(str(stock_id), data_fetcher)
            skip_reason = _validate_minimum_data(stock_payload["price_data"])
            if skip_reason:
                skipped.append({"stockId": str(stock_id), "reason": skip_reason})
                continue

            scored = _score_single_stock(
                stock_id=str(stock_id),
                stock_payload=stock_payload,
                market_data=market_data,
                profile=profile,
                weights=weights,
            )
            normalized = _normalize_score_result(str(stock_id), stock_payload, scored)
            bucket = _classify_result(normalized)
            normalized["bucket"] = bucket
            raw_results.append(normalized)

            if bucket == "A":
                a_list.append(normalized)
            elif bucket == "B":
                b_list.append(normalized)
            elif bucket == "avoid":
                avoid_list.append(normalized)
        except Exception as exc:
            skipped.append({"stockId": str(stock_id), "reason": str(exc)})

    a_list = _rank_results(a_list)
    b_list = _rank_results(b_list)
    avoid_list = _rank_results(avoid_list, include_rank=False)

    response_avoid_list = avoid_list if include_risk_list else []
    counts = {
        "requested": len(stock_pool),
        "scanned": len(raw_results),
        "skipped": len(skipped),
        "aList": len(a_list),
        "bList": len(b_list),
        "avoidList": len(response_avoid_list),
    }

    scan = AfterMarketScan(
        id=make_after_market_scan_id(scan_date),
        date=scan_date,
        market_scope=market_type,
        profile=profile,
        executed_at=executed_at,
        weights=weights,
        counts=counts,
        a_list=a_list,
        b_list=b_list,
        avoid_list=response_avoid_list,
        skipped=skipped,
        raw_results=raw_results,
        request_payload=sanitize_for_json(payload),
    )
    store.save_after_market_scan(scan)

    next_day_watchlist = NextDayWatchlist(
        source_scan_id=scan.id,
        trade_date=_next_trade_date(scan_date),
        stocks=[_watchlist_stock(item) for item in [*a_list, *b_list]],
        monitoring_rules=DEFAULT_MONITORING_RULES,
    )
    store.save_next_day_watchlist(next_day_watchlist)

    return {
        "scanId": scan.id,
        "executedAt": executed_at,
        "date": scan_date,
        "marketType": market_type,
        "profile": profile,
        "weights": weights,
        "counts": counts,
        "aList": a_list,
        "bList": b_list,
        "avoidList": response_avoid_list,
        "skipped": skipped,
        "nextDayWatchlistId": next_day_watchlist.id,
    }


def _normalize_weights(weights: Any) -> dict[str, int]:
    normalized = DEFAULT_WEIGHTS.copy()
    if isinstance(weights, dict):
        for key in normalized:
            try:
                normalized[key] = int(weights.get(key, normalized[key]))
            except (TypeError, ValueError):
                pass
    return normalized


def _safe_positive_int(value: Any, fallback: int) -> int:
    try:
        parsed = int(value)
        return parsed if parsed > 0 else fallback
    except (TypeError, ValueError):
        return fallback


def _resolve_stock_pool(payload: dict[str, Any], market_type: str) -> list[str]:
    stock_list = payload.get("stockList") or payload.get("stock_list")
    if stock_list:
        return [str(item).strip() for item in stock_list if str(item).strip()]
    return [str(item).strip() for item in ScannerEngine.get_stock_list(market_type) if str(item).strip()]


def _fetch_stock_payload(stock_id: str, data_fetcher: Any) -> dict[str, Any]:
    price_data = _call_fetcher(data_fetcher, "fetch_history", stock_id, period="6mo")
    name, industry, description = _get_stock_info(data_fetcher, stock_id)
    chip_data = {
        "institutional": _safe_fetch_frame(data_fetcher, "fetch_institutional_investors", stock_id, 90),
        "margin": _safe_fetch_frame(data_fetcher, "fetch_margin_trading", stock_id, 90),
        "sbl": _safe_fetch_frame(data_fetcher, "fetch_borrowing_sell", stock_id, 90),
    }
    return {
        "price_data": price_data if isinstance(price_data, pd.DataFrame) else pd.DataFrame(),
        "stock_name": name,
        "industry": industry,
        "description": description,
        "chip_data": chip_data,
    }


def _fetch_market_data(data_fetcher: Any) -> dict[str, pd.DataFrame]:
    return {
        "taiex": _safe_fetch_frame(data_fetcher, "fetch_market_index", "TSE", "6mo"),
        "otc": _safe_fetch_frame(data_fetcher, "fetch_market_index", "OTC", "6mo"),
    }


def _call_fetcher(data_fetcher: Any, method_name: str, *args: Any, **kwargs: Any) -> Any:
    method = getattr(data_fetcher, method_name)
    return method(*args, **kwargs)


def _safe_fetch_frame(data_fetcher: Any, method_name: str, *args: Any) -> pd.DataFrame:
    try:
        value = _call_fetcher(data_fetcher, method_name, *args)
        return value if isinstance(value, pd.DataFrame) else pd.DataFrame()
    except Exception:
        return pd.DataFrame()


def _get_stock_info(data_fetcher: Any, stock_id: str) -> tuple[str, str, str]:
    try:
        value = _call_fetcher(data_fetcher, "get_stock_info", stock_id)
        if isinstance(value, tuple):
            name = str(value[0]) if len(value) >= 1 else stock_id
            industry = str(value[1]) if len(value) >= 2 else ""
            description = str(value[2]) if len(value) >= 3 else ""
            return name, industry, description
    except Exception:
        pass
    return stock_id, "", ""


def _validate_minimum_data(price_data: pd.DataFrame) -> str:
    required = {"Open", "High", "Low", "Close", "Volume"}
    if price_data.empty:
        return "missing price data"
    if not required.issubset(price_data.columns):
        return "missing OHLCV columns"
    if len(price_data) < 45:
        return "insufficient history: need at least 45 rows"

    close = pd.to_numeric(price_data["Close"], errors="coerce")
    volume = pd.to_numeric(price_data["Volume"], errors="coerce")
    if close.dropna().empty or volume.dropna().empty:
        return "invalid price or volume data"
    if close.iloc[-1] < 10:
        return "price below 10"
    if volume.tail(20).mean() < 500:
        return "20-day average volume below 500"
    if volume.iloc[-1] < 300:
        return "latest volume below 300"
    return ""


def _score_single_stock(
    stock_id: str,
    stock_payload: dict[str, Any],
    market_data: dict[str, pd.DataFrame],
    profile: str,
    weights: dict[str, int],
) -> Any:
    scorer = _resolve_score_stock()
    attempts = [
        lambda: scorer(
            stock_id=stock_id,
            price_df=stock_payload["price_data"],
            chip_cache=stock_payload["chip_data"],
            market_df=market_data.get("taiex"),
            industry_df=None,
        ),
        lambda: scorer(
            stock_id=stock_id,
            price_data=stock_payload["price_data"],
            chip_data=stock_payload["chip_data"],
            market_data=market_data,
            profile=profile,
            weights=weights,
        ),
        lambda: scorer(stock_id, stock_payload, market_data, profile, weights),
        lambda: scorer(stock_id, stock_payload, weights),
        lambda: scorer(stock_payload, profile=profile, weights=weights),
    ]
    last_error: Optional[Exception] = None
    for attempt in attempts:
        try:
            return attempt()
        except TypeError as exc:
            last_error = exc
    if last_error:
        raise last_error
    return _fallback_score_stock(stock_id, stock_payload, market_data, profile, weights)


def _resolve_score_stock() -> Callable[..., dict[str, Any]]:
    if callable(score_stock):
        return score_stock
    try:
        from scanner.scoring import score_stock as imported_score_stock

        return imported_score_stock
    except Exception:
        return _fallback_score_stock


def _fallback_score_stock(
    stock_id: str,
    stock_payload: dict[str, Any],
    market_data: Optional[dict[str, pd.DataFrame]] = None,
    profile: str = "balanced",
    weights: Optional[dict[str, int]] = None,
) -> dict[str, Any]:
    price_data = stock_payload["price_data"]
    weights = weights or DEFAULT_WEIGHTS
    close = pd.to_numeric(price_data["Close"], errors="coerce")
    high = pd.to_numeric(price_data["High"], errors="coerce")
    low = pd.to_numeric(price_data["Low"], errors="coerce")
    open_ = pd.to_numeric(price_data["Open"], errors="coerce")
    volume = pd.to_numeric(price_data["Volume"], errors="coerce")

    technical = 0
    volume_score = 0
    relative_strength = 0
    chip = 0
    risk_score = 0
    reasons: list[str] = []
    risks: list[str] = []

    ma5 = close.rolling(5).mean()
    ma20 = close.rolling(20).mean()
    ma60 = close.rolling(60).mean()
    if close.iloc[-1] > ma5.iloc[-1] > ma20.iloc[-1] > ma60.iloc[-1]:
        technical += 10
        reasons.append("均線多頭排列")
    if close.iloc[-1] > high.shift(1).tail(20).max():
        technical += 10
        reasons.append("突破 20 日高")
    if ma5.iloc[-1] > ma20.iloc[-1] and ma5.iloc[-2] <= ma20.iloc[-2]:
        technical += 6
        reasons.append("均線黃金交叉")

    avg_volume20 = volume.tail(20).mean()
    if volume.iloc[-1] >= avg_volume20 * 1.5:
        volume_score += 8
        reasons.append("成交量放大")
    if close.iloc[-1] >= close.tail(20).max() and volume.iloc[-1] >= volume.tail(20).max():
        volume_score += 5
        reasons.append("價量同步創高")

    taiex = (market_data or {}).get("taiex")
    if isinstance(taiex, pd.DataFrame) and not taiex.empty and "Close" in taiex.columns:
        stock_return = (close.iloc[-1] / close.iloc[-20]) - 1
        market_close = pd.to_numeric(taiex["Close"], errors="coerce").dropna()
        if len(market_close) >= 20 and stock_return > (market_close.iloc[-1] / market_close.iloc[-20]) - 1:
            relative_strength += 6
            reasons.append("強於大盤")
    elif close.iloc[-1] > ma20.iloc[-1]:
        relative_strength += 3
        reasons.append("守住月線")

    upper_shadow = high.iloc[-1] - max(open_.iloc[-1], close.iloc[-1])
    day_range = max(high.iloc[-1] - low.iloc[-1], 0.01)
    if volume.iloc[-1] >= avg_volume20 * 2 and upper_shadow / day_range >= 0.45:
        risk_score -= 20
        risks.append("爆量長上影")
    if close.iloc[-1] < ma20.iloc[-1]:
        risk_score -= 12
        risks.append("跌破 MA20")
    if close.iloc[-1] < ma60.iloc[-1]:
        risk_score -= 20
        risks.append("跌破 MA60")

    total = min(technical, weights["technical"])
    total += min(chip, weights["chip"])
    total += min(volume_score, weights["volume"])
    total += min(relative_strength, weights["relativeStrength"])
    total += risk_score

    return {
        "stockId": stock_id,
        "stockName": stock_payload.get("stock_name", stock_id),
        "score": max(0, round(total)),
        "riskScore": risk_score,
        "technicalScore": min(technical, weights["technical"]),
        "chipScore": min(chip, weights["chip"]),
        "volumeScore": min(volume_score, weights["volume"]),
        "relativeStrengthScore": min(relative_strength, weights["relativeStrength"]),
        "reasons": reasons,
        "risks": risks,
    }


def _normalize_score_result(
    stock_id: str,
    stock_payload: dict[str, Any],
    scored: Any,
) -> dict[str, Any]:
    data = scored.to_dict() if hasattr(scored, "to_dict") else scored
    data = dict(data or {})
    return {
        "stockId": str(data.get("stockId") or data.get("stock_id") or stock_id),
        "stockName": str(data.get("stockName") or data.get("stock_name") or stock_payload.get("stock_name") or stock_id),
        "score": float(data.get("score", 0) or 0),
        "riskScore": float(data.get("riskScore", data.get("risk_score", 0)) or 0),
        "technicalScore": float(data.get("technicalScore", data.get("technical_score", 0)) or 0),
        "chipScore": float(data.get("chipScore", data.get("chip_score", 0)) or 0),
        "volumeScore": float(data.get("volumeScore", data.get("volume_score", 0)) or 0),
        "relativeStrengthScore": float(data.get("relativeStrengthScore", data.get("relative_strength_score", 0)) or 0),
        "reasons": list(data.get("reasons", []) or []),
        "risks": list(data.get("risks", []) or []),
        "nextDayPlan": str(data.get("nextDayPlan") or data.get("next_day_plan") or "觀察是否守住昨高與開盤低點"),
    }


def _classify_result(result: dict[str, Any]) -> str:
    score = float(result["score"])
    risk_score = float(result["riskScore"])
    if risk_score <= -30 or result.get("majorAvoid"):
        return "avoid"
    if score >= 75 and risk_score > -30:
        return "A"
    if 55 <= score <= 74 and risk_score > -30:
        return "B"
    return "hidden"


def _rank_results(results: list[dict[str, Any]], include_rank: bool = True) -> list[dict[str, Any]]:
    ranked = sorted(results, key=lambda item: (item.get("score", 0), item.get("riskScore", 0)), reverse=True)
    for index, item in enumerate(ranked, start=1):
        if include_rank:
            item["rank"] = index
    return ranked


def _watchlist_stock(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "stockId": item["stockId"],
        "stockName": item["stockName"],
        "sourceRank": item.get("rank"),
        "bucket": item.get("bucket"),
        "score": item.get("score"),
        "riskScore": item.get("riskScore"),
        "nextDayPlan": item.get("nextDayPlan"),
    }


def _next_trade_date(scan_date: str) -> str:
    try:
        base = datetime.fromisoformat(scan_date).date()
    except ValueError:
        base = date.today()
    next_day = base + timedelta(days=1)
    while next_day.weekday() >= 5:
        next_day += timedelta(days=1)
    return next_day.isoformat()
