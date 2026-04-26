"""
價量同步創N期新高
Price and Volume Sync New High

XScript 原始碼：
{@type:filter}
input:period(100,"計算天數");

value1=highest(high,period);
value2=highest(volume,period);
if high=value1 and volume=value2
then ret=1;
"""
import pandas as pd
from ..utils import highest


def 價量同步創n期新高(df: pd.DataFrame, period: int = 100) -> tuple[bool, str]:
    """
    價量同步創N期新高策略
    
    條件：
    - 當前最高價 = N 期最高價
    - 當前成交量 = N 期最高成交量
    
    Args:
        df: 股票歷史資料
        period: 計算天數（預設 100）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < period:
        return False, f"資料不足（需要至少 {period} 筆）"
    
    high = df['High']
    volume = df['Volume']
    
    # 計算 N 期最高價和最高量
    highest_price = highest(high, period)
    highest_vol = highest(volume, period)
    
    current_high = high.iloc[-1]
    current_volume = volume.iloc[-1]
    
    if current_high == highest_price and current_volume == highest_vol:
        return True, f"價量同步創{period}日新高（價:{current_high:.2f}, 量:{current_volume:.0f}）"
    
    return False, ""
