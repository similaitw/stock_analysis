# Auto-generated strategies for: 警示/當沖交易型
import pandas as pd
import numpy as np

class 當沖交易型Strategies:

    @staticmethod
    def 一分鐘K三連紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 一分鐘K三連紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\一分鐘K三連紅.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <> "Min" or Barinterval <>1 then RaiseRuntimeError("請設定頻率為1分鐘");
        if Date <> Date[1] then 
        	BarNumberOfToday=1
        else 
        	BarNumberOfToday+=1;{記錄今天的Bar數}
        if barnumberoftoday=3 then begin
        //今天第三根1分鐘K，也就是開盤第三分鐘
        	if trueall(close>=close[1],3)
        	//連三根K棒都是紅棒
        	and volume>average(volume[1],3)*2
        	//成交量是過去三根量平均量的兩倍以上
        	and close=highd(0)
        	//收最高
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主動性買盤大增(df: pd.DataFrame, Length: int = 20, Ratio: int = 50, TXT: str = "僅適用60分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 主動性買盤大增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\主動性買盤大增.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if barfreq<> "Min" or barinterval <> 60 then return;
        DayOSV = GetQuote("當日外盤量");
        AvgOutSideVol =  averageIF( close > close[1] ,volume,Length);
        switch(time)
        begin
        	case 90000: 
        	    if C>O and DayOSV > AvgOutSideVol *(1+ Ratio/100) then ret=1;
        	case 100000:
        		if C>O and DayOSV/2 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
        	case 110000:
        		if C>O and DayOSV/3 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
        	case 120000:
        		if C>O and DayOSV/4 > AvgOutSideVol *(1+ Ratio/100) then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 五分鐘K狹幅整理後帶量破(df: pd.DataFrame, Length: int = 100, Ratio: float = 0.5, RRatio: float = 1.5, TXT1: str = "僅適用5分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 五分鐘K狹幅整理後帶量破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\五分鐘K狹幅整理後帶量破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if barfreq<> "Min" or barinterval <> 5 then return;
        RangeHigh=highest(close[1],length);
        RangeLow=lowest(close[1],length);
        if RangeHigh[1] < RangeLow[1] * (1+ RRatio/100) then begin
        	if Close crosses over RangeHigh*(1+Ratio/100)
        	and volume>average(volume,length)*1.5
        	and trueall(GetField("成交量","D")>500,10)
        	and countif(GetField("主力買賣超張數","D")[1]>0,10)>=7
        	and GetSymbolField("tse.tw","收盤價","D")>GetSymbolField("tse.tw","收盤價","D")[1]
        	and GetSymbolField("tse.tw","收盤價","D")>average(GetSymbolField("tse.tw","收盤價","D"),5)
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 五分鐘線整理後突破(df: pd.DataFrame, Length: int = 20, Ratio: float = 0.5, RRatio: float = 1.5, TXT1: str = "僅適用5分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 五分鐘線整理後突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\五分鐘線整理後突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if barfreq<> "Min" or barinterval <> 5 then return;
        RangeHigh=highest(close[1],length);
        RangeLow=lowest(close[1],length);
        if Close > RangeHigh*(1+Ratio/100) then
           if RangeHigh <  RangeLow * (1+ RRatio/100) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 即將鎖第一根漲停(df: pd.DataFrame, Length: int = 20, Ratio: int = 1, TXT: str = "請用日線逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 即將鎖第一根漲停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\即將鎖第一根漲停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if BarFreq = "D" then 
          if Close > GetField("漲停價", "D")*(1- Ratio/100)  then
            if TrueAll(close[1] < Close[2]*1.068,Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多次到頂而破(df: pd.DataFrame, HitTimes: int = 3, RangeRatio: int = 1, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 多次到頂而破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\多次到頂而破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        //回算在此區間中 進去瓶頸區的次數 
        TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length);
        if  TouchRangeTimes >= HitTimes   and  ( q_ask> theHigh or   close > theHigh) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 斷頭後的止跌(df: pd.DataFrame, Length: int = 4, DVOL: int = 3000, TXT1: str = "僅適用日線", TXT2: str = "建議使用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 斷頭後的止跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\斷頭後的止跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if barfreq = "D" and 
           Close > Close[1] and 
           Close[Length] > Close * 1.1 and
           GetField("融資餘額張數")[Length] - GetField("融資餘額張數")[1] > DVOL 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 會打開的跌停(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 會打開的跌停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\會打開的跌停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(605);
        if q_ask=GetField("跌停價", "D") and
           q_bestasksize1<1500 and
           (closeD(2)-close)>0.07*Close  
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲停量縮不下來(df: pd.DataFrame, lastvolume1: int = 2000, lastvolume2: int = 10000, TXT1: str = "需使用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 漲停量縮不下來
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\漲停量縮不下來.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if Date <> Date[1] then UPLVol = 0;
        if Close =GetField("漲停價", "D") then 
        begin
          UPLVol += GetField("Volume", "Tick");
          if q_BestBidSize1 <lastvolume1 and 
             GetField("Volume", "D") >lastvolume2 and
        	 UPLVol > lastvolume1 
          then RET=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 火箭後拉回(df: pd.DataFrame, TXT1: str = "僅適用1分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 火箭後拉回
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\火箭後拉回.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if barfreq ="Min" and barinterval =1 and
           close[1]/close[2]>1.015 and //上個1分鐘線單分鐘拉超過1.5%
           GetField("High", "D") > high and //高不過高
           Close < GetField("High", "D")*0.99 and //自高檔回1%
           Close > Low[1] 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日累計量突破(df: pd.DataFrame, VolumeThre: int = 1000, AmountThre: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 當日累計量突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\當日累計量突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if GetField("Volume", "D") > VolumeThre or GetField("均價")*GetField("Volume", "D")/10 > AmountThre then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當沖一號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 當沖一號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\當沖一號.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <>"Min" or  barinterval<> 1 then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");
        if date<>date[1] then count=0;
        count=count+1;
        if GetField("開盤價","D")> GetField("收盤價","D")[1]*1.025
        and count>20
        and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
        and close =highest(high,count)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當沖二號_空_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 當沖二號(空)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\當沖二號(空).xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <>"Min" or  barinterval<> 1
        then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");
        if date<>date[1] then count=0;
        count=count+1;
        if GetField("開盤價","D")*1.025< GetField("收盤價","D")[1] 
        and count>10
        and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
        and close =lowest(low,count)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤中突破區間(df: pd.DataFrame, timeline: int = 100000, TXT1: str = "限用分鐘線", TXT2: str = "高點自開盤起算") -> tuple[bool, str]:
        """
        Original Strategy: 盤中突破區間
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\盤中突破區間.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if barfreq<> "Min" then return;
        if date <> date[1] then RangeHigh = 0;
        if Time < timeline then RangeHigh = maxlist(RangeHigh,high)
        	else if time >= timeline and  RangeHigh > 0 and Close > RangeHigh*1.005 then ret=1 ;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破波動範圍(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 突破波動範圍
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\突破波動範圍.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        HighLow=high-low;
        if C>highest(H[1],Length) *1.005 and  HighLow>highest(HighLow[1],Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 賣壓很輕(df: pd.DataFrame, rate: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 賣壓很輕
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\賣壓很輕.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if {內盤量}GetField("內盤量", "D")  < GetField("Volume", "D")*(Rate/100)  and Countif(close< close[1],5) < 3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌停一直在成交(df: pd.DataFrame, lastvolume1: int = 2000, lastvolume2: int = 10000, TXT1: str = "需使用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 跌停一直在成交
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\跌停一直在成交.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if Date <> Date[1] then DNLVol = 0;
        if Close = GetField("跌停價", "D") then 
        begin
          DNLVol += GetField("Volume", "Tick");
          if q_BestAskSize1 <lastvolume1 and 
             GetField("Volume", "D") >lastvolume2 and
        	 DNLVol > lastvolume1 
          then RET=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近期持續強勢股階梯式上漲(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 近期持續強勢股階梯式上漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\近期持續強勢股階梯式上漲.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq<> "Min"and barinterval<> 5 then raiseruntimeerror("本腳本只限五分鐘線");
        condition1 = GetSymbolField("tse.tw","收盤價","D") > average(GetSymbolField("tse.tw","收盤價","D"),10);
        //多頭市場
        condition2 = GetSymbolField("tse.tw","收盤價","D") / GetSymbolField("tse.tw","收盤價","D")[2]+0.01
        			  <  GetField("收盤價","D")/GetField("收盤價","D")[2];
        //前兩日比大盤明顯走強
        condition3 = GetField("收盤價","D")[1] <GetField("收盤價","D")[10]*1.07;
        //近十日沒有漲的太兇
        condition4 = Average(GetField("Volume", "D")[1], 100) >= 1000;
        if condition1 and condition2 and condition3 and condition4 then begin
        	if time=091500
        	and trueall(close>close[1],3)
        	//開盤三根五分鐘線都是紅棒
        	and average(volume,3)>average(volume,20)*1.3
        	//開盤的量能明顯增加
        	and GetField("收盤價","D")[1]<GetField("收盤價","D")[2]
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續五分鐘一路走高(df: pd.DataFrame, TXT1: str = "僅適用1分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 連續五分鐘一路走高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\連續五分鐘一路走高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if barfreq = "Min" and barinterval = 1 and
           TrueAll(close >Close[1] ,5) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開低不反彈再創新低(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開低不反彈再創新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開低不反彈再創新低.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <>"Min" or barinterval<> 1 then raiseruntimeerror("本腳本只適用於1分鐘線");
        if date<>date[1] then count=0;
        count=count+1;
        if GetField("開盤價","D")*1.025< GetField("收盤價","D")[1] 
        and count>10
        and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
        and close =lowest(low,count)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開大跌後未再探底(df: pd.DataFrame, ratio: int = 4, ratio1: float = 0.5) -> tuple[bool, str]:
        """
        Original Strategy: 開大跌後未再探底
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開大跌後未再探底.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if GetField("Open", "D") < GetField("RefPrice", "D") * (1 -Ratio/100) and 
           GetField("Open", "D") >= GetField("Low", "D")  and
           (GetField("Open", "D")- GetField("Low", "D"))<  Close * Ratio1 and
           Close > GetField("Open", "D") * (1 + Ratio1/100) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤三連陽(df: pd.DataFrame, TXT: str = "僅適用60分鐘線以內") -> tuple[bool, str]:
        """
        Original Strategy: 開盤三連陽
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤三連陽.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if barfreq = "Min" and barinterval <= 60 and
           (time[2] = 84500 or time[2] = 90000) and
            Close > Close[1] and Close[1] > Close[2] and
        	Close[2] > Open[2] 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤五分鐘K線三連陽(df: pd.DataFrame, TXT1: str = "僅適用5分鐘線", TXT2: str = "開盤前3根K棒") -> tuple[bool, str]:
        """
        Original Strategy: 開盤五分鐘K線三連陽
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤五分鐘K線三連陽.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if barfreq<> "Min" or barinterval <> 5 then return;
        if Date = CurrentDate   and
           (time[2] = 90000 or time[2] = 84500) and
           KBarOfDay = 3 and
           Close[2] > Open[2] and 
           TrueAll(Close > Open and Close > Close[1] ,2)  then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤五分鐘三創新高(df: pd.DataFrame, volumeRatio: float = 0.1, changeRatio: int = 3, averageVolume: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 開盤五分鐘三創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤五分鐘三創新高.xs
        XS Logic Reference:
        {@type:sensor}
        KBarOfDay+=1;
        if date<>date[1] then begin
        	KBarOfDay=1; 
        	BreakHigh = false;
        end; 
        condition1 = KBarOfDay = 6;
        //一分鐘線每天的第六根
        condition2 = Countif(High > High[1] and Close > Close[1] ,5) >=3;
        //近五根裡至少三根最高價比前一根高且收盤比前一根高
        if KBarOfDay = 1
        and close > getfield("close", "d")[1] 
        then BreakHigh = true;
        //開高
        value1 = average(GetField("Volume", "D")[1], 5);
        //五日均量
        condition3 = value1 > averageVolume;
        //五日均量大於某張數 
        value2 = rateofchange(GetField("Close", "D")[1], 3);
        condition4 = AbsValue(value2) < changeRatio;
        //前三日漲帳幅小於一定標準
        condition5 = summation(volume, 5) > value1 * volumeRatio;
        //前五根一分鐘線成交量的合計大於五日均量某個比例
        condition6 = GetSymbolField("TSE.TW","收盤價","D")>average(GetSymbolField("TSE.TW","收盤價","D"),10);
        //大盤屬於多頭結構
        if condition1 and condition2 and condition3
        and Condition4 and Condition5 and condition6
        and BreakHigh
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤五分鐘創三新低(df: pd.DataFrame, TXT: str = "僅適用1分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 開盤五分鐘創三新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤五分鐘創三新低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if barfreq = "Min"  and barinterval = 1 and Date = CurrentDate   and
           KBarOfDay = 6 and
           Countif(Low < Low[1] and Close < Close[1] ,5) >=3  then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤五分鐘創三新高(df: pd.DataFrame, TXT: str = "僅適用1分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 開盤五分鐘創三新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤五分鐘創三新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if barfreq<> "Min"  and barinterval = 1 and Date = CurrentDate   and
           KBarOfDay = 6 and
           Countif(High > High[1] and Close > Close[1] ,5) >=3  then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤反轉買進訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開盤反轉買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤反轉買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        if getsymbolfield("tse.tw","收盤價") > average(getsymbolfield("tse.tw","收盤價"),10) then begin
        	if Date <> Date[1] then begin
        		_BarIndex = 1;
        		_Open = Open;
        		_Low = Low;
        		_High = High;
        		_Volume = Volume;
        	end else begin
        		_Low = minlist(_Low, Low);
        		_High = maxlist(_High, High);
        		_Volume = _Volume + Volume;
        		_BarIndex = _BarIndex + 1;
        	end;
        	Condition1 = GetField("Open", "D") < GetField("Close", "D")[1];
        	//開低
        	Condition2 = Close > _Low * 1.02 and close>GetField("收盤價","D")[1];
        	//收盤比當天低點收高2%且突破前一日高點
        	Condition3 = Close*1.2 < GetField("Close", "D")[20]
        	//近二十日跌幅超過兩成
        	and close*1.07<getfield("close","D")[10];
        	//近十日跌幅超過7%
        	Condition4 = Time < 93000;
        	//時間在九點半之前
        	Condition5 = Average(GetField("Volume", "D")[1], 5) >= 1000;
        	//五日均量大於1000張
        	Condition6 = _Volume > GetField("Volume", "D")[1] * 0.2;
        	//今日迄今的量大於過去五日均量的兩成
        	if Condition1 And Condition2 And Condition3 And Condition4 And Condition5 And Condition6
        	then ret = 1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤委買暴增(df: pd.DataFrame, iVOL: int = 1000, Ratio: int = 10, TXT1: str = "適用1分鐘", TXT2: str = "僅開盤第1分鐘洗價") -> tuple[bool, str]:
        """
        Original Strategy: 開盤委買暴增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤委買暴增.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(300);
        if barfreq ="Min" and barinterval =1 and Date= Currentdate and
           Time =90000 and GetQuote("總委買") - GetQuote("總委賣") >iVOL and
           GetQuote("總委買") / summation(volume[1],270) > Ratio 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤暴量(df: pd.DataFrame, Vtimes: int = 3, atVolume: int = 100, TXT1: str = "僅適用1分鐘", TXT2: str = "盤中可用") -> tuple[bool, str]:
        """
        Original Strategy: 開盤暴量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開盤暴量.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(300);
        if barfreq <> "Min" or Barinterval <> 1 then return;
        if CurrentBar = 1 then
          begin
        	// 找到當日第一筆分鐘K線的成交量
        	//
        	idx = 0;
        	while date[idx] = date
        	  begin
        		OpenVolume = Volume[idx];
        		OpenVolumeDate = date[idx];
        		idx = idx + 1;
        	  end;
          end
        else
        	if Date <> OpenVolumeDate then
        	  begin
        		// 開盤量為換日後的第一筆分鐘K線的成交量
        		OpenVolumeDate = Date;
        		OpenVolume = Volume;
        	  end;
        if CurrentDate = OpenVolumeDate And 
           OpenVolume > AtVolume And
           OpenVolume > GetQuote("昨量")/270 * Vtimes then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開高不拉回後再創新高(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開高不拉回後再創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開高不拉回後再創新高.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <>"Min" or barinterval<> 1 then raiseruntimeerror("歹勢，本腳本只適用於1分鐘線");
        if date<>date[1] then count=0;
        count=count+1;
        if GetField("開盤價","D")> GetField("收盤價","D")[1]*1.025
        and count>5
        and lowest(low[1],count-1)*1.015>highest(high[1],count-1)
        and close =highest(high,count)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開高後不拉回(df: pd.DataFrame, Ratio: float = 2.5, aRatio: int = 1, TXT: str = "僅適用於15分鐘以內") -> tuple[bool, str]:
        """
        Original Strategy: 開高後不拉回
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\開高後不拉回.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if barfreq ="Min" and barinterval <=15 and time <= 091500 and
           GetField("Open", "D") > GetField("RefPrice", "D") *(1+Ratio/100) and 
           Close > GetField("High", "D")* (1- aRatio/100) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 階梯式上漲(df: pd.DataFrame, TXT1: str = "僅適用1分鐘線", TXT2: str = "只於9:10判斷") -> tuple[bool, str]:
        """
        Original Strategy: 階梯式上漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\當沖交易型\階梯式上漲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(12);
        if barfreq = "Min" and barinterval = 1 and time =91000 and
           TrueAll(close >Close[1] ,10) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
