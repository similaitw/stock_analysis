# Auto-generated strategies for: 自動交易/常見技術分析/多頭
import pandas as pd
import numpy as np

class 多頭Strategies:

    @staticmethod
    def ATR觸發上通道(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: ATR觸發上通道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\ATR觸發上通道.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(period + 3);
        value1=average(truerange,period);
        value2=average(close,period);
        value3=value2+N*value1;
        value4=value2-N*value1;
        // 多方進場策略：向上突破上通道。出場策略：向下跌破下通道。
        if close crosses over value3 then setposition(1);
        if close crosses below value4 then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DIF_MACD從負翻正(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: DIF-MACD從負翻正
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\DIF-MACD從負翻正.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        // 多方進場策略：DIF-MACD由負轉正。出場策略：DIF-MACD由正轉負。
        if oscValue Crosses Above 0	then setposition(1);
        if oscValue Crosses below 0	then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DIF黃金交叉MACD(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: DIF黃金交叉MACD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\DIF黃金交叉MACD.xs
        XS Logic Reference:
        {@type:autotrade}
        // 需告參數
        // 資料讀取筆數設定
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        // 多方進場策略：DIF黃金交叉MACD；出場策略：DIF死亡交叉MACD
        if difValue Crosses Above macdValue then setposition(1);
        if difValue Crosses below macdValue then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KD低檔黃金交叉(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KD低檔黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\KD低檔黃金交叉.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        SetTotalBar(maxlist(Length,6) * 3 + 8);
        Stochastic(Length, RSVt, Kt, _rsv, _k, _d);
        // 多方進場策略：K在低檔區由下往上突破D值。出場策略：K由上往下穿越D值。
        if _k < LowBound and _k crosses above _d then setposition(1);
        if _k > HighBound and _k crosses under _d then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM黃金交叉0(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM黃金交叉0
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\MTM黃金交叉0.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(maxlist(Length,6) + 8);
        // 多方進場策略：MTM黃金交叉0軸；出場策略：MTM死亡交叉0軸
        if Momentum(Close, Length) Crosses Above 0 then setposition(1); 
        if Momentum(Close, Length) Crosses below 0 then setposition(0); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI低檔價格背離(df: pd.DataFrame, RSILength: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: RSI低檔價格背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\RSI低檔價格背離.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(maxlist(RSILength,6) * 8 + 8);
        if RSILength < 5 then raiseruntimeerror("計算期別請超過五期");
        RSIValue = RSI(Close, RSILength);
        RSI_linearregslope = linearregslope(RSIValue, RSILength);
        Close_linearregslope = linearregslope(Close, RSILength);
        // 多方進場策略：RSI由下往上突破低檔區，且價格趨勢背離。出場策略：RSI由上往下穿越高檔區，且價格趨勢背離。
        if RSIValue Crosses Above _LThreshold and RSI_linearregslope > 0 and Close_linearregslope < 0 then setposition(1);
        if RSIValue Crosses Below _HThreshold and RSI_linearregslope < 0 and Close_linearregslope > 0 then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 均線黃金交叉(df: pd.DataFrame, Shortlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 均線黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\均線黃金交叉.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(8);
        setbarback(maxlist(Shortlength,Longlength,6));
        // 多方進場策略：短期均線「黃金」交叉長期均線。出場策略：長期均線「死亡」交叉短期均線。
        if Average(Close,Shortlength) Cross Above Average(Close,Longlength) then setposition(1);
        if Average(Close,Shortlength) Cross Below Average(Close,Longlength) then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 布林通道觸碰下軌(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 布林通道觸碰下軌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\布林通道觸碰下軌.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(Length + 3);
        up = bollingerband(Close, Length, UpperBand);
        down = bollingerband(Close, Length, -1 * LowerBand);
        mid = (up + down) / 2;
        // 多方包寧傑通道進場策略：最低價觸碰下軌道。出場策略：最高價觸碰上軌道。
        if low cross under down then setposition(1);
        if high cross over up then setposition(0);		
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量黃金交叉均線(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 帶量黃金交叉均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\帶量黃金交叉均線.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 設定資料讀取筆數
        settotalbar(3);
        setbarback(Length);
        avgP = Average(close, Length);
        avgVol = Average(volume, Length);
        // 多方進場策略：帶量黃金交叉均線；出場策略：帶量死亡交叉均線。
        if close cross above avgP and volume > avgVol * VolFactor then setposition(1);
        if close cross below avgP and volume > avgVol * VolFactor then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平滑CCI超賣(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 平滑CCI超賣
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\平滑CCI超賣.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告變數
        // 資料讀取筆數設定
        SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);
        cciValue = CommodityChannel(Length);
        cciMAValue = Average(cciValue, AvgLength);
        // 多方進場策略：平滑CCI死亡交叉超賣值。出場策略：平滑CCI黃金交叉超賣值。
        if cciMAValue Crosses Below OverSold then setposition(1);
        if cciMAValue Crosses above OverSold then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 短期RSI黃金交叉長期RSI(df: pd.DataFrame, ShortLength: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: 短期RSI黃金交叉長期RSI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\短期RSI黃金交叉長期RSI.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 設定資料讀取筆數
        settotalbar(maxlist(ShortLength,LongLength,6) * 8 + 8);
        RSI_Short=RSI(Close, ShortLength);
        RSI_Long=RSI(Close, LongLength);
        //多方進場策略：短期RSI黃金交叉長期RSI；出場策略：短期RSI死亡交叉長期RSI
        if RSI_Short Crosses Above RSI_Long then setposition(1);
        if RSI_Short Crosses below RSI_Long then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價黃金交叉三均線(df: pd.DataFrame, shortlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價黃金交叉三均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\股價黃金交叉三均線.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(3);
        setbarback(maxlist(shortlength,midlength,Longlength));
        shortaverage=Average(close,shortlength);
        midaverage=Average(close,midlength) ;
        Longaverage=Average(close,Longlength); 
        // 多方進場策略：收盤價黃金交叉三均線。出場策略：收盤價死亡交叉三均線。
        if close cross above maxlist(shortaverage, midaverage, longaverage) then setposition(1);
        if close cross below minlist(shortaverage, midaverage, longaverage) then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價黃金交叉單均線(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價黃金交叉單均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\股價黃金交叉單均線.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(3);
        setbarback(length);
        avgValue = Average(close,length);
        // 多方進場策略：收盤價黃金交叉均線。出場策略：收盤價死亡交叉均線。
        if close cross above avgValue then setposition(1);
        if close cross below avgValue then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價黃金交叉雙均線(df: pd.DataFrame, shortlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價黃金交叉雙均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\常見技術分析\多頭\股價黃金交叉雙均線.xs
        XS Logic Reference:
        {@type:autotrade}
        // 宣告參數
        // 資料讀取筆數設定
        settotalbar(3);
        setbarback(maxlist(shortlength,Longlength));
        Longaverage = Average(close,Longlength);
        shortaverage= Average(close,shortlength);
        // 多方進場策略：收盤價黃金交叉雙均線。出場策略：收盤價死亡交叉雙均線。
        if close cross above maxlist(shortaverage, longaverage) then setposition(1);
        if close cross below minlist(shortaverage, longaverage) then setposition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
