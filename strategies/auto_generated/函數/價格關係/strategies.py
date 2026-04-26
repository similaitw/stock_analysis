# Auto-generated strategies for: 函數/價格關係
import pandas as pd
import numpy as np

class 價格關係Strategies:

    @staticmethod
    def Extremes(df: pd.DataFrame, SourceSeries: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: Extremes
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\Extremes.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        	SourceSeries(numericseries), 	//來源數列
        	Length(numericsimple), 			//計算期間
            DscAsc(numericsimple), 			//極大值(1)或極小值(-1)
        	refExtremeValue(numericref), 	//輸出極值
        	refExtremeBar(numericref);		//輸出極值K棒相對位置
        	exLength(0),
        	exCalcBar(0),
        	calcInterval(0);
        if 1 > Length then 
        begin
          refExtremeValue = 0 ;
          refExtremeBar = -1 ;
          extremes = -1 ;
          return;
        end;
        if Length < exLength or currentbar = 1 or value2 >= Length - 1 then //強制進行重算的case
        begin
        	value1 = SourceSeries;
        	value2 = 0;
        	for value3 = 1 to Length - 1
        	begin
        		if DscAsc * SourceSeries[value3] > DscAsc * value1 then
        		begin
        			value1 = SourceSeries[value3];
        			value2 = value3;	
        		end;
        	end;
        end else if Length > exLength and Length - exLength = currentBar - exCalcBar then //判斷計算長度是否和K棒同步長大，若是，只需要計算差額。
        begin
        	calcInterval = Length - exLength;
        	for value3 = calcInterval - 1 to 0
        	begin
        		if DscAsc * SourceSeries[value3] >= DscAsc * value1 then
        		begin
        			value1 = SourceSeries[value3];
        			value2 = value3;	
        		end	else
        			value2 = value2 + 1;
        	end;	
        end else 
        begin
        	if DscAsc * SourceSeries >= DscAsc * value1 then begin
        		value1 = SourceSeries;
        		value2 = 0;	
        	end	else
        		value2 = value2 + 1;
        end;
        exLength = Length;
        exCalcBar = currentBar;
        refExtremeValue = value1;
        refExtremeBar = value2;
        extremes = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ExtremesArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: ExtremesArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\ExtremesArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        	SourceArray[MaxSize](numericarray), 	//來源陣列
        	Size(numericsimple), 					//來源陣列大小
            DscAsc(numericsimple), 					//極大值(1)或極小值(-1)
        	refExtremeValue(numericref), 			//輸出極值
        	refExtremeIndex(numericref);			//輸出極值陣列索引值
        			_bar(0),
        			counter(0);
        if  Size < 1 or Size > MaxSize then
        begin
          refExtremeValue = 0 ;
          refExtremeIndex = -1 ;
          ExtremesArray = -1 ;
          return;
        end;
        price = SourceArray[1];
        _bar = 1;
        for counter = 2 to Size 
          begin
        	if (DscAsc=1 and SourceArray[counter]>price) then
        	  begin
        		price = SourceArray[counter];
        		_bar = counter;
        	  end
        	else if (DscAsc=-1 and SourceArray[counter]<price) then
        	  begin	
        		price = SourceArray[counter];
        		_bar = counter;
        	  end;
          end;
        refExtremeValue = price;
        refExtremeIndex = _bar;
        ExtremesArray = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def FastHighestBar(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: FastHighestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\FastHighestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        Extremes(ThePrice, Length, 1, value1, _Output);
        FastHighestBar = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def FastLowestBar(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: FastLowestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\FastLowestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        Extremes(ThePrice, Length, -1, value1, _Output);
        FastLowestbar = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def HighDays(df: pd.DataFrame, length: str = "numeric") -> tuple[bool, str]:
        """
        Original Strategy: HighDays
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\HighDays.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 計算過去幾筆資料內創新高的次數
        //
        tt=0;
        currentHigh = high[length-1];
        for ix = length-2 downto 0 
        begin 
        	if ( high[ix] > currentHigh ) then
        	begin
        		tt+=1;　　
        		currentHigh = high[ix];
        	end; 
        end;
        HighDays=tt;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def HighestArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: HighestArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\HighestArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        ExtremesArray(thePriceArray, ArraySize, 1, _Output, value2);
        HighestArray = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def HighestBar(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: HighestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\HighestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        Extremes(ThePrice, Length, 1, value1, _Output);
        HighestBar = _Output;      
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LowDays(df: pd.DataFrame, length: str = "numeric") -> tuple[bool, str]:
        """
        Original Strategy: LowDays
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\LowDays.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 計算過去幾筆資料內創新低的次數
        //
        tt=0;
        currentlow = low[length-1];
        for ix = length-2 downto 0 
        begin 
        	if ( low[ix] < currentlow ) then
        	begin
        		tt+=1;　　
        		currentlow = low[ix];
        	end; 
        end;
        LowDays=tt;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LowestArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: LowestArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\LowestArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        ExtremesArray(thePriceArray, ArraySize, -1, _Output, value2);
        LowestArray = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LowestBar(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: LowestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\LowestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        Extremes(ThePrice, Length, -1, value1, _Output);
        Lowestbar = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MoM(df: pd.DataFrame, MomVal: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: MoM
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\MoM.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        if barfreq <> "M" and barfreq <> "AM" then
        	raiseruntimeerror("僅支援月頻率")
        else
        	MOM = (MomVal/MomVal[1]-1)*100;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthExtremes(df: pd.DataFrame, SourceSeries: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: NthExtremes
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthExtremes.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        	SourceSeries(numericseries), 	//來源數列
        	Length(numericsimple), 			//計算期間
            N(numericsimple),               //極值順序
            DscAsc(numericsimple), 			//極大值(1)或極小值(-1)
        	refExtremeValue(numericref), 	//輸出極值
        	refExtremeBar(numericref);		//輸出極值K棒相對位置
        array: nthA[500](0),nthB[500](0);
        if N>Length or Length>500 then
        begin
            refExtremeValue = 0;
            refExtremeBar = -1;
            NthExtremes = -1;
        end
        else
        begin
            for x = 0 to Length -1
            begin
                nthA[x] = SourceSeries[x];
                nthB[x] = x ;
            end;
            for x = 0 to Length -2
        	begin
        		for y = x + 1 to Length -1
        		begin
        			if ((DscAsc=1 and nthA[x] < nthA[y])or
        				(DscAsc=-1 and nthA[x] > nthA[y])) then
        			begin	
        				temp = nthA[ y ];
                        nthA[ y ] = nthA[ x ];
                        nthA[ x ] = temp;
        				temp = nthB[ y ];
                        nthB[ y ] = nthB[ x ];
                        nthB[ x ] = temp;
        			end;
        		end;
        	end;
            refExtremeValue = 	nthA[ N-1 ];
            refExtremeBar	= 	nthB[ N-1 ] + ExecOffset;
            NthExtremes = 1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthExtremesArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthExtremesArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthExtremesArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        	SourceArray[MaxSize](numericarray), 	//來源陣列
        	Size(numericsimple), 					//來源陣列大小
        	N(numericsimple),                       //極值順序
            DscAsc(numericsimple), 					//極大值(1)或極小值(-1)
        	refExtremeValue(numericref), 			//輸出極值
        	refExtremeIndex(numericref);			//輸出極值陣列索引值
        array: ntharrayA[200](0),ntharrayB[200](0);
        if N > Size or Size > MinList(MaxSize+1,200) then
        begin 
        	refExtremeValue = 0;
        	refExtremeIndex = -1;
        	NthExtremesarray = -1;
        end
        else 
        begin
        	if Size = MaxSize+1 then begin
        		startIndex = 0;
        		endIndex = MaxSize;
        		NIndex = N - 1;
        	end else begin
        		startIndex = 1;
        		endIndex = Size;
        		NIndex = N;
        	end;
        	for x = startIndex to endIndex
        	begin
        		ntharrayA[x] = SourceArray[x];
        		ntharrayB[x] = x;
        	end;
        	for x = startIndex to endIndex - 1
        	begin
        		for y = x + 1 to endIndex
        		begin
        			if((DscAsc = 1 and ntharrayA[x] < ntharrayA[y] )or
        				(DscAsc = -1 and ntharrayA[x] > ntharrayA[y])) then
        			begin
        				temp = ntharrayA[x];
        				ntharrayA[x] = ntharrayA[y];
        				ntharrayA[y] = temp;
        				temp = ntharrayB[x];
        				ntharrayB[x] = ntharrayB[y];
        				ntharrayB[y] = temp;
        			end;
        		end;
        	end;
        	refExtremeValue = ntharrayA[NIndex];
        	refExtremeIndex = ntharrayB[NIndex];
        	NthExtremesarray = 1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthHighest(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthHighest
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthHighest.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremes(thePrice, Length, N, 1, _Output, value2);
        NthHighest = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthHighestArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthHighestArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthHighestArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremesArray(thePriceArray, Size, N, 1, _Output, value2);
        NthHighestArray = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthHighestBar(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthHighestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthHighestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremes(thePrice, Length, N, 1, value1, _Output);
        NthHighestBar = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthLowest(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthLowest
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthLowest.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremes(thePrice, Length, N, -1, _Output, value2);
        NthLowest = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthLowestArray(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthLowestArray
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthLowestArray.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremesArray( thePriceArray, Size, N, -1, _Output, value2) ;
        NthLowestArray = _Output ;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NthLowestBar(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NthLowestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\NthLowestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        NthExtremes(thePrice, Length, N, -1, value1, _Output);
        NthLowestBar = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def OHLCPeriodsAgo(df: pd.DataFrame, FreqType: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: OHLCPeriodsAgo
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\OHLCPeriodsAgo.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        	FreqType(numericsimple), 	//指定K棒頻率，1:日線、2:週線、3:月線、3.25:季、3.5 半年、4:年線
        	FreqAgo(numericsimple), 	//指定K棒位置
        	refFreqOpen(numericref), 	//輸出K棒開盤價
        	refFreqHigh(numericref),	//輸出K棒最高價
        	refFreqLow(numericref), 	//輸出K棒最低價
        	refFreqClose(numericref);	//輸出K棒收盤價
        	varBarFreqInt(-1),
        	varBarIndex(-1);
        array:
        	arrayO[200](-1),
        	arrayH[200](-1),
        	arrayL[200](-1),
        	arrayC[200](-1);
        switch (barfreq)
        begin
        	case "Tick":
        		varBarFreqInt = 0;
        	case "Min","Hour":
        		varBarFreqInt = 1;
        	case "D","AD":
        		varBarFreqInt = 2;
        	case "W","AW":
        		varBarFreqInt = 3;
        	case "M","AM","Q","H","Y":
        		varBarFreqInt = 4;
        	default:
        		varBarFreqInt = -1;
        end;
        if  FreqAgo > 200 or FreqAgo < 0 or varBarFreqInt = -1 or varBarFreqInt > FreqType + 1 then return;
        switch (FreqType)
        begin
        	case 2:
        		condition1 = WeekofYear(Date) <> WeekofYear(Date[1]) ;
        		if WeekofYear(Date[1]) =53 and  DayofWeek(Date)> DayofWeek(Date[1]) then condition1= false;
          	case 3:
        		condition1 = Month(Date) <> Month(Date[1]);
        	case 3.25:
        	    condition1 = Mod(Month(Date),3)=1 and Mod(Month(Date[1]),3)=0 ;
        	case 3.5:
        	    condition1 = Mod(Month(Date),6)=1 and Mod(Month(Date[1]),6)=0 ;
        	case 4:
        		condition1 = Year(Date) <> Year(Date[1]);
        	default:
        		condition1 = Date <> Date[1];
        end;
        condition1 = CurrentBar = 1 or condition1;
        if condition1 then
        begin
        	varBarIndex = varBarIndex - 1;
        	if varBarIndex < 0 then varBarIndex = FreqAgo;	
        	arrayO[varBarIndex] = Open;
        	arrayH[varBarIndex] = High;
        	arrayL[varBarIndex] = Low;
        	arrayC[varBarIndex] = Close;
        end
        else
        begin
        	arrayC[varBarIndex] = Close;
        	if High > arrayH[varBarIndex] then
        		arrayH[varBarIndex] = High;
        	if Low < arrayL[varBarIndex] then
        		arrayL[varBarIndex] = Low;
        end;
        refFreqOpen = arrayO[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
        refFreqHigh = arrayH[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
        refFreqLow = arrayL[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
        refFreqClose = arrayC[Mod( varBarIndex + FreqAgo, FreqAgo + 1) ];
        OHLCPeriodsAgo = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def QoQ(df: pd.DataFrame, QoQVal: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: QoQ
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\QoQ.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        if barfreq <> "Q" then
        	raiseruntimeerror("僅支援季頻率")
        else
        	QoQ = 100*(QoQVal/QoQVal[1]-1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SimpleHighest(df: pd.DataFrame, thePrice: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SimpleHighest
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\SimpleHighest.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        highValue = thePrice[0];
        for i = 1 to Length-1
        begin
          if thePrice[i] > highValue then
            highValue = thePrice[i];
        end;
        SimpleHighest = highValue; 	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SimpleHighestBar(df: pd.DataFrame, thePrice: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SimpleHighestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\SimpleHighestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        highValue = thePrice[0];
        barOffset = 0;
        for i = 1 to Length-1
        begin
          if thePrice[i] > highValue then begin
            highValue = thePrice[i];
        	barOffset = i;
          end;	
        end;
        SimpleHighestBar = barOffset; 	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SimpleLowest(df: pd.DataFrame, thePrice: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SimpleLowest
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\SimpleLowest.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        lowValue = thePrice[0];
        for i = 1 to Length-1
        begin
          if thePrice[i] < lowValue then
            lowValue = thePrice[i];
        end;
        SimpleLowest = lowValue; 	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SimpleLowestBar(df: pd.DataFrame, thePrice: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SimpleLowestBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\SimpleLowestBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        lowValue = thePrice[0];
        barOffset = 0;
        for i = 1 to Length-1
        begin
          if thePrice[i] < lowValue then begin
            lowValue = thePrice[i];
        	barOffset = i;
          end;	
        end;
        SimpleLowestBar = barOffset; 	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def YoY(df: pd.DataFrame, YoYVal: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: YoY
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\價格關係\YoY.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        switch(barfreq)
        begin
        	Case "M","AM":
        		YoY = RateOfChange(YoYVal,12);
        	Case "Q":
        		YoY = RateOfChange(YoYVal,4);
        	Case "Y":
        		YoY = RateOfChange(YoYVal,1);
        	default:
        		raiseruntimeerror("僅支援月、季、年頻率");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
