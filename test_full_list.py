from scanner.engine import ScannerEngine
from data.storage import Storage
import os

print("1. Testing Storage Load...")
df = Storage.load_stock_list()
print(f"Loaded {len(df)} stocks.")

print("\n2. Testing Scanner Get List (All)...")
codes = ScannerEngine.get_stock_list('All')
print(f"Scanner got {len(codes)} codes.")
print(f"First 5: {codes[:5]}")

if len(codes) > 1000:
    print("\nSUCCESS: Full market list integrated.")
else:
    print("\nFAILURE: List seems too short.")
