import pandas as pd

from data.workspace_models import AfterMarketScan, NextDayWatchlist
from data.workspace_store import WorkspaceStore
from scanner import daily_after_market
from scanner.daily_after_market import run_after_market_scan


def _history(rows: int = 70, close: float = 100.0, volume: int = 1000) -> pd.DataFrame:
    index = pd.date_range("2026-01-01", periods=rows, freq="D")
    closes = pd.Series([close + idx * 0.2 for idx in range(rows)], index=index)
    return pd.DataFrame(
        {
            "Open": closes - 1,
            "High": closes + 2,
            "Low": closes - 2,
            "Close": closes,
            "Volume": [volume] * rows,
        },
        index=index,
    )


class FakeFetcher:
    @staticmethod
    def fetch_history(stock_id, period="6mo"):
        if stock_id == "9999":
            return _history(rows=10)
        return _history()

    @staticmethod
    def get_stock_info(stock_id):
        names = {"2330": "台積電", "2317": "鴻海", "2603": "長榮", "9999": "缺資料"}
        return names.get(stock_id, stock_id), "test", ""

    @staticmethod
    def fetch_institutional_investors(stock_id, days=90):
        return pd.DataFrame()

    @staticmethod
    def fetch_margin_trading(stock_id, days=90):
        return pd.DataFrame()

    @staticmethod
    def fetch_borrowing_sell(stock_id, days=90):
        return pd.DataFrame()

    @staticmethod
    def fetch_market_index(market="TSE", period="6mo"):
        return _history()


def test_after_market_scan_saves_scan_and_next_day_watchlist(tmp_path, monkeypatch):
    def fake_score_stock(stock_id, stock_payload, market_data, profile, weights):
        scores = {
            "2330": {"score": 82, "riskScore": -5, "reasons": ["均線多頭排列"]},
            "2317": {"score": 62, "riskScore": -8, "reasons": ["成交量放大"]},
            "2603": {"score": 68, "riskScore": -35, "reasons": ["突破 20 日高"], "risks": ["爆量長上影"]},
        }
        return scores[stock_id]

    monkeypatch.setattr(daily_after_market, "score_stock", fake_score_stock)
    store = WorkspaceStore(base_dir=str(tmp_path / "workspace"))

    result = run_after_market_scan(
        {
            "date": "2026-05-10",
            "marketType": "TEST",
            "stockList": ["2330", "2317", "2603", "9999"],
            "maxStocks": 4,
            "profile": "balanced",
            "includeRiskList": True,
        },
        data_fetcher=FakeFetcher,
        store=store,
    )

    assert result["scanId"].startswith("after_market_20260510_")
    assert result["counts"] == {
        "requested": 4,
        "scanned": 3,
        "skipped": 1,
        "aList": 1,
        "bList": 1,
        "avoidList": 1,
    }
    assert result["aList"][0]["stockId"] == "2330"
    assert result["bList"][0]["stockId"] == "2317"
    assert result["avoidList"][0]["stockId"] == "2603"
    assert result["skipped"] == [{"stockId": "9999", "reason": "insufficient history: need at least 45 rows"}]

    saved_scan = store.get_after_market_scan(result["scanId"])
    assert isinstance(saved_scan, AfterMarketScan)
    assert saved_scan.a_list[0]["stockId"] == "2330"

    watchlists = store.list_next_day_watchlists()
    assert len(watchlists) == 1
    assert isinstance(watchlists[0], NextDayWatchlist)
    assert [item["stockId"] for item in watchlists[0].stocks] == ["2330", "2317"]


def test_after_market_scan_can_hide_risk_list(tmp_path, monkeypatch):
    def fake_score_stock(stock_id, stock_payload, market_data, profile, weights):
        return {"stockId": stock_id, "score": 80, "riskScore": -40, "risks": ["注意/處置股"]}

    monkeypatch.setattr(daily_after_market, "score_stock", fake_score_stock)
    store = WorkspaceStore(base_dir=str(tmp_path / "workspace"))

    result = run_after_market_scan(
        {
            "date": "2026-05-10",
            "marketType": "TEST",
            "stockList": ["2330"],
            "includeRiskList": False,
        },
        data_fetcher=FakeFetcher,
        store=store,
    )

    assert result["avoidList"] == []
    assert result["counts"]["avoidList"] == 0
    assert store.get_after_market_scan(result["scanId"]).avoid_list == []


def test_after_market_scan_uses_real_scoring_signature(tmp_path, monkeypatch):
    monkeypatch.setattr(daily_after_market, "score_stock", None)
    store = WorkspaceStore(base_dir=str(tmp_path / "workspace"))

    result = run_after_market_scan(
        {
            "date": "2026-05-10",
            "marketType": "Custom",
            "stockList": ["2330"],
            "maxStocks": 1,
            "profile": "balanced",
        },
        data_fetcher=FakeFetcher,
        store=store,
    )

    assert result["counts"]["requested"] == 1
    assert result["counts"]["scanned"] == 1
    assert result["counts"]["skipped"] == 0
