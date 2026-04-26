"""
Multi-Indicator Technical Strategies
Combination of multiple technical indicators for stronger signals
"""
import pandas as pd
import numpy as np
from typing import Tuple

def 多頭排列(df: pd.DataFrame, **kwargs) -> Tuple[bool, str]:
    """
    MA5 > MA20 > MA60 多頭排列
    
    Args:
        df: 股價資料
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < 60:
        return False, ""
    
    try:
        close = df['Close']
        ma5 = close.rolling(5).mean()
        ma20 = close.rolling(20).mean()
        ma60 = close.rolling(60).mean()
        
        # 檢查最新一日
        if ma5.iloc[-1] > ma20.iloc[-1] > ma60.iloc[-1]:
            return True, "多頭排列"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"


def MACD_KD雙金叉(df: pd.DataFrame, **kwargs) -> Tuple[bool, str]:
    """
    MACD 和 KD 同時金叉
    
    Args:
        df: 股價資料
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < 30:
        return False, ""
    
    try:
        close = df['Close']
        high = df['High']
        low = df['Low']
        
        # MACD 計算
        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        
        # MACD 金叉判斷
        macd_cross = (macd.iloc[-1] > signal.iloc[-1] and 
                      macd.iloc[-2] <= signal.iloc[-2])
        
        # KD 計算
        low_9 = low.rolling(9).min()
        high_9 = high.rolling(9).max()
        rsv = (close - low_9) / (high_9 - low_9) * 100
        k = rsv.ewm(com=2, adjust=False).mean()
        d = k.ewm(com=2, adjust=False).mean()
        
        # KD 金叉判斷
        kd_cross = (k.iloc[-1] > d.iloc[-1] and 
                    k.iloc[-2] <= d.iloc[-2])
        
        if macd_cross and kd_cross:
            return True, "MACD+KD雙金叉"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"


def 布林通道突破(df: pd.DataFrame, period: int = 20, std_dev: float = 2.0, **kwargs) -> Tuple[bool, str]:
    """
    價格突破布林通道上軌
    
    Args:
        df: 股價資料
        period: 布林通道週期
        std_dev: 標準差倍數
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < period + 5:
        return False, ""
    
    try:
        close = df['Close']
        
        # 布林通道計算
        sma = close.rolling(period).mean()
        std = close.rolling(period).std()
        upper_band = sma + (std * std_dev)
        lower_band = sma - (std * std_dev)
        
        # 突破上軌判斷
        if close.iloc[-1] > upper_band.iloc[-1] and close.iloc[-2] <= upper_band.iloc[-2]:
            return True, f"突破布林上軌 ({close.iloc[-1]:.2f})"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"


def RSI背離(df: pd.DataFrame, period: int = 14, **kwargs) -> Tuple[bool, str]:
    """
    RSI 底背離 (價格創新低但RSI未創新低)
    
    Args:
        df: 股價資料
        period: RSI週期
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < period * 3:
        return False, ""
    
    try:
        close = df['Close']
        
        # RSI 計算
        delta = close.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        # 檢查最近20天的低點
        recent_window = 20
        if len(close) < recent_window:
            return False, ""
        
        recent_close = close.tail(recent_window)
        recent_rsi = rsi.tail(recent_window)
        
        # 找出價格低點
        price_low_idx = recent_close.idxmin()
        price_low = recent_close.min()
        
        # 找出RSI低點
        rsi_low_idx = recent_rsi.idxmin()
        rsi_low = recent_rsi.min()
        
        # 底背離: 價格創新低但RSI未創新低
        if price_low_idx > rsi_low_idx and price_low < recent_close.iloc[0]:
            return True, f"RSI底背離 (RSI:{rsi.iloc[-1]:.1f})"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"


def 量價齊揚突破(df: pd.DataFrame, ma_period: int = 20, volume_multiplier: float = 1.5, **kwargs) -> Tuple[bool, str]:
    """
    價格突破均線且成交量放大
    
    Args:
        df: 股價資料
        ma_period: 均線週期
        volume_multiplier: 成交量倍數
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < ma_period + 5:
        return False, ""
    
    try:
        close = df['Close']
        volume = df['Volume']
        
        # 計算均線和平均成交量
        ma = close.rolling(ma_period).mean()
        avg_volume = volume.rolling(ma_period).mean()
        
        # 價格突破均線
        price_breakout = (close.iloc[-1] > ma.iloc[-1] and 
                         close.iloc[-2] <= ma.iloc[-2])
        
        # 成交量放大
        volume_surge = volume.iloc[-1] > avg_volume.iloc[-1] * volume_multiplier
        
        if price_breakout and volume_surge:
            vol_ratio = volume.iloc[-1] / avg_volume.iloc[-1]
            return True, f"量價齊揚突破MA{ma_period} (量{vol_ratio:.1f}倍)"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"


def 三線合一(df: pd.DataFrame, **kwargs) -> Tuple[bool, str]:
    """
    均線、均量線、MACD 三線同步向上
    
    Args:
        df: 股價資料
    
    Returns:
        (is_match, reason)
    """
    if df.empty or len(df) < 30:
        return False, ""
    
    try:
        close = df['Close']
        volume = df['Volume']
        
        # 均線向上
        ma5 = close.rolling(5).mean()
        ma_up = ma5.iloc[-1] > ma5.iloc[-5]
        
        # 均量線向上
        vol_ma5 = volume.rolling(5).mean()
        vol_up = vol_ma5.iloc[-1] > vol_ma5.iloc[-5]
        
        # MACD 向上
        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        macd_up = macd.iloc[-1] > macd.iloc[-5]
        
        if ma_up and vol_up and macd_up:
            return True, "三線合一向上"
        
        return False, ""
    except Exception as e:
        return False, f"錯誤: {str(e)}"
