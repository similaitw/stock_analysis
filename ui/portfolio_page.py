import streamlit as st
from portfolios import PortfolioManager
import pandas as pd
from ui.language import Language

def render_portfolio_page():
    st.header("📂 組合管理 (Portfolio Manager)")
    
    pm = PortfolioManager()
    portfolios = pm.list_portfolios()
    
    # 統計資訊
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("總組合數", len(portfolios))
    with col2:
        total_stocks = sum(
            len(p.get('results', [{}])[-1].get('stocks', [])) 
            for p in portfolios 
            if p.get('results')
        )
        st.metric("追蹤股票數", total_stocks)
    with col3:
        if portfolios:
            latest_update = max(p.get('updated_at', '') for p in portfolios)
            st.metric("最後更新", latest_update[:10])
    
    st.markdown("---")
    
    # 組合清單
    if portfolios:
        st.subheader("📋 我的組合")
        
        # New: Create Portfolio Button
        with st.expander("➕ 建立新組合 (Create New Portfolio)"):
            c1, c2, c3 = st.columns([2, 2, 1])
            new_pf_name = c1.text_input("組合名稱", key="new_pf_name")
            new_pf_desc = c2.text_input("描述", key="new_pf_desc")
            if c3.button("建立 (Create)", key="create_pf_btn"):
                if new_pf_name:
                    pm.create_portfolio(new_pf_name, new_pf_desc, "Manual", "Manual", [])
                    st.success("建立成功！")
                    st.rerun()
                else:
                    st.error("請輸入名稱")

        for portfolio in portfolios:
            with st.expander(f"📁 {portfolio['name']} ({len(portfolio.get('results', [{}])[-1].get('stocks', []))} 檔)", expanded=False):
                col_info1, col_info2 = st.columns([3, 1])
                
                # Get current stocks
                current_stocks = []
                results = portfolio.get('results', [])
                if results:
                    current_stocks = results[-1].get('stocks', [])
                
                with col_info1:
                    st.write(f"**描述**: {portfolio.get('description', '無')}")
                    st.write(f"**策略**: {portfolio['strategy']}")
                    st.write(f"**市場**: {portfolio['market']}")
                    st.write(f"**更新時間**: {portfolio['updated_at'][:19]}")
                    
                    # 股票管理區
                    st.markdown("#### 📝 股票名單管理")
                    
                    # Add Stock
                    col_add1, col_add2 = st.columns([3, 1])
                    stock_to_add = col_add1.text_input(f"輸入股票代碼新增至 {portfolio['name']}", key=f"add_input_{portfolio['id']}")
                    if col_add2.button("➕ 新增", key=f"add_btn_{portfolio['id']}"):
                        if stock_to_add:
                            if pm.add_stock(portfolio['id'], stock_to_add):
                                st.success(f"已新增 {stock_to_add}")
                                st.rerun()
                            else:
                                st.error("新增失敗或已存在")
                    
                    # List Stocks with Remove button
                    if current_stocks:
                        st.write("**目前清單**:")
                        stock_cols = st.columns(5)
                        for i, stock in enumerate(current_stocks):
                            col_idx = i % 5
                            with stock_cols[col_idx]:
                                if st.button(f"🗑️ {stock}", key=f"rm_{portfolio['id']}_{stock}", help="點擊移除"):
                                    if pm.remove_stock(portfolio['id'], stock):
                                        st.success(f"已移除 {stock}")
                                        st.rerun()
                    else:
                        st.info("此組合目前沒有股票")
                
                with col_info2:
                    # 操作按鈕
                    st.markdown("#### ⚙️ 組合操作")
                    if st.button("🔄 重新執行掃描", key=f"rerun_{portfolio['id']}"):
                        st.session_state.rerun_portfolio_id = portfolio['id'] # Store ID for other pages
                        st.session_state.rerun_portfolio_strategy = portfolio['strategy']
                        st.warning("請前往「選股與回測」頁面執行掃描")
                    
                    if st.button("✏️ 編輯資訊", key=f"edit_{portfolio['id']}"):
                        st.session_state.edit_portfolio = portfolio['id']
                    
                    if st.button("🗑️ 刪除組合", key=f"delete_{portfolio['id']}", type="primary"):
                        if pm.delete_portfolio(portfolio['id']):
                            st.success(f"✅ 已刪除組合：{portfolio['name']}")
                            st.rerun()
                        else:
                            st.error("❌ 刪除失敗")
                
                # 編輯組合 (原有功能保持)
                if st.session_state.get('edit_portfolio') == portfolio['id']:
                    st.markdown("---")
                    st.subheader("✏️ 編輯組合資訊")
                    new_name = st.text_input("組合名稱", value=portfolio['name'], key=f"edit_name_{portfolio['id']}")
                    new_desc = st.text_input("組合描述", value=portfolio.get('description', ''), key=f"edit_desc_{portfolio['id']}")
                    
                    if st.button("💾 儲存變更", key=f"save_edit_{portfolio['id']}"):
                        if pm.update_portfolio(portfolio['id'], name=new_name, description=new_desc):
                            st.success("✅ 更新成功")
                            del st.session_state.edit_portfolio
                            st.rerun()
    else:
        st.info("📭 尚無儲存的組合")
        # Create first portfolio
        with st.form("create_first_pf"):
            st.write("建立第一個組合")
            n = st.text_input("名稱")
            d = st.text_input("描述")
            if st.form_submit_button("建立"):
                if n:
                    pm.create_portfolio(n, d, "Manual", "Manual", [])
                    st.rerun()

render_portfolio_page()
