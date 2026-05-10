"""
測試新增的多指標技術策略
Test new multi-indicator technical strategies
"""
import pandas as pd
from data.fetcher import DataFetcher
from strategies.xscript.technical.multi_indicator import (
    多頭排列, MACD_KD雙金叉, 布林通道突破, 
    RSI背離, 量價齊揚突破, 三線合一
)

def test_strategy(strategy_func, stock_id, strategy_name):
    """測試單一策略"""
    print(f"\n{'='*60}")
    print(f"測試策略: {strategy_name} | 股票: {stock_id}")
    print('='*60)
    
    try:
        # 抓取資料
        df = DataFetcher.fetch_history(stock_id, period="6mo")
        
        if df.empty:
            print(f"❌ 無法取得 {stock_id} 的資料")
            return False
        
        print(f"✅ 成功取得 {len(df)} 筆資料")
        
        # 執行策略
        is_match, reason = strategy_func(df)
        
        if is_match:
            print(f"🎯 訊號: {reason}")
            return True
        else:
            print(f"⚪ 無訊號")
            return False
            
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("\n" + "="*60)
    print("🧪 新增策略測試 - Multi-Indicator Technical Strategies")
    print("="*60)
    
    # 測試股票列表
    test_stocks = ['2330', '2317', '2454', '2308', '3008']
    
    # 策略列表
    strategies = [
        (多頭排列, "多頭排列"),
        (MACD_KD雙金叉, "MACD_KD雙金叉"),
        (布林通道突破, "布林通道突破"),
        (RSI背離, "RSI背離"),
        (量價齊揚突破, "量價齊揚突破"),
        (三線合一, "三線合一")
    ]
    
    results = {}
    
    # 測試每個策略
    for strategy_func, strategy_name in strategies:
        print(f"\n\n{'#'*60}")
        print(f"# 策略: {strategy_name}")
        print('#'*60)
        
        strategy_results = []
        
        for stock_id in test_stocks:
            is_signal = test_strategy(strategy_func, stock_id, strategy_name)
            if is_signal:
                strategy_results.append(stock_id)
        
        results[strategy_name] = strategy_results
    
    # 總結報告
    print("\n\n" + "="*60)
    print("📊 測試總結報告")
    print("="*60)
    
    for strategy_name, signals in results.items():
        signal_count = len(signals)
        print(f"\n{strategy_name}:")
        print(f"  訊號數量: {signal_count}/{len(test_stocks)}")
        if signals:
            print(f"  訊號股票: {', '.join(signals)}")
        else:
            print(f"  訊號股票: 無")
    
    total_signals = sum(len(signals) for signals in results.values())
    print(f"\n總訊號數: {total_signals}")
    print(f"平均每策略: {total_signals / len(strategies):.1f} 個訊號")
    
    print("\n✅ 測試完成！")

if __name__ == "__main__":
    main()
