from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Callable

import pandas as pd


@dataclass(frozen=True)
class IndicatorDefinition:
    id: str
    name: str
    category: str
    group: str
    session: str
    description: str
    params: dict[str, Any] = field(default_factory=dict)
    data_requirements: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


IndicatorEvaluator = Callable[[pd.DataFrame, dict[str, Any], dict[str, pd.DataFrame]], tuple[bool, str]]


def _num(params: dict[str, Any], key: str, default: float) -> float:
    try:
        return float(params.get(key, default))
    except (TypeError, ValueError):
        return default


def _int(params: dict[str, Any], key: str, default: int) -> int:
    try:
        return int(params.get(key, default))
    except (TypeError, ValueError):
        return default


def _series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(dtype="float64")
    return pd.to_numeric(df[column], errors="coerce")


def _cross_up(fast: pd.Series, slow: pd.Series) -> bool:
    if len(fast) < 2 or len(slow) < 2:
        return False
    return bool(fast.iloc[-1] > slow.iloc[-1] and fast.iloc[-2] <= slow.iloc[-2])


def _daily_net(df: pd.DataFrame, keywords: list[str]) -> pd.Series:
    if df.empty or "name" not in df.columns:
        return pd.Series(dtype="float64")
    mask = pd.Series(False, index=df.index)
    for keyword in keywords:
        mask |= df["name"].astype(str).str.contains(keyword, case=False, na=False)
    subset = df[mask].copy()
    if subset.empty:
        return pd.Series(dtype="float64")
    if "net" not in subset.columns and {"buy", "sell"}.issubset(subset.columns):
        subset["net"] = pd.to_numeric(subset["buy"], errors="coerce") - pd.to_numeric(
            subset["sell"], errors="coerce"
        )
    if "net" not in subset.columns or "date" not in subset.columns:
        return pd.Series(dtype="float64")
    return pd.to_numeric(subset["net"], errors="coerce").groupby(subset["date"]).sum().sort_index()


def _balance_series(df: pd.DataFrame, candidates: list[str]) -> pd.Series:
    if df.empty:
        return pd.Series(dtype="float64")
    for column in candidates:
        if column in df.columns:
            values = pd.to_numeric(df[column], errors="coerce")
            if "date" in df.columns:
                values.index = df["date"]
            return values.dropna()
    return pd.Series(dtype="float64")


def _ma_trend(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    short = _int(params, "short", 5)
    mid = _int(params, "mid", 20)
    long = _int(params, "long", 60)
    close = _series(df, "Close")
    if len(close) < long:
        return False, ""
    ma_short = close.rolling(short).mean().iloc[-1]
    ma_mid = close.rolling(mid).mean().iloc[-1]
    ma_long = close.rolling(long).mean().iloc[-1]
    if close.iloc[-1] > ma_short > ma_mid > ma_long:
        return True, f"多頭排列：收盤 > MA{short} > MA{mid} > MA{long}"
    return False, ""


def _ma_golden_cross(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    fast = _int(params, "fast", 5)
    slow = _int(params, "slow", 20)
    close = _series(df, "Close")
    if len(close) < slow + 1:
        return False, ""
    ma_fast = close.rolling(fast).mean()
    ma_slow = close.rolling(slow).mean()
    if _cross_up(ma_fast, ma_slow):
        return True, f"MA{fast} 向上穿越 MA{slow}"
    return False, ""


def _price_breakout(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 20)
    close = _series(df, "Close")
    if len(close) < period + 1:
        return False, ""
    previous_high = close.iloc[-period - 1 : -1].max()
    if close.iloc[-1] > previous_high:
        return True, f"收盤突破前 {period} 日高點 {previous_high:.2f}"
    return False, ""


def _volume_surge(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 20)
    multiple = _num(params, "multiple", 1.8)
    volume = _series(df, "Volume")
    if len(volume) < period + 1:
        return False, ""
    average = volume.iloc[-period - 1 : -1].mean()
    if average > 0 and volume.iloc[-1] >= average * multiple:
        return True, f"成交量為 {period} 日均量 {volume.iloc[-1] / average:.1f} 倍"
    return False, ""


def _rsi_rebound(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 14)
    level = _num(params, "level", 30)
    close = _series(df, "Close")
    if len(close) < period + 2:
        return False, ""
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rsi = 100 - (100 / (1 + gain / loss.replace(0, pd.NA)))
    if rsi.iloc[-1] > level and rsi.iloc[-2] <= level:
        return True, f"RSI{period} 由低檔站回 {level:g}"
    return False, ""


def _macd_golden_cross(df: pd.DataFrame, _params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    close = _series(df, "Close")
    if len(close) < 35:
        return False, ""
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    if _cross_up(macd, signal):
        return True, "MACD 向上穿越 Signal"
    return False, ""


def _kd_golden_cross(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 9)
    low = _series(df, "Low")
    high = _series(df, "High")
    close = _series(df, "Close")
    if len(close) < period + 3:
        return False, ""
    low_min = low.rolling(period).min()
    high_max = high.rolling(period).max()
    rsv = 100 * ((close - low_min) / (high_max - low_min).replace(0, pd.NA))
    k = rsv.ewm(com=2, adjust=False).mean()
    d = k.ewm(com=2, adjust=False).mean()
    if _cross_up(k, d):
        return True, f"KD{period} 黃金交叉"
    return False, ""


def _bollinger_breakout(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 20)
    dev = _num(params, "dev", 2.0)
    close = _series(df, "Close")
    if len(close) < period + 1:
        return False, ""
    ma = close.rolling(period).mean()
    std = close.rolling(period).std()
    upper = ma + dev * std
    if close.iloc[-1] > upper.iloc[-1] and close.iloc[-2] <= upper.iloc[-2]:
        return True, f"收盤突破布林上軌 ({period}, {dev:g})"
    return False, ""


def _obv_rising(df: pd.DataFrame, params: dict[str, Any], _chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    period = _int(params, "period", 5)
    close = _series(df, "Close")
    volume = _series(df, "Volume")
    if len(close) < period + 2:
        return False, ""
    direction = close.diff().apply(lambda value: 1 if value > 0 else (-1 if value < 0 else 0))
    obv = (direction * volume).fillna(0).cumsum()
    if obv.iloc[-1] > obv.iloc[-period - 1]:
        return True, f"OBV 近 {period} 日上升"
    return False, ""


def _foreign_continuous_buy(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    days = _int(params, "days", 3)
    threshold = _num(params, "threshold", 1000)
    foreign = _daily_net(chips.get("institutional", pd.DataFrame()), ["Foreign", "外資"])
    if len(foreign) < days:
        return False, ""
    recent = foreign.iloc[-days:]
    if (recent > 0).all() and recent.sum() >= threshold:
        return True, f"外資連 {days} 買，累計 {recent.sum():.0f} 張"
    return False, ""


def _trust_continuous_buy(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    days = _int(params, "days", 3)
    threshold = _num(params, "threshold", 300)
    trust = _daily_net(chips.get("institutional", pd.DataFrame()), ["Trust", "投信"])
    if len(trust) < days:
        return False, ""
    recent = trust.iloc[-days:]
    if (recent > 0).all() and recent.sum() >= threshold:
        return True, f"投信連 {days} 買，累計 {recent.sum():.0f} 張"
    return False, ""


def _institutional_sync_buy(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    threshold = _num(params, "threshold", 500)
    institutional = chips.get("institutional", pd.DataFrame())
    foreign = _daily_net(institutional, ["Foreign", "外資"])
    trust = _daily_net(institutional, ["Trust", "投信"])
    dealer = _daily_net(institutional, ["Dealer", "自營"])
    combined = pd.concat([foreign, trust, dealer], axis=1, keys=["外資", "投信", "自營"]).dropna()
    if combined.empty:
        return False, ""
    latest = combined.iloc[-1]
    if (latest > 0).all() and latest.sum() >= threshold:
        return True, f"三大法人同步買超，合計 {latest.sum():.0f} 張"
    return False, ""


def _trust_first_entry(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    threshold = _num(params, "threshold", 100)
    quiet_days = _int(params, "quiet_days", 5)
    trust = _daily_net(chips.get("institutional", pd.DataFrame()), ["Trust", "投信"])
    if len(trust) < quiet_days + 1:
        return False, ""
    today = trust.iloc[-1]
    previous = trust.iloc[-quiet_days - 1 : -1].sum()
    if today >= threshold and previous < threshold * 0.5:
        return True, f"投信首日介入：今日買超 {today:.0f} 張"
    return False, ""


def _margin_balance_rising(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    days = _int(params, "days", 3)
    margin = _balance_series(
        chips.get("margin", pd.DataFrame()),
        ["MarginPurchaseTodayBalance", "MarginPurchaseYesterdayBalance", "融資餘額"],
    )
    if len(margin) < days + 1:
        return False, ""
    if margin.iloc[-1] > margin.iloc[-days - 1]:
        return True, f"融資餘額近 {days} 日增加"
    return False, ""


def _short_covering(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    days = _int(params, "days", 3)
    short_sale = _balance_series(
        chips.get("margin", pd.DataFrame()),
        ["ShortSaleTodayBalance", "ShortSaleYesterdayBalance", "融券餘額"],
    )
    if len(short_sale) < days + 1:
        return False, ""
    if short_sale.iloc[-1] < short_sale.iloc[-days - 1]:
        return True, f"融券餘額近 {days} 日下降"
    return False, ""


def _sbl_balance_decline(_df: pd.DataFrame, params: dict[str, Any], chips: dict[str, pd.DataFrame]) -> tuple[bool, str]:
    days = _int(params, "days", 5)
    sbl = _balance_series(chips.get("sbl", pd.DataFrame()), ["balance", "借券賣出餘額"])
    if len(sbl) < days + 1:
        return False, ""
    if sbl.iloc[-1] < sbl.iloc[-days - 1]:
        return True, f"借券賣出餘額近 {days} 日下降"
    return False, ""


INDICATORS: dict[str, tuple[IndicatorDefinition, IndicatorEvaluator]] = {
    "tech.ma_trend": (
        IndicatorDefinition("tech.ma_trend", "均線多頭排列", "technical", "趨勢", "after_market", "收盤價站上短中長均線，適合盤後趨勢篩選。", {"short": 5, "mid": 20, "long": 60}, ["price"]),
        _ma_trend,
    ),
    "tech.ma_golden_cross": (
        IndicatorDefinition("tech.ma_golden_cross", "均線黃金交叉", "technical", "趨勢", "intraday_after_market", "短均線向上穿越長均線。", {"fast": 5, "slow": 20}, ["price"]),
        _ma_golden_cross,
    ),
    "tech.price_breakout": (
        IndicatorDefinition("tech.price_breakout", "收盤突破 N 日高", "technical", "突破", "intraday_after_market", "收盤突破前 N 日高點。", {"period": 20}, ["price"]),
        _price_breakout,
    ),
    "tech.volume_surge": (
        IndicatorDefinition("tech.volume_surge", "成交量放大", "technical", "量能", "intraday_after_market", "今日量大於過去均量倍數。", {"period": 20, "multiple": 1.8}, ["price"]),
        _volume_surge,
    ),
    "tech.rsi_rebound": (
        IndicatorDefinition("tech.rsi_rebound", "RSI 低檔轉強", "technical", "動能", "after_market", "RSI 自低檔門檻向上回升。", {"period": 14, "level": 30}, ["price"]),
        _rsi_rebound,
    ),
    "tech.macd_golden_cross": (
        IndicatorDefinition("tech.macd_golden_cross", "MACD 黃金交叉", "technical", "動能", "after_market", "MACD 線向上穿越 Signal。", {}, ["price"]),
        _macd_golden_cross,
    ),
    "tech.kd_golden_cross": (
        IndicatorDefinition("tech.kd_golden_cross", "KD 黃金交叉", "technical", "動能", "after_market", "K 值向上穿越 D 值。", {"period": 9}, ["price"]),
        _kd_golden_cross,
    ),
    "tech.bollinger_breakout": (
        IndicatorDefinition("tech.bollinger_breakout", "布林上軌突破", "technical", "波動", "intraday_after_market", "收盤突破布林通道上軌。", {"period": 20, "dev": 2.0}, ["price"]),
        _bollinger_breakout,
    ),
    "tech.obv_rising": (
        IndicatorDefinition("tech.obv_rising", "OBV 量能累積", "technical", "量能", "after_market", "OBV 近 N 日上升，觀察量能是否偏多。", {"period": 5}, ["price"]),
        _obv_rising,
    ),
    "chip.foreign_continuous_buy": (
        IndicatorDefinition("chip.foreign_continuous_buy", "外資連續買超", "chip", "法人", "after_market", "外資連續 N 日買超且累計達門檻。", {"days": 3, "threshold": 1000}, ["institutional"]),
        _foreign_continuous_buy,
    ),
    "chip.trust_continuous_buy": (
        IndicatorDefinition("chip.trust_continuous_buy", "投信連續買超", "chip", "法人", "after_market", "投信連續 N 日買超且累計達門檻。", {"days": 3, "threshold": 300}, ["institutional"]),
        _trust_continuous_buy,
    ),
    "chip.institutional_sync_buy": (
        IndicatorDefinition("chip.institutional_sync_buy", "三大法人同步買超", "chip", "法人", "after_market", "外資、投信、自營商同日同步買超。", {"threshold": 500}, ["institutional"]),
        _institutional_sync_buy,
    ),
    "chip.trust_first_entry": (
        IndicatorDefinition("chip.trust_first_entry", "投信首日介入", "chip", "法人", "after_market", "投信今日大買，前段時間未明顯買超。", {"threshold": 100, "quiet_days": 5}, ["institutional"]),
        _trust_first_entry,
    ),
    "chip.margin_balance_rising": (
        IndicatorDefinition("chip.margin_balance_rising", "融資餘額上升", "chip", "信用", "after_market", "融資餘額近 N 日增加。", {"days": 3}, ["margin"]),
        _margin_balance_rising,
    ),
    "chip.short_covering": (
        IndicatorDefinition("chip.short_covering", "融券回補", "chip", "信用", "after_market", "融券餘額近 N 日下降。", {"days": 3}, ["margin"]),
        _short_covering,
    ),
    "chip.sbl_balance_decline": (
        IndicatorDefinition("chip.sbl_balance_decline", "借券賣出餘額下降", "chip", "借券", "after_market", "借券賣出餘額近 N 日下降。", {"days": 5}, ["sbl"]),
        _sbl_balance_decline,
    ),
}


def get_indicator_catalog() -> list[dict[str, Any]]:
    return [definition.to_dict() for definition, _evaluator in INDICATORS.values()]


def get_indicator_definition(indicator_id: str) -> IndicatorDefinition | None:
    item = INDICATORS.get(indicator_id)
    return item[0] if item else None


def uses_chip_data(indicator_ids: list[str]) -> bool:
    for indicator_id in indicator_ids:
        definition = get_indicator_definition(indicator_id)
        if definition and any(req in definition.data_requirements for req in ["institutional", "margin", "sbl"]):
            return True
    return False


def evaluate_indicator(
    indicator_id: str,
    df: pd.DataFrame,
    params: dict[str, Any] | None = None,
    chip_cache: dict[str, pd.DataFrame] | None = None,
) -> tuple[bool, str]:
    item = INDICATORS.get(indicator_id)
    if not item:
        return False, f"找不到指標：{indicator_id}"
    definition, evaluator = item
    merged_params = {**definition.params, **(params or {})}
    return evaluator(df, merged_params, chip_cache or {})


def evaluate_indicator_set(
    df: pd.DataFrame,
    indicator_ids: list[str],
    match_mode: str = "AND",
    indicator_params: dict[str, dict[str, Any]] | None = None,
    chip_cache: dict[str, pd.DataFrame] | None = None,
) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    for indicator_id in indicator_ids:
        matched, reason = evaluate_indicator(
            indicator_id,
            df,
            (indicator_params or {}).get(indicator_id, {}),
            chip_cache,
        )
        if matched:
            definition = get_indicator_definition(indicator_id)
            label = definition.name if definition else indicator_id
            reasons.append(f"[{label}] {reason}")
    normalized_mode = match_mode.upper()
    if normalized_mode == "OR":
        return bool(reasons), reasons
    return len(reasons) == len(indicator_ids), reasons
