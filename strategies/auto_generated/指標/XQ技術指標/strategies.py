# Auto-generated strategies for: 指標/XQ技術指標
import pandas as pd
import numpy as np

class Xq技術指標Strategies:

    @staticmethod
    def strategy_3_6_乖離率(df: pd.DataFrame, Length1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 3-6 乖離率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\3-6 乖離率.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ 3-6 乖離率
        //
        Plot1(Bias(Length1) - Bias(Length2), "3-6乖離率(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_3_6乖離率轉折點(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 3-6乖離率轉折點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\3-6乖離率轉折點.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: 3-6乖離率轉折點
        //
        Value1 = 2 * Close[3] - Close[6];
        Plot1(Value1, "T");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ACC__加速量指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: ACC (加速量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\ACC (加速量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: ACC指標
        //
        value1 = Momentum(Close, Length); 
        value2 = Momentum(value1, Length);
        Plot1(value2, "ACC");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def AD_Osc_聚散擺盪指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: AD-Osc(聚散擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\AD-Osc(聚散擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: A/D Osc 指標
        // 
        bp = High - Open;
        sp = Close - Low;
        if High <> low then
        	ado = (bp + sp)/(2*(High - Low))*100
        else
        	ado = 50;
        plot1(ado, "A/D-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ADI__累積分配指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: ADI (累積分配指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\ADI (累積分配指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: A/DI 指標
        //
        if Close > Close[1] then
        	adi = adi[1] + (Close - minlist(low, close[1])) 
        else
          begin
        	if Close < Close[1] then
        		adi = adi[1] - (maxlist(high, close[1]) - close)
        	else
        		adi = adi[1];
          end;
        Plot1(adi, "A/DI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def AR_指標(df: pd.DataFrame, Length: int = 26) -> tuple[bool, str]:
        """
        Original Strategy: AR 指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\AR 指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: AR指標
        // 
        sum = Summation((Open - Low), Length);
        if sum <> 0 then
        	ar = 100 * Summation((High - Open), length) / sum
        else
        	ar = ar[1];
        Plot1(ar, "AR(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ATR__平均真實區域_(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: ATR (平均真實區域)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\ATR (平均真實區域).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: ATR指標
        //
        value1 = Average(TrueRange, Length);
        Plot1(value1, "ATR");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BBand_width__布林通道寬度指標_(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: BBand width (布林通道寬度指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\BBand width (布林通道寬度指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: BBandWidth指標
        //
        up = bollingerband(Close, Length, UpperBand);
        down = bollingerband(Close, Length, -1 * LowerBand);
        mid = (up + down) / 2;
        bbandwidth = 100 * (up - down) / mid;
        ema = XAverage(bbandwidth, EMALength);
        Plot1(bbandwidth , "BBand width(%)");
        Plot2(ema, "Band% EMA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BIAS_乖離率(df: pd.DataFrame, Length1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: BIAS 乖離率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\BIAS 乖離率.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ 乖離率
        //
        Plot1(Bias(Length1), "BIAS1(%)");
        Plot2(Bias(Length2), "BIAS2(%)");
        Plot3(Bias(Length3), "BIAS3(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BR_指標(df: pd.DataFrame, Length: int = 26) -> tuple[bool, str]:
        """
        Original Strategy: BR 指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\BR 指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ BR指標
        //
        sum= Summation((Close[1] - Low), length);
        if sum <> 0 then
        	_br = 100 * Summation((High - Close[1]), length) / sum
        else
        	_br = _br[1];
        Plot1(_br, "BR(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CCI__商品通道指標_(df: pd.DataFrame, Length1: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: CCI (商品通道指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\CCI (商品通道指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: CCI指標
        //
        Length1(14,"天數一"), 
        Length2(28,"天數二"), 
        Length3(42,"天數三"),
        UpBaseLine(100,"上基準線"), 
        MidBaseLine(0,"中基準線"), 
        UnderBaseLine(-100,"下基準線");
        Plot1(CommodityChannel(Length1), "CCI1");
        Plot2(CommodityChannel(Length2), "CCI2");
        Plot3(CommodityChannel(Length3), "CCI3");
        plot4(UpBaseLine, "上基準線", checkbox:=0);
        plot5(MidBaseLine, "中基準線", checkbox:=0);
        plot6(UnderBaseLine, "下基準線" , checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DMI__趨向指標_(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: DMI (趨向指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\DMI (趨向指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: DMI指標
        //
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value, "+DI");
        Plot2(ndi_value, "-DI");
        Plot3(adx_value, "ADX");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DMI_Osc_趨向擺盪線_(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: DMI-Osc(趨向擺盪線)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\DMI-Osc(趨向擺盪線).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: DMI-Osc指標
        //
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value - ndi_value, "DMI-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DPO__非趨勢價格擺盪指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: DPO (非趨勢價格擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\DPO (非趨勢價格擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: DPO指標
        //
        dpo = Close - Average(Close, Length)[(Length /2) + 1];
        Plot1(dpo, "DPO"); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def HL_Osc__高低價擺盪指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: HL-Osc (高低價擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\HL-Osc (高低價擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: HL-Osc 指標
        //
        tr = TrueRange;
        if tr <> 0 then
        	hlo = 100 * (H - C[1]) / tr
        else
        	hlo = 0;
        plot1(hlo, "HL-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KD_隨機指標(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KD 隨機指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\KD 隨機指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: KD指標
        //
        Stochastic(Length, RSVt, Kt, rsv, k, _d);
        Plot1(k, "K(%)");
        Plot2(_d, "D(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KDJ_隨機指標(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KDJ 隨機指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\KDJ 隨機指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: KDJ指標
        //
        Stochastic(Length, RSVt, Kt, rsv, k, _d);
        Plot1(k, "K(%)");
        Plot2(_d, "D(%)");
        if JType = 0 then
        	j = 3 * k - 2 * _d
        else
        	j = 3 * _d - 2 * k;
        Plot3(j, "J(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MA_Osc__移動平均線擺盪指標_(df: pd.DataFrame, Length1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: MA-Osc (移動平均線擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MA-Osc (移動平均線擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MA-Osc
        //
        value1 = Average(close, Length1);
        value2 = Average(close, Length2);
        value3 = (value1 - value2);
        Plot1(value3, "MA-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MACD_指標(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: MACD 指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MACD 指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MACD指標
        //
        price = WeightedClose();
        Value1 = XAverage(price, FastLength) - XAverage(price, SlowLength);
        Value2 = XAverage(Value1, MACDLength) ;
        Value3 = Value1 - Value2 ;
        // 前面區段資料變動較大, 先不繪出
        //
        if CurrentBar <= SlowLength then
        begin
        	Value1 = 0;
        	Value2 = 0;
        	Value3 = 0;
        end;
        Plot1(Value1, "DIF");
        Plot2(Value2, "MACD");
        Plot3(Value3, "Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MAM_移動平均動量指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MAM(移動平均動量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MAM(移動平均動量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MAM指標
        //
        Value1 = Average(Close, Length);
        Value2 = Average(Close, Length)[Distance];
        mam = Value1 - Value2;
        Plot1(mam, "MAM");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MI_質量指標_(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: MI(質量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MI(質量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MI指標
        //
        ema1 = XAverage(High - Low, length);
        ema2 = XAverage(ema1, length);
        if ema2 <> 0 then
        	divSeries = ema1 / ema2
        else
        	divSeries = 0;
        if CurrentBar >= sumLength then
        	mi = Summation(divSeries, sumLength)
        else
        	mi = 0;
        Plot1(mi, "MI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MO_運動量擺盪指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MO(運動量擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MO(運動量擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MO指標
        //
        mo = 100 * Close / Close[Length];
        Plot1(mo, "MO");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM_動量指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM(動量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\MTM(動量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MTM指標
        //
        value1 = Momentum(Close, Length); 
        if CurrentBar >= Length then
        	Value2 = Average(Value1, Length)
        else
        	Value2 = Value1;
        Plot1(value1, "MTM");
        Plot2(value2, "MA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PSY_心理線(df: pd.DataFrame, Length1: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: PSY 心理線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\PSY 心理線.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: 心理線
        //
        Value1 = 100 * CountIf(Close > Close[1], Length1) / Length1;
        Value2 = 100 * CountIf(Close > Close[1], Length2) / Length2;
        Plot1(Value1, "PSY1");
        Plot2(Value2, "PSY2");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RC_價格變動率指標_(df: pd.DataFrame, Length: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: RC(價格變動率指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\RC(價格變動率指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: RC指標
        //
        value1 = (Close - Close[Length]) / Close[Length];
        value2 = XAverage(value1, EMALength);
        Plot1(value1, "RC");
        Plot2(value2, "ERC");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI指標(df: pd.DataFrame, Length1: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: RSI指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\RSI指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: RSI指標
        //
        Plot1(RSI(Close, Length1), "RSI1");
        Plot2(RSI(Close, Length2), "RSI2");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSV_指標(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: RSV 指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\RSV 指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: RSV指標
        //
        Stochastic(Length, RSVt, Kt, rsv, k, _d);
        Plot1(rsv, "RSV(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TRIX_三重指數平滑移動平均指標_(df: pd.DataFrame, Length1: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: TRIX(三重指數平滑移動平均指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\TRIX(三重指數平滑移動平均指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: TRIX指標
        //
        Value1 = TRIX(Close, Length1) * 100;
        Value2 = TRIX(Close, Length2) * 100;
        Plot1(Value1, "TRIX1");
        Plot2(Value2, "TRIX2");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VHF_垂直水平過濾指標_(df: pd.DataFrame, Length: int = 42) -> tuple[bool, str]:
        """
        Original Strategy: VHF(垂直水平過濾指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\VHF(垂直水平過濾指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VHF指標
        //
        hp = highest(Close, Length);
        lp = lowest(Close, Length);
        numerator = hp - lp;
        denominator = Summation(absvalue((Close - Close[1])), Length);
        if denominator <> 0 then
        	_vhf = numerator / denominator
        else
        	_vhf = 0;
        Plot1(_vhf, "VHF");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def WAD_威廉多空力度線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: WAD 威廉多空力度線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\WAD 威廉多空力度線.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: WA/D 指標
        //
        if CurrentBar = 1 then
        	wad = 0
        else
          begin	
        	if close = close[1] then
        		_ad = 0
        	else	
        	  begin
        		if close < close[1] then
        			_ad = close - TrueHigh
        		else { close > close[1] }
        			_ad = close - TrueLow;
        	  end;
        	wad = _ad + wad[1];
          end;
        Plot1(wad, "WA/D");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 威廉指標(df: pd.DataFrame, Length1: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 威廉指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\威廉指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: 威廉指標
        //
        value1 = PercentR(Length1) - 100;
        value2 = PercentR(Length2) - 100;
        value3 = PercentR(Length3) - 100;
        Plot1(value1, "威廉指標1");
        Plot2(value2, "威廉指標2");
        Plot3(value3, "威廉指標3");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 快速KD_隨機指標(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 快速KD 隨機指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ技術指標\快速KD 隨機指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: 快速KD指標
        //
        Stochastic(Length, RSVt, 3, rsv, k, _d);
        Plot1(rsv, "K(%)");
        Plot2(k, "D(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
