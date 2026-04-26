"""
盤整N日後突破
Breakout After N Days Consolidation

XScript 原始碼：
{@type:filter}
input:period(20,"盤整的天數");
input:ratio(5,"盤整的最大波動範圍");

if highest(close,period)[1]<lowest(close,period)[1]*(1+ratio/100)
and close > highest(close,period)[1]
and volume >average(volume,period)
and volume>2000
then ret=1;
"""
import pandas as pd
from ..utils import highest, lowest


def 盤整n日後突破(df: pd.DataFrame, period: int = 20, ratio: int = 5) -> tuple[bool, str]:
    """
    盤整N日後突破策略
    
    條件：
    - 前 N 日最高 < 前 N 日最低 * (1 + ratio%)（盤整）
    - 當前收盤 > 前 N 日最高（突破）
    - 當前成交量 > N 日平均成交量
    - 當前成交量 > 2000
    
    Args:
        df: 股票歷史資料
        period: 盤整的天數（預設 20）
        ratio: 盤整的最大波動範圍%（預設 5）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < period + 1:
        return False, f"資料不足（需要至少 {period + 1} 筆）"
    
    close = df['Close']
    volume = df['Volume']
    
    # 前 N 日的資料（不包含當日）
    close_prev = close.iloc[:-1]
    
    # 計算前 N 日最高和最低
    highest_prev = highest(close_prev, period)
    lowest_prev = lowest(close_prev, period)
    
    # 當前數據
    current_close = close.iloc[-1]
    current_volume = volume.iloc[-1]
    avg_volume = volume.iloc[-period:].mean()
    
    # 檢查條件
    is_consolidation = highest_prev < lowest_prev * (1 + ratio / 100)
    is_breakout = current_close > highest_prev
    is_volume_high = current_volume > avg_volume and current_volume > 2000
    
    if is_consolidation and is_breakout and is_volume_high:
        volatility = ((highest_prev - lowest_prev) / lowest_prev * 100)
        return True, f"盤整突破（{period}日波動:{volatility:.1f}%, 突破價:{current_close:.2f}）"
    
    return False, ""
