from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Mapping

import pandas as pd


MIN_HISTORY_DAYS = 45
MIN_AVG_VOLUME_20 = 500
MIN_TODAY_VOLUME = 300
MIN_PRICE = 10


@dataclass(frozen=True)
class ScoreComponent:
    score: int = 0
    reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class RiskComponent:
    score: int = 0
    risks: tuple[str, ...] = field(default_factory=tuple)
    major: bool = False


@dataclass(frozen=True)
class ScoreBreakdown:
    stock_id: str
    total_score: int
    technical_score: int
    volume_score: int
    chip_score: int
    relative_strength_score: int
    risk_score: int
    classification: str
    reasons: tuple[str, ...] = field(default_factory=tuple)
    risks: tuple[str, ...] = field(default_factory=tuple)
    skip_reason: str | None = None
    major_risk: bool = False
    metrics: Mapping[str, float] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["score"] = self.total_score
        return payload


def score_stock(
    stock_id: str,
    price_df: pd.DataFrame,
    chip_cache: Mapping[str, pd.DataFrame] | None = None,
    market_df: pd.DataFrame | None = None,
    industry_df: pd.DataFrame | Mapping[str, pd.DataFrame] | None = None,
) -> ScoreBreakdown:
    """Score one stock from already-loaded after-market data."""
    chips = dict(chip_cache or {})
    prepared = _prepare_price_df(price_df)
    skip_reason = _base_filter_skip_reason(prepared)
    if skip_reason:
        return ScoreBreakdown(
            stock_id=stock_id,
            total_score=0,
            technical_score=0,
            volume_score=0,
            chip_score=0,
            relative_strength_score=0,
            risk_score=0,
            classification="skip",
            skip_reason=skip_reason,
        )

    technical = _score_technical(prepared)
    volume = _score_volume(prepared)
    chip = _score_chip(chips)
    relative = _score_relative_strength(stock_id, prepared, market_df, industry_df)
    risk = _score_risk(prepared, chips)

    positive_score = min(40, technical.score) + min(15, volume.score) + min(30, chip.score) + min(
        15, relative.score
    )
    total_score = max(0, min(100, positive_score + risk.score))
    reasons = technical.reasons + volume.reasons + chip.reasons + relative.reasons
    classification = classify_result(total_score=total_score, risk_score=risk.score, major_risk=risk.major)

    return ScoreBreakdown(
        stock_id=stock_id,
        total_score=total_score,
        technical_score=min(40, technical.score),
        volume_score=min(15, volume.score),
        chip_score=min(30, chip.score),
        relative_strength_score=min(15, relative.score),
        risk_score=risk.score,
        classification=classification,
        reasons=reasons,
        risks=risk.risks,
        major_risk=risk.major,
        metrics=_latest_metrics(prepared),
    )


def classify_result(total_score: int, risk_score: int, major_risk: bool = False) -> str:
    if major_risk or risk_score <= -30:
        return "avoid"
    if total_score >= 75:
        return "A"
    if 55 <= total_score <= 74:
        return "B"
    return "hidden"


def _prepare_price_df(df: pd.DataFrame | None) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    prepared = df.copy()
    for column in ["Open", "High", "Low", "Close", "Volume"]:
        if column in prepared.columns:
            prepared[column] = pd.to_numeric(prepared[column], errors="coerce")
    return prepared.dropna(subset=[column for column in ["Open", "High", "Low", "Close", "Volume"] if column in prepared])


def _base_filter_skip_reason(df: pd.DataFrame) -> str | None:
    required = {"Open", "High", "Low", "Close", "Volume"}
    missing = sorted(required - set(df.columns))
    if missing:
        return f"missing required columns: {', '.join(missing)}"
    if len(df) < MIN_HISTORY_DAYS:
        return f"insufficient history: {len(df)} rows < {MIN_HISTORY_DAYS}"
    close = df["Close"]
    volume = df["Volume"]
    if len(df) < 60:
        return f"insufficient MA60 history: {len(df)} rows < 60"
    if close.iloc[-1] < MIN_PRICE:
        return f"price below minimum: {close.iloc[-1]:.2f} < {MIN_PRICE}"
    avg_volume_20 = volume.iloc[-21:-1].mean()
    if avg_volume_20 < MIN_AVG_VOLUME_20:
        return f"20-day average volume too low: {avg_volume_20:.0f} < {MIN_AVG_VOLUME_20}"
    if volume.iloc[-1] < MIN_TODAY_VOLUME:
        return f"today volume too low: {volume.iloc[-1]:.0f} < {MIN_TODAY_VOLUME}"
    return None


def _score_technical(df: pd.DataFrame) -> ScoreComponent:
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    reasons: list[str] = []
    score = 0

    ma5 = close.rolling(5).mean()
    ma20 = close.rolling(20).mean()
    ma60 = close.rolling(60).mean()
    if close.iloc[-1] > ma5.iloc[-1] > ma20.iloc[-1] > ma60.iloc[-1]:
        score += 10
        reasons.append("均線多頭排列")

    previous_20_high = high.iloc[-21:-1].max()
    if close.iloc[-1] > previous_20_high:
        score += 10
        reasons.append("突破 20 日高")

    if _cross_up(ma5, ma20):
        score += 6
        reasons.append("均線黃金交叉")

    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    if _cross_up(macd, signal):
        score += 6
        reasons.append("MACD 黃金交叉")

    k, d = _kd(high, low, close)
    if _cross_up(k, d):
        score += 4
        reasons.append("KD 黃金交叉")

    rsi = _rsi(close)
    if len(rsi) >= 2 and rsi.iloc[-1] > 30 and rsi.iloc[-2] <= 30:
        score += 4
        reasons.append("RSI 低檔轉強")

    boll_upper = close.rolling(20).mean() + close.rolling(20).std() * 2
    if close.iloc[-1] > boll_upper.iloc[-1]:
        score += 4
        reasons.append("布林上軌突破")

    return ScoreComponent(min(score, 40), tuple(reasons))


def _score_volume(df: pd.DataFrame) -> ScoreComponent:
    close = df["Close"]
    volume = df["Volume"]
    reasons: list[str] = []
    score = 0
    avg20 = volume.iloc[-21:-1].mean()

    if avg20 > 0 and volume.iloc[-1] >= avg20 * 1.5:
        score += 8
        reasons.append("成交量放大")

    if close.iloc[-1] >= close.iloc[-21:-1].max() and volume.iloc[-1] >= volume.iloc[-21:-1].max():
        score += 5
        reasons.append("價量同步創高")

    direction = close.diff().apply(lambda value: 1 if value > 0 else (-1 if value < 0 else 0))
    obv = (direction * volume).fillna(0).cumsum()
    if obv.iloc[-1] > obv.iloc[-6]:
        score += 4
        reasons.append("OBV 上升")

    return ScoreComponent(min(score, 15), tuple(reasons))


def _score_chip(chips: Mapping[str, pd.DataFrame]) -> ScoreComponent:
    institutional = chips.get("institutional", pd.DataFrame())
    margin = chips.get("margin", pd.DataFrame())
    sbl = chips.get("sbl", pd.DataFrame())
    foreign = _daily_net(institutional, ["Foreign", "外資"])
    trust = _daily_net(institutional, ["Trust", "投信"])
    dealer = _daily_net(institutional, ["Dealer", "自營"])
    short_sale = _balance_series(margin, ["ShortSaleTodayBalance", "ShortSaleYesterdayBalance", "融券餘額"])
    sbl_balance = _balance_series(sbl, ["balance", "借券賣出餘額"])

    reasons: list[str] = []
    score = 0
    if len(foreign) >= 3 and (foreign.iloc[-3:] > 0).all() and foreign.iloc[-3:].sum() >= 1000:
        score += 8
        reasons.append("外資連續買超")
    if len(trust) >= 3 and (trust.iloc[-3:] > 0).all() and trust.iloc[-3:].sum() >= 300:
        score += 10
        reasons.append("投信連續買超")
    combined = pd.concat([foreign, trust, dealer], axis=1).dropna()
    if not combined.empty and (combined.iloc[-1] > 0).all() and combined.iloc[-1].sum() >= 500:
        score += 8
        reasons.append("三大法人同步買超")
    if len(trust) >= 6 and trust.iloc[-1] >= 100 and trust.iloc[-6:-1].abs().sum() < 50:
        score += 6
        reasons.append("投信首日介入")
    if len(sbl_balance) >= 6 and sbl_balance.iloc[-1] < sbl_balance.iloc[-6]:
        score += 4
        reasons.append("借券賣出餘額下降")
    if len(short_sale) >= 4 and short_sale.iloc[-1] < short_sale.iloc[-4]:
        score += 4
        reasons.append("融券回補")
    return ScoreComponent(min(score, 30), tuple(reasons))


def _score_relative_strength(
    stock_id: str,
    price_df: pd.DataFrame,
    market_df: pd.DataFrame | None,
    industry_df: pd.DataFrame | Mapping[str, pd.DataFrame] | None,
) -> ScoreComponent:
    reasons: list[str] = []
    score = 0
    stock_return = _period_return(price_df, 20)
    market_return = _period_return(market_df, 20)
    industry = _resolve_industry_df(stock_id, industry_df)
    industry_return = _period_return(industry, 20)

    if market_return is not None and stock_return is not None and stock_return > market_return:
        score += 6
        reasons.append("強於大盤")
    if industry_return is not None and stock_return is not None and stock_return > industry_return:
        score += 6
        reasons.append("強於產業")
    if market_return is not None and market_return < 0:
        latest = price_df.iloc[-1]
        ma20 = price_df["Close"].rolling(20).mean().iloc[-1]
        if latest["Close"] > latest["Open"] or latest["Close"] >= ma20:
            score += 3
            reasons.append("大盤弱勢仍抗跌")
    return ScoreComponent(min(score, 15), tuple(reasons))


def _score_risk(df: pd.DataFrame, chips: Mapping[str, pd.DataFrame]) -> RiskComponent:
    latest = df.iloc[-1]
    previous_close = df["Close"].iloc[-2]
    ma20 = df["Close"].rolling(20).mean().iloc[-1]
    ma60 = df["Close"].rolling(60).mean().iloc[-1]
    avg20 = df["Volume"].iloc[-21:-1].mean()
    day_range = max(latest["High"] - latest["Low"], 0.01)
    upper_shadow = latest["High"] - max(latest["Open"], latest["Close"])
    close_position = (latest["Close"] - latest["Low"]) / day_range
    daily_return = latest["Close"] / previous_close - 1
    open_return = latest["Open"] / previous_close - 1

    institutional = chips.get("institutional", pd.DataFrame())
    foreign = _daily_net(institutional, ["Foreign", "外資"])
    trust = _daily_net(institutional, ["Trust", "投信"])
    margin_balance = _balance_series(
        chips.get("margin", pd.DataFrame()),
        ["MarginPurchaseTodayBalance", "MarginPurchaseYesterdayBalance", "融資餘額"],
    )
    sbl_balance = _balance_series(chips.get("sbl", pd.DataFrame()), ["balance", "借券賣出餘額"])

    risks: list[str] = []
    score = 0
    major = False

    if avg20 > 0 and latest["Volume"] >= avg20 * 2 and upper_shadow / day_range >= 0.45:
        score -= 20
        risks.append("爆量長上影")
    if open_return >= 0.02 and latest["Close"] < latest["Open"] and close_position <= 0.3:
        score -= 12
        risks.append("開高走低")
    if latest["Close"] < ma20:
        score -= 12
        risks.append("跌破 MA20")
    if latest["Close"] < ma60:
        score -= 20
        risks.append("跌破 MA60")
    if len(margin_balance) >= 2 and margin_balance.iloc[-1] > margin_balance.iloc[-2] * 1.03 and daily_return < 0.01:
        score -= 15
        risks.append("融資大增但價格不漲")
    if len(foreign) >= 1 and len(trust) >= 1 and foreign.iloc[-1] < 0 and trust.iloc[-1] < 0:
        score -= 20
        risks.append("外資投信同步賣超")
    if len(trust) >= 4 and (trust.iloc[-4:-1] > 0).all() and trust.iloc[-1] < 0:
        score -= 15
        risks.append("投信連買後轉賣")
    if len(sbl_balance) >= 2 and sbl_balance.iloc[-1] > sbl_balance.iloc[-2] * 1.08:
        score -= 12
        risks.append("借券賣出餘額大增")
    if latest["High"] / previous_close >= 1.095 and latest["Close"] < latest["High"] * 0.985:
        score -= 15
        risks.append("漲停打開")

    if _truthy_latest(df, ["Attention", "Disposition", "注意股", "處置股"]):
        score -= 30
        major = True
        risks.append("注意/處置股")

    return RiskComponent(max(score, -50), tuple(risks), major)


def _cross_up(fast: pd.Series, slow: pd.Series) -> bool:
    if len(fast) < 2 or len(slow) < 2:
        return False
    return bool(fast.iloc[-1] > slow.iloc[-1] and fast.iloc[-2] <= slow.iloc[-2])


def _kd(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 9) -> tuple[pd.Series, pd.Series]:
    lowest = low.rolling(period).min()
    highest = high.rolling(period).max()
    rsv = ((close - lowest) / (highest - lowest).replace(0, pd.NA) * 100).fillna(50)
    k = rsv.ewm(com=2, adjust=False).mean()
    d = k.ewm(com=2, adjust=False).mean()
    return k, d


def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    return (100 - (100 / (1 + gain / loss.replace(0, float("nan"))))).fillna(50)


def _daily_net(df: pd.DataFrame, keywords: list[str]) -> pd.Series:
    if df is None or df.empty:
        return pd.Series(dtype="float64")
    work = df.copy()
    if "net" not in work.columns and {"buy", "sell"}.issubset(work.columns):
        work["net"] = pd.to_numeric(work["buy"], errors="coerce") - pd.to_numeric(work["sell"], errors="coerce")
    if "net" not in work.columns:
        return pd.Series(dtype="float64")
    if "name" in work.columns:
        mask = pd.Series(False, index=work.index)
        for keyword in keywords:
            mask |= work["name"].astype(str).str.contains(keyword, case=False, na=False)
        work = work[mask]
    if work.empty:
        return pd.Series(dtype="float64")
    net = pd.to_numeric(work["net"], errors="coerce")
    if "date" in work.columns:
        return net.groupby(work["date"]).sum().sort_index().dropna()
    return net.dropna()


def _balance_series(df: pd.DataFrame, candidates: list[str]) -> pd.Series:
    if df is None or df.empty:
        return pd.Series(dtype="float64")
    for column in candidates:
        if column in df.columns:
            values = pd.to_numeric(df[column], errors="coerce")
            if "date" in df.columns:
                values.index = df["date"]
            return values.dropna()
    return pd.Series(dtype="float64")


def _period_return(df: pd.DataFrame | None, days: int) -> float | None:
    if df is None or df.empty or "Close" not in df.columns or len(df) < days + 1:
        return None
    close = pd.to_numeric(df["Close"], errors="coerce").dropna()
    if len(close) < days + 1 or close.iloc[-days - 1] == 0:
        return None
    return float(close.iloc[-1] / close.iloc[-days - 1] - 1)


def _resolve_industry_df(
    stock_id: str, industry_df: pd.DataFrame | Mapping[str, pd.DataFrame] | None
) -> pd.DataFrame | None:
    if isinstance(industry_df, pd.DataFrame):
        return industry_df
    if isinstance(industry_df, Mapping):
        return industry_df.get(stock_id) or industry_df.get("default")
    return None


def _truthy_latest(df: pd.DataFrame, columns: list[str]) -> bool:
    for column in columns:
        if column in df.columns:
            value = df[column].iloc[-1]
            if isinstance(value, str):
                return value.strip().lower() in {"1", "true", "yes", "y", "注意", "處置"}
            return bool(value)
    return False


def _latest_metrics(df: pd.DataFrame) -> dict[str, float]:
    latest = df.iloc[-1]
    return {
        "close": float(latest["Close"]),
        "volume": float(latest["Volume"]),
        "ma20": float(df["Close"].rolling(20).mean().iloc[-1]),
        "ma60": float(df["Close"].rolling(60).mean().iloc[-1]),
        "avg_volume_20": float(df["Volume"].iloc[-21:-1].mean()),
    }
