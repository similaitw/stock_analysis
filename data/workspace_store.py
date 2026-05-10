from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from data.workspace_models import (
    AfterMarketScan,
    BacktestRun,
    NextDayWatchlist,
    PaperOrder,
    ResearchNote,
    ScreenRun,
    SignalEvent,
    TradePlan,
    Watchlist,
    now_iso,
)


class WorkspaceStore:
    COLLECTIONS = {
        "screen_runs": ScreenRun,
        "signal_events": SignalEvent,
        "backtest_runs": BacktestRun,
        "trade_plans": TradePlan,
        "paper_orders": PaperOrder,
        "watchlists": Watchlist,
        "research_notes": ResearchNote,
        "after_market_scans": AfterMarketScan,
        "next_day_watchlists": NextDayWatchlist,
    }

    SORT_KEYS = {
        "screen_runs": "executed_at",
        "signal_events": "detected_at",
        "backtest_runs": "executed_at",
        "trade_plans": "updated_at",
        "paper_orders": "updated_at",
        "watchlists": "updated_at",
        "research_notes": "updated_at",
        "after_market_scans": "executed_at",
        "next_day_watchlists": "created_at",
    }

    def __init__(self, base_dir: str = "data/workspace"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        for collection in self.COLLECTIONS:
            self._collection_dir(collection).mkdir(parents=True, exist_ok=True)

    def _collection_dir(self, collection: str) -> Path:
        return self.base_dir / collection

    def _write(self, collection: str, record_id: str, payload: dict[str, Any]) -> None:
        path = self._collection_dir(collection) / f"{record_id}.json"
        path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8",
        )

    def _read_all(self, collection: str) -> list[Any]:
        model_cls = self.COLLECTIONS[collection]
        records = []
        for path in self._collection_dir(collection).glob("*.json"):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                records.append(model_cls.from_dict(payload))
            except (json.JSONDecodeError, OSError, ValueError):
                continue
        sort_key = self.SORT_KEYS.get(collection, "updated_at")
        records.sort(key=lambda record: getattr(record, sort_key, ""), reverse=True)
        return records

    def _get_by_id(self, collection: str, record_id: str) -> Optional[Any]:
        path = self._collection_dir(collection) / f"{record_id}.json"
        if not path.exists():
            return None
        payload = json.loads(path.read_text(encoding="utf-8"))
        return self.COLLECTIONS[collection].from_dict(payload)

    def save_screen_run(self, screen_run: ScreenRun) -> ScreenRun:
        self._write("screen_runs", screen_run.id, screen_run.to_dict())
        for event in SignalEvent.from_screen_run(screen_run):
            self._write("signal_events", event.id, event.to_dict())
        return screen_run

    def list_screen_runs(self, limit: Optional[int] = None) -> list[ScreenRun]:
        records = self._read_all("screen_runs")
        return records[:limit] if limit else records

    def get_screen_run(self, screen_run_id: str) -> Optional[ScreenRun]:
        return self._get_by_id("screen_runs", screen_run_id)

    def save_after_market_scan(self, scan: AfterMarketScan) -> AfterMarketScan:
        self._write("after_market_scans", scan.id, scan.to_dict())
        return scan

    def list_after_market_scans(self, limit: Optional[int] = None) -> list[AfterMarketScan]:
        records = self._read_all("after_market_scans")
        return records[:limit] if limit else records

    def get_after_market_scan(self, scan_id: str) -> Optional[AfterMarketScan]:
        return self._get_by_id("after_market_scans", scan_id)

    def save_next_day_watchlist(self, watchlist: NextDayWatchlist) -> NextDayWatchlist:
        self._write("next_day_watchlists", watchlist.id, watchlist.to_dict())
        return watchlist

    def list_next_day_watchlists(self, limit: Optional[int] = None) -> list[NextDayWatchlist]:
        records = self._read_all("next_day_watchlists")
        return records[:limit] if limit else records

    def get_next_day_watchlist(self, watchlist_id: str) -> Optional[NextDayWatchlist]:
        return self._get_by_id("next_day_watchlists", watchlist_id)

    def save_backtest_run(self, backtest_run: BacktestRun) -> BacktestRun:
        self._write("backtest_runs", backtest_run.id, backtest_run.to_dict())
        return backtest_run

    def list_backtest_runs(self, limit: Optional[int] = None) -> list[BacktestRun]:
        records = self._read_all("backtest_runs")
        return records[:limit] if limit else records

    def get_backtest_run(self, backtest_run_id: str) -> Optional[BacktestRun]:
        return self._get_by_id("backtest_runs", backtest_run_id)

    def save_trade_plan(self, trade_plan: TradePlan) -> TradePlan:
        trade_plan.updated_at = now_iso()
        self._write("trade_plans", trade_plan.id, trade_plan.to_dict())
        return trade_plan

    def list_trade_plans(self, limit: Optional[int] = None) -> list[TradePlan]:
        records = self._read_all("trade_plans")
        return records[:limit] if limit else records

    def get_trade_plan(self, trade_plan_id: str) -> Optional[TradePlan]:
        return self._get_by_id("trade_plans", trade_plan_id)

    def update_trade_plan_status(self, trade_plan_id: str, status: str) -> Optional[TradePlan]:
        plan = self.get_trade_plan(trade_plan_id)
        if not plan:
            return None
        plan.status = status
        plan.updated_at = now_iso()
        return self.save_trade_plan(plan)

    def save_paper_order(self, paper_order: PaperOrder) -> PaperOrder:
        paper_order.updated_at = now_iso()
        self._write("paper_orders", paper_order.id, paper_order.to_dict())
        return paper_order

    def list_paper_orders(self, limit: Optional[int] = None) -> list[PaperOrder]:
        records = self._read_all("paper_orders")
        return records[:limit] if limit else records

    def get_paper_order(self, paper_order_id: str) -> Optional[PaperOrder]:
        return self._get_by_id("paper_orders", paper_order_id)

    def update_paper_order_status(
        self,
        paper_order_id: str,
        status: str,
        filled_price: Optional[float] = None,
    ) -> Optional[PaperOrder]:
        order = self.get_paper_order(paper_order_id)
        if not order:
            return None
        order.status = status
        order.updated_at = now_iso()
        if filled_price is not None:
            order.filled_price = filled_price
            order.filled_at = now_iso()
        self.save_paper_order(order)
        return order

    def save_watchlist(self, watchlist: Watchlist) -> Watchlist:
        watchlist.updated_at = now_iso()
        self._write("watchlists", watchlist.id, watchlist.to_dict())
        return watchlist

    def list_watchlists(self, limit: Optional[int] = None) -> list[Watchlist]:
        records = self._read_all("watchlists")
        return records[:limit] if limit else records

    def get_watchlist(self, watchlist_id: str) -> Optional[Watchlist]:
        return self._get_by_id("watchlists", watchlist_id)

    def add_stock_to_watchlist(self, watchlist_id: str, stock_id: str) -> Optional[Watchlist]:
        watchlist = self.get_watchlist(watchlist_id)
        if not watchlist:
            return None
        normalized = stock_id.strip()
        if normalized and normalized not in watchlist.stocks:
            watchlist.stocks.append(normalized)
            watchlist.updated_at = now_iso()
            self.save_watchlist(watchlist)
        return watchlist

    def save_research_note(self, note: ResearchNote) -> ResearchNote:
        note.updated_at = now_iso()
        self._write("research_notes", note.id, note.to_dict())
        return note

    def list_research_notes(
        self,
        stock_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list[ResearchNote]:
        records = self._read_all("research_notes")
        if stock_id:
            records = [record for record in records if record.stock_id == stock_id]
        return records[:limit] if limit else records

    def list_signal_events(
        self,
        stock_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> list[SignalEvent]:
        records = self._read_all("signal_events")
        if stock_id:
            records = [record for record in records if record.stock_id == stock_id]
        return records[:limit] if limit else records

    def get_dashboard_snapshot(self) -> dict[str, Any]:
        screen_runs = self.list_screen_runs(limit=5)
        backtest_runs = self.list_backtest_runs(limit=5)
        trade_plans = self.list_trade_plans(limit=5)
        paper_orders = self.list_paper_orders(limit=5)
        watchlists = self.list_watchlists(limit=5)
        notes = self.list_research_notes(limit=5)
        signals = self.list_signal_events(limit=10)

        pending_orders = len(
            [order for order in self.list_paper_orders() if order.status in {"planned", "submitted"}]
        )

        return {
            "counts": {
                "screen_runs": len(self.list_screen_runs()),
                "signal_events": len(self.list_signal_events()),
                "backtest_runs": len(self.list_backtest_runs()),
                "trade_plans": len(self.list_trade_plans()),
                "paper_orders": len(self.list_paper_orders()),
                "pending_orders": pending_orders,
                "watchlists": len(self.list_watchlists()),
                "research_notes": len(self.list_research_notes()),
            },
            "recent_screen_runs": screen_runs,
            "recent_signals": signals,
            "recent_backtests": backtest_runs,
            "recent_trade_plans": trade_plans,
            "recent_orders": paper_orders,
            "recent_watchlists": watchlists,
            "recent_notes": notes,
        }
