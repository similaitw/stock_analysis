import numpy as np
import pandas as pd

from scanner.scoring import classify_result, score_stock


def _price_frame(
    *,
    last_close: float = 130,
    last_open: float | None = None,
    last_high: float | None = None,
    last_low: float | None = None,
    last_volume: float = 2500,
    rows: int = 80,
    attention: bool = False,
) -> pd.DataFrame:
    index = pd.date_range("2026-01-01", periods=rows, freq="D")
    closes = np.linspace(80, 115, rows)
    closes[-1] = last_close
    close = pd.Series(closes, index=index)
    open_ = close * 0.99
    high = close * 1.01
    low = close * 0.98
    volume = pd.Series([1000.0] * rows, index=index)
    volume.iloc[-1] = last_volume
    open_.iloc[-1] = last_open if last_open is not None else last_close * 0.99
    high.iloc[-1] = last_high if last_high is not None else max(last_close * 1.01, last_close + 1)
    low.iloc[-1] = last_low if last_low is not None else min(last_close * 0.98, last_close - 1)
    data = pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume})
    if attention:
        data["Attention"] = False
        data.loc[index[-1], "Attention"] = True
    return data


def _institutional(
    foreign: list[float] | None = None,
    trust: list[float] | None = None,
    dealer: list[float] | None = None,
) -> pd.DataFrame:
    foreign = foreign or [400, 450, 500]
    trust = trust or [150, 160, 170]
    dealer = dealer or [60, 70, 80]
    dates = pd.date_range("2026-03-01", periods=max(len(foreign), len(trust), len(dealer)), freq="D")
    rows = []
    for idx, date in enumerate(dates):
        if idx < len(foreign):
            rows.append({"date": date.date().isoformat(), "name": "Foreign_Investor", "net": foreign[idx]})
        if idx < len(trust):
            rows.append({"date": date.date().isoformat(), "name": "Investment_Trust", "net": trust[idx]})
        if idx < len(dealer):
            rows.append({"date": date.date().isoformat(), "name": "Dealer", "net": dealer[idx]})
    return pd.DataFrame(rows)


def _chip_cache(
    foreign: list[float] | None = None,
    trust: list[float] | None = None,
    dealer: list[float] | None = None,
    sbl: list[float] | None = None,
    short_sale: list[float] | None = None,
) -> dict[str, pd.DataFrame]:
    days = pd.date_range("2026-03-01", periods=6, freq="D")
    return {
        "institutional": _institutional(foreign, trust, dealer),
        "sbl": pd.DataFrame(
            {
                "date": [day.date().isoformat() for day in days],
                "balance": sbl or [1200, 1160, 1110, 1080, 1040, 980],
            }
        ),
        "margin": pd.DataFrame(
            {
                "date": [day.date().isoformat() for day in days],
                "ShortSaleTodayBalance": short_sale or [500, 480, 460, 440, 430, 410],
                "MarginPurchaseTodayBalance": [1000, 1010, 1020, 1030, 1040, 1050],
            }
        ),
    }


def _benchmark(last_close: float) -> pd.DataFrame:
    rows = 80
    index = pd.date_range("2026-01-01", periods=rows, freq="D")
    close = pd.Series(np.linspace(100, last_close, rows), index=index)
    return pd.DataFrame({"Close": close})


def test_score_stock_returns_a_grade_with_full_reasons():
    result = score_stock(
        "2330",
        _price_frame(),
        _chip_cache(),
        market_df=_benchmark(104),
        industry_df=_benchmark(106),
    )

    assert result.classification == "A"
    assert result.total_score >= 75
    assert result.technical_score > 0
    assert result.volume_score > 0
    assert result.chip_score > 0
    assert result.relative_strength_score > 0
    assert "均線多頭排列" in result.reasons
    assert result.risks == ()


def test_score_stock_returns_b_grade_for_watchlist_candidate():
    result = score_stock(
        "2317",
        _price_frame(last_close=118, last_volume=1600),
        _chip_cache(foreign=[0, 200, 300], trust=[0, 0, 120], dealer=[0, 0, 50], sbl=[1000] * 6, short_sale=[500] * 6),
        market_df=_benchmark(118),
        industry_df=_benchmark(117),
    )

    assert result.classification == "B"
    assert 55 <= result.total_score <= 74
    assert result.risk_score == 0


def test_score_stock_avoids_major_attention_even_when_score_is_high():
    result = score_stock(
        "0000",
        _price_frame(attention=True),
        _chip_cache(),
        market_df=_benchmark(104),
        industry_df=_benchmark(106),
    )

    assert result.classification == "avoid"
    assert result.major_risk
    assert result.risk_score <= -30
    assert "注意/處置股" in result.risks


def test_score_stock_skips_when_price_history_is_insufficient():
    result = score_stock("9999", _price_frame(rows=20), _chip_cache())

    assert result.classification == "skip"
    assert result.skip_reason is not None
    assert "insufficient history" in result.skip_reason
    assert result.reasons == ()


def test_classify_result_thresholds():
    assert classify_result(total_score=75, risk_score=0) == "A"
    assert classify_result(total_score=55, risk_score=-29) == "B"
    assert classify_result(total_score=54, risk_score=0) == "hidden"
    assert classify_result(total_score=90, risk_score=-30) == "avoid"
