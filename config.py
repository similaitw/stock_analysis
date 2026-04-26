import os
from enum import Enum
from dotenv import load_dotenv

# Load .env file from the same directory as this config.py
_config_dir = os.path.dirname(os.path.abspath(__file__))
_env_path = os.path.join(_config_dir, '.env')
load_dotenv(_env_path)

class DataSource(Enum):
    """資料來源選項"""
    AUTO = "AUTO"           # 自動選擇 (有 Token 優先 FinMind)
    FINMIND = "FINMIND"     # 強制使用 FinMind
    YFINANCE = "YFINANCE"   # 強制使用 yfinance + twstock

class Config:
    """應用程式設定"""
    
    # FinMind API Token
    FINMIND_API_TOKEN = os.getenv("FINMIND_API_TOKEN", "")
    
    # 資料來源選擇
    DATA_SOURCE = os.getenv("DATA_SOURCE", "AUTO")
    
    @staticmethod
    def has_finmind_token() -> bool:
        """檢查是否有 FinMind Token"""
        return bool(Config.FINMIND_API_TOKEN and Config.FINMIND_API_TOKEN != "your_token_here")
    
    @staticmethod
    def get_data_source() -> DataSource:
        """取得資料來源設定"""
        try:
            return DataSource[Config.DATA_SOURCE.upper()]
        except KeyError:
            return DataSource.AUTO
    
    @staticmethod
    def should_use_finmind() -> bool:
        """判斷是否應該使用 FinMind"""
        source = Config.get_data_source()
        
        if source == DataSource.FINMIND:
            return Config.has_finmind_token()
        elif source == DataSource.YFINANCE:
            return False
        else:  # AUTO
            return Config.has_finmind_token()

if __name__ == "__main__":
    print(f"FinMind Token: {'已設定' if Config.has_finmind_token() else '未設定'}")
    print(f"資料來源: {Config.get_data_source()}")
    print(f"使用 FinMind: {Config.should_use_finmind()}")
