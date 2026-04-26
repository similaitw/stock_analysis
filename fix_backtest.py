import re

# 讀取檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到要替換的部分
old_code = '''    run_backtest_btn = st.sidebar.button("🚀 執行回測", type="primary")

    if run_backtest_btn:
        st.subheader(f"回測報告: {ticker} - {strategy_type}")'''

new_code = '''    run_backtest_btn = st.sidebar.button("🚀 執行回測", type="primary")

    if not run_backtest_btn:
        # 未執行回測時顯示說明頁面
        st.info("👈 請在左側設定回測參數，然後點擊「🚀 執行回測」按鈕")
        
        st.markdown("### 📋 當前設定")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("股票代碼", ticker)
            st.metric("期間", period)
        with col2:
            st.metric("策略", strategy_type)
            st.metric("初始資金", f"${initial_cash:,.0f}")
        with col3:
            st.metric("手續費", f"{commission_rate:.4%}")
        
        st.markdown("---")
        st.markdown("### 💡 策略說明")
        if strategy_type == "MA Crossover":
            st.write(f"**均線交叉策略** - 快線({p1})穿越慢線({p2})")
        elif strategy_type == "RSI":
            st.write(f"**RSI策略** - 週期{p1}, 超買{p_upper}, 超賣{p_lower}")
        elif strategy_type == "Bollinger Bands":
            st.write(f"**布林通道策略** - 週期{p1}, 標準差{p2}")
    
    elif run_backtest_btn:
        st.subheader(f"回測報告: {ticker} - {strategy_type}")'''

# 替換
if old_code in content:
    content = content.replace(old_code, new_code)
    print("✅ 找到並替換程式碼")
else:
    print("❌ 找不到要替換的程式碼")
    print("正在搜尋...")
    # 顯示相關區域
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'run_backtest_btn' in line:
            print(f"Line {i}: {line}")

# 寫回檔案
with open(r'e:\anti-gravity\stock\stock_analysis\ui\app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("完成！")
