"""
特定日期迄今漲跌幅超過一定幅度
特定日期迄今漲跌幅超過一定幅度

TODO: 需要實作此策略的邏輯
"""
import pandas as pd
from strategies.xscript.utils import *


def 特定日期迄今漲跌幅超過一定幅度(df: pd.DataFrame) -> tuple[bool, str]:
    """
    特定日期迄今漲跌幅超過一定幅度策略
    
    Args:
        df: 股票歷史資料
        
    Returns:
        (is_signal, message): 是否符合條件及訊息
    """
    # TODO: 實作策略邏輯
    # 1. 檢查資料長度
    # 2. 計算指標
    # 3. 檢查條件
    # 4. 返回結果
    
    return False, "策略尚未實作"
