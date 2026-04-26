from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Optional
from uuid import uuid4


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def make_id(prefix: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{stamp}_{uuid4().hex[:8]}"


def _safe_float(value: Any) -> Optional[float]:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def sanitize_for_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): sanitize_for_json(val) for key, val in value.items()}
    if isinstance(value, list):
        return [sanitize_for_json(item) for item in value]
    if isinstance(value, tuple):
        return [sanitize_for_json(item) for item in value]
    if isinstance(value, datetime):
        return value.isoformat()
    if hasattr(value, "isoformat") and callable(getattr(value, "isoformat")):
        try:
            return value.isoformat()
        except TypeError:
            pass
    if hasattr(value, "item") and callable(getattr(value, "item")):
        try:
            return value.item()
        except Exception:
            pass
    return value


@dataclass
class StrategyDefinition:
    name: str
    category: str = "custom"
    source: str = "existing-project"
    parameters: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StrategyDefinition":
        return cls(
            name=data.get("name", ""),
            category=data.get("category", "custom"),
            source=data.get("source", "existing-project"),
            parameters=data.get("parameters", {}) or {},
        )


@dataclass
class ScreenRun:
    id: str = field(default_factory=lambda: make_id("screen"))
    name: str = ""
    market_scope: str = "Tw50"
    stock_pool: list[str] = field(default_factory=list)
    strategies: list[StrategyDefinition] = field(default_factory=list)
    match_mode: str = "AND"
    executed_at: str = field(default_factory=now_iso)
    result_count: int = 0
    results: list[dict[str, Any]] = field(default_factory=list)
    source_page: str = "strategy_workspace"
    notes: str = ""
    status: str = "completed"

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["strategies"] = [strategy.to_dict() for strategy in self.strategies]
        return sanitize_for_json(data)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ScreenRun":
        return cls(
            id=data.get("id", make_id("screen")),
            name=data.get("name", ""),
            market_scope=data.get("market_scope", "Tw50"),
            stock_pool=list(data.get("stock_pool", []) or []),
            strategies=[
                StrategyDefinition.from_dict(item)
                for item in data.get("strategies", []) or []
            ],
            match_mode=data.get("match_mode", "AND"),
            executed_at=data.get("executed_at", now_iso()),
            result_count=int(data.get("result_count", 0) or 0),
            results=list(data.get("results", []) or []),
            source_page=data.get("source_page", "strategy_workspace"),
            notes=data.get("notes", ""),
            status=data.get("status", "completed"),
        )

    @classmethod
    def from_scan_results(
        cls,
        name: str,
        market_scope: str,
        stock_pool: list[str],
        strategy_names: list[str],
        match_mode: str,
        results: list[dict[str, Any]],
        strategy_params: Optional[dict[str, dict[str, Any]]] = None,
        source_page: str = "strategy_workspace",
        notes: str = "",
    ) -> "ScreenRun":
        definitions = [
            StrategyDefinition(
                name=strategy_name,
                category="strategy-scan",
                parameters=(strategy_params or {}).get(strategy_name, {}),
            )
            for strategy_name in strategy_names
        ]
        safe_results = sanitize_for_json(results)
        return cls(
            name=name,
            market_scope=market_scope,
            stock_pool=list(stock_pool),
            strategies=definitions,
            match_mode=match_mode,
            result_count=len(safe_results),
            results=safe_results,
            source_page=source_page,
            notes=notes,
        )


@dataclass
class SignalEvent:
    id: str = field(default_factory=lambda: make_id("signal"))
    screen_run_id: str = ""
    stock_id: str = ""
    stock_name: str = ""
    market_scope: str = ""
    strategy_names: list[str] = field(default_factory=list)
    reason: str = ""
    price: Optional[float] = None
    detected_at: str = field(default_factory=now_iso)
    raw_record: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SignalEvent":
        return cls(
            id=data.get("id", make_id("signal")),
            screen_run_id=data.get("screen_run_id", ""),
            stock_id=data.get("stock_id", ""),
            stock_name=data.get("stock_name", ""),
            market_scope=data.get("market_scope", ""),
            strategy_names=list(data.get("strategy_names", []) or []),
            reason=data.get("reason", ""),
            price=_safe_float(data.get("price")),
            detected_at=data.get("detected_at", now_iso()),
            raw_record=dict(data.get("raw_record", {}) or {}),
        )

    @classmethod
    def from_screen_run(cls, screen_run: ScreenRun) -> list["SignalEvent"]:
        strategy_names = [strategy.name for strategy in screen_run.strategies]
        events: list[SignalEvent] = []
        for record in screen_run.results:
            stock_id = str(record.get("Stock ID") or record.get("stock_id") or "")
            stock_name = str(record.get("Name") or record.get("stock_name") or "")
            reason = str(record.get("Signal") or record.get("reason") or "")
            price = _safe_float(record.get("Price") or record.get("price"))
            events.append(
                cls(
                    screen_run_id=screen_run.id,
                    stock_id=stock_id,
                    stock_name=stock_name,
                    market_scope=screen_run.market_scope,
                    strategy_names=strategy_names,
                    reason=reason,
                    price=price,
                    detected_at=screen_run.executed_at,
                    raw_record=sanitize_for_json(record),
                )
            )
        return events


@dataclass
class BacktestRun:
    id: str = field(default_factory=lambda: make_id("backtest"))
    screen_run_id: Optional[str] = None
    stock_id: str = ""
    stock_name: str = ""
    strategy_name: str = "MA Crossover"
    strategy_params: dict[str, Any] = field(default_factory=dict)
    period: str = "2y"
    executed_at: str = field(default_factory=now_iso)
    starting_cash: float = 1_000_000.0
    commission_rate: float = 0.001425
    final_value: float = 0.0
    total_return_pct: float = 0.0
    benchmark_return_pct: Optional[float] = None
    trades: list[dict[str, Any]] = field(default_factory=list)
    notes: str = ""
    fallback_note: str = ""

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "BacktestRun":
        return cls(
            id=data.get("id", make_id("backtest")),
            screen_run_id=data.get("screen_run_id"),
            stock_id=data.get("stock_id", ""),
            stock_name=data.get("stock_name", ""),
            strategy_name=data.get("strategy_name", "MA Crossover"),
            strategy_params=data.get("strategy_params", {}) or {},
            period=data.get("period", "2y"),
            executed_at=data.get("executed_at", now_iso()),
            starting_cash=float(data.get("starting_cash", 1_000_000.0) or 1_000_000.0),
            commission_rate=float(data.get("commission_rate", 0.001425) or 0.001425),
            final_value=float(data.get("final_value", 0.0) or 0.0),
            total_return_pct=float(data.get("total_return_pct", 0.0) or 0.0),
            benchmark_return_pct=_safe_float(data.get("benchmark_return_pct")),
            trades=list(data.get("trades", []) or []),
            notes=data.get("notes", ""),
            fallback_note=data.get("fallback_note", ""),
        )

    @classmethod
    def from_engine_result(
        cls,
        stock_id: str,
        stock_name: str,
        strategy_name: str,
        period: str,
        starting_cash: float,
        final_value: float,
        trades: list[dict[str, Any]],
        strategy_params: Optional[dict[str, Any]] = None,
        screen_run_id: Optional[str] = None,
        benchmark_return_pct: Optional[float] = None,
        notes: str = "",
        fallback_note: str = "",
        commission_rate: float = 0.001425,
    ) -> "BacktestRun":
        total_return_pct = 0.0
        if starting_cash:
            total_return_pct = ((final_value - starting_cash) / starting_cash) * 100
        return cls(
            screen_run_id=screen_run_id,
            stock_id=stock_id,
            stock_name=stock_name,
            strategy_name=strategy_name,
            strategy_params=(strategy_params or {}),
            period=period,
            starting_cash=starting_cash,
            commission_rate=commission_rate,
            final_value=final_value,
            total_return_pct=total_return_pct,
            benchmark_return_pct=benchmark_return_pct,
            trades=sanitize_for_json(trades),
            notes=notes,
            fallback_note=fallback_note,
        )


@dataclass
class TradePlan:
    id: str = field(default_factory=lambda: make_id("trade_plan"))
    screen_run_id: Optional[str] = None
    backtest_run_id: Optional[str] = None
    stock_id: str = ""
    stock_name: str = ""
    strategy_name: str = ""
    intended_action: str = "BUY"
    thesis: str = ""
    entry_idea: str = ""
    stop_loss: str = ""
    take_profit: str = ""
    size_note: str = ""
    risk_checks: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    status: str = "draft"
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TradePlan":
        return cls(
            id=data.get("id", make_id("trade_plan")),
            screen_run_id=data.get("screen_run_id"),
            backtest_run_id=data.get("backtest_run_id"),
            stock_id=data.get("stock_id", ""),
            stock_name=data.get("stock_name", ""),
            strategy_name=data.get("strategy_name", ""),
            intended_action=data.get("intended_action", "BUY"),
            thesis=data.get("thesis", ""),
            entry_idea=data.get("entry_idea", ""),
            stop_loss=data.get("stop_loss", ""),
            take_profit=data.get("take_profit", ""),
            size_note=data.get("size_note", ""),
            risk_checks=list(data.get("risk_checks", []) or []),
            tags=list(data.get("tags", []) or []),
            status=data.get("status", "draft"),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at", now_iso()),
        )


@dataclass
class PaperOrder:
    id: str = field(default_factory=lambda: make_id("paper_order"))
    trade_plan_id: str = ""
    stock_id: str = ""
    stock_name: str = ""
    side: str = "BUY"
    quantity: int = 0
    intended_price: float = 0.0
    status: str = "planned"
    notes: str = ""
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)
    filled_price: Optional[float] = None
    filled_at: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PaperOrder":
        return cls(
            id=data.get("id", make_id("paper_order")),
            trade_plan_id=data.get("trade_plan_id", ""),
            stock_id=data.get("stock_id", ""),
            stock_name=data.get("stock_name", ""),
            side=data.get("side", "BUY"),
            quantity=int(data.get("quantity", 0) or 0),
            intended_price=float(data.get("intended_price", 0.0) or 0.0),
            status=data.get("status", "planned"),
            notes=data.get("notes", ""),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at", now_iso()),
            filled_price=_safe_float(data.get("filled_price")),
            filled_at=data.get("filled_at"),
        )


@dataclass
class Watchlist:
    id: str = field(default_factory=lambda: make_id("watchlist"))
    name: str = ""
    owner: str = "team"
    stocks: list[str] = field(default_factory=list)
    description: str = ""
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Watchlist":
        return cls(
            id=data.get("id", make_id("watchlist")),
            name=data.get("name", ""),
            owner=data.get("owner", "team"),
            stocks=list(data.get("stocks", []) or []),
            description=data.get("description", ""),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at", now_iso()),
        )


@dataclass
class ResearchNote:
    id: str = field(default_factory=lambda: make_id("note"))
    title: str = ""
    stock_id: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    content: str = ""
    author: str = "team"
    created_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)
    related_watchlist_id: Optional[str] = None
    related_screen_run_id: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return sanitize_for_json(asdict(self))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ResearchNote":
        return cls(
            id=data.get("id", make_id("note")),
            title=data.get("title", ""),
            stock_id=data.get("stock_id"),
            tags=list(data.get("tags", []) or []),
            content=data.get("content", ""),
            author=data.get("author", "team"),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at", now_iso()),
            related_watchlist_id=data.get("related_watchlist_id"),
            related_screen_run_id=data.get("related_screen_run_id"),
        )
