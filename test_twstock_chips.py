import twstock
import pandas as pd
import time

stock_id = "2330"

print(f"Testing twstock for {stock_id}...")

# 1. Real-time info
try:
    stock = twstock.Stock(stock_id)
    print(f"Real-time Price: {stock.price[-1] if stock.price else 'N/A'}")
    print(f"Real-time Capacity: {stock.capacity[-1] if stock.capacity else 'N/A'}")
except Exception as e:
    print(f"Real-time error: {e}")

# 2. Historical Data
try:
    # twstock fetch uses year/month
    print("Fetching historical data (recent month)...")
    # This might fetch from TWSE directly, watch out for rate limits
    hist = stock.fetch_31() 
    print(f"Fetched {len(hist)} days")
    if len(hist) > 0:
        print(hist[0])
except Exception as e:
    print(f"Historical error: {e}")

# 3. Chip Data?
# twstock mainly provides price/volume and basic info.
# It does NOT natively provide extensive chip data (Institutions/Margins) easily in a structured way like FinMind without parsing.
# We might need to rely on scraping or other implementation for chips if FinMind is out.
# Or check if 'twstock' has institutional data.
print("Checking for institutional data in twstock...")
# It seems twstock is minimal.

# 4. Stock Info
print(f"Stock Info: {twstock.codes.get(stock_id)}")
