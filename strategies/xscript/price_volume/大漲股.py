"""
大漲股
Big Gainer

XScript 原始碼：
{@type:filter}
condition1=false;
condition2=false;
condition3=false;

//先把簡單的價量條件全部放在condition1
if highest(high,3)<lowest(low,3)*1.15
//區間震盪小於15%
and close>5
//股價大於5元
and close<200
//股價小於200元
and volume>300
//當日成交量大於300張
and high=highest(high,2)
//創兩日來新高
and close>close[1]*1.02
//最近一日上漲超過2%
then condition1=true;

//用condition2來處理月線斜率大於0.4
value1=average(close,20);
//先算出月線
value2=linearregslope(value1,10);
//算出月線這十天的斜率
if value2>0.4 then condition2=true;
//月線斜率要大於0.4

//處理布林帶寬
input:length(20,"計算天期");
input:width(35,"帶寬%");
variable:up1(0),down1(0),mid1(0),bbandwidth(0);
up1 = bollingerband(Close, Length, 1);
down1 = bollingerband(Close, Length, -1 );
mid1 = (up1 + down1) / 2;

bbandwidth = 100 * (up1 - down1) / mid1;
if bbandwidth <width
then condition3=true;

ret=condition1 and condition2 and condition3;
"""
import pandas as pd
from ..utils import highest, lowest, linear_reg_slope, average


def 大漲股(df: pd.DataFrame, length: int = 20, width: int = 35) -> tuple[bool, str]:
    """
    大漲股策略
    
    條件：
    - 價量條件：區間震盪<15%, 5<股價<200, 成交量>300, 創2日新高, 日漲幅>2%
    - 月線斜率 > 0.4
    - 布林帶寬 < width%
    
    Args:
        df: 股票歷史資料
        length: 布林通道期數（預設 20）
        width: 帶寬%（預設 35）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 30:
        return False, "資料不足（需要至少 30 筆）"
    
    close = df['Close']
    high = df['High']
    low = df['Low']
    volume = df['Volume']
    
    # 條件 1: 價量條件
    highest_3 = highest(high, 3)
    lowest_3 = lowest(low, 3)
    current_close = close.iloc[-1]
    current_high = high.iloc[-1]
    current_volume = volume.iloc[-1]
    prev_close = close.iloc[-2]
    highest_2 = highest(high, 2)
    
    condition1 = (
        highest_3 < lowest_3 * 1.15 and
        current_close > 5 and
        current_close < 200 and
        current_volume > 300 and
        current_high == highest_2 and
        current_close > prev_close * 1.02
    )
    
    # 條件 2: 月線斜率 > 0.4
    ma20 = close.rolling(window=20).mean()
    ma20_slope = linear_reg_slope(ma20, 10)
    condition2 = ma20_slope > 0.4
    
    # 條件 3: 布林帶寬 < width%
    std = close.rolling(window=length).std()
    ma = close.rolling(window=length).mean()
    upper = ma + 2 * std
    lower = ma - 2 * std
    mid = (upper + lower) / 2
    bbandwidth = 100 * (upper - lower) / mid
    condition3 = bbandwidth.iloc[-1] < width
    
    if condition1 and condition2 and condition3:
        return True, f"大漲股（月線斜率:{ma20_slope:.2f}, 布林帶寬:{bbandwidth.iloc[-1]:.1f}%）"
    
    return False, ""
