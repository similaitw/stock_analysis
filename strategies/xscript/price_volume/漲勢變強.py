"""
漲勢變強
Uptrend Strengthening

XScript 原始碼：
{@type:filter}
input: Length(100);
input: RRatio(100);

settotalbar(3);

variable: Scores(0);

if Close > Open and Close > Close[2]*1.07  {紅棒且累計三天漲幅大於7%}
   and Close < Close[Length]*(1+RRatio/100)  {累計漲幅不超過%}
then 
  begin
        scores = countif(close > close[1], length);
        If scores >= Length / 2 then ret=1;
  end;
"""
import pandas as pd
from ..utils import count_condition


def 漲勢變強(df: pd.DataFrame, length: int = 100, r_ratio: int = 100) -> tuple[bool, str]:
    """
    漲勢變強策略
    
    條件：
    - 收盤 > 開盤（紅棒）
    - 累計三天漲幅 > 7%
    - 累計 N 日漲幅 < RRatio%
    - 過去 N 日中，上漲天數 >= N/2
    
    Args:
        df: 股票歷史資料
        length: 計算期數（預設 100）
        r_ratio: 盤漲最大漲幅%（預設 100）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < max(length, 3):
        return False, f"資料不足（需要至少 {max(length, 3)} 筆）"
    
    current_close = df['Close'].iloc[-1]
    current_open = df['Open'].iloc[-1]
    close_2_days_ago = df['Close'].iloc[-3]
    close_n_days_ago = df['Close'].iloc[-length-1] if len(df) > length else df['Close'].iloc[0]
    
    # 條件 1: 紅棒
    is_red_candle = current_close > current_open
    
    # 條件 2: 累計三天漲幅 > 7%
    three_day_gain = (current_close - close_2_days_ago) / close_2_days_ago
    
    # 條件 3: 累計 N 日漲幅 < RRatio%
    n_day_gain = (current_close - close_n_days_ago) / close_n_days_ago
    
    if not (is_red_candle and three_day_gain > 0.07 and n_day_gain < (r_ratio / 100)):
        return False, ""
    
    # 條件 4: 計算過去 N 日中上漲天數
    close_series = df['Close'].iloc[-length:]
    up_days = (close_series > close_series.shift(1)).sum()
    
    if up_days >= length / 2:
        return True, f"漲勢變強（3日漲幅:{three_day_gain*100:.1f}%, {length}日內上漲{up_days}天）"
    
    return False, ""
