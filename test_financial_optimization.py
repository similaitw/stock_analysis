"""
驗證財報資料優化 (Phase 4 Verification)
Verify financial report data optimization
"""
from data.fetcher import DataFetcher
import pandas as pd

def verify_financial_data(stock_id):
    print(f"\n{'='*60}")
    print(f"驗證股票: {stock_id}")
    print('='*60)
    
    # 1. 測試月營收
    print("\n[1] 測試月營收 (fetch_monthly_revenue)...")
    rev_df = DataFetcher.fetch_monthly_revenue(stock_id)
    if not rev_df.empty:
        print(f"  成功取得 {len(rev_df)} 筆營收資料")
        print(f"  最新日期: {rev_df.iloc[-1]['date']}")
        print(f"  欄位: {list(rev_df.columns)}")
    else:
        print("  ❌ 無法取得營收資料")
        
    # 2. 測試財務比率
    print("\n[2] 測試財務比率 (fetch_financial_ratios)...")
    ratio_df = DataFetcher.fetch_financial_ratios(stock_id)
    if not ratio_df.empty:
        print(f"  成功取得 {len(ratio_df)} 季比率資料")
        print(f"  欄位: {list(ratio_df.columns)}")
        print(ratio_df.tail(2))
    else:
        print("  ❌ 無法取得比率資料")
        
    # 3. 測試 EPS
    print("\n[3] 測試 EPS (fetch_eps_data)...")
    eps_df = DataFetcher.fetch_eps_data(stock_id)
    if not eps_df.empty:
        print(f"  成功取得 {len(eps_df)} 季 EPS 資料")
        print(eps_df.tail(2))
    else:
        print("  ❌ 無法取得 EPS 資料")
        
    # 4. 測試資產負債表比率
    print("\n[4] 測試資產負債表比率 (fetch_balance_sheet_ratios)...")
    bs_df = DataFetcher.fetch_balance_sheet_ratios(stock_id)
    if not bs_df.empty:
        print(f"  成功取得 {len(bs_df)} 季資產負債表資料")
        print(f"  欄位: {list(bs_df.columns)}")
        print(bs_df.tail(2))
    else:
        print("  ❌ 無法取得資產負債表資料")

def main():
    test_stocks = ['2330', '2317', '2881'] # 不同產業: 半導體, 代工, 金融
    for stock in test_stocks:
        verify_financial_data(stock)
        
    print("\n✅ 驗證完成！")

if __name__ == "__main__":
    main()
