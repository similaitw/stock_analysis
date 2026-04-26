# Auto-generated strategies for: 指標/技術指標
import pandas as pd
import numpy as np

class 技術指標Strategies:

    @staticmethod
    def _b指標(df: pd.DataFrame, Length: int = 20, BandRange: int = 2, MALength: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: %b指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\%b指標.xs
        XS Logic Reference:
        {@type:indicator}
        up = bollingerband(Close, Length, BandRange);
        down = bollingerband(Close, Length, -1 * BandRange);
        if up - down = 0 then value1 = 0 else value1 = (close - down) * 100 / (up - down);
        value2 = average(value1, MALength);
        Plot1(value1, "%b");
        Plot2(value2, "%b平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def adaptive_price_zone(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: adaptive price zone
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\adaptive price zone.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/adaptive-price-zone/
        }
        	Length(14,"期數"), 
        	BandPct(2.0,"通道寬度");
        period = squareroot(Length);
        DSEMA = xaverage(xaverage(close, period), period);
        RangeEMA = xaverage(xaverage(high-low, period), period);
        UpBand = DSEMA + BandPct*RangeEMA;
        DownBand = DSEMA - BandPct*RangeEMA;
        Plot1(UpBand, "Upperband");
        Plot2(close, "Close");
        Plot3(DownBand, "BottomBand");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ado聚散擺盪平均線(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: ado聚散擺盪平均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\ado聚散擺盪平均線.xs
        XS Logic Reference:
        {@type:indicator}
        value1=average(ado,period);
        plot1(value1,"ado聚散擺盪平均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ADTM動態買賣氣指標(df: pd.DataFrame, length: int = 23, period: int = 8) -> tuple[bool, str]:
        """
        Original Strategy: ADTM動態買賣氣指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\ADTM動態買賣氣指標.xs
        XS Logic Reference:
        {@type:indicator}
        if open > open[1] then 
        	DTM = maxlist(high-open,open-open[1])
        else
        	DTM = 0;
        if open < open[1] then 
        	DBM = open-low
        else 
            DBM = 0;
        STM = Summation(DTM,length);
        SBM = Summation(DBM,length);
        if STM > SBM then 
        	ADTM = (STM-SBM)/STM
        else
          if STM < SBM then 
        	ADTM = (STM-SBM)/SBM
          else 
            ADTM = 0;
        ADTMMA = average(ADTM,period);
        plot1(ADTM, "ADTM");
        plot2(ADTMMA, "ADTM移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Aroon(df: pd.DataFrame, length: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: Aroon
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Aroon.xs
        XS Logic Reference:
        {@type:indicator}
        aroon_up = (length-nthhighestbar(1,high,length))/length*100;   
        aroon_down = (length-nthlowestbar(1,low,length))/length*100;   
        aroon_oscillator=aroon_up-aroon_down;   
        plot1(aroon_up,"aroon_up");   
        plot2(aroon_down,"aroon_down");   
        plot3(aroon_oscillator,"aroon_oscillator");  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ASI_Accumulation_Swing_Index_振動升降指標(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: ASI(Accumulation Swing Index)振動升降指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\ASI(Accumulation Swing Index)振動升降指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=high-low;
        value2=low-close[1];
        value3=high-low[1];
        value4=close[1]-open[1];
        value5=absvalue(close-close[1]);
        value6=absvalue(close-open);
        value7=absvalue(close[1]-open[1]);
        value8=(value5+0.5*value6+value7);
        switch(maxlist(value1,value2,value3)) begin
        	case value1:
        		value9=value1+0.5*value2+0.25*value4;
        	case value2:
        		value9=value2+0.5*value1+0.25*value4;
        	case value3:
        		value9=value3+0.25*value4;
        end;
        value10=maxlist(value1,value2);
        if value9*value10<>0 then 
        	si=50*value8/value9*value10/3
        else 
        	si=si[1];
        asi+=si;
        plot1(asi,"ASI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def bandpass_filter(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: bandpass filter
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\bandpass filter.xs
        XS Logic Reference:
        {@type:indicator}
        	period(20),
        	delta(0.1);
        price=(h+l)/2;
        beta=cosine(360/period);
        gamma=1/cosine(720*delta/period);
        alpha=gamma-squareroot(gamma*gamma-1);
        BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];
        plot1(BP);
        plot2(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def bband當沖操作指標(df: pd.DataFrame, length: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: bband當沖操作指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\bband當沖操作指標.xs
        XS Logic Reference:
        {@type:indicator}
        up1 = bollingerband(Close[1], Length, 2);
        down1 = bollingerband(Close[1], Length, -2 );
        if open*1.01>up1 then begin
        	dayprofit=open-close;
        end else if down1*1.01>open then begin
        	dayprofit=close-open;
        end else
        	dayprofit=0;
        accprofit=accprofit[1]+dayprofit;
        plot1(accprofit,"累計獲利");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BB指標(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: BB指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\BB指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/％b指標/
        }
        	Length(20, "天數"), 
        	UpperBand(2, "上"), 
        	LowerBand(2, "下"), 
        	pbLength(5, "%B平均天數");
        up = bollingerband(Close, Length, UpperBand);
        down = bollingerband(Close, Length, -1 * LowerBand);
        mid = (up + down) / 2;
        bbandwidth = 100 * (up - down) / mid;
        pb=(close-down)/(up-down);
        value1=average(pb,pbLength);
        plot1(pb,"%b");
        plot2(value1,"%b移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BW_MFI(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: BW MFI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\BW MFI.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        Market Facilitation Index
        }
        if volume <> 0 then
        	value1=(high-low)/volume;
        if value1>value1[1] and volume>volume[1] then begin
        	plot1(volume,"綠燈");
        	noplot(2);
        	noplot(3);
        	noplot(4);
        end;
        if value1>value1[1] and volume<=volume[1] then begin
        	plot2(volume,"偽裝");
        	noplot(1);
        	noplot(3);
        	noplot(4);
        end;
        if value1<=value1[1] and volume>volume[1] then begin
        	plot3(volume,"蟄伏");
        	noplot(1);
        	noplot(2);
        	noplot(4);
        end;
        if value1<=value1[1] and volume<=volume[1] then begin
        	plot4(volume,"衰退");
        	noplot(1);
        	noplot(2);
        	noplot(3);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Chaikin_蔡金波動性指標(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: Chaikin 蔡金波動性指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Chaikin 蔡金波動性指標.xs
        XS Logic Reference:
        {@type:indicator}
        // Chaikin Volatility 指標
        //
        Value1 = XAverage(High - Low, Length);
        if CurrentBar >= LengthROC And Value1[LengthROC] <> 0 then
        	_chaikin = 100 * (Value1 - Value1[LengthROC]) / Value1[LengthROC]
        else
        	_chaikin = 0;
        Plot1(_chaikin, "Chaikin");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CMI市場波動指標(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: CMI市場波動指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\CMI市場波動指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/如何判斷現在是趨勢還是盤整-一個還在研究的課/
        }
        value1=(close-close[period-1])/(highest(high,period)-lowest(low,period))*100;
        value2=absvalue(value1)-30;
        value3=average(value2,3);
        plot1(value3,"市場波動指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CMO_錢德動量擺盪指標_(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: CMO(錢德動量擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\CMO(錢德動量擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        if close >= close[1] then   
          SU = CLOSE - CLOSE[1]   
        else   
          SU = 0;   
        if close < close[1] then   
          SD = CLOSE[1] - CLOSE   
        else   
          SD = 0;    
        value1 = summation(SU,length);   
        value2 = summation(SD,length);   
        if value1+value2 <> 0 then value3 = (value1-value2)/(value1+value2)*100;
        plot1(value3, "CMO");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def coppock_indicator(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: coppock indicator
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\coppock indicator.xs
        XS Logic Reference:
        {@type:indicator}
        value1=rateofchange(close,14);
        value2=rateofchange(close,11);
        value3=value1+value2;
        value4=xaverage(value3,10);
        plot1(value4,"coppock indicator");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CPC指標(df: pd.DataFrame, t1: int = 10, t2: int = 5, t3: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: CPC指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\CPC指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/自訂指標的撰寫技巧以q指標為例/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 317頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        value1=close-close[1];//價格變化
        value2=summation(value1,t1);//累積價格變化
        value3=average(value2,t2);//短期平均
        value4=average(value2,t3);//長期平均
        plot1(value3,"短期累積價格變化平均");
        plot2(value4,"長期累積價格變化平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CR指標(df: pd.DataFrame, Length: int = 26) -> tuple[bool, str]:
        """
        Original Strategy: CR指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\CR指標.xs
        XS Logic Reference:
        {@type:indicator}
        Upsum =  summation(high - WeightedClose[1],Length);
        Downsum = summation(WeightedClose[1] - low,Length); 
        if Downsum <> 0 then
        	CR = Upsum / Downsum *100
        else
        	CR = CR[1]; 
        plot1(CR,"CR(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DBCD_異同離差乖離率_(df: pd.DataFrame, length1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: DBCD 異同離差乖離率 
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\DBCD 異同離差乖離率 .xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/異同離差乖離率dbcd在單一國家股票型基金的應用/
        }
        	length1(10,"短天期"),
        	length2(20,"長天期"),
        	length3(14,"平均天期");
        value1=bias(length1);
        value2=bias(length2);
        value3=value2-value1;
        value4=average(value3,length3);
        plot1(value4,"DBCD");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def demand_index(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: demand index
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\demand index.xs
        XS Logic Reference:
        {@type:indicator}
        { 
        James Sibbet's Demand Index Indicator 
        The Demand Index combines price and volume in 
        such a way that it is often a leading indicator of 
        price change. 
        } 
        variable : 
        	WtCRatio(1), VolRatio(1), VolAvg(Volume), 
        	bu(1), sel(1), Sign1(+1), 
        	WghtClose(Close), AvgTR(High - Low), 
        	Constant(1), bures(1), selres(1), 
        	TempDI(1), DMI(1); 
        If CurrentBar = 1 then 
        	VolAvg = Average(Volume, Length); 
        WghtClose = (High + Low + Close + Close) * 0.25; 
        AvgTR = Average (Highest (High, 2) - Lowest ( Low, 2), Length); 
        VolAvg = ((VolAvg [1] * (Length - 1)) + Volume) / Length; 
        If WghtClose <> 0 and WghtClose[1] <> 0 and 
        	AvgTR <> 0 and VolAvg <> 0 then Begin 
        	WtCRatio = (WghtClose - WghtClose[1]) / MinList(WghtClose,WghtClose[1]) ; 
        	VolRatio = Volume / VolAvg; 
        	Constant = ((WghtClose * 3) /AvgTR) * AbsValue (WtCRatio); 
        	If Constant > 88 then Constant = 88; 
        	Constant = VolRatio / ExpValue (Constant); 
        	If WtCRatio > 0 then Begin 
        		bu = VolRatio; 
        		sel = Constant; 
        	End Else Begin 
        		bu = Constant; 
        		sel = VolRatio; 
        	End; 
        	bures = ((bures [1] * (Length - 1)) + bu) / Length; 
        	selres = ((selres [1] * (Length - 1)) + sel) / Length; 
        	TempDI = +1; 
        	If selres > bures then Begin 
        		Sign1 = -1; 
        		If selres <> 0 then TempDI = bures / selres; 
        	End Else Begin 
        		Sign1 = +1; 
        		If bures <> 0 then TempDI = selres / bures; 
        	End; 
        	TempDI = TempDI * Sign1; 
        	If TempDI < 0 then 
        		DMI = -1 - TempDI 
        	else 
        		DMI = +1 - TempDI ; 
        End;
        Plot1(dmi);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DMI(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: DMI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\DMI.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/787/
        }
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        value1=pdi_value-ndi_value;
        plot1(pdi_value,"向上力量");
        plot2(ndi_value,"向下力量");
        plot3(value1,"多空力道差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ease_of_movement指標(df: pd.DataFrame, length1: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: ease of movement指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\ease of movement指標.xs
        XS Logic Reference:
        {@type:indicator}
        	length1(9,"一次平滑期數"),
        	length2(9,"二次平滑期數");
        value1=(high+low)/2;
        value2=value1-value1[1];
        value3=volume/(high-low);
        value4=value2/value3;
        value5=average(value4,length1);
        value6=average(value5,length2);
        plot1(value5,"EMV");
        plot2(value6,"EMV-MA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Elder_多頭力道指標(df: pd.DataFrame, Length: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: Elder 多頭力道指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Elder 多頭力道指標.xs
        XS Logic Reference:
        {@type:indicator}
        // Elder 多頭力道指標
        //
        Value1 = High - XAverage(Close, Length);
        Plot1(Value1, "多頭");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Elder_空頭力道指標(df: pd.DataFrame, Length: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: Elder 空頭力道指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Elder 空頭力道指標.xs
        XS Logic Reference:
        {@type:indicator}
        // Elder 空頭力道指標
        //
        Value1 = Low - XAverage(Close, Length);
        Plot1(Value1, "空頭");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EMA_SMA(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: EMA-SMA
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\EMA-SMA.xs
        XS Logic Reference:
        {@type:indicator}
        value1=EMA(close,period);
        value2=average(close,period);
        if close<>0 then 
        	value3=(value1-value2)/close*100;
        plot1(value3,"EMA-SMA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def empirical_mode_decomposition(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: empirical mode decomposition
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\empirical mode decomposition.xs
        XS Logic Reference:
        {@type:indicator}
        	period(20),
        	delta(0.1),
        	fraction(0.1);
        	price(0),gamma(0),alpha(0),beta(0),BP(0),
        	mean(0),peak(0),valley(0),avgpeak(0),avgvalley(0);
        price=(h+l)/2;
        beta=cosine(360/period);
        gamma=1/cosine(720*delta/period);
        alpha=gamma-squareroot(gamma*gamma-1);
        BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];
        mean=average(bp,2*period);
        peak=peak[1];
        valley=valley[1];
        if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
        if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
        avgpeak=average(peak,50);
        avgvalley=average(valley,50);
        plot1(mean);
        plot2(fraction*avgpeak);
        plot3(fraction*avgvalley);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def extracting_the_trend(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: extracting the trend
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\extracting the trend.xs
        XS Logic Reference:
        {@type:indicator}
        	period(20),
        	delta(0.1);
        price=(h+l)/2;
        beta=cosine(360/period);
        gamma=1/cosine(720*delta/period);
        alpha=gamma-squareroot(gamma*gamma-1);
        BP=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*BP[1]-alpha*BP[2];
        trend=average(bp,2*period);
        plot1(trend);
        plot2(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def HV歷史波動率指標(df: pd.DataFrame, LENGTH1: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: HV歷史波動率指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\HV歷史波動率指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=log(close/close[1]);
        HVS=STANDARDDEV(value1,LENGTH1,1)*100*SQUAREROOT(252);
        HVL=STANDARDDEV(VALUE1,LENGTH2,1)*100*SQUAREROOT(252);
        HVindex=HVS/HVL;
        plot1(hvindex,"歷史波動率指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def IMI日內動能指標(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: IMI日內動能指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\IMI日內動能指標.xs
        XS Logic Reference:
        {@type:indicator}
        if close > open then   
          up = close-open   
        else   
          up = 0;   
        if close < open then   
          dn = open-close   
        else   
          dn = 0;   
        upi = summation(up,length);   
        dni = summation(dn,length);   
        if upi+dni = 0 then imi = 0 else imi = upi/(upi+dni)*100;   
        plot1(imi, "IMI");  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KO能量潮指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: KO能量潮指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\KO能量潮指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=(close+high+low)/3;
        if CurrentBar = 1 then
        	kovolume = 0
        else begin	
        	if value1 > value1[1] then
        		kovolume = kovolume[1] + volume
        	else begin
        		if value1 < value1[1] then
        			kovolume = kovolume[1] - volume
        		else
        			kovolume = kovolume[1];
        	end;		
        end;
        Plot1(kovolume, "KO能量潮指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def K棒衍生指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: K棒衍生指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\K棒衍生指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/雙k棒可以延伸的多空趨勢指標/
        }
        array:k[22](0);
        if close<>0 then begin
        	//最近一日與前一日的多空力道總差額
        	k[1]=(open-open[1])/close;
        	k[2]=(high-high[1])/close;
        	k[3]=(low-low[1])/close;
        	k[4]=(close-close[1])/close;
        	//當日
        	k[5]=(high-low)/close;
        	k[6]=(high-close)/close;
        	k[7]=(high-open)/close;
        	k[8]=(open-low)/close;
        	k[9]=(close-open)/close;
        	k[10]=(close-low)/close;
        	k[11]=(open-high[1])/close;
        	k[12]=(open-low[1])/close;
        	k[13]=(open-close[1])/close;
        	k[14]=(high-open[1])/close;
        	k[15]=(high-low[1])/close;
        	k[16]=(high-close[1])/close;
        	k[17]=(low-open[1])/close;
        	k[18]=(low-high[1])/close;
        	k[19]=(low-close[1])/close;
        	k[20]=(close-open[1])/close;
        	k[21]=(close-high[1])/close;
        	k[22]=(close-low[1])/close;
        end;
        array: v1[8](0);
        v1[1]=k[1]+k[11]+k[12]+k[13];//隔日開盤多空總力道
        v1[2]=k[1]+k[2]+k[3]+k[4];//隔日多空總力道
        v1[3]=k[20]+k[21]+k[22];//隔日收盤多空結果
        v1[4]=k[9]+k[10]-k[6];//當日收盤多空結果
        v1[5]=k[14]+k[15]+k[16];//多頭最大力量
        v1[6]=(k[17]+k[18]+k[19])*-1;//空頭最大力量
        v1[7]=k[7]+k[9]+k[10];//當日多頭最大力量
        v1[8]=k[6]+k[8]-k[10];//當日空頭最大力量
        value1=v1[1]+v1[2]+v1[3]+v1[4];
        value2=v1[5]+v1[7];
        value3=v1[6]+v1[8];
        plot1(average(value1,5),"多空淨力");
        plot2(average(value2,5),"多頭總力");
        plot3(average(value3,5),"空頭總力");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LRR線性迴歸反轉指標(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: LRR線性迴歸反轉指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\LRR線性迴歸反轉指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=linearregslope(close,period);
        if value1>value1[1] then
        	lrr=1
        else
        	lrr=-1;
        plot1(lrr,"線性迴歸反轉指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Mass_Index(df: pd.DataFrame, length1: int = 9, length2: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: Mass Index
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Mass Index.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = average(range,length1);   
        value2 = average(value1,length1);   
        if value2 = 0 then value3 = 0 else value3 = value1/value2;
        value4 = summation(value3,length2); 
        plot1(value4,"Mass Index");    
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MFO資金流震盪指標(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: MFO資金流震盪指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\MFO資金流震盪指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/大盤多空轉換點之探討系列三-mfo資金流震盪指標/
        }
        if ((high-low[1])+(high[1]-low)) <> 0 then
        	value1= ((high-low[1])-(high[1]-low))/((high-low[1])+(high[1]-low))*volume
        else
        	value1=value1[1];
        value2= summation(value1,period)/summation(volume,period);
        plot1(value2,"MFO資金流震盪指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MF錢流指標(df: pd.DataFrame, N: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MF錢流指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\MF錢流指標.xs
        XS Logic Reference:
        {@type:indicator}
        ap=(high+low+close)/3;
        tv=ap*volume;
        if ap>ap[1] then begin
        	utv=tv;
        	dtv=0;
        end else begin
        	utv=0;
        	dtv=tv;
        end;
        up=UP[1]+(UTV-UP[1])/N;
        DN=DN[1]+(DTV-DN[1])/N;
        IF DN<>0 THEN 
        	MF=100-(100/(1+UP/DN))
        else
        	MF=MF[1];
        PLOT1(MF,"MF");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N日來漲幅較大天數(df: pd.DataFrame, ratio: int = 2, period: int = 20, period1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: N日來漲幅較大天數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\N日來漲幅較大天數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 327頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if close[1]<>0 then
        	value1=(close-close[1])/close[1]*100;
        value2=countif(value1>=ratio,period);
        plot1(value2,"漲幅大的天數");
        plot2(average(value2,period1),"移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N日內上漲天數(df: pd.DataFrame, length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: N日內上漲天數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\N日內上漲天數.xs
        XS Logic Reference:
        {@type:indicator}
        count=countif(close>close[1],length);
        plot1(count,"上漲天數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def range_trading指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: range trading指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\range trading指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=average(range,200);
        value2=average(range,3);
        value3=(value2-value1)/value1;
        plot1(value3,"長短天期range差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RunScore(df: pd.DataFrame, QDate: int = 20140630) -> tuple[bool, str]:
        """
        Original Strategy: RunScore
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\RunScore.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/Runscore指標/
        }
        //先設定一個季結束的日子
        if date > QDate then begin
        	if C>C[1] then RunScore += 1;//收漲加1分
        	if H>H[1] then RunScore += 1;//漲過昨高加1分
        	if C>H[1] then RunScore += 1;//收過昨高加1分
        	if C<C[1] then RunScore -= 1;//收跌扣1分
        	if L<L[1] then RunScore -= 1;//破昨低扣1分
        	if C<L[1] then RunScore -= 1;//收破昨低扣1分
        	vs += v; 
        	i += 1;
        end;
        plot1( RunScore,"漲跌分數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def R平方(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: R平方
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\R平方.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/趨勢檢定器/
        }
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        //做收盤價20天線性回歸
        {value1:斜率,value4:預期值}
        value5=rsquare(close,value4,Length);//算收盤價與線性回歸值的R平方 
        plot1(value5,"R平方");
        plot2(0.2,"趨勢成形線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Stoller平均波幅通道(df: pd.DataFrame, avlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: Stoller平均波幅通道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Stoller平均波幅通道.xs
        XS Logic Reference:
        {@type:indicator}
        	avlength(5,"均線期數"),
        	atrlength(15,"ATR平均期數"),
        	k(1.35,"常數");
        hband=average(close,avlength)+average(truerange,atrlength)*k;
        lband=average(close,avlength)-average(truerange,atrlength)*k;
        plot1(hband,"通道上限");
        plot2(close,"收盤價");
        plot3(lband,"通道下限");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def vortex_indicator(df: pd.DataFrame, period: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: vortex indicator
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\vortex indicator.xs
        XS Logic Reference:
        {@type:indicator}
        pvm=absvalue(high-low[1]);
        nvm=absvalue(low-high[1]);
        value1=summation(pvm,period);
        value2=summation(nvm,period);
        value3=summation(truerange,period);
        value4=value1/value3;
        value5=value2/value3;
        value6=value4-value5;
        plot1(value6,"vortex");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ZDZB築底指標(df: pd.DataFrame, period: int = 125) -> tuple[bool, str]:
        """
        Original Strategy: ZDZB築底指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\ZDZB築底指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/築底指標-2/
        }
        	period(125,"計算期數"),
        	length1(5,"短MA期數"),
        	length2(20,"長MA期數");
        zd=countif(close>=close[1],period)/countif(close<close[1],period);
        zdma1=average(zd,length1);
        zdma2=average(zd,length2);
        plot1(zdma1,"短天期築底指標");
        plot2(zdma2,"長天期築底指標");
        plot3(1,"多空分界");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Zero_Lag_Heikin_Ashi(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: Zero Lag Heikin-Ashi
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\Zero Lag Heikin-Ashi.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/先進指標zero-lag-heikinashi/
        }
        		price(0), haO(0), haC(0), haMax(0), haMin(0), 
        		TEMA1(0), EMAValue1(0), DbEMAValue1(0), 
        		TEMA2(0), EMAValue2(0), DbEMAValue2(0), ZeroLagHA(0);
        price = (close+open+high+low)/4;
        haO = (haO[1]+price)/2;
        haMax = maxlist(high, haO);
        haMin = minlist(low, haO);
        haC = (price+haO+haMax+haMin)/4;
        EMAValue1 = xaverage(haC, Length);
        DbEMAValue1 = xaverage(EMAValue1, Length);
        TEMA1 = 3*EMAValue1-3*DbEMAValue1+xaverage(DbEMAValue1, Length);
        EMAValue2 = xaverage(TEMA1, Length);
        DbEMAValue2 = xaverage(EMAValue2, Length);
        TEMA2 = 3*EMAValue2-3*DbEMAValue2+xaverage(DbEMAValue2, Length);
        ZeroLagHA = 2*TEMA1-TEMA2;
        plot1(ZeroLagHA, "Zero Lag HeikinAshi");
        plot2(average(C,20),"Average");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上影線佔實體比例五日平均(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上影線佔實體比例五日平均
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\上影線佔實體比例五日平均.xs
        XS Logic Reference:
        {@type:indicator}
        value1=average(upshadow,5);
        plot1(value1,"五日平均上影線佔實體比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲下跌幅度強弱度指標(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 上漲下跌幅度強弱度指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\上漲下跌幅度強弱度指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/雲端策略中心精進版之34多頭轉強策略/
        }
        if CurrentBar = 1 then begin
        	sumUp = Average(maxlist(close - close[1], 0), length); 
        	sumDown = Average(maxlist(close[1] - close, 0), length); 
        end else begin
        	up = maxlist(close - close[1], 0);
        	down = maxlist(close[1] - close, 0);	 
        	sumUp = sumUp[1] + (up - sumUp[1]) / length;
        	sumDown = sumDown[1] + (down - sumDown[1]) / length;
        end;
        if sumdown<>0 then rs=sumup/sumdown;
        plot1(rs,"強弱度");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲下跌角度線(df: pd.DataFrame, periods: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 上漲下跌角度線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\上漲下跌角度線.xs
        XS Logic Reference:
        {@type:indicator}
        Value1 = Angle(Date[periods], Date);
        Plot1(Value1, "角度");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲天數指標(df: pd.DataFrame, count1: int = 20, count2: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 上漲天數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\上漲天數指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=countif(close>close[1],count1);
        value2=countif(close>close[1],count2);
        value3=value1-value2;
        plot1(value1);
        plot2(value2);
        plot3(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主動買力(df: pd.DataFrame, p1: int = 5, p2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 主動買力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\主動買力.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("主動買力");
        value2=average(value1,p1);
        value3=average(value1,p2);
        plot1(value2,"主動買力短天期MA");
        plot2(value3,"主動買力長天期MA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 倉_put_call_ratio(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 倉 put call ratio
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\倉 put call ratio.xs
        XS Logic Reference:
        {@type:indicator}
        //台指選擇權現貨(TXO00.TF) 的 買賣權未平倉量比率
        value1=GetSymbolField("TXO00.TF", "買賣權未平倉量比率");
        plot1(value1,"put call ratio");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價格震盪指標(df: pd.DataFrame, length1: int = 5, length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 價格震盪指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\價格震盪指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = average(close, length1);
        value2 = average(close, length2);
        if value1 = 0 then value3 = 0 else value3 = 100 * (value1 - value2) / value1;
        plot1(value3, "OSCP");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價量斜率指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 價量斜率指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\價量斜率指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=average(close,5);
        value2=average(volume,5);
        value3=linearregslope(value1,5);
        value4=linearregslope(value2,5);
        value5=value4-value3;
        plot1(value3,"價斜率");
        plot2(value4,"量斜率");
        plot3(value5,"斜率差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價量齊揚天數(df: pd.DataFrame, sp: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 價量齊揚天數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\價量齊揚天數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/從相對的角度尋找真正價量齊揚的股票/
        }
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("資金流向");
        value2=GetField("強弱指標");
        count1=countif(value2>0and value1>value1[1],sp);
        value3=average(count1,5);
        plot1(value3/SP*100,"短期價量齊揚天數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 六合神拳指數(df: pd.DataFrame, length1: int = 6, length2: int = 10, length3: int = 10, length4: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 六合神拳指數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\六合神拳指數.xs
        XS Logic Reference:
        {@type:indicator}
        count=0;
        if RSI(Close, Length1) > RSI(Close, Length2)
        and rsi(close,length1)<50 then
        	count=1;
        if Momentum(Close, Length3) > 0 then
        	count=count+1;
        directionmovement(length4,pdi_value,ndi_value,adx_value);
        if pdi_value > ndi_value then 
        	count=count+1;
        stochastic(9,3,3,rsv1,k1,d1);
        if k1 > d1 then 
        	count=count+1;
        value1=average(volume,10);
        if linearregslope(value1,8)>0 then
        	count=count+1;
        value2=average(close,8);
        if linearregslope(value2,5)>0 then
        	count=count+1;
        plot1(count,"分數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 創新高天數減破底天數(df: pd.DataFrame, period: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 創新高天數減破底天數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\創新高天數減破底天數.xs
        XS Logic Reference:
        {@type:indicator}
        value1=countif(low<lowest(low[1],period),period);//近期創新低天數
        value2=countif(high>highest(high[1],period),period);//近期創新高天數
        value3=value2-value1;
        plot1(value3,"天數差");
        plot2(3);
        plot3(-3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 力度指標force_index(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 力度指標force index
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\力度指標force index.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/這個盤接下來到底會不會大跌-建構專屬的大盤儀/
        }
        	length(10,"短天期"),
        	length1(30,"長天期");
        fis=average(volume*(close-close[1]),length);
        fil=average(volume*(close-close[1]),length1);
        plot1(fis,"短期力度");
        plot2(fil,"長期力度");
        plot3(fis-fil,"長短力度差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 加速器指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 加速器指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\加速器指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/495/
        }
        Xslope = linearregslope((H+L)/(H+L)[20],20);
        plot1(Xslope,"方向速度" );
        plot2(Xslope-Xslope[1],"速度變化");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 加速指標(df: pd.DataFrame, period1: int = 5, period2: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 加速指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\加速指標.xs
        XS Logic Reference:
        {@type:indicator}
        if close>close[1] then
        	aspeed=(close-close[1])/close*100
        else 
        	aspeed=0;
        if close<close[1] then
        	dspeed=(close[1]-close)/close*100
        else
        	dspeed=0;
        a1=average(aspeed,period1);
        d1=average(dspeed,period1);
        p1=a1-d1;
        ap1=average(p1,period2);
        plot1(p1,"加速度");
        plot2(ap1,"移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 勁道指標(df: pd.DataFrame, day: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: 勁道指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\勁道指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/積極勁道指標/
        }
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("外盤量");//單位:元
        	value6=GetField("內盤量");//單位:元
        end else begin
        	value1=GetField("外盤量","D");//單位:元
        	value6=GetField("內盤量","D");//單位:元
        end;
        value2=volume*(close-close[1]);
        value8=average(volume,day);
        if value6<>0 then 
        	value7=(value1/value6)*volume*(close-close[1]);
        value3=value7*(close-close[1]);
        value4=average(value2,day)/value8;
        value5=average(value3,day)/value8;
        plot1(value4,"勁道指標");
        plot2(value5,"積極勁道指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 動量指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 動量指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\動量指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/尋找趨勢是否成形的指標動量指標/
        }
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("內盤量");//單位:元
        	value2=GetField("外盤量");//單位:元
        end else begin
        	value1=GetField("內盤量","D");//單位:元
        	value2=GetField("外盤量","D");//單位:元
        end;
        value3=(high+low)/2;//計算當天波動的平均價位
        //質量就是內外盤差乘均價
        if value2>value1 then
        	value4=value3*(value2-value1)
        else
        	value4=value3*(value1-value2);
        if close>=close[1] then begin //(方向是往上)
        	value5=(close-close[1])/close[1]*value4;//質量乘以速度
        	value6=0;
        end else begin//(方向是往下)
        	value5=0;
        	value6=(close[1]-close)/close[1]*value4;
        end;
        value8=average(value5,2);
        value9=average(value6,2);
        value10=value8-value9;
        plot1(value10,"動能差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 向上拉動與向下殺盤力道指標(df: pd.DataFrame, period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 向上拉動與向下殺盤力道指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\向上拉動與向下殺盤力道指標.xs
        XS Logic Reference:
        {@type:indicator}
        //當日向上拉動的力量
        value1=(high-open)+(close-low);
        //當日向下殺盤的力量
        value2=(open-low)+(high-close);
        if close<>0 then begin
        	//上拉力道
        	value3=average(value1,period)/close*100;
        	//下殺力道
        	value4=xaverage(value2,period)/close*100;
        end;
        value5=value3-value4;
        plot1(value5,"上拉下殺淨力道");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外盤成交比例指標(df: pd.DataFrame, short1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 外盤成交比例指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\外盤成交比例指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/外盤成交比例指標/
        }
        	short1(5,"短期平均"),
        	mid1(12,"長期平均");
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("內盤量");//單位:元
        	value2=GetField("外盤量");//單位:元
        end else begin
        	value1=GetField("內盤量","D");//單位:元
        	value2=GetField("外盤量","D");//單位:元
        end;
        value3=value1+value2;
        if value3<>0 then 
        	value4=value2/value3*100;
        value5=average(value4,short1);
        value6=average(value4,mid1);
        plot1(value5,"短期均線");
        plot2(value6,"長期均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多方力道線(df: pd.DataFrame, period1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 多方力道線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\多方力道線.xs
        XS Logic Reference:
        {@type:indicator}
        	period1(10,"計算期數"),
        	period2(5,"平滑期數");
        value1=summation(high-close,period1);//上檔賣壓
        value2=summation(close-open,period1); //多空實績
        value3=summation(close-low,period1);//下檔支撐
        value4=summation(open-close[1],period1);//隔夜力道
        if close<>0 then
        	value5=(value2+value3+value4-value1)/close;
        value6=average(value5,period2);
        plot1(value6,"多方力道");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空判斷分數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多空判斷分數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\多空判斷分數.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = techscore;
        plot1(value1, "多空指標");
        plot2(3, "低點");
        plot3(11, "高點");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空力道指標(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 多空力道指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\多空力道指標.xs
        XS Logic Reference:
        {@type:indicator}
        Value1 = high - close;   
        Value2 = close - low; 
        Value3 = average(Value1,length);   
        Value4 = average(Value2,length);   
        plot1(Value4 - Value3, "力道");  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭動能(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 多頭動能
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\多頭動能.xs
        XS Logic Reference:
        {@type:indicator}
        value1=high-close[1]+low-low[1];
        value2=average(value1,period);
        plot1(value2,"多頭動能平均值");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 天羅地網線(df: pd.DataFrame, period: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 天羅地網線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\天羅地網線.xs
        XS Logic Reference:
        {@type:indicator}
        value5=average(close,period);
        value6=standarddev(close,period,1);
        value7=value5+value6;
        value8=value5+2*value6;
        value9=value5-value6;
        value10=value5-2*value6;
        plot1(value8,"+2SD");
        plot2(value7,"+1SD");
        plot3(value5,"MA");
        plot4(value9,"-1SD");
        plot5(value10,"-2SD");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 循環指標(df: pd.DataFrame, period: int = 20, delta: float = 0.5, fraction: float = 0.1) -> tuple[bool, str]:
        """
        Original Strategy: 循環指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\循環指標.xs
        XS Logic Reference:
        {@type:indicator}
        price=(h+l)/2;
        beta=cosine(360/period);
        gamma=1/cosine(720*delta/period);
        alpha=gamma-squareroot(gamma*gamma-1);
        bp=0.5*(1-alpha)*(price-price[2])+beta*(1+alpha)*bp[1]-alpha*bp[2];
        mean=average(bp,2*period);
        peak=peak[1];
        valley=valley[1];
        if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
        if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
        avgpeak=average(peak,50);
        avgvalley=average(valley,50);
        plot1(mean);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月線與收盤價差(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 月線與收盤價差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\月線與收盤價差.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/自訂指標/
        }
        value1=average(close,22);
        value2=close-value1;
        value3=average(value2,3);
        plot1(value3,"月線與收盤價差三日移動平均");
        plot2(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 比大盤強的天數(df: pd.DataFrame, day: int = 10, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 比大盤強的天數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\比大盤強的天數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/股性系列之七-比大盤強的天數/
        }
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        value1=GetField("強弱指標");
        value2=countif(value1>1,day);
        value3=average(value2,period);
        plot1(Value2,"比大盤強的天數");
        plot2(value3,"移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 比大盤強的天數趨勢斜率(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 比大盤強的天數趨勢斜率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\比大盤強的天數趨勢斜率.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        value1=GetField("強弱指標");
        value2=countif(value1>1,period);
        value3=average(value2,period);
        linearreg(value3,period,0,value4,value5,value6,value7);
        plot1(value4,"強度斜率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波動區間指標(df: pd.DataFrame, short1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 波動區間指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\波動區間指標.xs
        XS Logic Reference:
        {@type:indicator}
        	short1(3,"短期平均"),
        	mid1(20,"長期平均");
        value1=highest(high,5);
        value2=lowest(low,5);
        if value2 <> 0 then
        	value3=(value1-value2)/value2*100;
        value4=average(value3,short1);
        value5=average(value3,mid1);
        plot1(value4,"短期平均區間");
        plot2(value5,"長期平均區間");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波動率指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 波動率指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\波動率指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/918/
        }
        value1 = 100*(average(H/L-1,20)+standarddev(H/L-1,20,1)*3);
        value2 = value1- average(value1,10);
        plot1(value1,"波動指標");
        if value2> 0 then plot2(value2,"波動放大");
        if value2<= 0 then plot3(value2,"波動縮小");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 淨買賣力指標(df: pd.DataFrame, Period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 淨買賣力指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\淨買賣力指標.xs
        XS Logic Reference:
        {@type:indicator}
        if high<>low and truerange <> 0 then begin 
        	value1=((high-open)+(close-low))/truerange;
        	value2=((open-low)+(high-close))/truerange;
        end else begin
        	value1=value1[1];
        	value2=value2[1];
        end;
        value3=value1-value2;
        value4=average(value3,Period);
        plot1(value4,"平均淨買賣力");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 真實波動區間指標(df: pd.DataFrame, Length1: int = 3, Length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 真實波動區間指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\真實波動區間指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/股性系列之六真實波動區間/
        }
        value1 = Average(TrueRange, Length1);
        value2 = Average(TrueRange, Length2);
        Plot1(value1, "短期ATR");
        plot2(value2, "長期ATR");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 短線交易比例(df: pd.DataFrame, p1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 短線交易比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\短線交易比例.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/短線過熱的指標/
        }
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("融資買進張數");
        value2=GetField("現股當沖張數");
        value3=GetField("資券互抵張數");
        value4=value1+value2+value3;
        if volume>0 then 
        	value5=value4/volume;
        value6=average(value5,p1);
        plot1(value5,"短線交易比例");
        plot2(value6,"移動平均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 終極擺盪指標(df: pd.DataFrame, length1: int = 7, length2: int = 14, length3: int = 28) -> tuple[bool, str]:
        """
        Original Strategy: 終極擺盪指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\終極擺盪指標.xs
        XS Logic Reference:
        {@type:indicator}
        variable : ruo(0),uo(0),bp(0);  
        bp = close-truelow;
        Value1=summation(bp,length1);   
        Value2=summation(bp,length2);   
        Value3=summation(bp,length3);   
        Value4=summation(truerange,length1);   
        Value5=summation(truerange,length2);   
        Value6=summation(truerange,length3);
        ruo = (value1/value4)*4+(value2/value5)*2+(value3/value6);   
        uo= ruo / 7 * 100;   
        plot1(uo, "UO");  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 線性迴歸斜率(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 線性迴歸斜率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\線性迴歸斜率.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/尋找目前趨勢還向上的股票/
        }
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        {value1:斜率,value4:預期值}
        plot1(value1,"線性迴歸斜率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股性綜合分數指標(df: pd.DataFrame, day: int = 20, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 股性綜合分數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\股性綜合分數指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/把股性拿來作為過濾條件/
        }
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("總成交次數","D");
        value2=average(value1,day);
        value3=GetField("強弱指標");
        value5=GetField("外盤均量");
        value6=average(value5,day);
        value7=GetField("主動買力");
        value8=average(value7,day);
        value9=GetField("開盤委買");
        value10=average(value9,day);
        value11=GetField("資金流向");
        value12=average(value11,day);
        value13=countif(value3>1,day);
        value14=average(value13,day);//比大盤強天數
        value16=GetField("法人買張");
        count=0;
        if value1>value2*(1+ratio/100) then count=count+1;
        //比大盤強的天數
        if value13>value14*(1+ratio/100) then count=count+1;
        if value5>value6*(1+ratio/100) then count=count+1;
        if value7>value8*(1+ratio/100) then count=count+1;
        if value9>value10*(1+ratio/100) then count=count+1;
        //真實波動區間
        if truerange> average(truerange,20) then count=count+1;
        //計算承接的力道
        if truerange<>0 then begin
        	if close<=open then
        		value15=(close-low)/truerange*100
        	else
        		value15=(open-low)/truerange*100;
        end;
        if value15 > average(value15,day)*(1+ratio/100) then count=count+1;
        //法人買張佔成交量比例
        if volume<>0 then value17=value16/volume*100;
        if value17>average(value17,10)*(1+ratio/100) then count=count+1;
        if value11>average(value11,10)*(1+ratio/100) then count=count+1;
        value18=countif(close>=close[1]*1.02,5);
        //N日來漲幅較大的天數
        if value18 >= 2 then count=count+1;
        value19=GetField("融資買進張數");
        value20=GetField("融券買進張數");
        value21=(value19+value20);
        value22=average(value21,day);
        //散戶作多指標
        if value21<value22*0.9 then count=count+1;
        plot1(average(count,3),"股性綜合分數指標");
        plot2(3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 蔡金波動指標(df: pd.DataFrame, length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 蔡金波動指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\蔡金波動指標.xs
        XS Logic Reference:
        {@type:indicator}
        if currentbar=1 then begin
        	cv1=0;
        end else if range<>0 then begin
        	REMA=xaverage(range,length);
        	if rema[length-1]=0 then 
        		cv1=cv1[1]
        	else 
        		cv1=(REMA-REMA[length-1])/rema[length-1];
        end;
        plot1(cv1,"波動率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 變異數指標(df: pd.DataFrame, length1: int = 10, length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 變異數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\變異數指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=varianceps(close,length1,1);
        value2=varianceps(close,length2,1);
        plot1(value1,"短天期變異數");
        plot2(value2,"長天期變異數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 逢低承接的力道(df: pd.DataFrame, short1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 逢低承接的力道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\逢低承接的力道.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/短線止跌的訊號/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 324頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        	short1(5,"短期平均"),
        	mid1(20,"長期平均");
        if truerange<>0 then begin
        	if close<=open then 
        		value1=(close-low)/truerange*100
        	else
        		value1=(open-low)/truerange*100;
        end;
        value2=average(value1,short1);
        value3=average(value2,mid1);
        plot1(value2,"短期均線");
        plot2(value3,"長期均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 進攻力道線(df: pd.DataFrame, period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 進攻力道線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\進攻力道線.xs
        XS Logic Reference:
        {@type:indicator}
        value1=summationif(close>close[1],high-close[1],period);
        plot1(value1,"進攻力道線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 隨機漫步指標(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 隨機漫步指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\隨機漫步指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = standarddev(close,length,1);   
        value2 = average(truerange,length);   
        RWIH = (high-low[length-1])/value2*value1;   
        RWIL = (high[length-1]-low)/value2*value1;   
        plot1(RWIH - RWIL, "RWI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 順勢指標(df: pd.DataFrame, length1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 順勢指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\技術指標\順勢指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/為自己的觀察名單標上交易訊號/
        }
        	length1(5,"短期平均"),
        	length2(10,"長期平均");
        bp1=(close-close[1])/truerange*100;
        abp1=average(bp1,length1);
        abp2=average(bp1,length2);
        plot1(abp1,"短期平均");
        plot2(abp2,"長期平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
