"""
波動幅度開始變大且往上攻
Volatility Increasing with Upward Breakout

XScript 原始碼：
{@type:filter}
SetBarFreq("AD");

input: Length(20, "計算區間");
input: VolLimit(1000, "成交量限制");

value1 = truerange();
value2 = highest(value1,Length);

SetTotalBar(Length + 3);

if value1 > value2[1] and value1 > value1[1] and close * 1.01 > high and 
   close > close[1] and volume > VolLimit
then ret=1;
"""
import pandas as pd
from ..utils import highest


def 波動幅度開始變大且往上攻(df: pd.DataFrame, length: int = 20, vol_limit: int = 1000) -> tuple[bool, str]:
    """
    波動幅度開始變大且往上攻策略
    
    條件：
    - 真實波幅 > 前一日的 N 日最高波幅
    - 真實波幅 > 前一日波幅
    - 收盤價接近最高價（close * 1.01 > high）
    - 收盤 > 前收
    - 成交量 > 限制
    
    Args:
        df: 股票歷史資料
        length: 計算區間（預設 20）
        vol_limit: 成交量限制（預設 1000）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < length + 3:
        return False, f"資料不足（需要至少 {length + 3} 筆）"
    
    high = df['High']
    low = df['Low']
    close = df['Close']
    volume = df['Volume']
    
    # 計算真實波幅 (True Range)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    
    # 當前真實波幅
    current_tr = tr.iloc[-1]
    prev_tr = tr.iloc[-2]
    
    # 前一日的 N 日最高波幅
    tr_series = pd.Series(tr.iloc[:-1])
    highest_tr_prev = highest(tr_series, length)
    
    # 檢查條件
    current_close = close.iloc[-1]
    prev_close = close.iloc[-2]
    current_high = high.iloc[-1]
    current_volume = volume.iloc[-1]
    
    if (current_tr > highest_tr_prev and
        current_tr > prev_tr and
        current_close * 1.01 > current_high and
        current_close > prev_close and
        current_volume > vol_limit):
        return True, f"波動變大往上攻（波幅:{current_tr:.2f}, 成交量:{current_volume:.0f}）"
    
    return False, ""
