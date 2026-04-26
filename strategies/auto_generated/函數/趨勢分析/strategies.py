# Auto-generated strategies for: 函數/趨勢分析
import pandas as pd
import numpy as np

class 趨勢分析Strategies:

    @staticmethod
    def Angle(df: pd.DataFrame, Date1: str = "numeric") -> tuple[bool, str]:
        """
        Original Strategy: Angle
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\Angle.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        Date1Bar = getbaroffset(date1); Date1Price =Open[Date1Bar];
        Date2Bar = getbaroffset(date2); Date2Price =Close[Date2Bar];
        if Date1Bar > Date2Bar then 
           _Slope = (Date2Price/Date1Price-1)*100 / (Date1Bar-Date2Bar);
        Angle = arcTangent(_Slope);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Angleprice(df: pd.DataFrame, Date1: str = "numeric") -> tuple[bool, str]:
        """
        Original Strategy: Angleprice
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\Angleprice.xs
        XS Logic Reference:
        {@type:function}
        Date1Price =Open[Date1];
        value1=tan(ang);
        value2=date1price*(1+value1*date1/100);
        angleprice=value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DownTrend(df: pd.DataFrame, TheSeries: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: DownTrend
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\DownTrend.xs
        XS Logic Reference:
        {@type:function_bool}
        {
        	判斷某個序列是否趨勢朝下
        	注意事項:
        	- 判斷N日趨勢會判斷均線的趨勢, 所以資料必須要有Length*2以上
        	- 每次計算時會讀取近Length*2筆計算, 為了效能起見, 僅需在最新筆呼叫此函數即可
        	範例:
        	SetBackBar(2 * Length);			// 需有2倍的資料筆數	
        	SetTotalBar(2);					// 
        	if CurrentBar <> GetTotalBar() then return;
        	ret = DownTrend(Close, Length);		
        }
        {
        	底下是目前選股系統腳本使用的計算邏輯
        	Condition1 = rateofchange(TheSeries, Length) <= Length; 
        	Condition2 = TheSeries < TheSeries[Length/2]; 
        	Condition3 = TheSeries < average(TheSeries, Length); 
        	Condition4 = TheSeries <= TheSeries[1];
        	retval = condition1 and condition2 and condition3 and condition4; 
        }
        Array: TheSeriesArray[](0);
        Array: LongMA[](0);			// 儲存長MA (MA(Length))
        Array: ShortMA[](0);		// 儲存短MA (MA(Length/2))
        ArraySeries(TheSeries, Length, TheSeriesArray);
        // Value1 = Average(TheSeries, Length);
        // Value2 = Average(TheSeries, Length/2);
        ArrayMASeries(TheSeries, Length, LongMA);
        ArrayMASeries(TheSeries, ShortLength, ShortMA);
        if Length >= 10 then begin
        	retval = 
        		ShortMA[1] <= LongMA[1] and // Value2 <= Value1 and
        		ArrayLinearRegSlope(LongMA, Length) < 0 and //LinearRegSlope(Value1, Length) < 0 and 
        		ArrayLinearRegSlope(ShortMA, ShortLength) < 0 and //LinearRegSlope(Value2, Length/2) < 0 and
        		LongMA[1] <= LongMA[2] and // Value1 <= Value1[1] and
        		ShortMA[1] <= ShortMA[2] and // Value2 <= Value2[1] and
        		TheSeriesArray[1] <= TheSeriesArray[2]; // TheSeries <= TheSeries[1];		
        end else begin
        	retval = 
        		ArrayLinearRegSlope(LongMA, Length) < 0 and //LinearRegSlope(Value1, Length) < 0 and 
        		LongMA[1] <= LongMA[2] and // Value1 <= Value1[1] and
        		TheSeriesArray[1] <= TheSeriesArray[2]; // TheSeries <= TheSeries[1];		
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LinearReg(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple", target: str = "numericsimple", _slope: str = "numericref", _angle: str = "numericref", intercept: str = "numericref", forecast: str = "numericref") -> tuple[bool, str]:
        """
        Original Strategy: LinearReg
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\LinearReg.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
              sumX2(Length*(Length+1)*(2*Length+1)/6 ), //平方和
              sumY(0),
              SumXY(0),
              t_slope(0),
              tIntercept(0);
        sumX2 = Length*(Length+1)*(2*Length+1)/6;
        SumX = (Length* (Length+1))/2;
        LinearReg = -1;
        if Length < 1 then return;
        SumXY=0; SumY =0;
        for Xi = 1 to Length
        Begin
           SumXY += Xi* thePrice[ Length -Xi];
           SumY  += thePrice[ Length -Xi];
        End;
        t_slope = IFF((Length*SumX2 -Square(SumX))<>0,
                     ( Length *SumXY -SumX *SumY) / (Length*SumX2 -Square(SumX)),
        			 0);
        tIntercept = (SumY - t_slope*SumX)/Length;
        _slope =t_slope;
        _angle = arctangent(t_slope);
        intercept =tIntercept;
        forecast = intercept + _slope * (Length - target + ExecOffset);
        LinearReg = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LinearRegAngle(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: LinearRegAngle
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\LinearRegAngle.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        LinearReg(thePrice, Length, 0, value1, _Output, value3, value4);
        LinearRegAngle = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def LinearRegSlope(df: pd.DataFrame, thePrice: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: LinearRegSlope
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\LinearRegSlope.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        LinearReg(thePrice, Length, 0, _Output, value2, value3, value4);
        LinearRegSlope = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NDaysAngle(df: pd.DataFrame, Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: NDaysAngle
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\NDaysAngle.xs
        XS Logic Reference:
        {@type:function}
        {
        	計算股價N日走勢的角度
        	上漲趨勢回傳值 = 0 ~ 90
        	下跌趨勢回傳值 = 0 ~ -90
        }
        {
                              | y=<Close/Close[N]-1>
        					  |
        	------------------+ y=0
        	- Y軸的數值, 是Close/Close[N]-1, 
        	- 第一筆的數值是0, 如果上漲50%, 則數值 = 0.5, 如果上漲100%, 則數值=1
        	- consider: X邊如果是N, Y邊如果是0.5(上漲50%), 那算出來的斜率 x 2N之後, 表示這是一個x=1/y=1的三角形, 角度=45度角
        	上漲跟下跌的差異
        	- 上漲100%, 例如4元漲到8元 => y = 1
        	- 下跌50%, 例如8元跌到4元 => y = -0.5
        }
        array: thePriceArray[](0);
        // 定義N日上漲 x% = 45度
        //
        if Length <= 5 then angle45 = 30
        else if Length <= 10 then angle45 = 50
        else if Length <= 20 then angle45 = 75
        else if Length <= 60 then angle45 = 100
        else if Length <= 120 then angle45 = 150
        else angle45 = 200;
        // 底邊 = Length
        // 高度 = 上漲%
        //
        factor45 = Length / (0.01 * angle45);
        Array_SetMaxIndex(thePriceArray, Length);
        for idx = 1 to Length begin
        	thePriceArray[idx] = (Close[idx-1] / Close[Length-1] - 1) * factor45;
        end;
        value1 = ArrayLinearRegSlope(thePriceArray, Length);
        value2 = arctangent(value1);
        // 因為下跌最多就是100%, 所以算出來最多角度=-45度, 所以下跌角度會 x 2, 希望上漲角度/下跌角度可以在同一個scale內
        //
        if value2 < 0 then value2 = value2 * 2;
        retval = value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SwingHigh(df: pd.DataFrame, Price: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SwingHigh
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\SwingHigh.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        //價格序列、時間長度、左區間、右區間、第幾個峰值
        now = Rightstrength;
        cnt = 0;
        while cnt < occur and now < Length
        begin
        	success = 1;
        	tmpnow = now+1;
        	while success = 1 and tmpnow-now <= LeftStrength
        	begin
        		if Price[now] < Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow+1;
        	end;
        	tmpnow = now-1;
        	while success = 1 and now-tmpnow <= RightStrength
        	begin
        		if Price[now] <= Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow-1;
        	end;
        	if success = 1 then
        		cnt = cnt+1;
        	now = now+1;
        end;
        if cnt < occur then
        	SwingHigh = -1
        else
        	swingHigh = Price[now-1];
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SwingHighBar(df: pd.DataFrame, Price: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SwingHighBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\SwingHighBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        Price(numericseries), 
        Length(numericsimple), 
        LeftStrength(numericsimple), 
        RightStrength(numericsimple), 
        occur(numericsimple);
        //價格序列、時間長度、左區間、右區間、第幾個峰值
        now = Rightstrength;
        cnt = 0;
        while cnt < occur and now < Length
        begin
        	success = true;
        	tmpnow = now+1;
        	while success = true and tmpnow-now <= LeftStrength
        	begin
        		if Price[now] < Price[tmpnow] then
        			success = false
        		else tmpnow = tmpnow+1;
        	end;
        	tmpnow = now-1;
        	while success = true and now-tmpnow <= RightStrength
        	begin
        		if Price[now] <= Price[tmpnow] then
        			success = false
        		else tmpnow = tmpnow-1;
        	end;
        	if success = true then
        		cnt = cnt+1;
        	now = now+1;
        end;
        if cnt < occur then
        	swingHighBar  = -1
        else
        	swingHighBar  = now-1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SwingLow(df: pd.DataFrame, Price: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SwingLow
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\SwingLow.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        //價格序列、時間長度、左區間、右區間、第幾個峰值
        now = Rightstrength;
        cnt = 0;
        while cnt < occur and now < Length
        begin
        	success = 1;
        	tmpnow = now+1;
        	while success = 1 and tmpnow-now <= LeftStrength
        	begin
        		if Price[now] > Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow+1;
        	end;
        	tmpnow = now-1;
        	while success = 1 and now-tmpnow <= RightStrength
        	begin
        		if Price[now] >= Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow-1;
        	end;
        	if success = 1 then
        		cnt = cnt+1;
        	now = now+1;
        end;
        if cnt < occur then
        	SwingLow = -1
        else
        	swingLow = Price[now-1];
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SwingLowBar(df: pd.DataFrame, Price: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: SwingLowBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\SwingLowBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        //價格序列、時間長度、左區間、右區間、第幾個峰值
        now = Rightstrength;
        cnt = 0;
        while cnt < occur and now < Length
        begin
        	success = 1;
        	tmpnow = now+1;
        	while success = 1 and tmpnow-now <= LeftStrength
        	begin
        		if Price[now] > Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow+1;
        	end;
        	tmpnow = now-1;
        	while success = 1 and now-tmpnow <= RightStrength
        	begin
        		if Price[now] >= Price[tmpnow] then
        			success = 0
        		else tmpnow = tmpnow-1;
        	end;
        	if success = 1 then
        		cnt = cnt+1;
        	now = now+1;
        end;
        if cnt < occur then
        	SwingLowBar = -1
        else
        	SwingLowBar = now-1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TimeSeriesForecast(df: pd.DataFrame, thePrice: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: TimeSeriesForecast
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\TimeSeriesForecast.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        LinearReg(thePrice, Length, TgtBar, value1, value2, value3, _Output);
        TimeSeriesForecast = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TSELSindex(df: pd.DataFrame, Length: str = "numeric", LowLimit: str = "numeric") -> tuple[bool, str]:
        """
        Original Strategy: TSELSindex
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\TSELSindex.xs
        XS Logic Reference:
        {@type:function}
        {
        函數說明
        https://www.xq.com.tw/xstrader/打造自己的大盤多空函數/
        }
        SetBarMode(1);
        if countif(GetSymbolField("tse.tw","外資買賣超金額","D") > 0,Length) >= LowLimit
        and GetSymbolField("tse.tw","外資買賣超金額","D") > 0 then
        	value1 = 1
        else
        	value1 = 0;
        tselsindex = value1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TSEMFI(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: TSEMFI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\TSEMFI.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        tp = (getsymbolfield("TSE.TW","最高價")+getsymbolfield("TSE.TW","最低價")+getsymbolfield("TSE.TW","收盤價")) /3;
        tv = tp * getsymbolfield("TSE.TW","成交量");
        if tp > tp[1] then begin
        	utv = tv;
        	dtv = 0;
        end else begin
        	utv = 0;
        	dtv = tv;
        end;
        pmf = Average(utv, MinList(CurrentBar, 6));
        nmf = Average(dtv, MinList(CurrentBar, 6));
        if CurrentBar < 6 or (pmf + nmf) = 0 then
        	mfivalue = 50
        else 
        	mfivalue = 100 * pmf /(pmf + nmf);
        if mfivalue > 50 then
        	tsemfi = 1
        else
        	tsemfi = 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def UpShadow(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: UpShadow
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\UpShadow.xs
        XS Logic Reference:
        {@type:function}
        //上影線佔實體比例
        SetBarMode(1);
        if range = 0 then
        	upshadow = 0
        else 
        	upshadow = (high - maxlist(open,close)) / range;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def UpTrend(df: pd.DataFrame, TheSeries: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: UpTrend
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\趨勢分析\UpTrend.xs
        XS Logic Reference:
        {@type:function_bool}
        {
        	判斷某個序列是否趨勢朝上
        	注意事項:
        	- 判斷N日趨勢會判斷均線的趨勢, 所以資料必須要有Length*2以上
        	- 每次計算時會讀取近Length*2筆計算, 為了效能起見, 僅需在最新筆呼叫此函數即可
        	範例:
        	SetBackBar(2 * Length);			// 需有2倍的資料筆數	
        	SetTotalBar(2);					// 
        	if CurrentBar <> GetTotalBar() then return;
        	ret = UpTrend(Close, Length);	
        }
        {
        	底下是目前選股系統腳本使用的計算邏輯
        	Condition1 = rateofchange(TheSeries, Length) >= Length; 
        	Condition2 = TheSeries > TheSeries[Length/2]; 
        	Condition3 = TheSeries > average(TheSeries, Length); 
        	Condition4 = TheSeries >= TheSeries[1];
        	retval = condition1 and condition2 and condition3 and condition4; 	
        }
        Array: TheSeriesArray[](0);
        Array: LongMA[](0);			// 儲存長MA (MA(Length))
        Array: ShortMA[](0);		// 儲存短MA (MA(Length/2))
        ArraySeries(TheSeries, Length, TheSeriesArray);
        // Value1 = Average(TheSeries, Length);
        // Value2 = Average(TheSeries, Length/2);
        ArrayMASeries(TheSeries, Length, LongMA);
        ArrayMASeries(TheSeries, ShortLength, ShortMA);
        if Length >= 10 then begin
        	retval = 
        		ShortMA[1] >= LongMA[1] and // Value2 >= Value1 and
        		ArrayLinearRegSlope(LongMA, Length) > 0 and //LinearRegSlope(Value1, Length) > 0 and 
        		ArrayLinearRegSlope(ShortMA, ShortLength) > 0 and //LinearRegSlope(Value2, Length/2) > 0 and
        		LongMA[1] >= LongMA[2] and // Value1 >= Value1[1] and
        		ShortMA[1] >= ShortMA[2] and // Value2 >= Value2[1] and
        		TheSeriesArray[1] >= TheSeriesArray[2]; // TheSeries >= TheSeries[1];
        end else begin
        	retval = 
        		ArrayLinearRegSlope(LongMA, Length) > 0 and //LinearRegSlope(Value1, Length) > 0 and 
        		LongMA[1] >= LongMA[2] and // Value1 >= Value1[1] and
        		TheSeriesArray[1] >= TheSeriesArray[2]; // TheSeries >= TheSeries[1];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
