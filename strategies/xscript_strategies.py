import pandas as pd
from data.fetcher import DataFetcher

class XScriptStrategies:
    """
    Strategies translated from XQ XScript.
    """

    @staticmethod
    def price_volume_high(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Strategy: Price and Volume simultaneous N-day high.
        XScript:
        value1=highest(high,period);
        value2=highest(volume,period);
        if high=value1 and volume=value2 then ret=1;
        """
        if df.empty or len(df) < period:
            return False, ""

        high_series = df['High']
        vol_series = df['Volume']
        
        # Check if latest High is the highest in the window
        # Rolling max includes the current row, so we check if current == rolling_max
        current_high = high_series.iloc[-1]
        rolling_max_high = high_series.rolling(window=period).max().iloc[-1]
        
        current_vol = vol_series.iloc[-1]
        rolling_max_vol = vol_series.rolling(window=period).max().iloc[-1]
        
        if current_high >= rolling_max_high and current_vol >= rolling_max_vol:
            return True, f"Price & Volume {period}-Day High"
            
        return False, ""

    @staticmethod
    def momentum_breakout(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: Momentum Breakout (Close > MA20 & MA60, and Volume increase)
        Simplified interpretation of 'Momentum Stock'
        """
        if df.empty or len(df) < 60:
            return False, ""
            
        close = df['Close']
        vol = df['Volume']
        
        ma20 = close.rolling(20).mean().iloc[-1]
        ma60 = close.rolling(60).mean().iloc[-1]
        
        # Volume > 1.5x average volume
        vol_ma5 = vol.rolling(5).mean().iloc[-1]
        
        cond_price = close.iloc[-1] > ma20 and ma20 > ma60
        cond_vol = vol.iloc[-1] > (vol_ma5 * 1.5)
        
        if cond_price and cond_vol:
            return True, "Momentum Breakout (Price > MA20/60 & Vol > 1.5x)"
            
        return False, ""

    @staticmethod
    def red_soldiers(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: 3 Red Soldiers (3 consecutive days up with increasing volume)
        XScript Concept: 連續三日收紅且量增
        """
        if df.empty or len(df) < 3:
            return False, ""
            
        last_3 = df.iloc[-3:]
        
        # Check if all 3 candles are red (Close > Open)
        # Note: In Taiwan, Red = Up, Green = Down. Logic: Close > Open is "Red".
        is_red = (last_3['Close'] > last_3['Open']).all()
        
        # Check if close is strictly increasing
        is_uptrend = (last_3['Close'].diff().iloc[1:] > 0).all()
        
        # Check if volume is generally increasing (last > prev)
        is_vol_up = last_3['Volume'].iloc[-1] > last_3['Volume'].iloc[-2]
        
        if is_red and is_uptrend and is_vol_up:
            return True, "3 Red Soldiers (Consecutive Up & Vol Inc)"
            
        return False, ""

    @staticmethod
    def price_volume_surge(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: 價量齊揚 (Price and Volume Surge)
        邏輯：收盤價創新高 + 成交量放大
        """
        if df.empty or len(df) < 20:
            return False, ""
        
        close = df['Close']
        volume = df['Volume']
        
        # 檢查收盤價是否創 20 日新高
        high_20 = close.rolling(20).max()
        is_price_high = close.iloc[-1] >= high_20.iloc[-1]
        
        # 檢查成交量是否大於 20 日平均的 1.5 倍
        vol_ma20 = volume.rolling(20).mean()
        is_volume_surge = volume.iloc[-1] > (vol_ma20.iloc[-1] * 1.5)
        
        if is_price_high and is_volume_surge:
            return True, "價量齊揚 (Price & Volume Surge)"
        
        return False, ""

    @staticmethod
    def ma_golden_cross(df: pd.DataFrame, fast: int = 5, slow: int = 20) -> tuple[bool, str]:
        """
        Strategy: MA 黃金交叉 (MA Golden Cross)
        邏輯：快線向上穿越慢線
        """
        if df.empty or len(df) < slow:
            return False, ""
        
        close = df['Close']
        ma_fast = close.rolling(fast).mean()
        ma_slow = close.rolling(slow).mean()
        
        # 今日黃金交叉：快線 > 慢線 且 昨日快線 <= 慢線
        if (ma_fast.iloc[-1] > ma_slow.iloc[-1] and 
            ma_fast.iloc[-2] <= ma_slow.iloc[-2]):
            return True, f"MA{fast}/{slow} 黃金交叉 (Golden Cross)"
        
        return False, ""

    @staticmethod
    def macd_golden_cross(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: MACD 黃金交叉 (MACD Golden Cross)
        邏輯：MACD 線向上穿越訊號線
        """
        if df.empty or len(df) < 35:
            return False, ""
        
        close = df['Close']
        
        # 計算 MACD
        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        
        # 今日黃金交叉：MACD > 訊號線 且 昨日 MACD <= 訊號線
        if (macd.iloc[-1] > signal.iloc[-1] and 
            macd.iloc[-2] <= signal.iloc[-2]):
            return True, "MACD 黃金交叉 (MACD Golden Cross)"
        
        return False, ""

    @staticmethod
    def kd_golden_cross(df: pd.DataFrame, period: int = 9) -> tuple[bool, str]:
        """
        Strategy: KD 黃金交叉 (KD Golden Cross)
        邏輯：K 線向上穿越 D 線
        """
        if df.empty or len(df) < period + 3:
            return False, ""
        
        # 計算 KD
        low_min = df['Low'].rolling(window=period).min()
        high_max = df['High'].rolling(window=period).max()
        
        rsv = 100 * ((df['Close'] - low_min) / (high_max - low_min))
        k = rsv.ewm(com=2, adjust=False).mean()
        d = k.ewm(com=2, adjust=False).mean()
        
        # 今日黃金交叉：K > D 且 昨日 K <= D
        if (k.iloc[-1] > d.iloc[-1] and 
            k.iloc[-2] <= d.iloc[-2]):
            return True, "KD 黃金交叉 (KD Golden Cross)"
        
        return False, ""

    @staticmethod
    def volume_breakout(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: 無量變有量 (Volume Breakout)
        邏輯：過去 10 天成交量萎縮，今日成交量放大
        XS 原意: trueall(volume[1]<=v1,10) and volume>v2
        改進: 以前 10 日均量為基準
        """
        if df.empty or len(df) < 20:
            return False, ""
        
        volume = df['Volume']
        
        # 基準：過去 10 天的成交量平均（不含今天）
        vol_avg_10 = volume.iloc[-11:-1].mean()
        
        # 條件 1: 過去 10 天成交量都小於平均的 1.2 倍 (表示相對平穩或低量)
        # 這裡放寬一點，避免太嚴格
        is_low_vol = (volume.iloc[-11:-1] <= vol_avg_10 * 1.2).all()
        
        # 條件 2: 今日成交量大於平均的 2 倍 (明顯放量)
        is_vol_spike = volume.iloc[-1] > (vol_avg_10 * 2.0)
        
        if is_low_vol and is_vol_spike:
            return True, "無量變有量 (Volume Spike)"
        
        return False, ""

    @staticmethod
    def ma_breakout_with_volume(df: pd.DataFrame, ma_period: int = 20) -> tuple[bool, str]:
        """
        Strategy: 帶量突破均線 (Breakout MA with Volume)
        邏輯：收盤價突破 MA，且成交量放大
        """
        if df.empty or len(df) < ma_period + 5:
            return False, ""
        
        close = df['Close']
        volume = df['Volume']
        
        ma = close.rolling(ma_period).mean()
        vol_ma5 = volume.rolling(5).mean()
        
        # 1. 價格突破: 昨日在 MA 下，今日在 MA 上
        is_breakout = (close.iloc[-2] < ma.iloc[-2]) and (close.iloc[-1] > ma.iloc[-1])
        
        # 2. 帶量: 今日成交量 > 5日均量 * 1.5
        is_volume_up = volume.iloc[-1] > (vol_ma5.iloc[-1] * 1.5)
        
        if is_breakout and is_volume_up:
            return True, f"帶量突破 MA{ma_period} (Volumetric Breakout)"
        
        return False, ""

    @staticmethod
    def w_bottom(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: W底型態 (W-Bottom / Double Bottom)
        邏輯 (簡化版):
        1. 最近 20-60 天內有兩個明顯低點
        2. 兩個低點接近
        3. 今日突破頸線 (兩個低點中間的高點)
        """
        if df.empty or len(df) < 60:
            return False, ""
        
        # 取近 60 天資料
        recent = df.iloc[-60:]
        close = recent['Close'].values
        
        # 尋找與今日收盤價接近的低點 (簡單 heuristic)
        # 這裡實作一個簡化的 W 底偵測：
        # 尋找兩個局部最小值
        
        # 為了效能與簡化，我們檢查特定型態特徵：
        # 1. 當前價格突破近 20 日高點
        # 2. 在這之前有兩個低點區間
        
        # 使用 Scipy 或詳細演算法可能太慢，我們用 rolling min 來近似
        # 近 5 日創新高 (突破頸線的跡象)
        if close[-1] < max(close[-20:]):
            return False, ""
            
        # 檢查過去是否有兩個低腳
        # 將數據分成兩段尋找低點 (例如 -40~-20 和 -20~-5)
        mid_idx = 20
        period1 = close[-40:-20]
        period2 = close[-20:-5]
        
        if len(period1) < 10 or len(period2) < 10:
            return False, ""

        min1 = min(period1)
        min2 = min(period2)
        
        # 頸線 (兩低點間的最高點)
        # neck_high = max(close[-40:-5])
        
        # 兩個低點差異在 3% 以內
        is_double_bottom = abs(min1 - min2) / min1 < 0.03
        
        # 且今日價格剛突破頸線 (或是近期高點)
        # 這裡假設突破近期高點視為潛在 W 底完成
        
        if is_double_bottom:
             return True, "W底型態 (W-Bottom Potential)"
             
        return False, ""

    @staticmethod
    def head_and_shoulders_bottom(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Strategy: 頭肩底 (Head and Shoulders Bottom)
        邏輯 (簡化版): 
        左肩(Low) -> 頭(Lower Low) -> 右肩(Higher Low) -> 突破頸線
        """
        if df.empty or len(df) < 60:
            return False, ""
            
        # 取近 60 天
        close = df['Close'].iloc[-60:].values
        
        # 分割區間尋找 左肩, 頭, 右肩
        # 假設分佈在三個區段
        n = len(close)
        p1 = close[:n//3]        # 左肩區
        p2 = close[n//3:2*n//3]  # 頭部區
        p3 = close[2*n//3:-1]    # 右肩區
        
        if len(p1) < 5 or len(p2) < 5 or len(p3) < 5:
            return False, ""
            
        min1 = min(p1) # 左肩低點
        min2 = min(p2) # 頭部低點
        min3 = min(p3) # 右肩低點
        
        # 特徵 1: 頭部最低
        is_head_lowest = min2 < min1 and min2 < min3
        
        # 特徵 2: 右肩與左肩高度差異不大 (例如 10%)
        is_shoulder_level = abs(min1 - min3) / min1 < 0.1
        
        # 特徵 3: 今日價格突破 (比右肩高，且接近或突破區間高點)
        current_price = close[-1]
        is_breakout = current_price > max(p3)
        
        if is_head_lowest and is_shoulder_level and is_breakout:
            return True, "頭肩底型態 (Head & Shoulders Bottom)"
            
        return False, ""
