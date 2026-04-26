"""
批量生成所有 XScript 策略框架
Generate All XScript Strategy Frameworks
"""
import os
import json

# 定義所有策略
STRATEGIES = {
    "price_volume": {
        "已實作": ["價量齊揚", "無量變有量", "帶量突破均線", "漲勢成形"],
        "待實作": [
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
    },
    "technical": {
        "已實作": ["MACD黃金交叉", "MA黃金交叉", "KD黃金交叉"],
        "待實作": [
            "RSI超賣", "RSI超買", "布林通道突破", "布林通道跌破",
            "威廉指標超賣", "DMI多頭", "ADX趨勢強度", "CCI超買超賣",
            "MACD死亡交叉", "MA死亡交叉", "KD死亡交叉", "乖離率過大",
            "乖離率過小", "MTM動量指標", "ROC變動率", "TRIX三重指數平滑",
            "PSY心理線", "OBV能量潮", "SAR拋物線", "BOLL寬度",
            "ATR波動率"
        ]
    },
    "pattern": {
        "已實作": ["W底型態", "頭肩底"],
        "待實作": [
            "三次到頂而破", "上昇旗形", "下跌後的吊人線", "下降趨勢改變",
            "下降趨勢明確", "做M頭的股票", "在上昇趨勢中的股票",
            "平台整理後突破", "平台整理後跌破", "突破下降旗型",
            "突破整理格局", "突破箱型", "突破繼續型態", "突破股票箱",
            "跌勢後的內困三日翻紅", "近期漲幅不大"
        ]
    }
}

def sanitize_filename(name: str) -> str:
    """清理檔名"""
    # 移除或替換特殊字元
    replacements = {
        "，": "_",
        " ": "_",
        "（": "_",
        "）": "",
        "%": "percent",
        "/": "_",
        "N": "n",
        "M": "m"
    }
    
    result = name
    for old, new in replacements.items():
        result = result.replace(old, new)
    
    return result.lower()

def generate_strategy_file(name: str, category: str, xs_file: str = None):
    """生成策略檔案"""
    filename = sanitize_filename(name)
    filepath = f"strategies/xscript/{category}/{filename}.py"
    
    # 檢查是否已存在
    if os.path.exists(filepath):
        return f"⏭️  跳過: {name}"
    
    # 生成程式碼
    code = f'''"""
{name}
{name.upper()}

XScript 原始檔案: {xs_file if xs_file else 'TODO'}
狀態: 待實作
"""
import pandas as pd
from ..utils import *


def {filename}(df: pd.DataFrame, **kwargs) -> tuple[bool, str]:
    """
    {name}策略
    
    Args:
        df: 股票歷史資料（包含 Open, High, Low, Close, Volume）
        **kwargs: 策略參數
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    # TODO: 實作策略邏輯
    # 步驟：
    # 1. 檢查資料長度是否足夠
    # 2. 計算所需指標
    # 3. 檢查策略條件
    # 4. 返回結果
    
    return False, "策略尚未實作 - {name}"
'''
    
    # 寫入檔案
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    
    return f"✅ 建立: {name}"

# 執行生成
print("=" * 70)
print("批量生成 XScript 策略框架")
print("=" * 70)

total_created = 0
total_skipped = 0

for category, strategies in STRATEGIES.items():
    print(f"\n📁 {category.upper()}")
    print("-" * 70)
    
    for name in strategies["待實作"]:
        result = generate_strategy_file(name, category)
        print(result)
        
        if result.startswith("✅"):
            total_created += 1
        else:
            total_skipped += 1

print("\n" + "=" * 70)
print(f"✅ 完成！")
print(f"   建立: {total_created} 個檔案")
print(f"   跳過: {total_skipped} 個檔案")
print(f"   總計: {total_created + total_skipped} 個策略")
print("=" * 70)

# 更新 __init__.py
print("\n更新模組 __init__.py...")

for category in STRATEGIES.keys():
    init_file = f"strategies/xscript/{category}/__init__.py"
    
    # 收集所有策略名稱
    all_strategies = STRATEGIES[category]["已實作"] + STRATEGIES[category]["待實作"]
    function_names = [sanitize_filename(name) for name in all_strategies]
    
    # 生成 __init__.py 內容
    content = f'''"""
{category.replace("_", " ").title()} 策略模組
"""

__all__ = {json.dumps(function_names, ensure_ascii=False, indent=4)}
'''
    
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 更新: {init_file}")

print("\n🎉 所有框架生成完成！")
