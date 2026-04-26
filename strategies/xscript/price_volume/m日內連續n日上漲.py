"""
M日內連續N日上漲
N Consecutive Up Days Within M Days

XScript 原始碼：
{@type:filter}
input:day(11);
input:m1(3);
setinputname(1,"計算天期");
setinputname(2,"連續上漲天數");

variable:x(0),count(0);
count=0;
for x=0 to day-m1 
begin
if close[x]>close[x+1]
and close[x+1]>close[x+2]
and close[x+2]>close[x+3]
then count=count+1;
end;
if count>=1
then ret=1;
"""
import pandas as pd


def m日內連續n日上漲(df: pd.DataFrame, day: int = 11, m1: int = 3) -> tuple[bool, str]:
    """
    M日內連續N日上漲策略
    
    條件：
    - 在過去 M 日內，至少有一次連續 N 日上漲
    
    Args:
        df: 股票歷史資料
        day: 計算天期（預設 11）
        m1: 連續上漲天數（預設 3）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < day + m1:
        return False, f"資料不足（需要至少 {day + m1} 筆）"
    
    close = df['Close']
    count = 0
    
    # 檢查過去 day 日內是否有連續 m1 日上漲
    for x in range(day - m1 + 1):
        # 檢查連續 m1 日上漲
        is_consecutive_up = True
        for i in range(m1):
            if close.iloc[-(x+i+1)] <= close.iloc[-(x+i+2)]:
                is_consecutive_up = False
                break
        
        if is_consecutive_up:
            count += 1
    
    if count >= 1:
        return True, f"{day}日內有{count}次連續{m1}日上漲"
    
    return False, ""
