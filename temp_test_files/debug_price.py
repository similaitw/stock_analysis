from data.fetcher import DataFetcher
import twstock

stock_id = "2330"

print(f"Testing {stock_id}...")
try:
    stock = twstock.Stock(stock_id)
    print(f"twstock price list: {stock.price}")
    # Check what DataFetcher does
    latest = DataFetcher.fetch_current_price(stock_id)
    print(f"DataFetcher result: {latest}")
except Exception as e:
    print(f"Error: {e}")
