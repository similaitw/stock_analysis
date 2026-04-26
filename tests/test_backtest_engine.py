import numpy as np
import pandas as pd

from backtest.engine import get_backtest_strategy_catalog, run_named_backtest
from scanner.engine import ScannerEngine


def _make_price_frame(closes: list[float]) -> pd.DataFrame:
    index = pd.date_range("2025-01-01", periods=len(closes), freq="D")
    close_series = pd.Series(closes, index=index)
    return pd.DataFrame(
        {
            "Open": close_series * 0.99,
            "High": close_series * 1.01,
            "Low": close_series * 0.98,
            "Close": close_series,
            "Volume": np.linspace(1000, 5000, len(closes)),
            "StockID": "2330",
        },
        index=index,
    )


def test_backtest_catalog_includes_core_and_preferred_signal_strategies():
    catalog = get_backtest_strategy_catalog(["XScript - Price/Vol High"])

    assert "MA Crossover" in catalog
    assert "RSI Oversold" in catalog
    assert "Bollinger Buy" in catalog
    assert catalog["XScript - Price/Vol High"]["mode"] == "signal"
    assert "holding_days" in catalog["XScript - Price/Vol High"]["params"]


def test_run_named_backtest_supports_signal_simulation(monkeypatch):
    price_df = _make_price_frame([100 + idx for idx in range(12)])

    def fake_check(strategy_name, df_slice, stock_id, params=None):
        if len(df_slice) == 5:
            return True, "Synthetic entry"
        return False, ""

    monkeypatch.setattr(ScannerEngine, "_check_strategy", staticmethod(fake_check))

    result = run_named_backtest(
        stock_id="2330",
        strategy_name="XScript - Price/Vol High",
        period="1y",
        strategy_params={"holding_days": 3, "stop_loss_pct": 0.0, "take_profit_pct": 0.0},
        price_df=price_df,
    )

    assert result["mode"] == "signal"
    assert result["fallback_note"]
    assert result["trades"]["Action"].tolist() == ["BUY", "SELL"]
    assert result["final_value"] > 1_000_000


def test_run_named_backtest_supports_rsi_backtrader():
    closes = [100 - idx for idx in range(20)] + [80 + idx for idx in range(30)] + [110 - idx for idx in range(20)]
    price_df = _make_price_frame(closes)

    result = run_named_backtest(
        stock_id="2330",
        strategy_name="RSI Oversold",
        period="1y",
        strategy_params={"period": 14, "lower": 35, "upper": 60},
        price_df=price_df,
    )

    assert result["mode"] == "backtrader"
    assert isinstance(result["trades"], pd.DataFrame)
    assert not result["price_df"].empty
    assert result["final_value"] > 0
