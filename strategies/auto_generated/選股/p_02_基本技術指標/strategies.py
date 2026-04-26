# Auto-generated strategies for: 選股/02.基本技術指標
import pandas as pd
import numpy as np


def _calc_rsi(close: pd.Series, length: int = 14) -> pd.Series:
    """計算 RSI 指標 (Relative Strength Index)"""
    delta = close.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.ewm(com=length - 1, adjust=False).mean()
    avg_loss = loss.ewm(com=length - 1, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def _calc_stochastic(high: pd.Series, low: pd.Series, close: pd.Series,
                     length: int = 9, smooth_k: int = 3, smooth_d: int = 3) -> tuple[pd.Series, pd.Series]:
    """計算 KD (Stochastic Oscillator)"""
    lowest_low = low.rolling(window=length).min()
    highest_high = high.rolling(window=length).max()
    denom = (highest_high - lowest_low).replace(0, np.nan)
    rsv = 100 * (close - lowest_low) / denom
    k = rsv.ewm(com=smooth_k - 1, adjust=False).mean()
    d = k.ewm(com=smooth_d - 1, adjust=False).mean()
    return k, d


def _calc_macd(close: pd.Series, fast: int = 12, slow: int = 26,
               signal: int = 9) -> tuple[pd.Series, pd.Series, pd.Series]:
    """計算 MACD"""
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    dif = ema_fast - ema_slow
    macd_signal = dif.ewm(span=signal, adjust=False).mean()
    osc = dif - macd_signal
    return dif, macd_signal, osc


def _calc_bollinger(close: pd.Series, length: int = 20,
                    std_mult: float = 2.0) -> tuple[pd.Series, pd.Series, pd.Series]:
    """計算布林通道 (Bollinger Bands)"""
    mid = close.rolling(window=length).mean()
    std = close.rolling(window=length).std(ddof=0)
    upper = mid + std_mult * std
    lower = mid - std_mult * std
    return upper, mid, lower


def _calc_cci(high: pd.Series, low: pd.Series, close: pd.Series,
              length: int = 14) -> pd.Series:
    """計算 CCI (Commodity Channel Index)"""
    typical = (high + low + close) / 3
    ma = typical.rolling(window=length).mean()
    mad = typical.rolling(window=length).apply(lambda x: np.mean(np.abs(x - x.mean())), raw=True)
    return (typical - ma) / (0.015 * mad.replace(0, np.nan))


def _crosses_above(a: pd.Series, b: pd.Series) -> pd.Series:
    """判斷 a 是否在最後一根 K 線往上穿越 b"""
    return (a.iloc[-1] > b.iloc[-1]) & (a.iloc[-2] <= b.iloc[-2])


def _crosses_below(a: pd.Series, b: pd.Series) -> pd.Series:
    """判斷 a 是否在最後一根 K 線往下穿越 b"""
    return (a.iloc[-1] < b.iloc[-1]) & (a.iloc[-2] >= b.iloc[-2])


class Cat02基本技術指標Strategies:

    @staticmethod
    def BBand出現買進訊號(df: pd.DataFrame, length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: BBand出現買進訊號
        XS Logic Reference:
        up1 = bollingerband(Close, Length, 1);
        down1 = bollingerband(Close, Length, -1);
        mid1 = (up1 + down1) / 2;
        bbandwidth = 100 * (up1 - down1) / mid1;
        if bbandwidth crosses above 5 and close > up1 and close > up1[1]
        and average(close,20) > average(close,20)[1]
        then ret=1;
        """
        if df.empty or len(df) < length + 2:
            return False, ""
        close = df['Close']
        upper, mid, lower = _calc_bollinger(close, length)
        bwidth = 100 * (upper - lower) / mid.replace(0, np.nan)

        # Bandwidth crosses above 5
        bw_cross = (bwidth.iloc[-1] > 5) and (bwidth.iloc[-2] <= 5)
        # Close above upper band (today and yesterday)
        close_above = close.iloc[-1] > upper.iloc[-1] and close.iloc[-2] > upper.iloc[-2]
        # MA20 rising
        ma20_rising = mid.iloc[-1] > mid.iloc[-2]

        if bw_cross and close_above and ma20_rising:
            bw_now = bwidth.iloc[-1]
            return True, f"布林通道擴張突破 (BWidth={bw_now:.1f}%, Close={close.iloc[-1]:.2f} > Upper={upper.iloc[-1]:.2f})"
        return False, ""

    @staticmethod
    def CCI超買(df: pd.DataFrame, Length: int = 14, AvgLength: int = 5, OverBought: float = 100.0) -> tuple[bool, str]:
        """
        Original Strategy: CCI超買
        CCI MA 穿越超買線 (OverBought)
        """
        if df.empty or len(df) < Length + AvgLength + 2:
            return False, ""
        cci = _calc_cci(df['High'], df['Low'], df['Close'], Length)
        cci_ma = cci.rolling(window=AvgLength).mean()

        if _crosses_above(cci_ma, pd.Series([OverBought] * len(cci_ma), index=cci_ma.index)):
            return True, f"CCI({Length}) MA({AvgLength}) 穿越超買線 ({OverBought:.0f}), CCI={cci.iloc[-1]:.1f}"
        return False, ""

    @staticmethod
    def CCI超賣(df: pd.DataFrame, Length: int = 14, AvgLength: int = 5, OverSold: float = -100.0) -> tuple[bool, str]:
        """
        Original Strategy: CCI超賣
        CCI MA 跌破超賣線 (OverSold)
        """
        if df.empty or len(df) < Length + AvgLength + 2:
            return False, ""
        cci = _calc_cci(df['High'], df['Low'], df['Close'], Length)
        cci_ma = cci.rolling(window=AvgLength).mean()

        if _crosses_below(cci_ma, pd.Series([OverSold] * len(cci_ma), index=cci_ma.index)):
            return True, f"CCI({Length}) MA({AvgLength}) 跌破超賣線 ({OverSold:.0f}), CCI={cci.iloc[-1]:.1f}"
        return False, ""

    @staticmethod
    def KD死亡交叉(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KD死亡交叉
        K值由上往下穿越D值
        """
        if df.empty or len(df) < Length * 3 + 2:
            return False, ""
        k, d = _calc_stochastic(df['High'], df['Low'], df['Close'], Length)
        if _crosses_below(k, d):
            return True, f"KD({Length}) 死亡交叉, K={k.iloc[-1]:.1f}, D={d.iloc[-1]:.1f}"
        return False, ""

    @staticmethod
    def KD黃金交叉(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KD黃金交叉
        K值由下往上穿越D值
        """
        if df.empty or len(df) < Length * 3 + 2:
            return False, ""
        k, d = _calc_stochastic(df['High'], df['Low'], df['Close'], Length)
        if _crosses_above(k, d):
            return True, f"KD({Length}) 黃金交叉, K={k.iloc[-1]:.1f}, D={d.iloc[-1]:.1f}"
        return False, ""

    @staticmethod
    def MACD死亡交叉(df: pd.DataFrame, FastLength: int = 12, SlowLength: int = 26, MACDLength: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: MACD死亡交叉
        DIF 向下穿越 Signal 線
        """
        if df.empty or len(df) < SlowLength + MACDLength + 2:
            return False, ""
        dif, macd_sig, osc = _calc_macd(df['Close'], FastLength, SlowLength, MACDLength)
        if _crosses_below(dif, macd_sig):
            return True, f"MACD({FastLength},{SlowLength},{MACDLength}) 死亡交叉, DIF={dif.iloc[-1]:.4f}, Signal={macd_sig.iloc[-1]:.4f}"
        return False, ""

    @staticmethod
    def MACD黃金交叉(df: pd.DataFrame, FastLength: int = 12, SlowLength: int = 26, MACDLength: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: MACD黃金交叉
        DIF 向上穿越 Signal 線
        """
        if df.empty or len(df) < SlowLength + MACDLength + 2:
            return False, ""
        dif, macd_sig, osc = _calc_macd(df['Close'], FastLength, SlowLength, MACDLength)
        if _crosses_above(dif, macd_sig):
            return True, f"MACD({FastLength},{SlowLength},{MACDLength}) 黃金交叉, DIF={dif.iloc[-1]:.4f}, Signal={macd_sig.iloc[-1]:.4f}"
        return False, ""

    @staticmethod
    def MTM穿越0(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM穿越0
        MTM (Momentum = Close - Close[N]) 往上穿越 0
        """
        if df.empty or len(df) < Length + 2:
            return False, ""
        close = df['Close']
        mtm = close - close.shift(Length)
        zero = pd.Series([0.0] * len(mtm), index=mtm.index)
        if _crosses_above(mtm, zero):
            return True, f"動能 MTM({Length}) 穿越 0 軸 ({mtm.iloc[-1]:.2f})"
        return False, ""

    @staticmethod
    def MTM跌破0(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM跌破0
        MTM 往下跌破 0
        """
        if df.empty or len(df) < Length + 2:
            return False, ""
        close = df['Close']
        mtm = close - close.shift(Length)
        zero = pd.Series([0.0] * len(mtm), index=mtm.index)
        if _crosses_below(mtm, zero):
            return True, f"動能 MTM({Length}) 跌破 0 軸 ({mtm.iloc[-1]:.2f})"
        return False, ""

    @staticmethod
    def RSI低檔背離(df: pd.DataFrame, RSILength: int = 6, Region: int = 20, Threshold: float = 40.0) -> tuple[bool, str]:
        """
        Original Strategy: RSI低檔背離
        RSI 穿越門檻值，RSI 值為近期高點，但價格呈下降趨勢 (底背離訊號)
        """
        if df.empty or len(df) < RSILength * 9 + 2:
            return False, ""
        close = df['Close']
        rsi = _calc_rsi(close, RSILength)

        # RSI crosses above threshold
        rsi_cross = (rsi.iloc[-1] > Threshold) and (rsi.iloc[-2] <= Threshold)
        if not rsi_cross:
            return False, ""

        # RSI at its highest in Region
        rsi_window = rsi.iloc[-Region:]
        rsi_is_high = rsi.iloc[-1] >= rsi_window.max() * 0.95

        # Price in downtrend (linear regression slope < 0)
        idx = np.arange(Region)
        price_window = close.iloc[-Region:].values
        if len(price_window) < Region:
            return False, ""
        slope = np.polyfit(idx, price_window, 1)[0]
        price_downtrend = slope < 0

        if rsi_is_high and price_downtrend:
            return True, f"RSI({RSILength}) 低檔背離 (RSI={rsi.iloc[-1]:.1f} 穿越 {Threshold}，但價格下降趨勢)"
        return False, ""

    @staticmethod
    def RSI死亡交叉(df: pd.DataFrame, ShortLength: int = 6, LongLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: RSI死亡交叉
        短天期 RSI 往下穿越長天期 RSI
        """
        if df.empty or len(df) < LongLength * 9 + 2:
            return False, ""
        close = df['Close']
        rsi_short = _calc_rsi(close, ShortLength)
        rsi_long = _calc_rsi(close, LongLength)
        if _crosses_below(rsi_short, rsi_long):
            return True, f"RSI 死亡交叉 (RSI{ShortLength}={rsi_short.iloc[-1]:.1f} < RSI{LongLength}={rsi_long.iloc[-1]:.1f})"
        return False, ""

    @staticmethod
    def RSI高檔背離(df: pd.DataFrame, RSILength: int = 6, Region: int = 20, Threshold: float = 60.0) -> tuple[bool, str]:
        """
        Original Strategy: RSI高檔背離
        RSI 跌破門檻值，RSI 值為近期低點，但價格呈上升趨勢 (頂背離訊號)
        """
        if df.empty or len(df) < RSILength * 9 + 2:
            return False, ""
        close = df['Close']
        rsi = _calc_rsi(close, RSILength)

        # RSI crosses below threshold
        rsi_cross = (rsi.iloc[-1] < Threshold) and (rsi.iloc[-2] >= Threshold)
        if not rsi_cross:
            return False, ""

        # RSI at its lowest in Region
        rsi_window = rsi.iloc[-Region:]
        rsi_is_low = rsi.iloc[-1] <= rsi_window.min() * 1.05

        # Price in uptrend (linear regression slope > 0)
        idx = np.arange(Region)
        price_window = close.iloc[-Region:].values
        if len(price_window) < Region:
            return False, ""
        slope = np.polyfit(idx, price_window, 1)[0]
        price_uptrend = slope > 0

        if rsi_is_low and price_uptrend:
            return True, f"RSI({RSILength}) 高檔背離 (RSI={rsi.iloc[-1]:.1f} 跌破 {Threshold}，但價格上升趨勢)"
        return False, ""

    @staticmethod
    def RSI黃金交叉(df: pd.DataFrame, ShortLength: int = 6, LongLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: RSI黃金交叉
        短天期 RSI 往上穿越長天期 RSI
        """
        if df.empty or len(df) < LongLength * 9 + 2:
            return False, ""
        close = df['Close']
        rsi_short = _calc_rsi(close, ShortLength)
        rsi_long = _calc_rsi(close, LongLength)
        if _crosses_above(rsi_short, rsi_long):
            return True, f"RSI 黃金交叉 (RSI{ShortLength}={rsi_short.iloc[-1]:.1f} > RSI{LongLength}={rsi_long.iloc[-1]:.1f})"
        return False, ""

    @staticmethod
    def 均線多頭排列(df: pd.DataFrame, Leng1: int = 5, Leng2: int = 20, Leng3: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 均線多頭排列
        close > MA5 > MA20 > MA60
        """
        if df.empty or len(df) < Leng3 + 1:
            return False, ""
        close = df['Close']
        ma1 = close.rolling(Leng1).mean()
        ma2 = close.rolling(Leng2).mean()
        ma3 = close.rolling(Leng3).mean()

        c = close.iloc[-1]
        m1 = ma1.iloc[-1]
        m2 = ma2.iloc[-1]
        m3 = ma3.iloc[-1]

        if c > m1 > m2 > m3:
            return True, f"均線多頭排列 Close={c:.2f} > MA{Leng1}={m1:.2f} > MA{Leng2}={m2:.2f} > MA{Leng3}={m3:.2f}"
        return False, ""

    @staticmethod
    def 均線空頭排列(df: pd.DataFrame, Leng1: int = 5, Leng2: int = 20, Leng3: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 均線空頭排列
        close < MA5 < MA20 < MA60
        """
        if df.empty or len(df) < Leng3 + 1:
            return False, ""
        close = df['Close']
        ma1 = close.rolling(Leng1).mean()
        ma2 = close.rolling(Leng2).mean()
        ma3 = close.rolling(Leng3).mean()

        c = close.iloc[-1]
        m1 = ma1.iloc[-1]
        m2 = ma2.iloc[-1]
        m3 = ma3.iloc[-1]

        if c < m1 < m2 < m3:
            return True, f"均線空頭排列 Close={c:.2f} < MA{Leng1}={m1:.2f} < MA{Leng2}={m2:.2f} < MA{Leng3}={m3:.2f}"
        return False, ""

    @staticmethod
    def 布林通道超買(df: pd.DataFrame, Length: int = 20, UpperBand: float = 2.0) -> tuple[bool, str]:
        """
        Original Strategy: 布林通道超買
        High >= 布林通道上軌
        """
        if df.empty or len(df) < Length + 1:
            return False, ""
        upper, mid, lower = _calc_bollinger(df['Close'], Length, UpperBand)
        high = df['High'].iloc[-1]
        up = upper.iloc[-1]
        if high >= up:
            return True, f"布林通道超買 High={high:.2f} >= 上軌={up:.2f}"
        return False, ""

    @staticmethod
    def 布林通道超賣(df: pd.DataFrame, Length: int = 20, LowerBand: float = 2.0) -> tuple[bool, str]:
        """
        Original Strategy: 布林通道超賣
        Low <= 布林通道下軌
        """
        if df.empty or len(df) < Length + 1:
            return False, ""
        upper, mid, lower = _calc_bollinger(df['Close'], Length, LowerBand)
        low = df['Low'].iloc[-1]
        lo = lower.iloc[-1]
        if low <= lo:
            return True, f"布林通道超賣 Low={low:.2f} <= 下軌={lo:.2f}"
        return False, ""

    @staticmethod
    def 帶量突破均線(df: pd.DataFrame, Length: int = 10, VolFactor: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 帶量突破均線
        close 突破 MA(Length)，且今日量 > 過去 N 日均量 × VolFactor
        """
        if df.empty or len(df) < Length + 2:
            return False, ""
        close = df['Close']
        volume = df['Volume']
        ma = close.rolling(Length).mean()

        # Close crosses above MA today (was below yesterday)
        price_cross = (close.iloc[-1] > ma.iloc[-1]) and (close.iloc[-2] < ma.iloc[-2])
        # Volume condition: today volume > avg volume * factor
        avg_vol = volume.iloc[-(Length + 1):-1].mean()
        vol_expand = volume.iloc[-1] > avg_vol * VolFactor

        if price_cross and vol_expand:
            vol_ratio = volume.iloc[-1] / avg_vol if avg_vol > 0 else 0
            return True, f"帶量突破均線MA({Length}) Close={close.iloc[-1]:.2f} > MA={ma.iloc[-1]:.2f}, 量比={vol_ratio:.1f}x"
        return False, ""

    @staticmethod
    def 成交量放大(df: pd.DataFrame, Length: int = 5, VolFactor: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 成交量放大
        Volume > Average(Volume[1], Length) * VolFactor
        """
        if df.empty or len(df) < Length + 2:
            return False, ""
        volume = df['Volume']
        avg_vol = volume.iloc[-(Length + 1):-1].mean()
        today_vol = volume.iloc[-1]

        if avg_vol > 0 and today_vol > avg_vol * VolFactor:
            vol_ratio = today_vol / avg_vol
            return True, f"成交量放大 {vol_ratio:.1f}x (今={today_vol:.0f}, 均={avg_vol:.0f})"
        return False, ""

    @staticmethod
    def 短期均線穿越長期均線(df: pd.DataFrame, Shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 短期均線穿越長期均線 (黃金交叉)
        MA(short) 往上穿越 MA(long)
        """
        if df.empty or len(df) < Longlength + 2:
            return False, ""
        close = df['Close']
        ma_short = close.rolling(Shortlength).mean()
        ma_long = close.rolling(Longlength).mean()

        if _crosses_above(ma_short, ma_long):
            return True, f"均線黃金交叉 MA{Shortlength}={ma_short.iloc[-1]:.2f} 穿越 MA{Longlength}={ma_long.iloc[-1]:.2f}"
        return False, ""

    @staticmethod
    def 短期均線跌破長期均線(df: pd.DataFrame, Shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 短期均線跌破長期均線 (死亡交叉)
        MA(short) 往下跌破 MA(long)
        """
        if df.empty or len(df) < Longlength + 2:
            return False, ""
        close = df['Close']
        ma_short = close.rolling(Shortlength).mean()
        ma_long = close.rolling(Longlength).mean()

        if _crosses_below(ma_short, ma_long):
            return True, f"均線死亡交叉 MA{Shortlength}={ma_short.iloc[-1]:.2f} 跌破 MA{Longlength}={ma_long.iloc[-1]:.2f}"
        return False, ""

    @staticmethod
    def 跌破糾結均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10,
                    Longlength: int = 20, Percent: int = 5, XLen: int = 20,
                    Volpercent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 跌破糾結均線
        三條均線糾結（差距 < Percent%），帶量向下突破
        """
        if df.empty or len(df) < Longlength + XLen + 2:
            return False, ""
        close = df['Close']
        volume = df['Volume']
        high = df['High']
        low = df['Low']

        ma_s = close.rolling(shortlength).mean()
        ma_m = close.rolling(midlength).mean()
        ma_l = close.rolling(Longlength).mean()

        # 計算均線糾結程度
        avg_h = pd.concat([ma_s, ma_m, ma_l], axis=1).max(axis=1)
        avg_l = pd.concat([ma_s, ma_m, ma_l], axis=1).min(axis=1)
        avg_hlp = 100 * avg_h / avg_l.replace(0, np.nan) - 100

        # Condition 1: 過去 XLen 天均線都在糾結狀態
        cond1 = (avg_hlp.iloc[-XLen:] < Percent).all()
        # Condition 2: 今日成交量 > 過去 XLen 日均量 × (1 + Volpercent%)
        avg_vol = volume.iloc[-(XLen + 1):-1].mean()
        cond2 = volume.iloc[-1] > avg_vol * (1 + Volpercent / 100)
        # Condition 3: 平均量 > 2000 張
        avg_vol5 = volume.iloc[-6:-1].mean()
        cond3 = avg_vol5 >= 2000
        # Condition 4: 收盤跌破均線下緣 2%，且創 XLen 新低
        al = avg_l.iloc[-1]
        cond4 = close.iloc[-1] < al * 0.98 and low.iloc[-1] < low.iloc[-(XLen + 1):-1].min()

        if cond1 and cond2 and cond4:
            return True, f"跌破糾結均線 MA糾結={avg_hlp.iloc[-1]:.1f}% < {Percent}%, Close={close.iloc[-1]:.2f} < 均線下緣={al:.2f}*0.98"
        return False, ""

    @staticmethod
    def 週KD低檔黃金交叉(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 週KD低檔黃金交叉
        KD 黃金交叉且 K < 30 (低檔)
        """
        if df.empty or len(df) < Length * 3 + 2:
            return False, ""
        k, d = _calc_stochastic(df['High'], df['Low'], df['Close'], Length)

        cross_up = _crosses_above(k, d)
        k_low = k.iloc[-1] < 30

        if cross_up and k_low:
            return True, f"週KD低檔黃金交叉 K={k.iloc[-1]:.1f}(<30), D={d.iloc[-1]:.1f}"
        return False, ""

    @staticmethod
    def 週線月線黃金交叉且站穩(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 週線月線黃金交叉且站穩
        MA5(週線) 穿越 MA20(月線)，且近 5 天每天收盤上漲且站上週線
        """
        if df.empty or len(df) < 25:
            return False, ""
        close = df['Close']
        ma5 = close.rolling(5).mean()
        ma20 = close.rolling(20).mean()

        # 3 根 K 線前發生黃金交叉（避開當日）
        cross_happened = False
        for i in range(1, 4):
            if (ma5.iloc[-i] > ma20.iloc[-i]) and (ma5.iloc[-(i + 1)] <= ma20.iloc[-(i + 1)]):
                cross_happened = True
                break

        # 近 5 天連續上漲且收盤 > MA5
        last5_close = close.iloc[-5:]
        last5_ma5 = ma5.iloc[-5:]
        all_up = all(last5_close.iloc[i] > last5_close.iloc[i - 1] for i in range(1, 5))
        all_above_ma5 = (last5_close > last5_ma5).all()

        if cross_happened and all_up and all_above_ma5:
            return True, f"週線月線黃金交叉且站穩 MA5={ma5.iloc[-1]:.2f} > MA20={ma20.iloc[-1]:.2f}, 近5天收漲"
        return False, ""
