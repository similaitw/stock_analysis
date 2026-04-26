import os
import sys

print("=== FinMind 診斷測試 ===\n")

# 1. Check .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"1. .env 檔案檢查:")
print(f"   路徑: {env_path}")
print(f"   存在: {os.path.exists(env_path)}")
if os.path.exists(env_path):
    with open(env_path, 'r') as f:
        content = f.read()
        has_token = 'FINMIND_API_TOKEN=' in content and 'your_token_here' not in content
        print(f"   包含 Token: {has_token}")
print()

# 2. Test config import
print("2. Config 模組測試:")
try:
    from config import Config
    print(f"   ✅ Config 載入成功")
    print(f"   Token 已設定: {Config.has_finmind_token()}")
    print(f"   應使用 FinMind: {Config.should_use_finmind()}")
    if Config.has_finmind_token():
        print(f"   Token (前20字): {Config.FINMIND_API_TOKEN[:20]}...")
except Exception as e:
    print(f"   ❌ 錯誤: {e}")
    sys.exit(1)
print()

# 3. Test FinMind import
print("3. FinMind 模組測試:")
try:
    from FinMind.data import DataLoader
    print(f"   ✅ FinMind 模組載入成功")
except Exception as e:
    print(f"   ❌ 錯誤: {e}")
    sys.exit(1)
print()

# 4. Test API connection
print("4. FinMind API 連線測試:")
try:
    api = DataLoader()
    print(f"   ✅ DataLoader 建立成功")
    
    # Try login
    result = api.login_by_token(api_token=Config.FINMIND_API_TOKEN)
    print(f"   登入結果: {result}")
    
    # Try fetching data
    print(f"\n   測試抓取 2330 三大法人資料...")
    import datetime
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    
    df = api.taiwan_stock_institutional_investors(
        stock_id="2330",
        start_date=start_date,
        end_date=end_date
    )
    
    if not df.empty:
        print(f"   ✅ 成功取得 {len(df)} 筆資料")
        print(f"   欄位: {df.columns.tolist()}")
        print(f"\n   最新 3 筆資料:")
        print(df.tail(3))
    else:
        print(f"   ⚠️ 回傳空資料")
        
except Exception as e:
    print(f"   ❌ API 連線失敗")
    print(f"   錯誤訊息: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n=== 診斷完成 ===")
