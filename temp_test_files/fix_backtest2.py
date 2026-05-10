import re

# 讀取檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到策略回測的開始部分
old_section = '''elif app_mode == mode_options[1]:  # Strategy Backtest
    # 1. Strategy Backtest Interface
    from data.storage import Storage
    if not os.path.exists(Storage.STOCK_LIST_PATH):
        st.sidebar.warning("股票清單未建立，請先點擊「更新股票清單」")
        ticker = st.sidebar.text_input("股票代碼 (Stock ID)", "2330")
    else:
        df_stocks = Storage.load_stock_list()
        df_stocks['label'] = df_stocks['code'] + " " + df_stocks['name'] + " (" + df_stocks['market'] + ")"
        
        default_idx = 0
        match = df_stocks[df_stocks['code'] == '2330']
        if not match.empty:
            default_idx = match.index[0]
        
        selected_option = st.sidebar.selectbox(
            "搜尋股票 (Search Stock)", 
            df_stocks['label'], 
            index=int(default_idx)
        )
        ticker = selected_option.split(" ")[0]

    period = st.sidebar.selectbox("回測期間 (Backtest Period)", ["3mo", "6mo", "1y", "2y", "5y", "10y"], index=2)

    st.sidebar.subheader("策略參數 (Strategy Params)")
    strategy_type = st.sidebar.selectbox("策略 (Strategy)", ["MA Crossover", "RSI", "Bollinger Bands"])
    
    # Common Params
    initial_cash = st.sidebar.number_input("初始資金 (Initial Cash)", 10000, 10000000, 1000000)
    commission_rate = st.sidebar.number_input("手續費 (Commission)", 0.0, 0.01, 0.001425, format="%.6f")
    stop_loss_pct = st.sidebar.number_input("停損 % (Stop Loss)", 0.0, 50.0, 0.0, step=0.5) / 100.0
    take_profit_pct = st.sidebar.number_input("停利 % (Take Profit)", 0.0, 100.0, 0.0, step=0.5) / 100.0
    
    p1 = 10
    p2 = 30
    p_lower = 30
    p_upper = 70
    
    if strategy_type == "MA Crossover":
        p1 = st.sidebar.number_input("快線 (Fast MA)", 1, 100, 10)
        p2 = st.sidebar.number_input("慢線 (Slow MA)", 5, 300, 30)
    elif strategy_type == "RSI":
        p1 = st.sidebar.number_input("週期 (Period)", 5, 50, 14)
        p_upper = st.sidebar.number_input("超買 (Upper)", 50, 95, 70)
        p_lower = st.sidebar.number_input("超賣 (Lower)", 5, 50, 30)
    elif strategy_type == "Bollinger Bands":
        p1 = st.sidebar.number_input("週期 (Period)", 5, 100, 20)
        p2 = st.sidebar.number_input("標準差 (Std Dev)", 1.0, 5.0, 2.0)

    run_backtest_btn = st.sidebar.button("🚀 執行回測", type="primary")'''

new_section = '''elif app_mode == mode_options[1]:  # Strategy Backtest
    st.header("策略回測 (Strategy Backtest)")
    
    # === 主頁面參數設定 ===
    st.markdown("### 📊 回測參數設定")
    
    # 股票選擇
    from data.storage import Storage
    col_stock, col_period = st.columns([2, 1])
    
    with col_stock:
        if not os.path.exists(Storage.STOCK_LIST_PATH):
            st.warning("股票清單未建立，請先點擊「更新股票清單」")
            ticker = st.text_input("股票代碼 (Stock ID)", "2330")
        else:
            df_stocks = Storage.load_stock_list()
            df_stocks['label'] = df_stocks['code'] + " " + df_stocks['name'] + " (" + df_stocks['market'] + ")"
            
            default_idx = 0
            match = df_stocks[df_stocks['code'] == '2330']
            if not match.empty:
                default_idx = match.index[0]
            
            selected_option = st.selectbox(
                "搜尋股票 (Search Stock)", 
                df_stocks['label'], 
                index=int(default_idx)
            )
            ticker = selected_option.split(" ")[0]
    
    with col_period:
        period = st.selectbox("回測期間 (Backtest Period)", ["3mo", "6mo", "1y", "2y", "5y", "10y"], index=2)
    
    st.markdown("---")
    st.markdown("### 🎯 策略設定")
    
    col_strategy, col_cash, col_commission = st.columns(3)
    
    with col_strategy:
        strategy_type = st.selectbox("策略 (Strategy)", ["MA Crossover", "RSI", "Bollinger Bands"])
    
    with col_cash:
        initial_cash = st.number_input("初始資金 (Initial Cash)", 10000, 10000000, 1000000)
    
    with col_commission:
        commission_rate = st.number_input("手續費 (Commission)", 0.0, 0.01, 0.001425, format="%.6f")
    
    # 停損停利
    col_sl, col_tp = st.columns(2)
    with col_sl:
        stop_loss_pct = st.number_input("停損 % (Stop Loss)", 0.0, 50.0, 0.0, step=0.5) / 100.0
    with col_tp:
        take_profit_pct = st.number_input("停利 % (Take Profit)", 0.0, 100.0, 0.0, step=0.5) / 100.0
    
    # 策略參數
    st.markdown("### ⚙️ 策略參數")
    
    p1 = 10
    p2 = 30
    p_lower = 30
    p_upper = 70
    
    if strategy_type == "MA Crossover":
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            p1 = st.number_input("快線 (Fast MA)", 1, 100, 10)
        with col_p2:
            p2 = st.number_input("慢線 (Slow MA)", 5, 300, 30)
    elif strategy_type == "RSI":
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            p1 = st.number_input("週期 (Period)", 5, 50, 14)
        with col_p2:
            p_upper = st.number_input("超買 (Upper)", 50, 95, 70)
        with col_p3:
            p_lower = st.number_input("超賣 (Lower)", 5, 50, 30)
    elif strategy_type == "Bollinger Bands":
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            p1 = st.number_input("週期 (Period)", 5, 100, 20)
        with col_p2:
            p2 = st.number_input("標準差 (Std Dev)", 1.0, 5.0, 2.0)
    
    st.markdown("---")
    run_backtest_btn = st.button("🚀 執行回測", type="primary", use_container_width=True)'''

# 替換
if old_section in content:
    content = content.replace(old_section, new_section)
    print("✅ 成功替換策略回測區塊")
else:
    print("❌ 找不到要替換的區塊")

# 寫回檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("完成！")
