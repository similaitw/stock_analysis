"""
簡化測試 XScript 策略（使用模擬資料）
Simplified Test for XScript Strategies (with Mock Data)
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 導入策略
from strategies.xscript.price_volume.uptrend_forming import uptrend_forming
from strategies.xscript.price_volume.漲勢變強 import 漲勢變強
from strategies.xscript.price_volume.漲勢加速 import 漲勢加速
from strategies.xscript.price_volume.多頭轉強 import 多頭轉強
from strategies.xscript.price_volume.大漲股 import 大漲股

def generate_mock_data(days=120, trend='uptrend'):
    """生成模擬資料"""
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    
    if trend == 'uptrend':
        # 上漲趨勢
        base_price = 100
        prices = base_price + np.cumsum(np.random.randn(days) * 0.5 + 0.3)
    elif trend == 'downtrend':
        # 下跌趨勢
        base_price = 100
        prices = base_price + np.cumsum(np.random.randn(days) * 0.5 - 0.3)
    else:
        # 盤整
        base_price = 100
        prices = base_price + np.cumsum(np.random.randn(days) * 0.3)
    
    # 確保價格為正
    prices = np.maximum(prices, 10)
    
    # 生成 OHLC 資料
    df = pd.DataFrame({
        'Open': prices * (1 + np.random.randn(days) * 0.01),
        'High': prices * (1 + np.abs(np.random.randn(days)) * 0.02),
        'Low': prices * (1 - np.abs(np.random.randn(days)) * 0.02),
        'Close': prices,
        'Volume': np.random.randint(500, 5000, days)
    }, index=dates)
    
    # 確保 High >= Close >= Low 和 High >= Open >= Low
    df['High'] = df[['Open', 'High', 'Close']].max(axis=1)
    df['Low'] = df[['Open', 'Low', 'Close']].min(axis=1)
    
    return df

def test_strategy(strategy_func, strategy_name, df):
    """測試單一策略"""
    print(f"\n{'='*60}")
    print(f"測試策略: {strategy_name}")
    print(f"{'='*60}")
    
    try:
        print(f"資料筆數: {len(df)}")
        print(f"日期範圍: {df.index[0].date()} ~ {df.index[-1].date()}")
        print(f"最新收盤價: {df['Close'].iloc[-1]:.2f}")
        print(f"期間漲跌: {((df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100):.2f}%")
        
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
    print("\n" + "="*60)
    print("XScript 策略測試（使用模擬資料）")
    print("="*60)
    
    # 定義測試策略
    strategies = [
        (uptrend_forming, "漲勢成形"),
        (漲勢變強, "漲勢變強"),
        (漲勢加速, "漲勢加速"),
        (多頭轉強, "多頭轉強"),
        (大漲股, "大漲股"),
    ]
    
    # 測試不同趨勢
    test_scenarios = [
        ('uptrend', '上漲趨勢'),
        ('downtrend', '下跌趨勢'),
        ('sideways', '盤整'),
    ]
    
    results = {}
    
    for trend, trend_name in test_scenarios:
        print(f"\n\n{'#'*60}")
        print(f"# 測試場景: {trend_name}")
        print(f"{'#'*60}")
        
        # 生成模擬資料
        df = generate_mock_data(days=120, trend=trend)
        
        scenario_results = []
        
        for strategy_func, strategy_name in strategies:
            result = test_strategy(strategy_func, strategy_name, df)
            scenario_results.append((strategy_name, result))
        
        results[trend_name] = scenario_results
    
    # 顯示總結
    print("\n\n" + "="*60)
    print("測試總結")
    print("="*60)
    
    for scenario, scenario_results in results.items():
        print(f"\n{scenario}:")
        for strategy_name, result in scenario_results:
            status = "✅ 符合" if result else "❌ 不符合"
            print(f"  {strategy_name:20s} {status}")
    
    print("\n" + "="*60)
    print("測試完成！")
    print("="*60)
    print("\n說明：")
    print("- 此測試使用模擬資料，僅驗證策略邏輯是否正常運作")
    print("- 實際使用時需要真實股票資料")
    print("- 策略參數可能需要根據實際情況調整")

if __name__ == "__main__":
    main()
