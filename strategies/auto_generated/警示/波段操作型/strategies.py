# Auto-generated strategies for: 警示/波段操作型
import pandas as pd
import numpy as np

class 波段操作型Strategies:

    @staticmethod
    def strategy_60分鐘線九連陽(df: pd.DataFrame, TXT: str = "僅適用60分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 60分鐘線九連陽
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\60分鐘線九連陽.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(10);
        if barfreq<> "Min" or barinterval <> 60 then return;
        if TrueAll(Close > Close[1] and Close > Open ,9) then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SAR買進訊號(df: pd.DataFrame, AFIncrement: float = 0.02, AFMax: float = 0.2) -> tuple[bool, str]:
        """
        Original Strategy: SAR買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\SAR買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(100);
        	sarValue(0);
        sarValue = SAR(AFIncrement, AFIncrement, AFMax);	
        if close crosses over sarValue then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 休息後風雲再起(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 休息後風雲再起
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\休息後風雲再起.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        condition1 =  Close[3] > low[3]* 1.01;
        condition2 =  close[2] > open[2] * 1.01 and open[2]>close[3];
        condition3 =  close[1] < close[2] and high[1] < close[1]* 1.005;
        condition4 =  close > close[1] * 1.01;
        if condition1 and condition2 and condition3 and condition4 then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低PB股的逆襲(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 低PB股的逆襲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\低PB股的逆襲.xs
        XS Logic Reference:
        {@type:sensor}
        if GetSymbolField("tse.tw","收盤價") > average(GetSymbolField("tse.tw","收盤價"),10)
        then begin
        	if close<12
        	and H = highest(H,20)
        	and close<lowest(low,20)*1.07
        	and highest(h,40)>close*1.1
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低檔連n日拉尾盤(df: pd.DataFrame, Length: int = 3, Ratio: int = 1, closetime: int = 132500, ratiotoLow: int = 7, daystoLow: int = 5, TXT1: str = "最高算5天", TXT2: str = "限用5分鐘") -> tuple[bool, str]:
        """
        Original Strategy: 低檔連n日拉尾盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\低檔連n日拉尾盤.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(300);
        if barfreq <> "Min" or barinterval <> 5  or Length>5 or daystoLow >5 then return;
        if close >= lowest(close,daystoLow * TodayBars) *( 1 + ratiotoLow*0.01) then return;
        if time >= closetime then 
        begin
          for i = 0 to Length-1
          begin
        	// 判斷是否拉尾盤
            if close[TodayBars*i] <= close[TodayBars*i+1] * (1+ Ratio/100) then return;
          end;
          ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 反常必有妖(df: pd.DataFrame, TXT: str = "僅適用60分鐘") -> tuple[bool, str]:
        """
        Original Strategy: 反常必有妖
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\反常必有妖.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(30);
        if barinterval <> 60  or barfreq<> "Min" then return;
        if Close > close[1] * 1.02  then
        begin
        	value2=average(truerange,30);
        	value3=average(truerange,3);
        	if truerange>value3 and value3>value2 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 均線多頭排列(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, SuperLong: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 均線多頭排列
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\均線多頭排列.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,midlength,Longlength,SuperLong));
        if Close > close[1] then
        begin
         shortaverage=Average(close,shortlength);
         midaverage=Average(close,midlength) ;
         Longaverage = Average(close,Longlength); 
         SuperLongaverage = Average(close,SuperLong); 
         if  close>shortaverage and 
             shortaverage>midaverage and 
        	 midaverage>Longaverage and 
        	 Longaverage>SuperLongaverage
         then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外盤買氣轉強(df: pd.DataFrame, short1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 外盤買氣轉強
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\外盤買氣轉強.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1=GetField("內盤量");//內盤量
        value2=GetField("外盤量");//外盤量
        value3=value1+value2;
        if value3<>0 then value4=value2/value3*100;
        //外盤比重
        value5=average(value4,short1);
        value6=average(value4,mid1);
        if close*1.4<close[90]
        and value5 crosses above value6 
        and value4>60
        and average(volume,100)>1000
        and tselsindex(10,6)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多次到底而破(df: pd.DataFrame, day: int = 100, band1: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 多次到底而破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\多次到底而破.xs
        XS Logic Reference:
        {@type:sensor}
        value1=nthlowest(1,low[1],day);
        value2=nthlowest(3,low[1],day);
        value4=nthlowestbar(1,low,day);
        value5=nthlowestbar(3,low,day);
        value6=nthlowestbar(5,low,day);
        value7=absvalue(value4-value6);
        value8=absvalue(value5-value6);
        value9=absvalue(value4-value5);
        condition1=false;
        if value7>3 and value8>3 and value9>3
        then condition1=true;
        value3=(value1-value2)/value2;
        if value3<=band1/100
        and close crosses under value1
        and volume>2000
        and condition1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多次到頂而突破(df: pd.DataFrame, HitTimes: int = 3, RangeRatio: int = 1, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 多次到頂而突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\多次到頂而突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(300);
        setbarback(100);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        theHigh = Highest(High[1],Length);  //找到過去區間的最高點
        HighLowerBound = theHigh *(100-RangeRatio)/100;  // 設為瓶頸區間上界
        //回算在此區間中 進去瓶頸區的次數 
        TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length);
        if  TouchRangeTimes >= HitTimes   
        and close > theHigh 
        and close[50]*1.2 < close[20]
        and tselsindex(10,6)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量突破糾結的均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, Percent: int = 2, Volpercent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 帶量突破糾結的均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\帶量突破糾結的均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(shortlength,midlength,Longlength));
        if volume > average(volume,Longlength) * (1 + volpercent * 0.01) then
        begin
        	shortaverage = average(close,shortlength);
        	midaverage = average(close,midlength);
        	Longaverage = average(close,Longlength);
        	if Close crosses over maxlist(shortaverage,midaverage,Longaverage) then
        	begin
        		value1= absvalue(shortaverage -midaverage);
        		value2= absvalue(midaverage -Longaverage);
        		value3= absvalue(Longaverage -shortaverage);
        		if maxlist(value1,value2,value3)*100 < Percent*Close then  ret=1;
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量衝破季線(df: pd.DataFrame, PriceLength: int = 66, BelowLength: int = 66, VolLength: int = 20, Volpercent: int = 20, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 帶量衝破季線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\帶量衝破季線.xs
        XS Logic Reference:
        {@type:sensor}
        //股價長期低於季線
        //帶量突破季線
        settotalbar(BelowLength + 8);
        setbarback(maxlist(PriceLength,VolLength));
        if Close crosses over PriceAverage and
           volume > Average(volume[1],VolLength)* (1+Volpercent/100) and
           trueall(close[1] < PriceAverage[1],  BelowLength-1) then
           ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平均量黃金交叉(df: pd.DataFrame, shortlength: int = 5, Longlength: int = 22) -> tuple[bool, str]:
        """
        Original Strategy: 平均量黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\平均量黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(shortlength,Longlength));
        Longaverage = Average(volume,Longlength);
        shortaverage=Average(volume,shortlength) ;
        if shortaverage crosses over  Longaverage then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 抗跌(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 抗跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\抗跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if open>open[1] and open < 1.005*low then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 暴量剛起漲(df: pd.DataFrame, Length: int = 20, VLength: int = 10, volpercent: int = 50, Rate: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 暴量剛起漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\暴量剛起漲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(Length,VLength));
        if Close >  Close[1] and
           Volume >=  average(volume,VLength) *(1+ volpercent/100) and
           Close <= lowest(close,Length) * (1+Rate/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月線連兩個月收紅的小型股(df: pd.DataFrame, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 月線連兩個月收紅的小型股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\月線連兩個月收紅的小型股.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(120);
        if  GetField("總市值","D")<2000000000 //單位是元
        and close<40
        and getfield("close","M")[1]>getfield("close","M")[2] 
        and getfield("close","M")[2]>getfield("close","M")[3]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 沖擊底部(df: pd.DataFrame, BarPercent: int = 75) -> tuple[bool, str]:
        """
        Original Strategy: 沖擊底部
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\沖擊底部.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if q_Ask > Close[1] and high[1] > high[2] and low[1] > low[2] and close[1] > close[2] then
          if TrueAll( (close[1]-low[1])>(high[1]-low[1])*BarPercent/100 ,2) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 沿均線前進(df: pd.DataFrame, Length: int = 10, FollowLength: int = 5, Ratio: int = 2, LongShort: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 沿均線前進
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\沿均線前進.xs
        XS Logic Reference:
        {@type:sensor}
        //沿著均線前進
        settotalbar(FollowLength + 3);
        setbarback(Length);
        condition1= false;
        switch(LongShort)
        begin
        case =1:
         condition1 = close > highest(high[1],Length);
        case -1:
         condition1 = close < lowest(low[1],Length);
        case 0:
         condition1=true;
        end;
        If Condition1 and 
           TrueAll(absvalue(close-average(close,Length))< Close*Ratio/100,FollowLength)
        then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人作多股(df: pd.DataFrame, ForceType: int = 1, Atleast: int = 1000, TXT: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 法人作多股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\法人作多股.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if barfreq <> "D" then return;
        Switch ( ForceType ) 
        Begin 
        Case 1: ForcePush =Getfield("外資買賣超")[1];
        Case 2: ForcePush =Getfield("投信買賣超")[1];
        Case 3: ForcePush =Getfield("自營商買賣超")[1]; 
        End; 
        if  volume > volume[1] then 
        begin
              condition1 = ( close[1]-open[1]  > 0.75 *high[1]-low[1] )  and //長紅棒
                           (high[1] -low[1]) > 2 *( high[2]-low[2]);      
              if condition1 and q_Ask > highest(high[1],3) and ForcePush >Atleast then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人爭下車(df: pd.DataFrame, ForceType: int = 1, Periods: int = 20, Percent: int = 5, Type: int = 1, TXT: str = "僅適用日線逐筆洗價", TXT2: str = "盤中無當日即時法人買賣資料") -> tuple[bool, str]:
        """
        Original Strategy: 法人爭下車
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\法人爭下車.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Periods + 3);
        if BarFreq <> "D" or absvalue(Type) > 1 then return;
            Switch ( ForceType ) 
            Begin 
                Case 1: 
                    ForcePush = Getfield("外資持股")[Type];
                Case 2: 
                    ForcePush = Getfield("投信持股")[Type]; 
                Case 3: 
                    ForcePush = Getfield("自營商持股")[Type]; 
                default: 
                    ForcePush = Getfield("外資持股")[Type]+Getfield("投信持股")[Type]+Getfield("自營商持股")[Type];
            End; 
        if currentbar <= Periods then return;
        if Close < Close[1] and
           ForcePush[Type] < ForcePush[Periods+Type] * (1 - Percent * 0.01) 
        then 
           ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人累計買超超過N張(df: pd.DataFrame, ForceType: int = 1, Periods: int = 20, Size: int = 3000, Type: int = 1, TXT1: str = "僅適用日線", TXT2: str = "盤中無當日法人資料") -> tuple[bool, str]:
        """
        Original Strategy: 法人累計買超超過N張
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\法人累計買超超過N張.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Periods + 3);
        if barfreq <> "D" then return;
        if Type = 0 then value1 = 0 else value1 = 1;
        Switch ( ForceType ) 
        Begin 
        Case 1: 
        ForcePush = Getfield("外資持股")[value1];
        Case 2: 
        ForcePush = Getfield("投信持股")[value1]; 
        Case 3: 
        ForcePush = Getfield("自營商持股")[value1]; 
        default: 
        ForcePush = Getfield("外資持股")[value1]+Getfield("投信持股")[value1]+Getfield("自營商持股")[value1];
        End; 
        if currentbar <= Periods then return;
        if ForcePush[value1] - ForcePush[Periods+value1] >= Size then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波幅縮小後的突破(df: pd.DataFrame, period2: int = 4, period1: int = 12, ratio: int = 2, TXT: str = "建議使用5分鐘") -> tuple[bool, str]:
        """
        Original Strategy: 波幅縮小後的突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\波幅縮小後的突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(period1,period2));
        if close > close[1] * (1 + ratio*0.01) then 
        begin
        	value1=average(truerange,period1);
        	value2=average(truerange,period2);
        	if value1>value2 and value2 < close* 0.02 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 海龜進場法則(df: pd.DataFrame, Length: int = 10, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 海龜進場法則
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\海龜進場法則.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar((Length + 3)*5);
        if barfreq <> "D" and barfreq <> "AD" then Return;
        if close > highest(getfield("High","W")[1],Length)//近n週最高價
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤整後噴出(df: pd.DataFrame, Length: int = 30, percent: float = 2.5) -> tuple[bool, str]:
        """
        Original Strategy: 盤整後噴出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\盤整後噴出.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(9);
        setbarback(Length);
        value1=highest(high[1],Length);
        value2=lowest(low[1],Length);
        if close crosses above value1
        and value1 < value2 *( 1 + percent * 0.01) //最近幾根bar的收盤價高點與低點差不到N%
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破下降趨勢線(df: pd.DataFrame, Length: int = 20, Rate: int = 150) -> tuple[bool, str]:
        """
        Original Strategy: 突破下降趨勢線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\突破下降趨勢線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        Factor = 100/Close[Length];
        value1 = linearregslope(high*Factor,Length);
        value2 = linearregslope(high*Factor,3);
        if close > open and close < close[length]  and  value1 < 0 and value2-value1 > Rate*0.01 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破糾結均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, Percent: int = 5, XLen: int = 20, Volpercent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 突破糾結均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\突破糾結均線.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        Shortaverage = average(close,shortlength);
        Midaverage = average(close,midlength);
        Longaverage = average(close,Longlength);
        AvgH = maxlist(Shortaverage,Midaverage,Longaverage);
        AvgL = minlist(Shortaverage,Midaverage,Longaverage);
        if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;
        condition1 = trueAll(AvgHLp < Percent,XLen);
        condition2 = V > average(V[1],XLen)*(1+Volpercent/100) ;
        condition3 = C > AvgH *(1.02) and H > highest(H[1],XLen);
        condition4 = average(volume[1], 5) >= 1000; 
        if condition1 
        and condition2 
        and condition3 
        and condition4 
        and tselsindex(10,6)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商獨自偏好(df: pd.DataFrame, Length: int = 20, _BuyRatio: int = 5, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 自營商獨自偏好
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\自營商獨自偏好.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if barfreq <> "D" then return;
        SumForce = Summation(GetField("自營商買賣超")[1], Length);
        SumTotalVolume = Summation(Volume[1], Length);
        OtherForce = Summation(GetField("外資買賣超")[1] + GetField("投信買賣超")[1], Length);
        if SumForce > SumTotalVolume  *_BuyRatio  and SumForce > OtherForce   then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 藍籌股RSI低檔背離(df: pd.DataFrame, Periods: int = 50, Length: int = 6, LowFilter: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 藍籌股RSI低檔背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\藍籌股RSI低檔背離.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Periods,maxlist(Length,6) * 8) + 3);
        condition1 = false;
        condition2 = false;
        condition3 = false;
        condition4 = false;
        rsivalue = RSI(Close,Length);
        value1 = highestbar(high,Periods);//轉折高點距離
        value2 = lowestbar(low,Periods);//轉折低點距離
        if value2 = 0	//今日為創新低的第二隻腳
        then condition1 = true
        else return;
        if rsivalue <= LowFilter	//RSI位於低檔區
        then condition2 = true
        else return;
        if value2[value1] + value1 < Periods //在計算區間內存在第一隻腳
        then condition3 = true
        else return;
        if rsivalue[value2[value1] + value1] < rsivalue //RSI不再創新低
        then condition4 = true
        else return;
        if condition1 and condition2 and condition3 and condition4
        then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 調整型均線黃金交叉(df: pd.DataFrame, Length: int = 6, TLength: int = 20, AddLength: int = 1, TuneRatio: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 調整型均線黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\調整型均線黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(TLength + 8);
        if Length >= TLength then return;
        AvgTR = average(TrueRange,Length);
        value2 = intportion( (TLength -Length)/ AddLength);
        for value1 =  Length to TLength
        begin
            if mod( value1 ,AddLength) = 0  or value1 =TLength then
        	 begin
        		if (AvgTR > Close *  TuneRatio*0.01 ) then
        		begin
        		AvgTR = average(TrueRange,value1);
        		value3 = value1; 
        		end;
           end;
        end;
        if close crosses over  average(close[1] ,value3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 貪婪指數太高(df: pd.DataFrame, RSILength: int = 5, CLength: int = 5, VLength: int = 20, Raise: int = 20, TXT1: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 貪婪指數太高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\貪婪指數太高.xs
        XS Logic Reference:
        {@type:sensor}
        variable : MTRatio(0),CloseRatio(0),AVGV(0);
        if barfreq <> "D" then return;
        if close > lowest(low,VLength) * (1+Raise/100) then
        begin
        	MTRatio=getfield("融資增減張數")[1]/volume[1];
        	CloseRatio = close/close[CLength];
        	AVGV = volume[1]/average(volume[1],VLength);
        	value1 = RSI(MTRatio,RSILength)+RSI(CloseRatio,RSILength)+RSI(AVGV,RSILength);
        	if RSI(value1,RSILength) >75 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 進入上漲軌道(df: pd.DataFrame, period: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 進入上漲軌道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\進入上漲軌道.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1=countif(low<lowest(low[1],period),period);
        value2=countif(high>highest(high[1],period),period);
        value3=value2-value1;
        if value3 crosses over 4
        and tselsindex(10,6)[Z]=1 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 長波段回升(df: pd.DataFrame, Length1: int = 30, Size1: int = 2000, Length2: int = 20, Size2: int = 1000, Ratio: int = 10, Percent: int = 3, Type: int = 1, TXT1: str = "僅適用日線", TXT2: str = "盤中無當日融資資料") -> tuple[bool, str]:
        """
        Original Strategy: 長波段回升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\長波段回升.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Length1,Length2) + 3);
        if barfreq <> "D"  or (currenttime < 133000 and Type=0) then return;
        if Type = 0 then value1 = 0 else value1 = 1;
        condition1=false;
        condition2=false;
        condition3=false;
        condition4=false;
        if close/close[1] > 1 + Percent * 0.01 //今日強勢股
        then condition1=true
        else return;
        if average(volume,Length1) < Size1//長期乏人問津
        then condition2=true
        else return;
        if  trueany( Low < Low[1],length1) then return;//多日未破底
        value2=GetField("Pomremain")[value1];//融資餘額
        value3=GetField("Pomusingratio")[value1];//融資使用率
        if value2[Length2]-value2 > Size2 and value3 < Ratio * 0.01//籌碼長期沈澱
        then condition3 = true 
        else return;
        if average(truerange,5)>average(truerange,10)//短線波動幅度開始變大
        then condition4 = true
        else return;
        if condition1 and condition2 and condition3 and condition4 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 雙KD向上(df: pd.DataFrame, Length_D: int = 9, Length_W: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 雙KD向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\雙KD向上.xs
        XS Logic Reference:
        {@type:sensor}
        stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        condition1 = kk_d crosses above dd_d;		// 日KD crosses over
        condition2 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
        condition3 = average(volume[1], 5) >= 1000;
        condition4 = kk_d[1] <= 30;							// 日K 低檔
        condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
        // 成交量判斷
        Condition6 = Average(Volume[1], 100) >= 1000;
        if condition1 
        and condition2 
        and condition3 
        and condition4 
        and condition5 
        and condition6
        and tselsindex(10,6)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 領先大盤創200日新高(df: pd.DataFrame, period: int = 200) -> tuple[bool, str]:
        """
        Original Strategy: 領先大盤創200日新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\波段操作型\領先大盤創200日新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalBar(period*2);
        value1 = GetSymbolField("tse.tw","收盤價");
        value2 = highest(value1,period);//大盤區間高點
        value3 = barslast(close=highest(close,period));
        if value1<value2//大盤未過新高
        and close=highest(close,period)//股價創新高
        and value3[1]>100
        and GetSymbolField("tse.tw","收盤價")>average(GetSymbolField("tse.tw","收盤價"),10)
        and average(volume,100)>1000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
