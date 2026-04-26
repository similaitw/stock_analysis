"""
五日週轉率大於二十日週轉率
5-Day Turnover Rate Greater Than 20-Day

XScript 原始碼：
{@type:filter}
if turnoverrate(5)>turnoverrate(20)
then ret=1;
outputfield(1,turnoverrate(5),1,"5日平均週轉率");
outputfield(2,turnoverrate(20),1,"20日平均週轉率");
"""
import pandas as pd


def 五日週轉率大於二十日週轉率(df: pd.DataFrame) -> tuple[bool, str]:
    """
    五日週轉率大於二十日週轉率策略
    
    條件：
    - 5 日平均週轉率 > 20 日平均週轉率
    
    Args:
        df: 股票歷史資料
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    if len(df) < 20:
        return False, "資料不足（需要至少 20 筆）"
    
    volume = df['Volume']
    
    # 計算週轉率（簡化：使用成交量比率）
    # 實際週轉率 = 成交量 / 流通股數，這裡簡化為成交量平均
    turnover_5 = volume.iloc[-5:].mean()
    turnover_20 = volume.iloc[-20:].mean()
    
    if turnover_5 > turnover_20:
        ratio = (turnover_5 / turnover_20 - 1) * 100
        return True, f"5日週轉率>{20日週轉率}（高{ratio:.1f}%）"
    
    return False, ""
