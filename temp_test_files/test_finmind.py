from FinMind.data import DataLoader
import pandas as pd

try:
    api = DataLoader()
    # Test 1: Institutional Investors (Foreign/Investment Trust)
    # 2330, last 10 days
    print("Fetching Institutional Data...")
    df_inst = api.taiwan_stock_institutional_investors(
        stock_id='2330',
        start_date='2023-01-01',
    )
    print(f"Institutional Data Head:\n{df_inst.tail(3)}")

    # Test 2: Monthly Revenue
    print("\nFetching Revenue Data...")
    df_rev = api.taiwan_stock_month_revenue(
        stock_id='2330',
        start_date='2023-01-01',
    )
    print(f"Revenue Data Head:\n{df_rev.tail(3)}")
    
    # Test 3: Margin (Financial Statements) - might be different API
    # FinMind margin data is in taiwan_stock_financial_statement
    print("\nFetching Financial Stats...")
    df_fin = api.taiwan_stock_financial_statement(
        stock_id='2330',
        start_date='2023-01-01',
    )
    print(f"Financial Data Head:\n{df_fin.tail(3)}")

except Exception as e:
    print(f"Error: {e}")
