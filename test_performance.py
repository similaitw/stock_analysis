"""
效能監控工具 (Performance Monitoring)
監控系統效能、快取命中率、API 呼叫統計
"""
import time
import pandas as pd
from data.cache import DataCache
from data.fetcher import DataFetcher
from scanner.engine import ScannerEngine

class PerformanceMonitor:
    """效能監控類別"""
    
    def __init__(self):
        self.start_time = None
        self.api_calls = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.errors = 0
    
    def start(self):
        """開始監控"""
        self.start_time = time.time()
        print("🔍 效能監控開始...")
        print("="*60)
    
    def stop(self):
        """停止監控並顯示報告"""
        if not self.start_time:
            print("❌ 監控未啟動")
            return
        
        elapsed = time.time() - self.start_time
        
        print("\n" + "="*60)
        print("📊 效能監控報告")
        print("="*60)
        print(f"執行時間: {elapsed:.2f} 秒")
        print(f"API 呼叫: {self.api_calls} 次")
        print(f"快取命中: {self.cache_hits} 次")
        print(f"快取未中: {self.cache_misses} 次")
        
        if self.cache_hits + self.cache_misses > 0:
            hit_rate = (self.cache_hits / (self.cache_hits + self.cache_misses)) * 100
            print(f"快取命中率: {hit_rate:.1f}%")
        
        print(f"錯誤數: {self.errors} 次")
        
        # DataCache 統計
        cache_stats = DataCache.get_stats()
        print(f"\n快取狀態:")
        print(f"  總條目: {cache_stats['total']}")
        print(f"  有效: {cache_stats['valid']}")
        print(f"  過期: {cache_stats['expired']}")
        
        print("="*60)

def test_cache_performance():
    """測試快取效能"""
    print("\n" + "#"*60)
    print("# 測試 1: 快取效能測試")
    print("#"*60)
    
    monitor = PerformanceMonitor()
    monitor.start()
    
    test_stocks = ['2330', '2317', '2454']
    
    # 第一輪: 無快取
    print("\n第一輪抓取 (無快取):")
    start = time.time()
    for stock in test_stocks:
        df = DataFetcher.fetch_history(stock, '1mo')
        print(f"  {stock}: {len(df)} 筆")
    first_round = time.time() - start
    print(f"耗時: {first_round:.2f} 秒")
    
    # 第二輪: 有快取
    print("\n第二輪抓取 (有快取):")
    start = time.time()
    for stock in test_stocks:
        df = DataFetcher.fetch_history(stock, '1mo')
        print(f"  {stock}: {len(df)} 筆")
    second_round = time.time() - start
    print(f"耗時: {second_round:.2f} 秒")
    
    # 計算加速比
    if second_round > 0:
        speedup = first_round / second_round
        print(f"\n快取加速: {speedup:.1f}x")
    
    monitor.stop()

def test_scanner_performance():
    """測試掃描器效能"""
    print("\n" + "#"*60)
    print("# 測試 2: 掃描器效能測試")
    print("#"*60)
    
    monitor = PerformanceMonitor()
    monitor.start()
    
    # 測試不同規模
    test_cases = [
        (['2330', '2317', '2454', '2308', '3008'], "小規模 (5檔)"),
        (['2330', '2317', '2454', '2308', '3008', '2881', '2882', '2891', '2886', '2609'], "中規模 (10檔)")
    ]
    
    strategies = ['多頭排列', '三線合一']
    
    for stock_list, desc in test_cases:
        print(f"\n{desc}:")
        start = time.time()
        
        results = ScannerEngine.scan_strategies(
            strategy_names=strategies,
            stock_list=stock_list,
            match_mode='OR'
        )
        
        elapsed = time.time() - start
        print(f"  掃描時間: {elapsed:.2f} 秒")
        print(f"  每檔平均: {elapsed/len(stock_list):.2f} 秒")
        print(f"  訊號數: {len(results)}")
    
    monitor.stop()

def test_strategy_registry():
    """測試策略註冊系統"""
    print("\n" + "#"*60)
    print("# 測試 3: 策略註冊系統")
    print("#"*60)
    
    from strategies.registry import StrategyRegistry
    
    StrategyRegistry.initialize()
    
    # 統計策略數量
    all_strategies = StrategyRegistry.get_all_strategies()
    
    print("\n策略統計:")
    total = 0
    for category, strategies in all_strategies.items():
        count = len(strategies)
        total += count
        print(f"  {category}: {count} 個策略")
    
    print(f"\n總計: {total} 個策略")
    
    # 測試參數驗證
    print("\n參數驗證測試:")
    test_strategy = "多頭排列"
    params = StrategyRegistry.get_strategy_params(test_strategy)
    print(f"  策略: {test_strategy}")
    print(f"  參數: {params}")

def main():
    """主測試流程"""
    print("\n" + "="*60)
    print("🚀 系統效能監控與測試")
    print("="*60)
    
    # 清除快取
    DataCache.clear()
    print("✅ 快取已清除\n")
    
    # 執行測試
    test_cache_performance()
    test_scanner_performance()
    test_strategy_registry()
    
    print("\n✅ 所有測試完成！")

if __name__ == "__main__":
    main()
