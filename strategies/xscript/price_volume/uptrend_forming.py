"""
漲勢成形
Uptrend Forming Pattern

XScript 原始碼：
{@type:filter}
Value1=linearregslope(close,3);
value2=linearregslope(close,5);
value3=linearregslope(close,20);

settotalbar(23);

if value1 > value2 and value2 > value3 and value1 > value1[1] and 
   value1[1] > value1[2] and value1 > 0.3 and value3[2] < 0.1 and value3 > 0
then ret=1;
"""
import pandas as pd
from ..utils import linear_reg_slope


def uptrend_forming(df: pd.DataFrame) -> tuple[bool, str]:
    """
    漲勢成形策略
    
    條件：
    - 3日線性回歸斜率 > 5日線性回歸斜率 > 20日線性回歸斜率
    - 3日斜率持續上升（連續2日）
    - 3日斜率 > 0.3
    - 20日斜率從低點轉正（2日前 < 0.1，現在 > 0）
    
    Args:
        df: 股票歷史資料，需包含 Close 欄位
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 23:
        return False, "資料不足（需要至少 23 筆）"
    
    # 計算線性回歸斜率
    slope_3 = linear_reg_slope(df['Close'], 3)
    slope_5 = linear_reg_slope(df['Close'], 5)
    slope_20 = linear_reg_slope(df['Close'], 20)
    
    # 計算前兩期的 3日斜率
    slope_3_prev1 = linear_reg_slope(df['Close'].iloc[:-1], 3)
    slope_3_prev2 = linear_reg_slope(df['Close'].iloc[:-2], 3)
    
    # 計算 2日前的 20日斜率
    slope_20_prev2 = linear_reg_slope(df['Close'].iloc[:-2], 20)
    
    # 檢查條件
    if (slope_3 > slope_5 and 
        slope_5 > slope_20 and
        slope_3 > slope_3_prev1 and
        slope_3_prev1 > slope_3_prev2 and
        slope_3 > 0.3 and
        slope_20_prev2 < 0.1 and
        slope_20 > 0):
        return True, f"漲勢成形（3日斜率:{slope_3:.2f}, 5日:{slope_5:.2f}, 20日:{slope_20:.2f}）"
    
    return False, ""
