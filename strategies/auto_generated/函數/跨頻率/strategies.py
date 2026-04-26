# Auto-generated strategies for: 函數/跨頻率
import pandas as pd
import numpy as np

class 跨頻率Strategies:

    @staticmethod
    def xfMin_CrossOver(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_CrossOver
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_CrossOver.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入兩個序列(跟目前的頻率不同), 判斷是否crossover
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // SeriesA, SeriesB是傳入的序列
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string), 
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        posA = 0;
        posB = 0;
        valA = xfMin_getvalue(FreqType, SeriesA, posA);
        valB = xfMin_getvalue(FreqType, SeriesB, posB);
        if valA <= valB then
        begin
        	xfMin_CrossOver = false;
        	return;
        end; 
        for idx = 1 to 6
        begin
        	posA = posA + 1;
        	posB = posB + 1;
        	valA = xfMin_getvalue(FreqType, SeriesA, posA);
        	valB = xfMin_getvalue(FreqType, SeriesB, posB);
        	if valA < valB then
        	begin
        		xfMin_CrossOver = true;
        		return;
        	end
        	else
        	begin
        		if valA > valB then
        		begin
        			xfMin_CrossOver = false;
        			return;
        		end;
        	end; 
        end;
        xfMin_CrossOver = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_CrossUnder(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_CrossUnder
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_CrossUnder.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入兩個序列(跟目前的頻率不同), 判斷是否crossunder
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // SeriesA, SeriesB是傳入的序列
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string), 
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        posA = 0;
        posB = 0;
        valA = xfMin_getvalue(FreqType, SeriesA, posA);
        valB = xfMin_getvalue(FreqType, SeriesB, posB);
        if valA >= valB then
        begin
        	xfMin_CrossUnder = false;
        	return;
        end; 
        for idx = 1 to 6
        begin
        	posA = posA + 1;
        	posB = posB + 1;
        	valA = xfMin_getvalue(FreqType, SeriesA, posA);
        	valB = xfMin_getvalue(FreqType, SeriesB, posB);
        	if valA > valB then
        	begin
        		xfMin_CrossUnder = true;
        		return;
        	end
        	else
        	begin
        		if valA < valB then
        		begin
        			xfMin_CrossUnder = false;
        			return;
        		end;
        	end; 
        end;
        xfMin_CrossUnder = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_DirectionMovement(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_DirectionMovement
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_DirectionMovement.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率DirectionMovement function (for DMI相關指標)
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, Length
        // Return: pdi_value(+di), ndi_value(-di), adx_value(adx)
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string),		//引用頻率
        	length(numericsimple),	//計算期間
        	pdi_value(numericref),	//回傳+DI
        	ndi_value(numericref),	//回傳-DI
        	adx_value(numericref);	//回傳ADX
        	padm(0), nadm(0), radx(0),
        	LastPAdm(0), LastNAdm(0), LastRAdx(0), LastATR(0),
        	atr(0), pdm(0), ndm(0), tr(0),
        	dValue0(0), dValue1(0), dx(0),
        	changeHigh(0),changeLow(0),closePeriod(0),
        	idx(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        //跨頻率會用到的前期值需要手動記錄
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, GetFielddate("Date")) <> xfMin_getdtvalue(FreqType, GetFielddate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);
        if condition1 then
        begin
        	LastPAdm = padm[1];
        	LastNAdm = nadm[1];
        	LastRAdx = radx[1];
        	LastATR = atr[1];
        end;
        //取得跨頻率會用到的變數值
        switch (FreqType)
        begin
        	case  "1":
        		if GetField("Close", "1")[1] > GetField("High", "1") then
        			tr = GetField("Close", "1")[1] - GetField("Low", "1")
        		else if GetField("Close", "1")[1] < GetField("Low", "1") then
        			tr = GetField("High", "1") - GetField("Close", "1")[1]
        		else
        			tr = GetField("High", "1") - GetField("Low", "1");
        		changeHigh = GetField("High", "1") - GetField("High", "1")[1];
        		changeLow = GetField("Low", "1")[1] - GetField("Low", "1");
        		closePeriod = GetField("Close", "1");
        	case  "2":
        		if GetField("Close", "2")[1] > GetField("High", "2") then
        			tr = GetField("Close", "2")[1] - GetField("Low", "2")
        		else if GetField("Close", "2")[1] < GetField("Low", "2") then
        			tr = GetField("High", "2") - GetField("Close", "2")[1]
        		else
        			tr = GetField("High", "2") - GetField("Low", "2");
        		changeHigh = GetField("High", "2") - GetField("High", "2")[1];
        		changeLow = GetField("Low", "2")[1] - GetField("Low", "2");
        		closePeriod = GetField("Close", "2");
        	case  "3":
        		if GetField("Close", "3")[1] > GetField("High", "3") then
        			tr = GetField("Close", "3")[1] - GetField("Low", "3")
        		else if GetField("Close", "3")[1] < GetField("Low", "3") then
        			tr = GetField("High", "3") - GetField("Close", "3")[1]
        		else
        			tr = GetField("High", "3") - GetField("Low", "3");
        		changeHigh = GetField("High", "3") - GetField("High", "3")[1];
        		changeLow = GetField("Low", "3")[1] - GetField("Low", "3");
        		closePeriod = GetField("Close", "3");
        	case  "5":
        		if GetField("Close", "5")[1] > GetField("High", "5") then
        			tr = GetField("Close", "5")[1] - GetField("Low", "5")
        		else if GetField("Close", "5")[1] < GetField("Low", "5") then
        			tr = GetField("High", "5") - GetField("Close", "5")[1]
        		else
        			tr = GetField("High", "5") - GetField("Low", "5");
        		changeHigh = GetField("High", "5") - GetField("High", "5")[1];
        		changeLow = GetField("Low", "5")[1] - GetField("Low", "5");
        		closePeriod = GetField("Close", "5");
        	case "10":
        		if GetField("Close", "10")[1] > GetField("High", "10") then
        			tr = GetField("Close", "10")[1] - GetField("Low", "10")
        		else if GetField("Close", "10")[1] < GetField("Low", "10") then
        			tr = GetField("High", "10") - GetField("Close", "10")[1]
        		else
        			tr = GetField("High", "10") - GetField("Low", "10");
        		changeHigh = GetField("High", "10") - GetField("High", "10")[1];
        		changeLow = GetField("Low", "10")[1] - GetField("Low", "10");
        		closePeriod = GetField("Close", "10");
        	case "15":
        		if GetField("Close", "15")[1] > GetField("High", "15") then
        			tr = GetField("Close", "15")[1] - GetField("Low", "15")
        		else if GetField("Close", "15")[1] < GetField("Low", "15") then
        			tr = GetField("High", "15") - GetField("Close", "15")[1]
        		else
        			tr = GetField("High", "15") - GetField("Low", "15");
        		changeHigh = GetField("High", "15") - GetField("High", "15")[1];
        		changeLow = GetField("Low", "15")[1] - GetField("Low", "15");
        		closePeriod = GetField("Close", "15");
        	case "30":
        		if GetField("Close", "30")[1] > GetField("High", "30") then
        			tr = GetField("Close", "30")[1] - GetField("Low", "30")
        		else if GetField("Close", "30")[1] < GetField("Low", "30") then
        			tr = GetField("High", "30") - GetField("Close", "30")[1]
        		else
        			tr = GetField("High", "30") - GetField("Low", "30");
        		changeHigh = GetField("High", "30") - GetField("High", "30")[1];
        		changeLow = GetField("Low", "30")[1] - GetField("Low", "30");
        		closePeriod = GetField("Close", "30");
        	case "60":
        		if GetField("Close", "60")[1] > GetField("High", "60") then
        			tr = GetField("Close", "60")[1] - GetField("Low", "60")
        		else if GetField("Close", "60")[1] < GetField("Low", "60") then
        			tr = GetField("High", "60") - GetField("Close", "60")[1]
        		else
        			tr = GetField("High", "60") - GetField("Low", "60");
        		changeHigh = GetField("High", "60") - GetField("High", "60")[1];
        		changeLow = GetField("Low", "60")[1] - GetField("Low", "60");
        		closePeriod = GetField("Close", "60");
        	case "D":
        		if GetField("Close", "D")[1] > GetField("High", "D") then
        			tr = GetField("Close", "D")[1] - GetField("Low", "D")
        		else if GetField("Close", "D")[1] < GetField("Low", "D") then
        			tr = GetField("High", "D") - GetField("Close", "D")[1]
        		else
        			tr = GetField("High", "D") - GetField("Low", "D");
        		changeHigh = GetField("High", "D") - GetField("High", "D")[1];
        		changeLow = GetField("Low", "D")[1] - GetField("Low", "D");
        		closePeriod = GetField("Close", "D");
        	case "W":
        		if GetField("Close", "W")[1] > GetField("High", "W") then
        			tr = GetField("Close", "W")[1] - GetField("Low", "W")
        		else if GetField("Close", "W")[1] < GetField("Low", "W") then
        			tr = GetField("High", "W") - GetField("Close", "W")[1]
        		else
        			tr = GetField("High", "W") - GetField("Low", "W");
        		changeHigh = GetField("High", "W") - GetField("High", "W")[1];
        		changeLow = GetField("Low", "W")[1] - GetField("Low", "W");
        		closePeriod = GetField("Close", "W");
        	case "M":
        		if GetField("Close", "M")[1] > GetField("High", "M") then
        			tr = GetField("Close", "M")[1] - GetField("Low", "M")
        		else if GetField("Close", "M")[1] < GetField("Low", "M") then
        			tr = GetField("High", "M") - GetField("Close", "M")[1]
        		else
        			tr = GetField("High", "M") - GetField("Low", "M");
        		changeHigh = GetField("High", "M") - GetField("High", "M")[1];
        		changeLow = GetField("Low", "M")[1] - GetField("Low", "M");
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		if GetField("Close", "AD")[1] > GetField("High", "AD") then
        			tr = GetField("Close", "AD")[1] - GetField("Low", "AD")
        		else if GetField("Close", "AD")[1] < GetField("Low", "AD") then
        			tr = GetField("High", "AD") - GetField("Close", "AD")[1]
        		else
        			tr = GetField("High", "AD") - GetField("Low", "AD");
        		changeHigh = GetField("High", "AD") - GetField("High", "AD")[1];
        		changeLow = GetField("Low", "AD")[1] - GetField("Low", "AD");
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		if GetField("Close", "AW")[1] > GetField("High", "AW") then
        			tr = GetField("Close", "AW")[1] - GetField("Low", "AW")
        		else if GetField("Close", "AW")[1] < GetField("Low", "AW") then
        			tr = GetField("High", "AW") - GetField("Close", "AW")[1]
        		else
        			tr = GetField("High", "AW") - GetField("Low", "AW");
        		changeHigh = GetField("High", "AW") - GetField("High", "AW")[1];
        		changeLow = GetField("Low", "AW")[1] - GetField("Low", "AW");
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		if GetField("Close", "AM")[1] > GetField("High", "AM") then
        			tr = GetField("Close", "AM")[1] - GetField("Low", "AM")
        		else if GetField("Close", "AM")[1] < GetField("Low", "AM") then
        			tr = GetField("High", "AM") - GetField("Close", "AM")[1]
        		else
        			tr = GetField("High", "AM") - GetField("Low", "AM");
        		changeHigh = GetField("High", "AM") - GetField("High", "AM")[1];
        		changeLow = GetField("Low", "AM")[1] - GetField("Low", "AM");
        		closePeriod = GetField("Close", "AM");
        	default:
        		if Close[1] > High then
        			tr = Close[1] - Low
        		else if Close[1] < Low then
        			tr = High - Close[1]
        		else
        			tr = High - Low;
        		changeHigh = High - High[1];
        		changeLow = Low[1] - Low;
        		closePeriod = Close;
        end;
        //原始的技術指標計算
        value1 = xfMin_GetCurrentBar(FreqType);
        if value1 = 1 then
         begin
        	padm = closePeriod / 10000;
        	nadm = padm;
        	atr = padm * 5;
        	radx = 20;
         end
        else
         begin
        	pdm = maxlist(changeHigh, 0);
        	ndm = maxlist(changeLow, 0);
        	if pdm < ndm then
        		pdm = 0
        	else 
        	  begin
        		if pdm > ndm then
        			ndm = 0
        		else
        		  begin
        			pdm = 0;
        			ndm = 0;
        		  end;		
        	  end;
        	padm = LastPAdm + (pdm - LastPAdm) / length;
        	nadm = LastNAdm + (ndm - LastNAdm) / length;
        	atr = LastATR + (tr - LastATR) / length;
        	if atr <> 0 then begin
        		dValue0 = 100 * padm / atr;
        		dValue1 = 100 * nadm / atr;
        	end;
        	if dValue0 + dValue1 <> 0 then
        		dx = AbsValue(100 * (dValue0 - dValue1) / (dValue0 + dValue1));
        	radx = LastRAdx + (dx - LastRAdx) / length;
         end;
        pdi_value = dValue0;
        ndi_value = dValue1;
        adx_value = radx;
        xfMin_directionmovement = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_EMA(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_EMA
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_EMA.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率EMA
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, Series, Length
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	Factor(0), lastEMA(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);
        if condition1 then
        	lastEMA = xfMin_EMA[1];
        value1 = xfMin_GetCurrentBar(FreqType);
        if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);
        if value1 = 1 then
        	xfMin_EMA = Series
        else if value1 <= Length then
            xfMin_EMA = (Series + (lastEMA * (value1 - 1)))/value1	
        else
        	xfMin_EMA = lastEMA + Factor * (Series - lastEMA);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_GetBoolean(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_GetBoolean
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_GetBoolean.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // TFSeries是傳入的布林序列
        // poi是要取得的位置
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        // 
        	FreqType(string), 
        	TFSeries(truefalseseries),
        	poi(numeric);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        _pos = poi; 
        if _pos <= 0 then
        	xfMin_GetBoolean = TFSeries[0]
        else
        begin
        	idx = 0;
        	while _pos > 0 and idx < currentbar-1
        	begin
        		switch (FreqType)
        		begin
        			case "1","2","3","5","10","15","30","60":
        				dt = xfMin_getdtvalue(FreqType, datetime[idx]);
        				dt2 = xfMin_getdtvalue(FreqType, datetime[idx+1]);
        				if dt <> dt2 then _pos = _pos - 1; 
        				idx = idx + 1;			  		 
        			default:
        				dt = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx]);
        				dt2 = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
        				if dt <> dt2 then _pos = _pos - 1; 
        				idx = idx + 1;
        		end;
        	end;
        	xfMin_GetBoolean = TFSeries[idx];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_GetCurrentBar(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_GetCurrentBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_GetCurrentBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 取得指定頻率的K棒編號（CurrentBar）
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string);		//引用頻率
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
        if currentbar = 1 then 
        	xfMin_GetCurrentBar = 1
        else if condition1 then
        	xfMin_GetCurrentBar = xfMin_GetCurrentBar[1] + 1
        else
        	xfMin_GetCurrentBar = xfMin_GetCurrentBar[1];
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_GetDTValue(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_GetDTValue
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_GetDTValue.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 回傳某個日期的'normalized' value
        // 用這個value來比對是否已經跨期
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // dtValue 是目前資料序列上面的Date
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string), 
        	dtValue(numeric);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        switch (FreqType)
        begin
        	case "1","2","3","5","10","15","30","60":
        		// 回傳分鐘線的日期時間YYYYMMDDhhmmss。例如：2018/9/10 12:03:59的五分線會回傳20180910120000
        		if symbolExchange="TF" then begin
        			if dtValue < 19870106000000 then begin
        				xfMin_GetDTValue = dtValue;
        				return;
        			end;
        			value1 = strtonum(FreqType);
        			value2 = strtonum(rightstr(numtostr(dtValue,0),6));
        			if value2>=084500 and value2<150000 then value20=084500
        			else if value2 >=150000 then value20=150000
        			else value20=000000;
        			value21= timediff(value2,value20,"M");
        			value3 = IntPortion(value21 / value1) * value1;
        			value31= timeadd(value20,"M",value3);
        			xfMin_GetDTValue = dtValue - value2 + value31;
        		end 
        		else begin
        			if dtValue < 19870106000000 then begin
        				xfMin_GetDTValue = dtValue;
        				return;
        			end;
        			value1 = strtonum(FreqType);
        			value2 = strtonum(rightstr(numtostr(dtValue,0),6));
        			value3 = IntPortion(minute(value2) / value1) * value1;
        			xfMin_GetDTValue = dtValue - value2 + EncodeTime(hour(value2), value3, 0);	
        		end;
        	case "D" , "AD":
        		// 回傳YYYYMMDD
        		xfMin_GetDTValue = dtValue;
        	case "W" , "AW":
        		// 年度 * 100 + 周別, e.g. 201001, 表示是2010年的第一週
        		xfMin_GetDTValue = Year(dtValue) * 100 + WeekofYear(dtValue);
        		// 每年的第一週需要判斷是否和去年的最後一週重疊 
        		if WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) = 53 then 
        			xfMin_GetDTValue = Year(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) * 100 + WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue)));
        	case "M" , "AM":
        		// 年度 * 100 + 月別, e.g. 201001, 表示是2010年的第一個月
        		xfMin_GetDTValue = Year(dtValue) * 100 + Month(dtValue);
        	default:
        		xfMin_GetDTValue = dtValue;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_GetValue(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_GetValue
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_GetValue.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // PriceSeries是傳入的序列
        // poi是要取得的位置
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        // 
        	FreqType(string), 
        	PriceSeries(numericseries),
        	poi(numeric);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        _pos = poi; 
        if _pos <= 0 then
        	xfMin_GetValue = PriceSeries[0]
        else
        begin
        	idx = 0;
        	while _pos > 0 and idx < currentbar-1
        	begin
        		switch (FreqType)
        		begin
        			case "1","2","3","5","10","15","30","60":
        				dt = xfMin_getdtvalue(FreqType, datetime[idx]);
        				dt2 = xfMin_getdtvalue(FreqType, datetime[idx+1]);
        				if dt <> dt2 then _pos = _pos - 1; 
        				idx = idx + 1;			  		 
        			default:
        				dt = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx]);
        				dt2 = xfMin_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
        				if dt <> dt2 then _pos = _pos - 1; 
        				idx = idx + 1;
        		end;
        	end;
        	xfMin_GetValue = PriceSeries[idx];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_MACD(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_MACD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_MACD.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率MACD函數
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, FastLength, SlowLength, MACDLength;
        // 輸出: DifValue, MACDValue, OscValue;
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        	FreqType(string),		//引用頻率
        	Price(numericseries), 	
        	FastLength(numericsimple), SlowLength(numericsimple), MACDLength(numericsimple),
        	DifValue(numericref), MACDValue(numericref), OscValue(numericref);
        DifValue = xfMin_XAverage(FreqType, Price, FastLength) - xfMin_XAverage(FreqType, Price, SlowLength);
        MACDValue = xfMin_XAverage(FreqType, DifValue, MACDLength);
        OscValue = DifValue - MACDValue;
        xfMin_macd = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfmin_MTM(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfmin_MTM
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfmin_MTM.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率MTM函數(for MTM指標)
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, Series, Length
        //
        	FreqType(string),		//引用頻率
        	Length(numericsimple);	//計算期間
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        switch (FreqType)
        begin
        	case  "1":
        		xfMin_MTM = GetField("收盤價", "1") - GetField("收盤價", "1")[length];
        	case  "2":
        		xfMin_MTM = GetField("收盤價", "2") - GetField("收盤價", "2")[length];
        	case  "3":
        		xfMin_MTM = GetField("收盤價", "3") - GetField("收盤價", "3")[length];
        	case  "5":
        		xfMin_MTM = GetField("收盤價", "5") - GetField("收盤價", "5")[length];
        	case "10":
        		xfMin_MTM = GetField("收盤價", "10") - GetField("收盤價", "10")[length];
        	case "15":
        		xfMin_MTM = GetField("收盤價", "15") - GetField("收盤價", "15")[length];
        	case "30":
        		xfMin_MTM = GetField("收盤價", "30") - GetField("收盤價", "30")[length];
        	case "60":
        		xfMin_MTM = GetField("收盤價", "60") - GetField("收盤價", "60")[length];
        	case "D":
        		xfMin_MTM = GetField("收盤價", "D") - GetField("收盤價", "D")[length];
        	case "W":
        		xfMin_MTM = GetField("收盤價", "W") - GetField("收盤價", "W")[length];
        	case "M":
        		xfMin_MTM = GetField("收盤價", "M") - GetField("收盤價", "M")[length];
        	case "AD":
        		xfMin_MTM = GetField("收盤價", "AD") - GetField("收盤價", "AD")[length];
        	case "AW":
        		xfMin_MTM = GetField("收盤價", "AW") - GetField("收盤價", "AW")[length];
        	case "AM":
        		xfMin_MTM = GetField("收盤價", "AM") - GetField("收盤價", "AM")[length];
        	default:
        		xfMin_MTM = close - close[length];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_PercentR(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_PercentR
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_PercentR.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率PercentR函數(for 威廉指標)
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
        // 輸出: rsv_value, k_value, d_value
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string), 
        	Length(numericsimple);
        	maxHigh(0), minLow(0),variableA(0),variableB(0),closePeriod(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        switch (upperstr(FreqType))
        begin
        	case  "1":
        		maxHigh = simplehighest(GetField("High", "1"),Length);
        		minLow = simplelowest(GetField("Low", "1"),Length);
        		closePeriod = GetField("Close", "1");	
        	case  "2":
        		maxHigh = simplehighest(GetField("High", "2"),Length);
        		minLow = simplelowest(GetField("Low", "2"),Length);
        		closePeriod = GetField("Close", "2");	
        	case  "3":
        		maxHigh = simplehighest(GetField("High", "3"),Length);
        		minLow = simplelowest(GetField("Low", "3"),Length);
        		closePeriod = GetField("Close", "3");	
        	case  "5":
        		maxHigh = simplehighest(GetField("High", "5"),Length);
        		minLow = simplelowest(GetField("Low", "5"),Length);
        		closePeriod = GetField("Close", "5");
        	case "10":
        		maxHigh = simplehighest(GetField("High", "10"),Length);
        		minLow = simplelowest(GetField("Low", "10"),Length);
        		closePeriod = GetField("Close", "10");
        	case "15":
        		maxHigh = simplehighest(GetField("High", "15"),Length);
        		minLow = simplelowest(GetField("Low", "15"),Length);
        		closePeriod = GetField("Close", "15");
        	case "30":
        		maxHigh = simplehighest(GetField("High", "30"),Length);
        		minLow = simplelowest(GetField("Low", "30"),Length);
        		closePeriod = GetField("Close", "30");
        	case "60":
        		maxHigh = simplehighest(GetField("High", "60"),Length);
        		minLow = simplelowest(GetField("Low", "60"),Length);
        		closePeriod = GetField("Close", "60");
        	case "D":
        		maxHigh = simplehighest(GetField("High", "D"),Length);
        		minLow = simplelowest(GetField("Low", "D"),Length);
        		closePeriod = GetField("Close", "D");
        	case "W":
        		maxHigh = simplehighest(GetField("High", "W"),Length);
        		minLow = simplelowest(GetField("Low", "W"),Length);
        		closePeriod = GetField("Close", "W");
        	case "M":
        		maxHigh = simplehighest(GetField("High", "M"),Length);
        		minLow = simplelowest(GetField("Low", "M"),Length);
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		maxHigh = simplehighest(GetField("High", "AD"),Length);
        		minLow = simplelowest(GetField("Low", "AD"),Length);
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		maxHigh = simplehighest(GetField("High", "AW"),Length);
        		minLow = simplelowest(GetField("Low", "AW"),Length);
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		maxHigh = simplehighest(GetField("High", "AM"),Length);
        		minLow = simplelowest(GetField("Low", "AM"),Length);
        		closePeriod = GetField("Close", "AM");
        	default:
        		maxHigh = simplehighest(High,Length);
        		minLow = simplelowest(Low,Length);
        		closePeriod = Close;
        end;
        variableB = maxHigh - minLow;
        if variableB <> 0 then  
        	xfMin_PercentR = 100 - ((maxHigh - closePeriod) / variableB) * 100
        else 
        	xfMin_PercentR = 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_RSI(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_RSI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_RSI.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率RSI函數
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, Series, Length
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	SumUp(0), SumDown(0), 
        	LastSumUp(0), LastSumDown(0),LastRefSeries(Series), 
        	up(0), down(0),
        	closePeriod(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
        if condition1 then
        begin
        	LastSumUp = SumUp[1];
        	LastSumDown = SumDown[1];
        	LastRefSeries = Series[1];
        end;
        if xfMin_GetCurrentBar(FreqType) = 1 then
          begin
        	SumUp = Average(maxlist(Series - LastRefSeries, 0), Length); 
        	SumDown = Average(maxlist(LastRefSeries - Series, 0), Length); 
          end
        else
          begin
        	up = maxlist(Series - LastRefSeries, 0);
        	down = maxlist(LastRefSeries - Series, 0);
        	SumUp = LastSumUp + (up - LastSumUp) / Length;
        	SumDown = LastSumDown + (down - LastSumDown) / Length;
          end;
        if SumUp + SumDown = 0 then
        	xfMin_RSI = 0
        else
        	xfMin_RSI = 100 * SumUp / (SumUp + SumDown);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_Stochastic(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_Stochastic
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_Stochastic.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率Stochastic函數(for KD/RSV相關指標)
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
        // 輸出: rsv_value, k_value, d_value
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string), 
        	Length(numericsimple), rsvt(numericsimple), kt(numericsimple),
        	rsv(numericref), k(numericref), d(numericref);
        	maxHigh(0), minLow(0),lastK(50),lastD(50),closePeriod(0);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);	
        if condition1 then
        begin
        	lastK = k[1];
        	lastD = d[1];
        end;
        switch (FreqType)
        begin
        	case  "1":
        		maxHigh = simplehighest(GetField("High", "1"),Length);
        		minLow = simplelowest(GetField("Low", "1"),Length);
        		closePeriod = GetField("Close", "1");
        	case  "2":
        		maxHigh = simplehighest(GetField("High", "2"),Length);
        		minLow = simplelowest(GetField("Low", "2"),Length);
        		closePeriod = GetField("Close", "2");
        	case  "3":
        		maxHigh = simplehighest(GetField("High", "3"),Length);
        		minLow = simplelowest(GetField("Low", "3"),Length);
        		closePeriod = GetField("Close", "3");
        	case  "5":
        		maxHigh = simplehighest(GetField("High", "5"),Length);
        		minLow = simplelowest(GetField("Low", "5"),Length);
        		closePeriod = GetField("Close", "5");
        	case "10":
        		maxHigh = simplehighest(GetField("High", "10"),Length);
        		minLow = simplelowest(GetField("Low", "10"),Length);
        		closePeriod = GetField("Close", "10");
        	case "15":
        		maxHigh = simplehighest(GetField("High", "15"),Length);
        		minLow = simplelowest(GetField("Low", "15"),Length);
        		closePeriod = GetField("Close", "15");
        	case "30":
        		maxHigh = simplehighest(GetField("High", "30"),Length);
        		minLow = simplelowest(GetField("Low", "30"),Length);
        		closePeriod = GetField("Close", "30");
        	case "60":
        		maxHigh = simplehighest(GetField("High", "60"),Length);
        		minLow = simplelowest(GetField("Low", "60"),Length);
        		closePeriod = GetField("Close", "60");
        	case "D":
        		maxHigh = simplehighest(GetField("High", "D"),Length);
        		minLow = simplelowest(GetField("Low", "D"),Length);
        		closePeriod = GetField("Close", "D");
        	case "W":
        		maxHigh = simplehighest(GetField("High", "W"),Length);
        		minLow = simplelowest(GetField("Low", "W"),Length);
        		closePeriod = GetField("Close", "W");
        	case "M":
        		maxHigh = simplehighest(GetField("High", "M"),Length);
        		minLow = simplelowest(GetField("Low", "M"),Length);
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		maxHigh = simplehighest(GetField("High", "AD"),Length);
        		minLow = simplelowest(GetField("Low", "AD"),Length);
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		maxHigh = simplehighest(GetField("High", "AW"),Length);
        		minLow = simplelowest(GetField("Low", "AW"),Length);
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		maxHigh = simplehighest(GetField("High", "AM"),Length);
        		minLow = simplelowest(GetField("Low", "AM"),Length);
        		closePeriod = GetField("Close", "AM");
        	default:
        		maxHigh = simplehighest(High,Length);
        		minLow = simplelowest(Low,Length);
        		closePeriod = Close;
        end;
        if maxHigh <> minLow then
        	rsv = 100 * (closePeriod - minLow) / (maxHigh - minLow)
        else
        	rsv = 50;
        if currentbar = 1 then
        begin
        	k = 50;
        	d = 50;
        end
        else
        begin
        	k = (lastK * (rsvt - 1) + rsv) / rsvt;
        	d = (lastD * (kt - 1) + k) / kt;
        end; 
        xfMin_Stochastic = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_WeightedClose(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_WeightedClose
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_WeightedClose.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率WeightedClose函數
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string);
        if getinfo("Instance")=3 or getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        switch (UpperStr(FreqType))
        begin
        	case  "1":
        		xfMin_WeightedClose = (2 * GetField("Close", "1") + GetField("High", "1") + GetField("Low", "1")) / 4;
        	case  "2":
        		xfMin_WeightedClose = (2 * GetField("Close", "2") + GetField("High", "2") + GetField("Low", "2")) / 4;
        	case  "3":
        		xfMin_WeightedClose = (2 * GetField("Close", "3") + GetField("High", "3") + GetField("Low", "3")) / 4;
        	case  "5":
        		xfMin_WeightedClose = (2 * GetField("Close", "5") + GetField("High", "5") + GetField("Low", "5")) / 4;	
        	case "10":
        		xfMin_WeightedClose = (2 * GetField("Close", "10") + GetField("High", "10") + GetField("Low", "10")) / 4;	
        	case "15":
        		xfMin_WeightedClose = (2 * GetField("Close", "15") + GetField("High", "15") + GetField("Low", "15")) / 4;	
        	case "30":
        		xfMin_WeightedClose = (2 * GetField("Close", "30") + GetField("High", "30") + GetField("Low", "30")) / 4;	
        	case "60":
        		xfMin_WeightedClose = (2 * GetField("Close", "60") + GetField("High", "60") + GetField("Low", "60")) / 4;
        	case "D":
        		xfMin_WeightedClose = (2 * GetField("Close", "D") + GetField("High", "D") + GetField("Low", "D")) / 4;
        	case "W":
        		xfMin_WeightedClose = (2 * GetField("Close", "W") + GetField("High", "W") + GetField("Low", "W")) / 4;
        	case "M":
        		xfMin_WeightedClose = (2 * GetField("Close", "M") + GetField("High", "M") + GetField("Low", "M")) / 4;
        	case "AD":
        		xfMin_WeightedClose = (2 * GetField("Close", "AD") + GetField("High", "AD") + GetField("Low", "AD")) / 4;
        	case "AW":
        		xfMin_WeightedClose = (2 * GetField("Close", "AW") + GetField("High", "AW") + GetField("Low", "AW")) / 4;
        	case "AM":
        		xfMin_WeightedClose = (2 * GetField("Close", "AM") + GetField("High", "AM") + GetField("Low", "AM")) / 4;
        	default:
        		xfMin_WeightedClose = (2 * Close + High + Low) / 4;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xfMin_XAverage(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xfMin_XAverage
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xfMin_XAverage.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率XAverage
        //
        // FreqType是預期要比對的期別, 支援 "1", "2", "3", "5", "10", "15", "30", "60", "D", "W", "M", "AD", "AW", "AM"
        // 輸入: FreqType, Series, Length
        // 不支援XS選股、XS選股自訂排行與XS選股回測。
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	Factor(0), lastXAverage(0);
        if getinfo("Instance")=3 and getinfo("Instance")=31 then raiseruntimeerror("此函數不支援XS選股與XS選股自訂排行");
        if FreqType="D" or FreqType="AD" or FreqType="W" or FreqType="AW" or FreqType="M" or FreqType="AM" then 
        	condition1 = xfMin_getdtvalue(FreqType, getfieldDate("Date")) <> xfMin_getdtvalue(FreqType, getfieldDate("Date")[1])
        else 
        	condition1 = xfMin_getdtvalue(FreqType, datetime) <> xfMin_getdtvalue(FreqType, datetime[1]);
        if condition1 then
        	lastXAverage = xfMin_XAverage[1];
        value1 = xfMin_GetCurrentBar(FreqType);
        if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);
        if value1 = 1 then
        	xfMin_XAverage = Series
        else
        	xfMin_XAverage = lastXAverage + Factor * (Series - lastXAverage);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_CrossOver(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_CrossOver
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_CrossOver.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入兩個序列(跟目前的頻率不同), 判斷是否crossover
        //
        // FreqType是傳入序列的資料期別, 支援"D", "W", "M"
        // SeriesA, SeriesB是傳入的序列
        //
        	FreqType(string), 
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0);
        posA = 0;
        posB = 0;
        valA = xf_getvalue(FreqType, SeriesA, posA);
        valB = xf_getvalue(FreqType, SeriesB, posB);
        if valA <= valB then
        begin
        	xf_CrossOver = false;
        	return;
        end; 
        for idx = 1 to 6
        begin
        	posA = posA + 1;
        	posB = posB + 1;
        	valA = xf_getvalue(FreqType, SeriesA, posA);
        	valB = xf_getvalue(FreqType, SeriesB, posB);
        	if valA < valB then
        	begin
        		xf_CrossOver = true;
        		return;
        	end
        	else
        	begin
        		if valA > valB then
        		begin
        			xf_CrossOver = false;
        			return;
        		end;
        	end; 
        end;
        xf_CrossOver = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_CrossUnder(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_CrossUnder
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_CrossUnder.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入兩個序列(跟目前的頻率不同), 判斷是否crossunder
        //
        // FreqType是傳入序列的資料期別, 支援"D", "W", "M"
        // SeriesA, SeriesB是傳入的序列
        //
        	FreqType(string), 
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0);
        posA = 0;
        posB = 0;
        valA = xf_getvalue(FreqType, SeriesA, posA);
        valB = xf_getvalue(FreqType, SeriesB, posB);
        if valA >= valB then
        begin
        	xf_CrossUnder = false;
        	return;
        end; 
        for idx = 1 to 6
        begin
        	posA = posA + 1;
        	posB = posB + 1;
        	valA = xf_getvalue(FreqType, SeriesA, posA);
        	valB = xf_getvalue(FreqType, SeriesB, posB);
        	if valA > valB then
        	begin
        		xf_CrossUnder = true;
        		return;
        	end
        	else
        	begin
        		if valA < valB then
        		begin
        			xf_CrossUnder = false;
        			return;
        		end;
        	end; 
        end;
        xf_CrossUnder = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_DirectionMovement(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_DirectionMovement
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_DirectionMovement.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率DirectionMovement function (for DMI相關指標)
        //
        // FreqType是預期要比對的期別, 支援"D", "W", "M"
        // 輸入: FreqType, Length
        // Return: pdi_value(+di), ndi_value(-di), adx_value(adx)
        //
        	FreqType(string),		//引用頻率
        	length(numericsimple),	//計算期間
        	pdi_value(numericref),	//回傳+DI
        	ndi_value(numericref),	//回傳-DI
        	adx_value(numericref);	//回傳ADX
        	padm(0), nadm(0), radx(0),
        	LastPAdm(0), LastNAdm(0), LastRAdx(0), LastATR(0),
        	atr(0), pdm(0), ndm(0), tr(0),
        	dValue0(0), dValue1(0), dx(0),
        	changeHigh(0),changeLow(0),closePeriod(0),
        	idx(0);
        //跨頻率會用到的前期值需要手動記錄
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if condition1 then
        begin
        	LastPAdm = padm[1];
        	LastNAdm = nadm[1];
        	LastRAdx = radx[1];
        	LastATR = atr[1];
        end;
        //取得跨頻率會用到的變數值
        switch (FreqType)
        begin
        	case "D":
        		if GetField("Close", "D")[1] > GetField("High", "D") then
        			tr = GetField("Close", "D")[1] - GetField("Low", "D")
        		else if GetField("Close", "D")[1] < GetField("Low", "D") then
        			tr = GetField("High", "D") - GetField("Close", "D")[1]
        		else
        			tr = GetField("High", "D") - GetField("Low", "D");
        		changeHigh = GetField("High", "D") - GetField("High", "D")[1];
        		changeLow = GetField("Low", "D")[1] - GetField("Low", "D");
        		closePeriod = GetField("Close", "D");
        	case "W":
        		if GetField("Close", "W")[1] > GetField("High", "W") then
        			tr = GetField("Close", "W")[1] - GetField("Low", "W")
        		else if GetField("Close", "W")[1] < GetField("Low", "W") then
        			tr = GetField("High", "W") - GetField("Close", "W")[1]
        		else
        			tr = GetField("High", "W") - GetField("Low", "W");
        		changeHigh = GetField("High", "W") - GetField("High", "W")[1];
        		changeLow = GetField("Low", "W")[1] - GetField("Low", "W");
        		closePeriod = GetField("Close", "W");
        	case "M":
        		if GetField("Close", "M")[1] > GetField("High", "M") then
        			tr = GetField("Close", "M")[1] - GetField("Low", "M")
        		else if GetField("Close", "M")[1] < GetField("Low", "M") then
        			tr = GetField("High", "M") - GetField("Close", "M")[1]
        		else
        			tr = GetField("High", "M") - GetField("Low", "M");
        		changeHigh = GetField("High", "M") - GetField("High", "M")[1];
        		changeLow = GetField("Low", "M")[1] - GetField("Low", "M");
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		if GetField("Close", "AD")[1] > GetField("High", "AD") then
        			tr = GetField("Close", "AD")[1] - GetField("Low", "AD")
        		else if GetField("Close", "AD")[1] < GetField("Low", "AD") then
        			tr = GetField("High", "AD") - GetField("Close", "AD")[1]
        		else
        			tr = GetField("High", "AD") - GetField("Low", "AD");
        		changeHigh = GetField("High", "AD") - GetField("High", "AD")[1];
        		changeLow = GetField("Low", "AD")[1] - GetField("Low", "AD");
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		if GetField("Close", "AW")[1] > GetField("High", "AW") then
        			tr = GetField("Close", "AW")[1] - GetField("Low", "AW")
        		else if GetField("Close", "AW")[1] < GetField("Low", "AW") then
        			tr = GetField("High", "AW") - GetField("Close", "AW")[1]
        		else
        			tr = GetField("High", "AW") - GetField("Low", "AW");
        		changeHigh = GetField("High", "AW") - GetField("High", "AW")[1];
        		changeLow = GetField("Low", "AW")[1] - GetField("Low", "AW");
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		if GetField("Close", "AM")[1] > GetField("High", "AM") then
        			tr = GetField("Close", "AM")[1] - GetField("Low", "AM")
        		else if GetField("Close", "AM")[1] < GetField("Low", "AM") then
        			tr = GetField("High", "AM") - GetField("Close", "AM")[1]
        		else
        			tr = GetField("High", "AM") - GetField("Low", "AM");
        		changeHigh = GetField("High", "AM") - GetField("High", "AM")[1];
        		changeLow = GetField("Low", "AM")[1] - GetField("Low", "AM");
        		closePeriod = GetField("Close", "AM");
        	default:
        		if Close[1] > High then
        			tr = Close[1] - Low
        		else if Close[1] < Low then
        			tr = High - Close[1]
        		else
        			tr = High - Low;
        		changeHigh = High - High[1];
        		changeLow = Low[1] - Low;
        		closePeriod = Close;
        end;
        //原始的技術指標計算
        value1 = xf_GetCurrentBar(FreqType);
        if value1 = 1 then
         begin
        	padm = closePeriod / 10000;
        	nadm = padm;
        	atr = padm * 5;
        	radx = 20;
         end
        else
         begin
        	pdm = maxlist(changeHigh, 0);
        	ndm = maxlist(changeLow, 0);
        	if pdm < ndm then
        		pdm = 0
        	else 
        	  begin
        		if pdm > ndm then
        			ndm = 0
        		else
        		  begin
        			pdm = 0;
        			ndm = 0;
        		  end;		
        	  end;
        	padm = LastPAdm + (pdm - LastPAdm) / length;
        	nadm = LastNAdm + (ndm - LastNAdm) / length;
        	atr = LastATR + (tr - LastATR) / length;
        	if atr <> 0 then begin
        		dValue0 = 100 * padm / atr;
        		dValue1 = 100 * nadm / atr;
        	end;
        	if dValue0 + dValue1 <> 0 then
        		dx = AbsValue(100 * (dValue0 - dValue1) / (dValue0 + dValue1));
        	radx = LastRAdx + (dx - LastRAdx) / length;
         end;
        pdi_value = dValue0;
        ndi_value = dValue1;
        adx_value = radx;
        xf_directionmovement = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_EMA(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_EMA
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_EMA.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率EMA
        //
        // FreqType是預期要比對的期別, 支援"D", "W", "M"
        // 輸入: FreqType, Series, Length
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	Factor(0), lastEMA(0);
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if condition1 then
        	lastEMA = xf_EMA[1];
        value1 = xf_GetCurrentBar(FreqType);
        if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);
        if value1 = 1 then
        	xf_EMA = Series
        else if value1 <= Length then
            xf_EMA = (Series + (lastEMA * (value1 - 1)))/value1	
        else
        	xf_EMA = lastEMA + Factor * (Series - lastEMA);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_GetBoolean(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_GetBoolean
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_GetBoolean.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        // 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
        //
        // FreqType是傳入序列的資料期別, 支援"D", "W", "M"
        // TFSeries是傳入的布林序列
        // poi是要取得的位置
        // 
        	FreqType(string), 
        	TFSeries(truefalseseries),
        	poi(numeric);
        _pos = poi; 
        if _pos <= 0 then
        	xf_GetBoolean = TFSeries[0]
        else
        begin
        	idx = 0;
        	while _pos > 0 and idx < currentbar-1
        	begin
        		dt = xf_getdtvalue(FreqType, getFieldDate("Date")[idx]);
        		dt2 = xf_getdtvalue(FreqType, getFieldDate("Date")[idx+1]);
        		if dt <> dt2 then _pos = _pos - 1; 
        		idx = idx + 1;
        	end;
        	xf_GetBoolean = TFSeries[idx];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_GetCurrentBar(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_GetCurrentBar
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_GetCurrentBar.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 取得指定頻率的K棒編號（CurrentBar）
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        // 輸入: FreqType
        //
        	FreqType(string);		//引用頻率
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if currentbar = 1 then 
        	xf_GetCurrentBar = 1
        else if condition1 then
        	xf_GetCurrentBar = xf_GetCurrentBar[1] + 1
        else
        	xf_GetCurrentBar = xf_GetCurrentBar[1];
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_GetDTValue(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_GetDTValue
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_GetDTValue.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 回傳某個日期的'normalized' value
        // 用這個value來比對是否已經跨期
        //
        // FreqType是預期要比對的期別, 支援"D", "W", "M"
        // dtValue 是目前資料序列上面的Date
        //
        	FreqType(string), 
        	dtValue(numeric);
        switch (FreqType)
        begin
        	case "D" , "AD":
        		xf_GetDTValue = dtValue;
        	case "W" , "AW":
        		// 年度 * 100 + 周別, e.g. 201001, 表示是2010年的第一週
        		// 
        		xf_GetDTValue = Year(dtValue) * 100 + WeekofYear(dtValue);
        		// 每年的第一週需要判斷是否和去年的最後一週重疊
        		// 
        		if mod(dtValue, 10000) <= 104 and WeekofYear(DateAdd(dtValue,"D", 1-DayofWeek(dtValue))) = 53 then 
        			xf_GetDTValue = round(dtValue / 10000 - 1, 0) * 100 + 53;
        	case "M" , "AM":
        		// 年度 * 100 + 月別, e.g. 201001, 表示是2010年的第一個月
        		//
        		xf_GetDTValue = Year(dtValue) * 100 + Month(dtValue);
        	default:
        		xf_GetDTValue = dtValue;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_GetValue(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_GetValue
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_GetValue.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 傳入一個序列(跟目前的頻率不同), 取得這個序列以此頻率的第幾筆
        //
        // FreqType是傳入序列的資料期別, 支援"D", "W", "M"
        // PriceSeries是傳入的序列
        // poi是要取得的位置
        // 
        	FreqType(string), 
        	PriceSeries(numericseries),
        	poi(numeric);
        _pos = poi; 
        if _pos <= 0 then
        	xf_GetValue = PriceSeries[0]
        else
        begin
        	idx = 0;
        	while _pos > 0 and idx < currentbar-1
        	begin
        		dt = xf_getdtvalue(FreqType, getfieldDate("Date")[idx]);
        		dt2 = xf_getdtvalue(FreqType, getfieldDate("Date")[idx+1]);
        		if dt <> dt2 then _pos = _pos - 1; 
        		idx = idx + 1;
        	end;
        	xf_GetValue = PriceSeries[idx];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_MACD(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_MACD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_MACD.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率MACD函數
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        // 輸入: FreqType, FastLength, SlowLength, MACDLength;
        // 輸出: DifValue, MACDValue, OscValue;
        	FreqType(string),		//引用頻率
        	Price(numericseries), 	
        	FastLength(numericsimple), SlowLength(numericsimple), MACDLength(numericsimple),
        	DifValue(numericref), MACDValue(numericref), OscValue(numericref);
        DifValue = xf_XAverage(FreqType, Price, FastLength) - xf_XAverage(FreqType, Price, SlowLength);
        MACDValue = xf_XAverage(FreqType, DifValue, MACDLength);
        OscValue = DifValue - MACDValue;
        xf_MACD = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_PercentR(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_PercentR
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_PercentR.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率PercentR函數(for 威廉指標)
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        // 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
        // 輸出: rsv_value, k_value, d_value
        //
        	FreqType(string), 
        	Length(numericsimple);
        	maxHigh(0), minLow(0),variableA(0),variableB(0),closePeriod(0);
        switch (upperstr(FreqType))
        begin
        	case "D":
        		maxHigh = highest(GetField("High", "D"),Length);
        		minLow = lowest(GetField("Low", "D"),Length);
        		closePeriod = GetField("Close", "D");
        	case "W":
        		maxHigh = highest(GetField("High", "W"),Length);
        		minLow = lowest(GetField("Low", "W"),Length);
        		closePeriod = GetField("Close", "W");
        	case "M":
        		maxHigh = highest(GetField("High", "M"),Length);
        		minLow = lowest(GetField("Low", "M"),Length);
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		maxHigh = highest(GetField("High", "AD"),Length);
        		minLow = lowest(GetField("Low", "AD"),Length);
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		maxHigh = highest(GetField("High", "AW"),Length);
        		minLow = lowest(GetField("Low", "AW"),Length);
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		maxHigh = highest(GetField("High", "AM"),Length);
        		minLow = lowest(GetField("Low", "AM"),Length);
        		closePeriod = GetField("Close", "AM");
        	default:
        		maxHigh = highest(High,Length);
        		minLow = lowest(Low,Length);
        		closePeriod = Close;
        end;
        variableB = maxHigh - minLow;
        if variableB <> 0 then  
        	xf_PercentR = 100 - ((maxHigh - closePeriod) / variableB) * 100
        else 
        	xf_PercentR = 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_RSI(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_RSI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_RSI.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率RSI函數
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        // 輸入: FreqType, Series, Length
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	SumUp(0), SumDown(0), 
        	LastSumUp(0), LastSumDown(0),LastRefSeries(Series), 
        	up(0), down(0),
        	closePeriod(0);
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if condition1 then
        begin
        	LastSumUp = SumUp[1];
        	LastSumDown = SumDown[1];
        	LastRefSeries = Series[1];
        end;
        if xf_GetCurrentBar(FreqType) = 1 then
          begin
        	SumUp = Average(maxlist(Series - LastRefSeries, 0), Length); 
        	SumDown = Average(maxlist(LastRefSeries - Series, 0), Length); 
          end
        else
          begin
        	up = maxlist(Series - LastRefSeries, 0);
        	down = maxlist(LastRefSeries - Series, 0);
        	SumUp = LastSumUp + (up - LastSumUp) / Length;
        	SumDown = LastSumDown + (down - LastSumDown) / Length;
          end;
        if SumUp + SumDown = 0 then
        	xf_RSI = 0
        else
        	xf_RSI = 100 * SumUp / (SumUp + SumDown);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_Stochastic(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_Stochastic
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_Stochastic.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率Stochastic函數(for KD/RSV相關指標)
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        // 輸入: FreqType, SeriesH, SeriesL, SeriesC, Length, rsvt, kt
        // 輸出: rsv_value, k_value, d_value
        //
        	FreqType(string), 
        	Length(numericsimple), rsvt(numericsimple), kt(numericsimple),
        	rsv(numericref), k(numericref), d(numericref);
        	maxHigh(0), minLow(0),lastK(50),lastD(50),closePeriod(0);
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if condition1 then
        begin
        	lastK = k[1];
        	lastD = d[1];
        end;
        switch (FreqType)
        begin
        	case "D":
        		maxHigh = highest(GetField("High", "D"),Length);
        		minLow = lowest(GetField("Low", "D"),Length);
        		closePeriod = GetField("Close", "D");
        	case "W":
        		maxHigh = highest(GetField("High", "W"),Length);
        		minLow = lowest(GetField("Low", "W"),Length);
        		closePeriod = GetField("Close", "W");
        	case "M":
        		maxHigh = highest(GetField("High", "M"),Length);
        		minLow = lowest(GetField("Low", "M"),Length);
        		closePeriod = GetField("Close", "M");
        	case "AD":
        		maxHigh = highest(GetField("High", "AD"),Length);
        		minLow = lowest(GetField("Low", "AD"),Length);
        		closePeriod = GetField("Close", "AD");
        	case "AW":
        		maxHigh = highest(GetField("High", "AW"),Length);
        		minLow = lowest(GetField("Low", "AW"),Length);
        		closePeriod = GetField("Close", "AW");
        	case "AM":
        		maxHigh = highest(GetField("High", "AM"),Length);
        		minLow = lowest(GetField("Low", "AM"),Length);
        		closePeriod = GetField("Close", "AM");
        	default:
        		maxHigh = highest(High,Length);
        		minLow = lowest(Low,Length);
        		closePeriod = Close;
        end;
        if maxHigh <> minLow then
        	rsv = 100 * (closePeriod - minLow) / (maxHigh - minLow)
        else
        	rsv = 50;
        if currentbar = 1 then
        begin
        	k = 50;
        	d = 50;
        end
        else
        begin
        	k = (lastK * (rsvt - 1) + rsv) / rsvt;
        	d = (lastD * (kt - 1) + k) / kt;
        end; 
        xf_Stochastic = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_WeightedClose(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_WeightedClose
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_WeightedClose.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 跨頻率WeightedClose函數
        //
        // FreqType是預期要引用的頻率, 支援"D", "W", "M"
        //
        	FreqType(string);
        switch (upperstr(FreqType))
        begin
        	case "D":
        		xf_WeightedClose = (2 * GetField("Close", "D") + GetField("High", "D") + GetField("Low", "D")) / 4;
        	case "W":
        		xf_WeightedClose = (2 * GetField("Close", "W") + GetField("High", "W") + GetField("Low", "W")) / 4;
        	case "M":
        		xf_WeightedClose = (2 * GetField("Close", "M") + GetField("High", "M") + GetField("Low", "M")) / 4;
        	case "AD":
        		xf_WeightedClose = (2 * GetField("Close", "AD") + GetField("High", "AD") + GetField("Low", "AD")) / 4;
        	case "AW":
        		xf_WeightedClose = (2 * GetField("Close", "AW") + GetField("High", "AW") + GetField("Low", "AW")) / 4;
        	case "AM":
        		xf_WeightedClose = (2 * GetField("Close", "AM") + GetField("High", "AM") + GetField("Low", "AM")) / 4;
        	default:
        		xf_WeightedClose = (2 * Close + High + Low) / 4;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def xf_XAverage(df: pd.DataFrame, FreqType: str = "string") -> tuple[bool, str]:
        """
        Original Strategy: xf_XAverage
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\跨頻率\xf_XAverage.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(2);
        // 跨頻率XAverage
        //
        // FreqType是預期要比對的期別, 支援"D", "W", "M"
        // 輸入: FreqType, Series, Length
        //
        	FreqType(string),		//引用頻率
        	Series(numericseries),	//價格序列
        	Length(numericsimple);	//計算期間
        	Factor(0), lastXAverage(0);
        condition1 = xf_getdtvalue(FreqType, getFieldDate("Date")) <> xf_getdtvalue(FreqType, getFieldDate("Date")[1]);
        if condition1 then
        	lastXAverage = xf_XAverage[1];
        value1 = xf_GetCurrentBar(FreqType);
        if Length + 1 = 0 then Factor = 1 else Factor = 2 / (Length + 1);
        if value1 = 1 then
        	xf_XAverage = Series
        else
        	xf_XAverage = lastXAverage + Factor * (Series - lastXAverage);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
