# Auto-generated strategies for: 選股/03.進階技術分析
import pandas as pd
import numpy as np

class Cat03進階技術分析Strategies:

    @staticmethod
    def KD與均線同步出現買進訊號(df: pd.DataFrame, Length: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: KD與均線同步出現買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\KD與均線同步出現買進訊號.xs
        XS Logic Reference:
        {@type:filter}
        stochastic(9,3,3,rsv1,k1,d1);
        // K線黃金交叉
        condition1 = k1 crosses over d1;
        condition2 = close crosses over average(close,Length) or close[1] crosses over average(close[1],Length);
        // 確認有一定的成交量
        condition3 = average(volume,20) > 1000;
        ret = condition1 and condition2 and condition3;
        outputfield(1,average(close,Length),2,"60日均線", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def K棒突破布林值上緣(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: K棒突破布林值上緣
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\K棒突破布林值上緣.xs
        XS Logic Reference:
        {@type:filter}
        	Length(20, "期數"), 
        	UpperBand(2, "通道上緣");
        settotalbar(3);
        Ret = close >= bollingerband(Close, Length, UpperBand);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI黃金交叉且股價非盤整(df: pd.DataFrame, n1: int = 6, n2: int = 12, n3: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: RSI黃金交叉且股價非盤整
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\RSI黃金交叉且股價非盤整.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(maxlist(n1,n2,6) * 9);
        value2 = highdays(n2);
        if rsi(close,n1) crosses over rsi(close,n2) and
           rsi(close,n1) < 50 and
           value2 >= n3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 佔大盤成交量比開始上昇(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 佔大盤成交量比開始上昇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\佔大盤成交量比開始上昇.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("佔全市場成交量比","D");
        SetTotalBar(5);
        if value1[4]=lowest(value1,5) and 
           value1=highest(value1,5) and 
           close crosses above average(close,5)
        then ret=1;
        SetOutputName1("佔全市場成交量比(%)");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 冷門股出量(df: pd.DataFrame, limit1: int = 700, limit2: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 冷門股出量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\冷門股出量.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1 = average(volume,5);
        if value1 < limit1 and volume > limit2 and High > close[1] and volume > volume[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外盤成交變多(df: pd.DataFrame, shortPeriod: int = 5, midPeriod: int = 12, minVolume: int = 2000) -> tuple[bool, str]:
        """
        Original Strategy: 外盤成交變多
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\外盤成交變多.xs
        XS Logic Reference:
        {@type:filter}
        	sVolume(0),
        	bVolume(0),
        	ratio(0),
        	ratioAvgShort(0),
        	ratioAvgLong(0);
        SetTotalBar(MaxList(shortPeriod, midPeriod) + 3);
        sVolume = GetField("內盤量", "D");//內盤量
        bVolume = GetField("外盤量", "D"); //外盤量
        if sVolume + bVolume <> 0 then
        	ratio = bVolume / (sVolume + bVolume) * 100
        else
        	ratio = 50;
        ratioAvgShort = average(ratio,shortPeriod);
        ratioAvgLong = average(ratio,midPeriod);
        if 
        	volume > minVolume and 
        	ratioAvgShort < 40 and 
        	ratioAvgLong < 40 and 
        	absvalue(ratioAvgShort-ratioAvgLong) < 10 and 
        	ratioAvgShort crosses above ratioAvgLong
        then 
        	ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多指標都出現買進訊號(df: pd.DataFrame, rsilength: int = 6, rsilimit: int = 50, rLength: int = 3, rLimit: str = "-50", dmiLength: int = 10, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 多指標都出現買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\多指標都出現買進訊號.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(120);
        //=========計算RSI======================
        Value1=rsi(close,rsilength);//計算RSI的值
        //==========計算威廉指標==================
        value2 = PercentR(rLength) - 100;
        //============計算DMI=======================
        DirectionMovement(dmiLength, pdi_value, ndi_value, adx_value);
        value4=pdi_value;
        //============純粹只是想確認本週股價都沒有跌破前週低==============
        condition1 = GetField("Low", "W") > GetField("Low", "W")[1];
        //============ XQ: tt指標==========================================
        qf = 0;
        qu = 0;
        qd = 0;
        for kk = 1 to length
          begin
        	if close[(kk - 1)] > close[kk] then
        		qu = qu + Volume[(kk - 1)]
        	else
        	  begin
        		if close[(kk - 1)] < close[kk] then
        			qd = qd + Volume[(kk - 1)]
        		else { close[(kk - 1)] = close[kk] }
        			qf = qf + Volume[(kk - 1)];
        	  end;
          end;
        if (qd + qf/2) <> 0 then
        	tt = 100 * (qu + qf/2) /(qd + qf/2)
        else
        	tt = 1000;
        value5=tt;
        //==================設定警示條件====================================
        if value1 > rsilimit 
        and value2 > rLimit
        and condition1 = true
        and value4 > 0
        and value5 > 800 
        then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空分數翻昇(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多空分數翻昇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\多空分數翻昇.xs
        XS Logic Reference:
        {@type:filter}
        // 計算技術指標分數序列, 判斷指標分數是否翻轉
        //
        settotalbar(168);
        value1 = techscore();
        value2 = average(value1, 10);
        if value2 crosses above 5 then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空分數轉空(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多空分數轉空
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\多空分數轉空.xs
        XS Logic Reference:
        {@type:filter}
        // 計算技術指標分數序列, 判斷指標分數是否翻轉
        //
        settotalbar(168);
        value1 = techscore();
        value2 = average(value1, 10);
        if value2 crosses under 10 then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 天量後價量未再創新高(df: pd.DataFrame, XLength: int = 60, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 天量後價量未再創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\天量後價量未再創新高.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        VolumeHighBar = highestbar(volume, XLength);
        PriceHighBar = highestbar(high, Length);
        // 近日內成交量創新高, 可是價格沒有創新高
        //
        if VolumeHighBar > 0 and 
           VolumeHighBar <= Length and
           PriceHighBar = VolumeHighBar then
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 布林帶寬大於N_(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 布林帶寬大於N%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\布林帶寬大於N%.xs
        XS Logic Reference:
        {@type:filter}
        	Length(20, "天數"), 
        	UpperBand(2, "上"), 
        	LowerBand(2, "下"),
        	BBW(80,"N");
        	bbandwidth(0);
        bbandwidth = bollingerbandwidth(Close, Length, UpperBand, LowerBand);
        if bbandwidth >= BBW then ret=1;
        outputfield(1,bbandwidth,2,"布林帶寬");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 布林帶寬小於N_(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 布林帶寬小於N%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\布林帶寬小於N%.xs
        XS Logic Reference:
        {@type:filter}
        	Length(20, "天數"), 
        	UpperBand(2, "上"), 
        	LowerBand(2, "下"),
        	BBW(20,"N");
        	bbandwidth(0);
        bbandwidth = bollingerbandwidth(Close, Length, UpperBand, LowerBand);
        if bbandwidth <= BBW then ret=1;
        outputfield(1,bbandwidth,2,"布林帶寬");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量突破均線後未拉回(df: pd.DataFrame, day: int = 5, length: int = 10, percent: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 帶量突破均線後未拉回
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\帶量突破均線後未拉回.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1=average(close,length);
        value2=average(volume,length);
        if close[day-1] crosses over average(close[day-1], length) and
           volume[day-1] > average(volume[day-1], length) * (1+percent/100) and
           volume > 1000
        then
          begin
        	keyprice = average(close[day-1], length);
        	if trueall(close > keyprice, day-1) then ret = 1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 底部越來越高且資金流入的蓄勢股(df: pd.DataFrame, r1: int = 7) -> tuple[bool, str]:
        """
        Original Strategy: 底部越來越高且資金流入的蓄勢股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\底部越來越高且資金流入的蓄勢股.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(8);
        value1 = RateOfChange(close, 12);
        value2 = lowest(low,3);
        value3 = lowest(low,8);
        value4 = lowest(low,13);
        condition1=false;
        condition2=false;
        if 
        	value1 < r1 and
        	value2 > value3 and 
        	value3 > value4 and
        	close = highest(close,13)
        then 
        	condition1=true;
        Value5=average(GetField("佔全市場成交量比","D"),13);
        if linearregslope(Value5,5) > 0
        then condition2=true;
        if condition1 and condition2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波動幅度開始變大(df: pd.DataFrame, Length: int = 20, VolLimit: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 波動幅度開始變大
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\波動幅度開始變大.xs
        XS Logic Reference:
        {@type:filter}
        value1 = truerange();
        value2 = highest(value1,Length);
        SetTotalBar(Length + 3);
        if 
        	value1 > value2[1] and 
        	value1 > value1[1] and 
        	close * 1.01 > high and 
        	close > close[1] and 
        	volume > VolLimit
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤整後跌破(df: pd.DataFrame, length: int = 20, percent: int = 7) -> tuple[bool, str]:
        """
        Original Strategy: 盤整後跌破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\盤整後跌破.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1 = highest(high[1],length);
        value2 = lowest(low[1],length);
        if 
        	close crosses under value2 and 
        	value1 < value2 *( 1 + percent * 0.01) //最近幾根bar的收盤價高點與低點差不到N%
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破糾結均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, Percent: int = 2, Volpercent: int = 25, VolLimit: int = 2000) -> tuple[bool, str]:
        """
        Original Strategy: 突破糾結均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\突破糾結均線.xs
        XS Logic Reference:
        {@type:filter}
        shortaverage = average(close,shortlength);
        midaverage = average(close,midlength);
        Longaverage = average(close,Longlength);
        maxaverage = maxlist(shortaverage,midaverage,Longaverage);
        SetTotalBar(8);
        if 
        	volume > average(volume,Longlength) * (1 + volpercent * 0.01) and 
        	volume > VolLimit and
            Close crosses over maxaverage 
        then
          begin
        	value1= absvalue(shortaverage -midaverage);
        	value2= absvalue(midaverage -Longaverage);
        	value3= absvalue(Longaverage -shortaverage);
        	if maxlist(value1,value2,value3)*100 < Percent*Close then  ret=1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 築底指標出現買進訊號(df: pd.DataFrame, period: int = 125, length1: int = 5, length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 築底指標出現買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\築底指標出現買進訊號.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(Period + 8);
        zd = countif(close>=close[1],period) / countif(close<close[1],period);
        zdma1 = average(zd,length1);
        zdma2 = average(zd,length2);
        if zdma1<1 and zdma2<1 and zdma1 crosses above zdma2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價下跌而外盤量佔比上升(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價下跌而外盤量佔比上升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\股價下跌而外盤量佔比上升.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period * 2 + 3);
        value1 = GetField("外盤量");//日的外盤量
        if volume <> 0 then 
        	value2 = value1 / volume
        else
        	value2 = 0;
        value3 = average(value2, period);
        if linearregslope(value3,period) > 0 and
           linearregslope(close,period) < 0 and 
           volume > 1000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價蠢蠢欲動(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 股價蠢蠢欲動
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\股價蠢蠢欲動.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(23);
        value1=truerange();
        value2=highest(value1,20);
        if value1 > value2[1] and 
           value1 > value1[1] and 
           close*1.01 > high and 
           close > close[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價跌破走跌後的高壓電線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 股價跌破走跌後的高壓電線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\股價跌破走跌後的高壓電線.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(8);
        value1 = (average(close,30) + average(close,72)) / 2;	//地心引力線
        value2 = value1*1.2;//高壓電線
        value3 = linearregslope(value2,5);
        if absvalue(value3) <= 0.1 and close crosses under value1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 趨勢成形(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 趨勢成形
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\趨勢成形.xs
        XS Logic Reference:
        {@type:filter}
        // ADX趨勢成形
        //
        SetTotalBar(Length*11);
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        if adx_value Crosses Above Threshold and close=high
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌破均線後站不回(df: pd.DataFrame, day: int = 3, length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 跌破均線後站不回
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\跌破均線後站不回.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(length + 3);
        if close[day-1] crosses under average(close[day-1], length) then
          begin
        	keyprice = average(close[day-1], length);
        	if trueall(close < keyprice, day-1) then ret = 1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 雙KD向上(df: pd.DataFrame, Length_D: int = 9, Length_W: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 雙KD向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\03.進階技術分析\雙KD向上.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);
        condition1 = kk_d crosses above dd_d;		// 日KD crosses over
        condition2 = xf_crossover("W", kk_w, dd_w);	// 周KD crosses over
        condition3 = average(volume[1], 5) >= 1000;
        condition4 = kk_d[1] <= 30;							// 日K 低檔
        condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
        ret = condition1 and condition2 and condition3 and condition4 and condition5;
        outputfield(1,kk_d,2,"日K值");
        outputfield(2,kk_w,2,"週K值", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
