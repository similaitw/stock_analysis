from data.fetcher import DataFetcher
from scanner.engine import ScannerEngine
import pandas as pd

def test_fetcher():
    print("=== Testing DataFetcher ===")
    stock_id = "2330"
    
    # 1. Price
    price = DataFetcher.fetch_current_price(stock_id)
    print(f"Current Price ({stock_id}): {price}")
    
    # 2. History
    df = DataFetcher.fetch_history(stock_id, period="1mo")
    print(f"History Shape: {df.shape}")
    
    # 3. Fundamentals
    fund = DataFetcher.fetch_fundamentals(stock_id)
    print(f"Fundamentals: {fund}")
    
    # 4. Chips (Stubbed)
    inst = DataFetcher.fetch_institutional_investors(stock_id)
    print(f"Institutional Data: {inst.empty}")

def test_scanner():
    print("\n=== Testing ScannerEngine ===")
    strategies = [
        "XScript - Price/Vol High",
        "XScript - Momentum Breakout",
        "XScript - 3 Red Soldiers"
    ]
    
    for strat in strategies:
        print(f"Scanning strategy: {strat}")
        # Use TEST market to avoid long wait
        res = ScannerEngine.scan(strat, market_type="TEST")
        print(f"Result count: {len(res)}")
        if not res.empty:
            print(res.head())

if __name__ == "__main__":
    test_fetcher()
    test_scanner()
