"""
漲勢加速
Uptrend Accelerating

XScript 原始碼：
{@type:filter}
setbarfreq("AD");

variable:aspeed(0),dspeed(0),a1(0),d1(0),p1(0),ap1(0);
if close>close[1] then aspeed=(close-close[1])/close*100
else aspeed=0;
if close<close[1] then dspeed=(close[1]-close)/close*100
else dspeed=0;

a1=average(aspeed,5);
d1=average(dspeed,5);

p1=a1-d1;
ap1=average(p1,9);

if p1 crosses over ap1
and rsi(close,6)<=75
and close*1.3<close[30]

then ret=1;
"""
import pandas as pd
import numpy as np
from ..utils import crosses_above, average


def 漲勢加速(df: pd.DataFrame) -> tuple[bool, str]:
    """
    漲勢加速策略
    
    條件：
    - 計算上漲速度和下跌速度
    - 動能指標 p1 向上穿越其 9 日均線
    - RSI(6) <= 75
    - 當前價格 * 1.3 < 30日前價格（漲幅未過大）
    
    Args:
        df: 股票歷史資料
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 40:
        return False, "資料不足（需要至少 40 筆）"
    
    # 計算上漲速度和下跌速度
    close = df['Close']
    aspeed = np.where(close > close.shift(1), (close - close.shift(1)) / close * 100, 0)
    dspeed = np.where(close < close.shift(1), (close.shift(1) - close) / close * 100, 0)
    
    # 轉換為 Series
    aspeed_series = pd.Series(aspeed, index=df.index)
    dspeed_series = pd.Series(dspeed, index=df.index)
    
    # 計算 5 日平均
    a1 = aspeed_series.rolling(window=5).mean()
    d1 = dspeed_series.rolling(window=5).mean()
    
    # 計算動能指標
    p1 = a1 - d1
    ap1 = p1.rolling(window=9).mean()
    
    # 計算 RSI(6)
    delta = close.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=6).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=6).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    # 檢查條件
    current_close = close.iloc[-1]
    close_30_days_ago = close.iloc[-31] if len(close) > 30 else close.iloc[0]
    
    if (crosses_above(p1, ap1) and 
        rsi.iloc[-1] <= 75 and
        current_close * 1.3 < close_30_days_ago):
        return True, f"漲勢加速（RSI:{rsi.iloc[-1]:.1f}, 動能向上穿越）"
    
    return False, ""
