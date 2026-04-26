import sys
import os

# Simulate UI import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Testing config import...")
print(f"Current dir: {os.getcwd()}")
print(f"Script dir: {os.path.dirname(__file__)}")
print(f"sys.path: {sys.path[:3]}")

try:
    from config import Config
    print(f"\n✅ Config imported successfully")
    print(f"Has FinMind Token: {Config.has_finmind_token()}")
    print(f"Should use FinMind: {Config.should_use_finmind()}")
    print(f"Token (first 20 chars): {Config.FINMIND_API_TOKEN[:20]}...")
except ImportError as e:
    print(f"\n❌ Config import failed: {e}")
except Exception as e:
    print(f"\n❌ Error: {e}")
