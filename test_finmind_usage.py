from data.fetcher import DataFetcher
from config import Config

print("=== 測試 FinMind 是否被使用 ===\n")

print(f"Config 狀態:")
print(f"  - has_finmind_token: {Config.has_finmind_token()}")
print(f"  - should_use_finmind: {Config.should_use_finmind()}")
print()

print("測試抓取 2330 三大法人資料:")
print("-" * 50)
df = DataFetcher.fetch_institutional_investors("2330", days=30)
print("-" * 50)

if not df.empty:
    print(f"\n✅ 成功取得 {len(df)} 筆資料")
    print(f"欄位: {df.columns.tolist()}")
    print(f"\n最新 3 筆:")
    print(df.tail(3))
else:
    print("\n❌ 未取得資料")
