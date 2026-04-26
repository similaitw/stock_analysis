"""
今收破昨高
Today's Close Breaks Yesterday's High

XScript 原始碼：
{@type:filter}
if close>=high[1]
then ret=1;
"""
import pandas as pd


def 今收破昨高(df: pd.DataFrame) -> tuple[bool, str]:
    """
    今收破昨高策略
    
    條件：
    - 今日收盤價 >= 昨日最高價
    
    Args:
        df: 股票歷史資料
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 2:
        return False, "資料不足（需要至少 2 筆）"
    
    current_close = df['Close'].iloc[-1]
    prev_high = df['High'].iloc[-2]
    
    if current_close >= prev_high:
        breakout_pct = ((current_close - prev_high) / prev_high * 100)
        return True, f"今收破昨高（收:{current_close:.2f}, 昨高:{prev_high:.2f}, +{breakout_pct:.1f}%）"
    
    return False, ""
