"""
測試 XScript 策略
Test XScript Strategies
"""
import sys
import pandas as pd
from datetime import datetime, timedelta

# 導入策略
from strategies.xscript.price_volume.uptrend_forming import uptrend_forming
from strategies.xscript.price_volume.漲勢變強 import 漲勢變強
from strategies.xscript.price_volume.漲勢加速 import 漲勢加速
from strategies.xscript.price_volume.多頭轉強 import 多頭轉強
from strategies.xscript.price_volume.大漲股 import 大漲股

# 導入資料獲取
from data.fetcher import DataFetcher

def test_strategy(strategy_func, strategy_name, ticker, period='1y'):
    """測試單一策略"""
    print(f"\n{'='*70}")
    print(f"測試策略: {strategy_name}")
    print(f"股票代碼: {ticker}")
    print(f"{'='*70}")
    
    try:
        # 獲取資料
        print(f"正在獲取 {ticker} 的歷史資料...")
        df = DataFetcher.fetch_data(ticker, period=period)
        
        if df is None or df.empty:
            print(f"❌ 無法獲取 {ticker} 的資料")
            return False
        
        print(f"✅ 成功獲取 {len(df)} 筆資料")
        print(f"   日期範圍: {df.index[0].date()} ~ {df.index[-1].date()}")
        print(f"   最新收盤價: {df['Close'].iloc[-1]:.2f}")
        
        # 執行策略
        print(f"\n執行策略檢測...")
        is_signal, message = strategy_func(df)
        
        if is_signal:
            print(f"✅ 符合條件！")
            print(f"   訊息: {message}")
            return True
        else:
            print(f"❌ 不符合條件")
            if message:
                print(f"   原因: {message}")
            return False
            
    except Exception as e:
        print(f"❌ 測試過程發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """主測試函數"""
    print("\n" + "="*70)
    print("XScript 策略測試")
    print("="*70)
    
    # 定義測試策略
    strategies = [
        (uptrend_forming, "漲勢成形"),
        (漲勢變強, "漲勢變強"),
        (漲勢加速, "漲勢加速"),
        (多頭轉強, "多頭轉強"),
        (大漲股, "大漲股"),
    ]
    
    # 測試股票列表
    test_tickers = [
        "2330",  # 台積電
        "2317",  # 鴻海
        "2454",  # 聯發科
    ]
    
    results = {}
    
    for ticker in test_tickers:
        print(f"\n\n{'#'*70}")
        print(f"# 測試股票: {ticker}")
        print(f"{'#'*70}")
        
        ticker_results = []
        
        for strategy_func, strategy_name in strategies:
            result = test_strategy(strategy_func, strategy_name, ticker)
            ticker_results.append((strategy_name, result))
        
        results[ticker] = ticker_results
    
    # 顯示總結
    print("\n\n" + "="*70)
    print("測試總結")
    print("="*70)
    
    for ticker, ticker_results in results.items():
        print(f"\n{ticker}:")
        for strategy_name, result in ticker_results:
            status = "✅ 符合" if result else "❌ 不符合"
            print(f"  {strategy_name:20s} {status}")
    
    print("\n" + "="*70)
    print("測試完成！")
    print("="*70)

if __name__ == "__main__":
    main()
