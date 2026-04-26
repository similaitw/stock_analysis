"""
底部愈墊愈高且資金流入的蓄勢股
Bottom Rising with Capital Inflow

XScript 原始碼：
{@type:filter}
input:r1(7,"近來漲幅上限%");

value1 = RateOfChange(close, 12);
value2 = lowest(low,3);
value3 = lowest(low,8);
value4 = lowest(low,13);

condition1=false;
condition2=false;

if value1 < r1 and value2 > value3 and value3 > value4 and close = highest(close,13)
then condition1=true;

Value5=average(GetField("佔全市場成交量比","D"),13);

if linearregslope(Value5,5) > 0
then condition2=true;

if condition1 and condition2
then ret=1;
"""
import pandas as pd
from ..utils import lowest, highest, linear_reg_slope


def 底部愈墊愈高且資金流入的蓄勢股(df: pd.DataFrame, r1: int = 7) -> tuple[bool, str]:
    """
    底部愈墊愈高且資金流入的蓄勢股策略
    
    條件：
    - 12日漲幅 < r1%
    - 3日最低 > 8日最低 > 13日最低（底部墊高）
    - 收盤價 = 13日最高（創新高）
    - 成交量佔比的5日斜率 > 0（資金流入）
    
    Args:
        df: 股票歷史資料
        r1: 近來漲幅上限%（預設 7）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 20:
        return False, "資料不足（需要至少 20 筆）"
    
    close = df['Close']
    low = df['Low']
    volume = df['Volume']
    
    # 計算 12 日漲幅
    roc_12 = ((close.iloc[-1] - close.iloc[-13]) / close.iloc[-13] * 100) if len(close) > 12 else 0
    
    # 計算各期最低點
    low_3 = lowest(low, 3)
    low_8 = lowest(low, 8)
    low_13 = lowest(low, 13)
    
    # 計算 13 日最高
    high_13 = highest(close, 13)
    
    # 條件 1: 底部墊高且創新高
    condition1 = (
        roc_12 < r1 and
        low_3 > low_8 and
        low_8 > low_13 and
        close.iloc[-1] == high_13
    )
    
    # 條件 2: 成交量佔比上升（簡化：使用成交量本身）
    volume_ratio = volume / volume.rolling(window=20).mean()
    volume_ratio_avg = volume_ratio.rolling(window=13).mean()
    volume_slope = linear_reg_slope(volume_ratio_avg, 5)
    condition2 = volume_slope > 0
    
    if condition1 and condition2:
        return True, f"底部蓄勢（底部墊高，資金流入，斜率:{volume_slope:.3f}）"
    
    return False, ""
