"""
N年來漲了M倍的公司
N-Year M-Times Gainer

XScript 原始碼：
{@type:filter}
input:y1(10,"計算的年數");
input:ratio(800,"上漲的倍數%");

value1=rateofchange(GetField("收盤價","AM"),y1*12);

if value1>=ratio
then ret=1;
"""
import pandas as pd


def n年來漲了m倍的公司(df: pd.DataFrame, y1: int = 10, ratio: int = 800) -> tuple[bool, str]:
    """
    N年來漲了M倍的公司策略
    
    條件：
    - N 年漲幅 >= ratio%
    
    Args:
        df: 股票歷史資料
        y1: 計算的年數（預設 10）
        ratio: 上漲的倍數%（預設 800，即 8 倍）
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    days_needed = y1 * 252  # 假設一年 252 個交易日
    
    if len(df) < days_needed:
        return False, f"資料不足（需要至少 {y1} 年資料）"
    
    close = df['Close']
    
    # 計算 N 年漲幅
    current_close = close.iloc[-1]
    n_years_ago_close = close.iloc[-days_needed] if len(close) >= days_needed else close.iloc[0]
    
    roc = ((current_close - n_years_ago_close) / n_years_ago_close * 100)
    
    if roc >= ratio:
        times = (roc / 100) + 1
        return True, f"{y1}年漲{times:.1f}倍（漲幅:{roc:.1f}%）"
    
    return False, ""
