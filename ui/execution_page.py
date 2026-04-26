import pandas as pd
import streamlit as st

from data.workspace_models import PaperOrder
from data.workspace_store import WorkspaceStore


PLAN_STATUSES = ["draft", "review", "ready", "archived"]
ORDER_STATUSES = ["planned", "submitted", "filled", "cancelled"]


def render_execution_page() -> None:
    store = WorkspaceStore()
    st.header("📝 模擬執行中心")
    st.caption("管理 TradePlan 與 PaperOrder，追蹤模擬執行狀態。")

    trade_plans = store.list_trade_plans(limit=50)
    if not trade_plans:
        st.info("目前沒有 TradePlan。先到驗證中心建立一筆交易計畫。")
        return

    mapping = {
        f"{plan.updated_at} | {plan.stock_id} | {plan.strategy_name} | {plan.status}": plan.id
        for plan in trade_plans
    }
    selected_label = st.selectbox("選擇 TradePlan", list(mapping.keys()), key="execution_trade_plan")
    trade_plan = store.get_trade_plan(mapping[selected_label])
    if not trade_plan:
        st.error("找不到指定的 TradePlan。")
        return

    st.subheader(f"{trade_plan.stock_id} {trade_plan.stock_name}".strip())
    st.write({
        "strategy": trade_plan.strategy_name,
        "status": trade_plan.status,
        "entry_idea": trade_plan.entry_idea,
        "stop_loss": trade_plan.stop_loss,
        "take_profit": trade_plan.take_profit,
        "size_note": trade_plan.size_note,
        "risk_checks": trade_plan.risk_checks,
    })

    status_col1, status_col2 = st.columns(2)
    with status_col1:
        next_status = st.selectbox("更新 TradePlan 狀態", PLAN_STATUSES, index=PLAN_STATUSES.index(trade_plan.status) if trade_plan.status in PLAN_STATUSES else 0)
    with status_col2:
        if st.button("更新計畫狀態", key="update_trade_plan_status"):
            store.update_trade_plan_status(trade_plan.id, next_status)
            st.success("TradePlan 狀態已更新。")
            st.rerun()

    st.markdown("---")
    st.subheader("建立模擬委託")
    order_col1, order_col2, order_col3 = st.columns(3)
    with order_col1:
        quantity = st.number_input("數量", min_value=1, value=1000, step=100, key="paper_order_qty")
    with order_col2:
        intended_price = st.number_input("目標價格", min_value=0.0, value=0.0, step=0.5, key="paper_order_price")
    with order_col3:
        side = st.selectbox("方向", [trade_plan.intended_action, "SELL" if trade_plan.intended_action == "BUY" else "BUY"], key="paper_order_side")

    order_notes = st.text_input("委託備註", value="由模擬執行中心建立", key="paper_order_notes")
    if st.button("建立 PaperOrder", key="create_paper_order"):
        paper_order = PaperOrder(
            trade_plan_id=trade_plan.id,
            stock_id=trade_plan.stock_id,
            stock_name=trade_plan.stock_name,
            side=side,
            quantity=int(quantity),
            intended_price=float(intended_price),
            notes=order_notes,
        )
        store.save_paper_order(paper_order)
        st.success(f"PaperOrder 已建立：{paper_order.id}")

    st.markdown("---")
    st.subheader("最近模擬委託")
    paper_orders = store.list_paper_orders(limit=20)
    if paper_orders:
        st.dataframe(
            pd.DataFrame(
                [
                    {
                        "ID": item.id,
                        "股票": f"{item.stock_id} {item.stock_name}".strip(),
                        "方向": item.side,
                        "數量": item.quantity,
                        "狀態": item.status,
                        "目標價": item.intended_price,
                        "更新": item.updated_at,
                    }
                    for item in paper_orders
                ]
            ),
            width="stretch",
            hide_index=True,
        )

        order_mapping = {f"{item.updated_at} | {item.stock_id} | {item.status}": item.id for item in paper_orders}
        selected_order_label = st.selectbox("更新 PaperOrder 狀態", list(order_mapping.keys()), key="paper_order_status_select")
        order_status = st.selectbox("新的狀態", ORDER_STATUSES, key="paper_order_new_status")
        filled_price = st.number_input("Filled Price（若適用）", min_value=0.0, value=0.0, step=0.5, key="paper_order_filled_price")
        if st.button("更新 PaperOrder", key="update_paper_order"):
            store.update_paper_order_status(
                order_mapping[selected_order_label],
                order_status,
                filled_price if order_status == "filled" and filled_price > 0 else None,
            )
            st.success("PaperOrder 已更新。")
            st.rerun()
