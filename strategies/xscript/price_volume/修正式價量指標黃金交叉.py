"""
修正式價量指標黃金交叉
Modified Price-Volume Indicator Golden Cross

XScript 原始碼：
{@type:filter}
setbarfreq("AD");

input:day(10, "移動平均線天數");

variable:tvp(0),mpc(0);
mpc=(open+high+low+close)/4;

if mpc[1]<>0
then tvp=tvp[1]+(mpc-mpc[1])/mpc[1]*volume
else tvp=tvp[1];

value1=average(tvp,day);
If tvp crosses over value1 and volume>1000
and tvp>value1*1.05
then ret=1;
"""
import pandas as pd
from ..utils import crosses_above


def 修正式價量指標黃金交叉(df: pd.DataFrame, day: int = 10) -> tuple[bool, str]:
    """
    修正式價量指標黃金交叉策略
    
    條件：
    - TVP（總價量）向上穿越其移動平均線
    - 成交量 > 1000
    - TVP > 均線 * 1.05
    
    Args:
        df: 股票歷史資料
        day: 移動平均線天數（預設 10）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < day + 5:
        return False, f"資料不足（需要至少 {day + 5} 筆）"
    
    # 計算中間價格
    mpc = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    volume = df['Volume']
    
    # 計算 TVP（總價量指標）
    tvp = pd.Series(0.0, index=df.index)
    for i in range(1, len(df)):
        if mpc.iloc[i-1] != 0:
            tvp.iloc[i] = tvp.iloc[i-1] + (mpc.iloc[i] - mpc.iloc[i-1]) / mpc.iloc[i-1] * volume.iloc[i]
        else:
            tvp.iloc[i] = tvp.iloc[i-1]
    
    # 計算 TVP 的移動平均
    tvp_ma = tvp.rolling(window=day).mean()
    
    # 檢查條件
    current_volume = volume.iloc[-1]
    current_tvp = tvp.iloc[-1]
    current_ma = tvp_ma.iloc[-1]
    
    if (crosses_above(tvp, tvp_ma) and 
        current_volume > 1000 and
        current_tvp > current_ma * 1.05):
        return True, f"價量指標黃金交叉（TVP:{current_tvp:.0f}, MA:{current_ma:.0f}）"
    
    return False, ""
