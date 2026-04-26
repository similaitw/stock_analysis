from data.workspace_models import (
    BacktestRun,
    PaperOrder,
    ScreenRun,
    StrategyDefinition,
    TradePlan,
)


def test_screen_run_roundtrip_keeps_strategies_and_results():
    screen_run = ScreenRun.from_scan_results(
        name="Tw50 Momentum Scan",
        market_scope="Tw50",
        stock_pool=["2330", "2317"],
        strategy_names=["MA Crossover", "Momentum Breakout"],
        match_mode="AND",
        results=[{"Stock ID": "2330", "Name": "TSMC", "Price": 950.5, "Signal": "[MA] Golden Cross"}],
        strategy_params={"MA Crossover": {"pfast": 10, "pslow": 30}},
    )

    payload = screen_run.to_dict()
    restored = ScreenRun.from_dict(payload)

    assert restored.name == "Tw50 Momentum Scan"
    assert restored.stock_pool == ["2330", "2317"]
    assert restored.strategies[0].name == "MA Crossover"
    assert restored.results[0]["Stock ID"] == "2330"


def test_backtest_run_engine_result_computes_return():
    run = BacktestRun.from_engine_result(
        stock_id="2330",
        stock_name="TSMC",
        strategy_name="MA Crossover",
        period="2y",
        starting_cash=1_000_000,
        final_value=1_120_000,
        trades=[{"Date": "2026-01-01", "Action": "BUY"}],
    )

    assert round(run.total_return_pct, 2) == 12.0
    assert run.trades[0]["Action"] == "BUY"


def test_paper_order_and_trade_plan_roundtrip():
    trade_plan = TradePlan(
        stock_id="2330",
        stock_name="TSMC",
        strategy_name="MA Crossover",
        thesis="Trend continuation",
        risk_checks=["確認流動性"],
    )
    order = PaperOrder(
        trade_plan_id=trade_plan.id,
        stock_id="2330",
        stock_name="TSMC",
        side="BUY",
        quantity=1000,
        intended_price=950.0,
    )

    restored_plan = TradePlan.from_dict(trade_plan.to_dict())
    restored_order = PaperOrder.from_dict(order.to_dict())

    assert restored_plan.stock_id == "2330"
    assert restored_plan.risk_checks == ["確認流動性"]
    assert restored_order.quantity == 1000
    assert restored_order.intended_price == 950.0
