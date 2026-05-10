"""
測試籌碼策略效能優化
比較優化前後的掃描速度
"""
import time
import pandas as pd
from scanner.engine import ScannerEngine

def test_chip_strategy_performance():
    print("=" * 60)
    print("籌碼策略效能測試 (Chip Strategy Performance Test)")
    print("=" * 60)
    
    # 測試策略列表
    chip_strategies = [
        "N日以來投信曾大買過",
        "N日內三大法人曾同步買超",
        "外資拉抬"
    ]
    
    # 測試股票列表（小樣本）
    test_stocks = ['2330', '2317', '2454', '2308', '2303', '2881', '2882', '2891', '2886', '2609']
    
    print(f"\n測試配置:")
    print(f"  策略數量: {len(chip_strategies)}")
    print(f"  股票數量: {len(test_stocks)}")
    print(f"  預期 API 呼叫次數（優化前）: {len(test_stocks) * len(chip_strategies) * 3} 次")
    print(f"  預期 API 呼叫次數（優化後）: {len(test_stocks) * 3} 次")
    print(f"  理論減少: {((len(chip_strategies) - 1) / len(chip_strategies)) * 100:.1f}%")
    
    print("\n" + "-" * 60)
    print("開始掃描測試...")
    print("-" * 60)
    
    start_time = time.time()
    
    results = ScannerEngine.scan_strategies(
        strategy_names=chip_strategies,
        market_type='Tw50',
        match_mode='OR',
        stock_list=test_stocks
    )
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print("\n" + "=" * 60)
    print("測試結果")
    print("=" * 60)
    print(f"掃描時間: {elapsed:.2f} 秒")
    print(f"每支股票平均時間: {elapsed / len(test_stocks):.2f} 秒")
    print(f"找到訊號數量: {len(results)}")
    
    if not results.empty:
        print(f"\n找到的股票:")
        print(results[['Stock ID', 'Name', 'Signal']].to_string(index=False))
    
    print("\n" + "=" * 60)
    print("效能評估")
    print("=" * 60)
    
    # 效能基準（基於優化建議文件）
    # 優化前預估: 10支股票 * 3策略 * 2秒/API = 60秒
    # 優化後預估: 10支股票 * 2秒 = 20秒
    
    if elapsed < 30:
        print("✅ 效能優異！快取機制運作正常")
    elif elapsed < 60:
        print("⚠️  效能良好，但可能還有優化空間")
    else:
        print("❌ 效能不佳，請檢查快取機制")
    
    return elapsed, len(results)

if __name__ == "__main__":
    try:
        elapsed, signal_count = test_chip_strategy_performance()
        print(f"\n測試完成！總時間: {elapsed:.2f}秒，訊號數: {signal_count}")
    except Exception as e:
        print(f"\n❌ 測試失敗: {e}")
        import traceback
        traceback.print_exc()
