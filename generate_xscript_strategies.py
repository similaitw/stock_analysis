"""
批量生成 XScript 策略的 Python 腳本
"""
import os
from pathlib import Path

# 策略列表
price_volume_strategies = [
    "漲勢變強", "漲勢加速", "多頭轉強", "大漲股", 
    "底部愈墊愈高且資金流入的蓄勢股", "波動幅度開始變大且往上攻",
    "盤整N日後突破", "收盤價創N日來新高", "M日內連續N日上漲",
    "N年來漲了M倍的公司", "五日週轉率大於二十日週轉率", "今收破昨高",
    "修正式價量指標黃金交叉", "價量同步創N期新高", "創最低總市值",
    "創百日來新高但距離低點不太遠", "區間內股價創新高天數達一定水準",
    "多日價量背離後跌破", "多次到底而跌破", "大跌後的急拉",
    "收盤價收N日來新低", "昨天成交量不到2000張今天已超過2000張",
    "曾經一個月漲超過兩成的股票", "最近N日漲跌幅小於M%",
    "有一定成交值且過去三日漲幅小", "波段漲幅不大，近N日有過漲停的",
    "漲多後跌破頭部", "炒高後無量反轉下跌", "特定日期迄今漲跌幅超過一定幅度",
    "站在五十二週高點之上", "總市值跌到歷年低點", "股價超過N日未再破底",
    "行業轉強個股也轉強", "跌到52週低點之下", "週線二連紅",
    "過去M日有N日HHLL", "過去N日價穩量縮", "量價背離"
]

def create_strategy_file(strategy_name: str, category: str):
    """建立策略檔案"""
    # 轉換檔名
    filename = strategy_name.replace(" ", "_").replace("，", "_").lower()
    filepath = f"strategies/xscript/{category}/{filename}.py"
    
    # 檢查檔案是否已存在
    if os.path.exists(filepath):
        print(f"⏭️  跳過（已存在）: {filepath}")
        return
    
    # 生成程式碼
    code = f'''"""
{strategy_name}
{strategy_name.upper().replace("，", " ")}

TODO: 需要實作此策略的邏輯
"""
import pandas as pd
from ..utils import *


def {filename}(df: pd.DataFrame) -> tuple[bool, str]:
    """
    {strategy_name}策略
    
    Args:
        df: 股票歷史資料
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    # TODO: 實作策略邏輯
    # 1. 檢查資料長度
    # 2. 計算指標
    # 3. 檢查條件
    # 4. 返回結果
    
    return False, "策略尚未實作"
'''
    
    # 寫入檔案
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f"✅ 建立: {filepath}")

# 批量建立價量選股策略
print("=" * 60)
print("批量建立價量選股策略檔案...")
print("=" * 60)

for strategy in price_volume_strategies:
    create_strategy_file(strategy, "price_volume")

print(f"\n✅ 完成！共建立 {len(price_volume_strategies)} 個策略檔案")
