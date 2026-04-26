"""
XScript 共用工具函數
XScript Utility Functions

提供 XScript 語法中常用的函數實作
"""
import pandas as pd
import numpy as np
from typing import Union, List


def trueall(condition: Union[pd.Series, bool], period: int) -> bool:
    """
    檢查條件在過去 N 期是否全部為真
    XScript: trueall(condition, period)
    
    Args:
        condition: 條件序列或布林值
        period: 檢查期數
        
    Returns:
        bool: 是否全部為真
    """
    if isinstance(condition, bool):
        return condition
    
    if isinstance(condition, pd.Series):
        if len(condition) < period:
            return False
        return condition.iloc[-period:].all()
    
    return False


def trueany(condition: Union[pd.Series, bool], period: int) -> bool:
    """
    檢查條件在過去 N 期是否有任何一期為真
    XScript: trueany(condition, period)
    
    Args:
        condition: 條件序列或布林值
        period: 檢查期數
        
    Returns:
        bool: 是否有任何一期為真
    """
    if isinstance(condition, bool):
        return condition
    
    if isinstance(condition, pd.Series):
        if len(condition) < period:
            return False
        return condition.iloc[-period:].any()
    
    return False


def linear_reg_slope(series: pd.Series, period: int) -> float:
    """
    計算線性回歸斜率
    XScript: linearregslope(series, period)
    
    Args:
        series: 資料序列
        period: 計算期數
        
    Returns:
        float: 線性回歸斜率
    """
    if len(series) < period:
        return 0.0
    
    y = series.iloc[-period:].values
    x = np.arange(period)
    
    # 使用最小二乘法計算斜率
    slope = np.polyfit(x, y, 1)[0]
    return slope


def crosses_above(series1: pd.Series, series2: Union[pd.Series, float]) -> bool:
    """
    檢查 series1 是否向上穿越 series2
    XScript: series1 Crosses Above series2
    
    Args:
        series1: 序列1
        series2: 序列2 或數值
        
    Returns:
        bool: 是否向上穿越
    """
    if len(series1) < 2:
        return False
    
    current = series1.iloc[-1]
    previous = series1.iloc[-2]
    
    if isinstance(series2, (int, float)):
        threshold = series2
        prev_threshold = series2
    else:
        if len(series2) < 2:
            return False
        threshold = series2.iloc[-1]
        prev_threshold = series2.iloc[-2]
    
    # 前一期在下方，當前期在上方
    return previous <= prev_threshold and current > threshold


def crosses_below(series1: pd.Series, series2: Union[pd.Series, float]) -> bool:
    """
    檢查 series1 是否向下穿越 series2
    XScript: series1 Crosses Below series2
    
    Args:
        series1: 序列1
        series2: 序列2 或數值
        
    Returns:
        bool: 是否向下穿越
    """
    if len(series1) < 2:
        return False
    
    current = series1.iloc[-1]
    previous = series1.iloc[-2]
    
    if isinstance(series2, (int, float)):
        threshold = series2
        prev_threshold = series2
    else:
        if len(series2) < 2:
            return False
        threshold = series2.iloc[-1]
        prev_threshold = series2.iloc[-2]
    
    # 前一期在上方，當前期在下方
    return previous >= prev_threshold and current < threshold


def highest(series: pd.Series, period: int) -> float:
    """
    取得過去 N 期的最高值
    XScript: highest(series, period)
    
    Args:
        series: 資料序列
        period: 期數
        
    Returns:
        float: 最高值
    """
    if len(series) < period:
        return series.max() if len(series) > 0 else 0.0
    
    return series.iloc[-period:].max()


def lowest(series: pd.Series, period: int) -> float:
    """
    取得過去 N 期的最低值
    XScript: lowest(series, period)
    
    Args:
        series: 資料序列
        period: 期數
        
    Returns:
        float: 最低值
    """
    if len(series) < period:
        return series.min() if len(series) > 0 else 0.0
    
    return series.iloc[-period:].min()


def average(series: pd.Series, period: int) -> float:
    """
    計算簡單移動平均
    XScript: average(series, period)
    
    Args:
        series: 資料序列
        period: 期數
        
    Returns:
        float: 平均值
    """
    if len(series) < period:
        return series.mean() if len(series) > 0 else 0.0
    
    return series.iloc[-period:].mean()


def summation(series: pd.Series, period: int) -> float:
    """
    計算過去 N 期的總和
    XScript: summation(series, period)
    
    Args:
        series: 資料序列
        period: 期數
        
    Returns:
        float: 總和
    """
    if len(series) < period:
        return series.sum() if len(series) > 0 else 0.0
    
    return series.iloc[-period:].sum()


def count_condition(condition: pd.Series, period: int) -> int:
    """
    計算過去 N 期中條件為真的次數
    
    Args:
        condition: 條件序列
        period: 期數
        
    Returns:
        int: 為真的次數
    """
    if len(condition) < period:
        return condition.sum() if len(condition) > 0 else 0
    
    return condition.iloc[-period:].sum()


def maxlist(*values) -> float:
    """
    取得多個值中的最大值
    XScript: maxlist(v1, v2, v3, ...)
    
    Returns:
        float: 最大值
    """
    return max(values)


def minlist(*values) -> float:
    """
    取得多個值中的最小值
    XScript: minlist(v1, v2, v3, ...)
    
    Returns:
        float: 最小值
    """
    return min(values)


def weighted_close(df: pd.DataFrame) -> pd.Series:
    """
    計算加權收盤價
    XScript: weightedclose()
    
    公式: (High + Low + Close * 2) / 4
    
    Args:
        df: 包含 High, Low, Close 的 DataFrame
        
    Returns:
        pd.Series: 加權收盤價序列
    """
    return (df['High'] + df['Low'] + df['Close'] * 2) / 4


def typical_price(df: pd.DataFrame) -> pd.Series:
    """
    計算典型價格
    XScript: typicalprice()
    
    公式: (High + Low + Close) / 3
    
    Args:
        df: 包含 High, Low, Close 的 DataFrame
        
    Returns:
        pd.Series: 典型價格序列
    """
    return (df['High'] + df['Low'] + df['Close']) / 3
