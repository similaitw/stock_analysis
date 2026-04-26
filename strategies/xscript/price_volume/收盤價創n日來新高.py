"""
收盤價創N日來新高
Close Price Hits N-Day High

XScript 原始碼：
{@type:filter}
input:period(100,"計算天數");
if close=highest(close,period)
then ret=1;
value2=GetField("總市值","D");
outputfield(1,value2,0,"總市值");
"""
import pandas as pd
from ..utils import highest


def 收盤價創n日來新高(df: pd.DataFrame, period: int = 100) -> tuple[bool, str]:
    """
    收盤價創N日來新高策略
    
    條件：
    - 當前收盤價 = N 日最高收盤價
    
    Args:
        df: 股票歷史資料
        period: 計算天數（預設 100）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < period:
        return False, f"資料不足（需要至少 {period} 筆）"
    
    close = df['Close']
    
    # 計算 N 日最高收盤價
    highest_close = highest(close, period)
    current_close = close.iloc[-1]
    
    if current_close == highest_close:
        prev_high = highest(close.iloc[:-1], period - 1) if len(close) > 1 else 0
        gain_from_prev_high = ((current_close - prev_high) / prev_high * 100) if prev_high > 0 else 0
        return True, f"創{period}日新高（價格:{current_close:.2f}, 較前高漲:{gain_from_prev_high:.1f}%）"
    
    return False, ""
