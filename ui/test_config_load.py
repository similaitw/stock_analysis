import os
import sys

# Simulate exact UI import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("=== Simulating Streamlit UI Config Load ===\n")
print(f"Current working directory: {os.getcwd()}")
print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")

try:
    from config import Config
    print("\n[OK] Config imported")
    print(f"Has FinMind Token: {Config.has_finmind_token()}")
    print(f"Should use FinMind: {Config.should_use_finmind()}")
    
    if Config.has_finmind_token():
        print(f"Token (first 30 chars): {Config.FINMIND_API_TOKEN[:30]}...")
    else:
        print(f"Token value: '{Config.FINMIND_API_TOKEN}'")
        
    # Check .env location
    import config
    config_file = config.__file__
    config_dir = os.path.dirname(config_file)
    env_path = os.path.join(config_dir, '.env')
    print(f"\nConfig file location: {config_file}")
    print(f"Expected .env path: {env_path}")
    print(f".env exists: {os.path.exists(env_path)}")
    
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f".env content ({len(lines)} lines):")
            for line in lines[:5]:
                if 'TOKEN' in line and '=' in line:
                    key, val = line.split('=', 1)
                    print(f"  {key}={val[:30]}..." if len(val) > 30 else f"  {line.strip()}")
                else:
                    print(f"  {line.strip()}")
                    
except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()
