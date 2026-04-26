from __future__ import annotations

import copy
from typing import Any, Optional

import backtrader as bt
import pandas as pd

from data.fetcher import DataFetcher
from scanner.engine import ScannerEngine
from strategies.bollinger import BollingerStrategy
from strategies.ma_crossover import MACrossoverStrategy
from strategies.registry import StrategyRegistry
from strategies.rsi import RSIStrategy


BACKTRADER_STRATEGY_SPECS: dict[str, dict[str, Any]] = {
    "MA Crossover": {
        "mode": "backtrader",
        "strategy_class": MACrossoverStrategy,
        "description": "使用 Backtrader 執行移動平均交叉回測。",
        "params": {
            "pfast": {"label": "快線週期", "type": "int", "default": 10, "min": 3, "max": 60, "step": 1},
            "pslow": {"label": "慢線週期", "type": "int", "default": 30, "min": 10, "max": 240, "step": 1},
            "stop_loss": {
                "label": "停損比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 0.5,
                "step": 0.01,
            },
            "take_profit": {
                "label": "停利比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 1.0,
                "step": 0.01,
            },
        },
    },
    "RSI Oversold": {
        "mode": "backtrader",
        "strategy_class": RSIStrategy,
        "description": "使用 Backtrader 執行 RSI 超賣 / 超買回測。",
        "params": {
            "period": {"label": "RSI 週期", "type": "int", "default": 14, "min": 5, "max": 60, "step": 1},
            "lower": {"label": "超賣門檻", "type": "int", "default": 30, "min": 5, "max": 50, "step": 1},
            "upper": {"label": "超買門檻", "type": "int", "default": 70, "min": 50, "max": 95, "step": 1},
            "stop_loss": {
                "label": "停損比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 0.5,
                "step": 0.01,
            },
            "take_profit": {
                "label": "停利比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 1.0,
                "step": 0.01,
            },
        },
    },
    "Bollinger Buy": {
        "mode": "backtrader",
        "strategy_class": BollingerStrategy,
        "description": "使用 Backtrader 執行布林通道回測。",
        "params": {
            "period": {"label": "均線週期", "type": "int", "default": 20, "min": 10, "max": 60, "step": 1},
            "devfactor": {
                "label": "標準差倍數",
                "type": "float",
                "default": 2.0,
                "min": 1.0,
                "max": 4.0,
                "step": 0.1,
            },
            "stop_loss": {
                "label": "停損比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 0.5,
                "step": 0.01,
            },
            "take_profit": {
                "label": "停利比例 (0=關閉)",
                "type": "float",
                "default": 0.0,
                "min": 0.0,
                "max": 1.0,
                "step": 0.01,
            },
        },
    },
}

CORE_SIGNAL_STRATEGIES: dict[str, str] = {
    "XScript - Price/Vol High": "用策略訊號模擬進出場，適合驗證突破型訊號。",
    "XScript - Momentum Breakout": "用策略訊號模擬進出場，適合驗證動能突破型訊號。",
    "XScript - 3 Red Soldiers": "用策略訊號模擬進出場，適合驗證 K 棒型態訊號。",
    "XScript - 價量齊揚": "用策略訊號模擬進出場，適合驗證價量共振訊號。",
    "XScript - MA黃金交叉": "用策略訊號模擬進出場，適合驗證均線交叉訊號。",
    "XScript - MACD黃金交叉": "用策略訊號模擬進出場，適合驗證 MACD 訊號。",
    "XScript - KD黃金交叉": "用策略訊號模擬進出場，適合驗證 KD 訊號。",
    "XScript - 無量變有量": "用策略訊號模擬進出場，適合驗證量能放大訊號。",
    "XScript - 帶量突破均線": "用策略訊號模擬進出場，適合驗證帶量突破訊號。",
    "XScript - W底型態": "用策略訊號模擬進出場，適合驗證型態完成訊號。",
    "XScript - 頭肩底": "用策略訊號模擬進出場，適合驗證型態完成訊號。",
}

UNSUPPORTED_SIGNAL_STRATEGIES = {"Advanced Funnel", "Best Combo"}

SIGNAL_SIMULATION_PARAMS: dict[str, dict[str, Any]] = {
    "holding_days": {
        "label": "持有天數",
        "type": "int",
        "default": 10,
        "min": 1,
        "max": 120,
        "step": 1,
        "help": "若沒有觸發停損或停利，持有到指定天數後出場。",
    },
    "stop_loss_pct": {
        "label": "停損百分比",
        "type": "float",
        "default": 8.0,
        "min": 0.0,
        "max": 50.0,
        "step": 0.5,
        "help": "0 代表停損關閉。",
    },
    "take_profit_pct": {
        "label": "停利百分比",
        "type": "float",
        "default": 15.0,
        "min": 0.0,
        "max": 200.0,
        "step": 0.5,
        "help": "0 代表停利關閉。",
    },
}

class BacktestEngine:
    def __init__(self, strategy_class=MACrossoverStrategy, **strategy_params):
        self.cerebro = bt.Cerebro()
        self.cerebro.addstrategy(strategy_class, **strategy_params)
        self.cerebro.addanalyzer(bt.analyzers.Transactions, _name='txn')
        
        # Default settings (can be overridden by UI via wrapper or direct access)
        self.cerebro.broker.setcash(1000000.0)
        self.cerebro.broker.setcommission(commission=0.001425) # Approx generic commission

    @staticmethod
    def _prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            raise ValueError("Input dataframe is empty")

        prepared = df.copy()
        if not isinstance(prepared.index, pd.DatetimeIndex):
            prepared.index = pd.to_datetime(prepared.index)
        return prepared

    def load_dataframe(self, df: pd.DataFrame):
        prepared = self._prepare_dataframe(df)
        data = bt.feeds.PandasData(dataname=prepared)
        self.cerebro.adddata(data)

    def load_data(self, stock_id: str, period="2y", interval="1d"):
        # Fetch data
        df = DataFetcher.fetch_history(stock_id, period=period, interval=interval)
        if df.empty:
            raise ValueError(f"No data for {stock_id}")

        self.load_dataframe(df)

    def run(self):
        print('Starting Portfolio Value: %.2f' % self.cerebro.broker.getvalue())
        strats = self.cerebro.run()
        final_value = self.cerebro.broker.getvalue()
        print('Final Portfolio Value: %.2f' % final_value)
        
        # Extract Trade Log
        txns = strats[0].analyzers.txn.get_analysis()
        trades_list = []
        for date, txn_list in txns.items():
            for txn in txn_list:
                # txn: [amount, price, sid, symbol, value] in Backtrader newer versions
                # or [amount, price, sid, symbol, value, comm]
                # Usually amount (+buy, -sell), price, -
                
                # Check structure
                # amount, price, sid, symbol, value
                amount = txn[0]
                price = txn[1]
                value = txn[4] if len(txn) > 4 else 0
                
                action = 'BUY' if amount > 0 else 'SELL'
                trades_list.append({
                    'Date': date,
                    'Action': action,
                    'Price': price,
                    'Amount': abs(amount),
                    'Value': value,
                })
        
        if trades_list:
            df_trades = pd.DataFrame(trades_list)
            df_trades['Date'] = pd.to_datetime(df_trades['Date'])
            df_trades = df_trades.sort_values('Date')
        else:
            df_trades = pd.DataFrame(columns=['Date', 'Action', 'Price', 'Amount', 'Value'])
            
        return final_value, df_trades


def _registry_strategy_names() -> set[str]:
    try:
        categories = StrategyRegistry.get_all_strategies()
    except Exception:
        return set()

    names: set[str] = set()
    for strategies in categories.values():
        names.update(strategies)
    return names


def _build_signal_strategy_spec(strategy_name: str) -> dict[str, Any]:
    strategy_params = StrategyRegistry.get_strategy_params(strategy_name)
    param_specs: dict[str, dict[str, Any]] = {}

    for param_name, param_info in strategy_params.items():
        param_specs[param_name] = {
            "label": param_name,
            "type": param_info.get("type", "str"),
            "default": param_info.get("default", 0),
        }

    param_specs.update(copy.deepcopy(SIGNAL_SIMULATION_PARAMS))

    description = CORE_SIGNAL_STRATEGIES.get(
        strategy_name,
        "使用策略訊號模擬進出場，適合先驗證訊號在歷史資料上的可用性。",
    )
    return {
        "mode": "signal",
        "description": description,
        "fallback_note": "此策略目前走訊號模擬回測：訊號出現時進場，搭配持有天數與停損停利規則出場。",
        "params": param_specs,
    }


def get_backtest_strategy_catalog(preferred_names: Optional[list[str]] = None) -> dict[str, dict[str, Any]]:
    catalog = copy.deepcopy(BACKTRADER_STRATEGY_SPECS)

    for strategy_name in CORE_SIGNAL_STRATEGIES:
        catalog[strategy_name] = _build_signal_strategy_spec(strategy_name)

    preferred = preferred_names or []
    registry_names = _registry_strategy_names()
    for strategy_name in preferred:
        if strategy_name in catalog or strategy_name in UNSUPPORTED_SIGNAL_STRATEGIES:
            continue
        if strategy_name in registry_names:
            catalog[strategy_name] = _build_signal_strategy_spec(strategy_name)

    return catalog


def _cast_param_value(value: Any, param_type: str) -> Any:
    if param_type == "int":
        return int(value)
    if param_type == "float":
        return float(value)
    if param_type == "bool":
        if isinstance(value, str):
            return value.lower() in {"1", "true", "yes", "on"}
        return bool(value)
    return str(value)


def _normalize_params(raw_params: Optional[dict[str, Any]], param_specs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    raw_params = raw_params or {}

    for param_name, param_spec in param_specs.items():
        default_value = param_spec.get("default")
        value = raw_params.get(param_name, default_value)
        normalized[param_name] = _cast_param_value(value, param_spec.get("type", "str"))

    return normalized


def _run_signal_strategy_backtest(
    stock_id: str,
    strategy_name: str,
    price_df: pd.DataFrame,
    strategy_params: Optional[dict[str, Any]] = None,
    starting_cash: float = 1_000_000.0,
    commission_rate: float = 0.001425,
) -> tuple[float, pd.DataFrame]:
    params = dict(strategy_params or {})
    holding_days = max(int(params.pop("holding_days", 10)), 1)
    stop_loss_pct = max(float(params.pop("stop_loss_pct", 8.0)), 0.0) / 100.0
    take_profit_pct = max(float(params.pop("take_profit_pct", 15.0)), 0.0) / 100.0

    prepared = BacktestEngine._prepare_dataframe(price_df)

    cash = float(starting_cash)
    quantity = 0
    entry_price = 0.0
    entry_index: Optional[int] = None
    trades: list[dict[str, Any]] = []

    for idx in range(len(prepared)):
        current_slice = prepared.iloc[: idx + 1]
        current_date = current_slice.index[-1]
        current_price = float(current_slice["Close"].iloc[-1])

        if quantity > 0:
            exit_reason = ""
            if stop_loss_pct > 0 and current_price <= entry_price * (1 - stop_loss_pct):
                exit_reason = f"Stop loss {stop_loss_pct * 100:.1f}%"
            elif take_profit_pct > 0 and current_price >= entry_price * (1 + take_profit_pct):
                exit_reason = f"Take profit {take_profit_pct * 100:.1f}%"
            elif entry_index is not None and (idx - entry_index) >= holding_days:
                exit_reason = f"Timed exit after {holding_days} bars"

            if exit_reason:
                proceeds = quantity * current_price * (1 - commission_rate)
                cash += proceeds
                trades.append(
                    {
                        "Date": current_date,
                        "Action": "SELL",
                        "Price": current_price,
                        "Amount": quantity,
                        "Value": proceeds,
                        "Reason": exit_reason,
                    }
                )
                quantity = 0
                entry_price = 0.0
                entry_index = None
                continue

        if quantity == 0:
            is_signal, reason = ScannerEngine._check_strategy(strategy_name, current_slice, stock_id, params=params)
            if not is_signal:
                continue

            buy_quantity = int(cash / (current_price * (1 + commission_rate)))
            if buy_quantity <= 0:
                continue

            cost = buy_quantity * current_price * (1 + commission_rate)
            cash -= cost
            quantity = buy_quantity
            entry_price = current_price
            entry_index = idx
            trades.append(
                {
                    "Date": current_date,
                    "Action": "BUY",
                    "Price": current_price,
                    "Amount": buy_quantity,
                    "Value": cost,
                    "Reason": reason or strategy_name,
                }
            )

    final_value = cash
    if quantity > 0:
        final_value += quantity * float(prepared["Close"].iloc[-1])

    if trades:
        trade_frame = pd.DataFrame(trades)
        trade_frame["Date"] = pd.to_datetime(trade_frame["Date"])
    else:
        trade_frame = pd.DataFrame(columns=["Date", "Action", "Price", "Amount", "Value", "Reason"])

    return final_value, trade_frame


def run_named_backtest(
    stock_id: str,
    strategy_name: str,
    period: str = "2y",
    strategy_params: Optional[dict[str, Any]] = None,
    starting_cash: float = 1_000_000.0,
    commission_rate: float = 0.001425,
    price_df: Optional[pd.DataFrame] = None,
) -> dict[str, Any]:
    catalog = get_backtest_strategy_catalog(preferred_names=[strategy_name])
    if strategy_name not in catalog:
        raise ValueError(f"Strategy '{strategy_name}' is not supported by the validation backtest flow")

    spec = catalog[strategy_name]
    normalized_params = _normalize_params(strategy_params, spec.get("params", {}))

    history = price_df.copy() if price_df is not None else DataFetcher.fetch_history(stock_id, period=period)
    if history.empty:
        raise ValueError(f"No data for {stock_id}")

    if spec["mode"] == "backtrader":
        strategy_class = spec["strategy_class"]
        engine = BacktestEngine(strategy_class=strategy_class, **normalized_params)
        engine.cerebro.broker.setcash(starting_cash)
        engine.cerebro.broker.setcommission(commission=commission_rate)
        engine.load_dataframe(history)
        final_value, trades = engine.run()
    else:
        final_value, trades = _run_signal_strategy_backtest(
            stock_id=stock_id,
            strategy_name=strategy_name,
            price_df=history,
            strategy_params=normalized_params,
            starting_cash=starting_cash,
            commission_rate=commission_rate,
        )

    return {
        "mode": spec["mode"],
        "description": spec.get("description", ""),
        "fallback_note": spec.get("fallback_note", ""),
        "strategy_params": normalized_params,
        "price_df": BacktestEngine._prepare_dataframe(history),
        "final_value": final_value,
        "trades": trades,
    }

if __name__ == "__main__":
    engine = BacktestEngine(pfast=5, pslow=20)
    try:
        engine.load_data("2330")
        engine.run()
        # engine.cerebro.plot() # Requires matplotlib interactive backend which might not work well in headless
    except Exception as e:
        print(f"Error: {e}")
