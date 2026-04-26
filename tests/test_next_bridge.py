import json
import sys

import pandas as pd

from dev_tools import next_bridge


class _FakeFetcher:
    @staticmethod
    def get_stock_info(ticker):
        print(f"[mock] stock info {ticker}")
        return "台積電", "半導體業", "mock-description"

    @staticmethod
    def fetch_current_price(ticker):
        print(f"[mock] current price {ticker}")
        return 999.0

    @staticmethod
    def fetch_fundamentals(ticker):
        print(f"[mock] fundamentals {ticker}")
        return {"EPS": 88.8}

    @staticmethod
    def fetch_history(ticker, period="6mo"):
        print(f"[mock] history {ticker} {period}")
        return pd.DataFrame(
            [
                {"Date": pd.Timestamp("2026-04-23"), "Close": 950.0, "Volume": 1000},
                {"Date": pd.Timestamp("2026-04-24"), "Close": 999.0, "Volume": 2000},
            ]
        ).set_index("Date")


def test_next_bridge_emits_json_to_stdout_only(monkeypatch, capsys):
    monkeypatch.setattr(next_bridge, "DataFetcher", _FakeFetcher)
    monkeypatch.setattr(sys, "argv", ["next_bridge.py", "research", "2330"])

    assert next_bridge.main() == 0

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert payload["ticker"] == "2330"
    assert payload["currentPrice"] == 999.0
    assert payload["history"][-1]["close"] == 999.0
    assert "[mock]" in captured.err
