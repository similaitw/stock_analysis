from data.fetcher import DataFetcher
import twstock

stock_id = "2330"

print(f"Testing {stock_id} via DataFetcher...")
try:
    # This should now handle the exception internally and print an error message, then return yfinance price
    latest = DataFetcher.fetch_current_price(stock_id)
    print(f"DataFetcher result: {latest}")
except Exception as e:
    print(f"Outer Error: {e}")
