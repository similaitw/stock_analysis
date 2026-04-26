import streamlit as st
import pandas as pd
from ui.comparison import render_comparison_chart, render_volume_distribution, render_return_distribution
from data.fetcher import DataFetcher
from portfolios import PortfolioManager

def render_comparison_page():
    """渲染多股票比較頁面"""
    st.header("⚖️ 多股票比較 (Stock Comparison)")
    
    # === 1. 股票選擇 (Selection) ===
    with st.sidebar:
        st.subheader("1. 選擇股票來源")
        source = st.radio("Source", ["Manual Input", "Portfolio", "Strategy Scan"], index=1)
        
        candidates = []
        
        if source == "Manual Input":
            user_input = st.text_area("Stock Codes (comma separated)", "2330, 2317, 2454, 2881")
            candidates = [s.strip() for s in user_input.split(',') if s.strip()]
            
        elif source == "Portfolio":
            pm = PortfolioManager()
            portfolios = pm.list_portfolios()
            if portfolios:
                pf_map = {p['name']: p for p in portfolios}
                selected_pf = st.selectbox("Select Portfolio", list(pf_map.keys()))
                if selected_pf:
                    # Load portfolio to get stocks
                    pf_data = pm.load_portfolio(pf_map[selected_pf]['id'])
                    # stocks default to latest result or definition?
                    # usually check 'results' -> 'stocks' or we store 'stocks' in portfolio definition
                    # The Scanner stores list in result. Let's assume we can get it.
                    # Current PortfolioManager implementation might need checking.
                    # Assuming basic implementation returns a dict with 'results'
                    if pf_data and 'results' in pf_data and pf_data['results']:
                         candidates = pf_data['results'][-1].get('stocks', [])
            else:
                st.info("No portfolios found.")
                
        elif source == "Strategy Scan":
            if 'strategy_scan_results' in st.session_state:
                df = st.session_state.strategy_scan_results
                if not df.empty:
                    candidates = df['Stock ID'].tolist()
                else:
                    st.info("Last scan result is empty.")
            elif 'sb_scan_results' in st.session_state: # From Selection page
                df = st.session_state.sb_scan_results
                if not df.empty:
                     candidates = df['Stock ID'].tolist()
            else:
                st.info("No scan results found. Go to 'Strategy Lab' first.")
        
        # Candidate Checklist
        st.subheader("2. 比較清單")
        selected_stocks = []
        if candidates:
            # Check all by default if count < 10, else top 5
            default_checks = candidates[:5]
            
            # Select All / Deselect All
            col_u1, col_u2 = st.columns(2)
            if col_u1.button("Select Top 5"):
                st.session_state.comp_selections = candidates[:5]
            if col_u2.button("Clear"):
                st.session_state.comp_selections = []
                
            # Use multiselect for better UI than many checkboxes if list is long
            selected_stocks = st.multiselect(
                "Select stocks to compare:",
                candidates,
                default=candidates[:5] if len(candidates) <= 5 else candidates[:5],
                key="comp_multiselect"
            )
        else:
            st.warning("No stocks selected.")

    # === 2. 比較圖表 (Visualizations) ===
    if selected_stocks:
        st.info(f"Comparing {len(selected_stocks)} stocks: {', '.join(selected_stocks)}")
        
        tab_price, tab_fund, tab_chip = st.tabs(["💰 價格強弱", "📊 基本面PK", "🏦 籌碼PK"])
        
        with tab_price:
            period = st.radio("Period", ["3mo", "6mo", "1y", "2y", "5y"], index=2, horizontal=True)
            fig = render_comparison_chart(selected_stocks, period)
            st.plotly_chart(fig, width='stretch')
            
            # Additional Stats: Correlation Matrix?
            
        with tab_fund:
            st.subheader("基本面數據比較 (Fundamental Comparison)")
            # Fetch fundamentals for all
            fund_list = []
            for ticker in selected_stocks:
                info = DataFetcher.fetch_fundamentals(ticker)
                info['Stock'] = ticker
                fund_list.append(info)
            
            if fund_list:
                df_fund = pd.DataFrame(fund_list)
                # Reorder columns
                cols = ['Stock', 'Revenue YoY', 'Margin', 'EPS', 'Yield', 'Inst Buy']
                available_cols = [c for c in cols if c in df_fund.columns]
                st.dataframe(df_fund[available_cols], width='stretch')
                
                # Bar Charts for comparison
                import plotly.express as px
                c1, c2 = st.columns(2)
                with c1:
                    fig_yield = px.bar(df_fund, x='Stock', y='Yield', title="殖利率 (Yield)", color='Stock')
                    st.plotly_chart(fig_yield, width='stretch')
                with c2:
                    fig_rev = px.bar(df_fund, x='Stock', y='Revenue YoY', title="營收成長 (Rev YoY)", color='Stock')
                    st.plotly_chart(fig_rev, width='stretch')

        with tab_chip:
            st.subheader("籌碼面數據比較 (Chip Comparison)")
            # 3-day Institutional Buy
            chip_list = []
            for ticker in selected_stocks:
                # Need a quick way to get chip summary
                # fetch_institutional_investors returns history.
                # Let's get sum of last 5 days
                df_inst = DataFetcher.fetch_institutional_investors(ticker, days=5)
                net_buy = 0
                if not df_inst.empty:
                    net_buy = df_inst['net'].sum()
                
                chip_list.append({
                    'Stock': ticker,
                    'Inst Net Buy (5d)': net_buy
                })
            
            df_chip = pd.DataFrame(chip_list)
            st.dataframe(df_chip, width='stretch')
            
            fig_chip = px.bar(df_chip, x='Stock', y='Inst Net Buy (5d)', title="近5日法人買賣超 (Inst Net Buy)", color='Inst Net Buy (5d)')
            st.plotly_chart(fig_chip, width='stretch')

    else:
        st.write("Please select stocks from the sidebar to start comparison.")

