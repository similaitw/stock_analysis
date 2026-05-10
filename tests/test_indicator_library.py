import numpy as np
import pandas as pd

from strategies.indicator_library import (
    evaluate_indicator,
    evaluate_indicator_set,
    get_indicator_catalog,
)


def _price_frame() -> pd.DataFrame:
    closes = list(np.linspace(80, 100, 70))
    closes[-1] = 108
    index = pd.date_range("2026-01-01", periods=len(closes), freq="D")
    close = pd.Series(closes, index=index)
    volume = pd.Series([1000] * 69 + [3000], index=index)
    return pd.DataFrame(
        {
            "Open": close * 0.99,
            "High": close * 1.01,
            "Low": close * 0.98,
            "Close": close,
            "Volume": volume,
        },
        index=index,
    )


def test_indicator_catalog_contains_technical_and_chip_modules():
    catalog = get_indicator_catalog()
    ids = {item["id"] for item in catalog}

    assert "tech.ma_trend" in ids
    assert "tech.volume_surge" in ids
    assert "chip.foreign_continuous_buy" in ids
    assert {item["category"] for item in catalog} >= {"technical", "chip"}


def test_evaluate_indicator_set_supports_and_or_composition():
    df = _price_frame()

    matched_and, reasons_and = evaluate_indicator_set(
        df,
        ["tech.ma_trend", "tech.volume_surge"],
        match_mode="AND",
    )
    matched_or, reasons_or = evaluate_indicator_set(
        df,
        ["tech.volume_surge", "chip.foreign_continuous_buy"],
        match_mode="OR",
    )

    assert matched_and
    assert len(reasons_and) == 2
    assert matched_or
    assert len(reasons_or) == 1


def test_chip_indicator_uses_cached_institutional_data():
    df = _price_frame()
    institutional = pd.DataFrame(
        [
            {"date": "2026-01-01", "name": "Foreign_Investor", "buy": 2000, "sell": 1000},
            {"date": "2026-01-02", "name": "Foreign_Investor", "buy": 2500, "sell": 1000},
            {"date": "2026-01-03", "name": "Foreign_Investor", "buy": 3000, "sell": 1000},
        ]
    )

    matched, reason = evaluate_indicator(
        "chip.foreign_continuous_buy",
        df,
        {"days": 3, "threshold": 1000},
        {"institutional": institutional},
    )

    assert matched
    assert "外資連 3 買" in reason
