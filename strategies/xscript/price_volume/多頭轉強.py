"""
多頭轉強
Bullish Turning Strong

XScript 原始碼：
{@type:filter}
setbarfreq("AD");

input:length(10, "天期");
variable: sumUp(0), sumDown(0), up(0), down(0),RS(0);

if CurrentBar = 1 then  begin
    sumUp = Average(maxlist(close - close[1], 0), length);
    sumDown = Average(maxlist(close[1] - close, 0), length);
end else begin
    up = maxlist(close - close[1], 0);
    down = maxlist(close[1] - close, 0);
    sumUp = sumUp[1] + (up - sumUp[1]) / length;
    sumDown = sumDown[1] + (down - sumDown[1]) / length;
end;

if sumdown<>0
then rs=sumup/sumdown;

if rs crosses over 4
and close<close[3]*1.06
and Average(Volume[1], 100) >= 500
then ret=1;
"""
import pandas as pd
import numpy as np
from ..utils import crosses_above, maxlist


def 多頭轉強(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
    """
    多頭轉強策略
    
    條件：
    - RS（相對強度）向上穿越 4
    - 最近 3 日漲幅 < 6%
    - 100 日平均成交量 >= 500 張
    
    Args:
        df: 股票歷史資料
        length: 天期（預設 10）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 110:
        return False, "資料不足（需要至少 110 筆）"
    
    close = df['Close']
    volume = df['Volume']
    
    # 計算 RS（簡化版 RSI 計算）
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    # 使用 EMA 計算
    avg_gain = gain.ewm(span=length, adjust=False).mean()
    avg_loss = loss.ewm(span=length, adjust=False).mean()
    
    rs = avg_gain / avg_loss.replace(0, np.nan)
    rs = rs.fillna(0)
    
    # 條件 1: RS 向上穿越 4
    rs_cross = crosses_above(rs, 4)
    
    # 條件 2: 最近 3 日漲幅 < 6%
    current_close = close.iloc[-1]
    close_3_days_ago = close.iloc[-4] if len(close) > 3 else close.iloc[0]
    three_day_gain = (current_close - close_3_days_ago) / close_3_days_ago
    
    # 條件 3: 100 日平均成交量 >= 500
    avg_volume_100 = volume.iloc[-101:-1].mean() if len(volume) > 100 else volume.mean()
    
    if rs_cross and three_day_gain < 0.06 and avg_volume_100 >= 500:
        return True, f"多頭轉強（RS:{rs.iloc[-1]:.2f}, 3日漲幅:{three_day_gain*100:.1f}%）"
    
    return False, ""
