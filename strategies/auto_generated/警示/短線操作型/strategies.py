# Auto-generated strategies for: 警示/短線操作型
import pandas as pd
import numpy as np

class 短線操作型Strategies:

    @staticmethod
    def 一小時線長期盤整後突破(df: pd.DataFrame, Periods: int = 20, Ratio: int = 3, Direction: int = 1, TXT1: str = "僅適用60分鐘") -> tuple[bool, str]:
        """
        Original Strategy: 一小時線長期盤整後突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\一小時線長期盤整後突破.xs
        XS Logic Reference:
        {@type:sensor}
        //盤整後噴出
        settotalbar(3);
        setbarback(Periods);
        condition1 = false;
        if (highest(high[1],Periods-1) - lowest(low[1],Periods-1))/close[1] <= ratio*0.01 
        then condition1=true//近期波動在?%以內
        else return;
        if condition1 and Direction > 0 and high = highest(high, Periods)
        then ret=1;//盤整後往上突破
        if condition1 and Direction < 0 and low = lowest(low, Periods)
        then ret=1;//盤整後往下跌破
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 一黑破三紅(df: pd.DataFrame, periods: int = 20, ratio: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 一黑破三紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\一黑破三紅.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        setbarback(Periods);
        if periods < 5 then return;
        condition1=false;
        condition2=false;
        condition3=false;
        if (high[1] - low[periods-1])/low[periods-1] >= ratio*0.01 
        then condition1=true//近n日漲幅超過?%
        else return;
        if high>highest(high[1],3) and c<lowest(low[1],3)
        then condition2=true//開盤是四日來新高但收盤比三日前低點低
        else return;
        //前二天每天比前一天上漲且連續三天收紅棒
        condition3 = TrueAll(c[1]>c[2], 2) and
        			 TrueAll(open[1]<close[1], 3); 
        if condition1 and condition2 and condition3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三根長下影線(df: pd.DataFrame, Percent: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 三根長下影線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\三根長下影線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        condition1 = (minlist(open,close)-low) > absvalue(open-close)*3; 
        condition2 = minlist(open,close) > low * (100 + Percent)/100;
        if trueall( condition1 and condition2, 3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 中小型股整理結束(df: pd.DataFrame, Periods: int = 20, Ratio: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 中小型股整理結束
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\中小型股整理結束.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(300);
        setbarback(50);
        condition1 = false;
        if (highest(high[1],Periods-1) - lowest(low[1],Periods-1)) <= ratio*0.01*close[1]
        then condition1=true//近期波動在?%以內
        else return;
        if condition1 
        and high = highest(high, Periods)
        and GetSymbolField("tse.tw","收盤價")>average(GetSymbolField("tse.tw","收盤價"),10)
        and average(GetSymbolField("tse.tw","收盤價"),5)>average(GetSymbolField("tse.tw","收盤價"),20)
        then ret=1;//盤整後往上突破
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力慢慢收集籌碼後攻堅(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 主力慢慢收集籌碼後攻堅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\主力慢慢收集籌碼後攻堅.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        Value1=GetField("分公司買進家數","D")[Z];
        value2=GetField("分公司賣出家數","D")[Z];
        value3=(value2-value1);
        //賣出的家數比買進家數多的部份
        value4=average(close,5);
        //五日移動平均
        if countif(value3>30, period)/period >0.7
        and linearregslope(value4,5)>0
        and Average(Volume[1], 100) >= 500
        and tselsindex(10,7)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 加速趕底中(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 加速趕底中
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\加速趕底中.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(210);
        if Close[4] > Close *1.07 and
           TrueAll (truerange/Close > 0.02,3) and
           Close < Highest(high,200) *0.7 
        then Ret=1;
        {自高檔回跌三成且近5期收低7%以上,近3期每期波動至少有2%}
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資買超但只開平高盤(df: pd.DataFrame, Atleast: int = 1000, Gap: int = 2, TXT1: str = "僅適用日線", TXT2: str = "需逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 外資買超但只開平高盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\外資買超但只開平高盤.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq = "D" and  Getfield("外資買賣超")[1] > Atleast and
           GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100) and
           GetField("Open", "D") > GetField("RefPrice", "D") 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資連日大買超_股價未開高(df: pd.DataFrame, Periods: int = 3, Atleast: int = 10000, Gap: int = 1, TXT1: str = "僅適用日線", TXT2: str = "需逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 外資連日大買超，股價未開高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\外資連日大買超，股價未開高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Periods);
        if BarFreq = "D" and
           Trueall( Getfield("外資買賣超")[1]*Close*0.1 > Atleast ,Periods)  and
           GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資連續買超n天(df: pd.DataFrame, Periods: int = 5, TXT1: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 外資連續買超n天
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\外資連續買超n天.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Periods);
        if BarFreq <> "D"  then return;
        Ret = TrueAll(GetField("外資買賣超")[1] > 0, Periods);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信初介入(df: pd.DataFrame, day: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 投信初介入
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信初介入.xs
        XS Logic Reference:
        {@type:sensor}
        if GetSymbolField("TSE.TW","收盤價") > average(GetSymbolField("TSE.TW","收盤價"),10)
        and Average(Volume[1], 100) >= 1000
        then begin
        	value1 = summation(GetField("投信買賣超")[1], day); 
        	value2 = summation(volume[2], day);
        	condition1 = value1 < value2 * 0.02;
        	//先前投信不怎麼買這檔股票
        	if getfielddate("投信買賣超") <> date then
        		value99 = GetField("投信買賣超")[1]
        	else
        		value99 = GetField("投信買賣超");
        	condition2 = value99>= volume[1] * 0.15;
        	//投信開始較大買超
        	condition3 = H > H[1];
        	//買了股價有往上攻
        	condition4 = C > C[1];
        	//今天收盤有往上走
        	condition5=close<close[10]*1.05;
        	condition6=GetSymbolField("TSE.TW","收盤價") > average(GetSymbolField("TSE.TW","收盤價"),10);
        	if condition1 
        	and condition2 
        	and condition3 
        	and condition4
        	and condition5 
        	and condition6
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信外資同步進場(df: pd.DataFrame, Fboughts: int = 100, Sboughts: int = 100, TXT1: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信外資同步進場
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信外資同步進場.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D"  then return;
        if GetField("外資買賣超")[1]>Fboughts and GetField("投信買賣超")[1]>Sboughts
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信搶買的股票(df: pd.DataFrame, miniratio: int = 10, lv: int = 2000, holdratio: int = 10, TXT1: str = "僅適用日線", TXT2: str = "需選用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 投信搶買的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信搶買的股票.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D"  then return;
        //1.中小型股
        //2.原來庫存低
        //3.今天買進張數超過成交量的一成
        //4.收今天最高
        value1=GetField("Stotalbuy")[1];//投信買張
        value2=GetField("Ssharesheld")[1];//投信持股
        value3=GetField("Ssharesheldratio")[1];//投信持股比例
        if close > high[1] and close[1]=high[1]   and //昨天收高 今日再漲
           value1 > volume[1] * miniratio*0.01 and //昨日買進張數超過成交量的一成
           value2 < lv and //原來庫存低
           value3 < holdratio //原來庫存低
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信殺完之跌深反彈(df: pd.DataFrame, day: int = 5, ratio: int = 60, TXT1: str = "僅適用日線", TXT2: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 投信殺完之跌深反彈
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信殺完之跌深反彈.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(day + 3);
        if close>open and close[3] > close[1] * 1.1  and BarFreq ="D" then
        begin
          if TrueAll(GetField("Sdifference")[1] <0,day) and
             GetField("Ssharesheld")[1] < GetField("Ssharesheld")[Day+1] * (1- Ratio/100) 
          then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信買張超過成交量一成(df: pd.DataFrame, Ratio: int = 10, Gap: float = 2.5, TXT1: str = "僅適用日線", TXT2: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 投信買張超過成交量一成
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信買張超過成交量一成.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D"  or currenttime > 90500 then return;
        value1=GetField("Stotalbuy")[1];//投信買張
        value2=GetField("Ssharesheldratio")[1];//投信持股比例
        if value2<Ratio and value1/volume[1]>0.1 and close < close[1] *(1 + Gap * 0.01)
        then ret=1;     
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信連日大買超_股價未開高(df: pd.DataFrame, Periods: int = 3, Atleast: int = 10000, Gap: int = 1, TXT1: str = "僅適用日線", TXT2: str = "需逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 投信連日大買超，股價未開高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\投信連日大買超，股價未開高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Periods + 3);
        if BarFreq = "D" and
           Trueall( Getfield("投信買賣超")[1]*Close*0.1 > Atleast ,Periods)  and
           GetField("Open", "D") < GetField("RefPrice", "D") *(1+Gap/100) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲勢加速的股票(df: pd.DataFrame, day2: int = 5, day1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 漲勢加速的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\漲勢加速的股票.xs
        XS Logic Reference:
        {@type:sensor}
        if angle(date[day1],date[day2])>0
        and angle(date[day2],date)>angle(date[day1],date[day2])
        and angle(date[day2],date)>25
        and GetSymbolField("tse.tw","收盤價","W")
        >average(GetSymbolField("tse.tw","收盤價","W"),13)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 炒高後沒有量(df: pd.DataFrame, Periods: int = 120, Ratio: int = 50, Sizes: int = 2000, TXT1: str = "僅適用日線", TXT2: str = "需選用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 炒高後沒有量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\炒高後沒有量.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Periods);
        if BarFreq = "D"  and currenttime>130000 and
           getfield("融資餘額張數")[1] > 2000 and //昨日融資餘額多於2000張
           getfield("融券餘額張數")[1] < 2000 and //昨日融券餘額少於2000張
           close >= close[Periods] *(1 + Ratio*0.01) and //過去半年漲幅超過五成
           average(volume[1],5) < Sizes and //五日均量低於N張
           GetQuote("DailyVolume")< 500 and //當日總量
           GetQuote("OutSize") < GetQuote("DailyVolume")*0.5 //當日外盤量小於總量一半
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 短線轉強(df: pd.DataFrame, day: int = 66, ratio: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 短線轉強
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\短線轉強.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1=GetField("法人買張")[Z]; value2=average(value1,day);
        value3=GetField("強弱指標")[Z]; value4=average(value3,day);
        value5=GetField("外盤均量")[Z]; value6=average(value5,day);
        value7=GetField("主動買力")[Z]; value8=average(value7,day);
        value9=GetField("開盤委買"); value10=average(value9,day);
        count=0;
        if value1>=value2*(1+ratio/100) then count=count+1;
        if value3>=value4*(1+ratio/100) then count=count+1;
        if value5>=value6*(1+ratio/100) then count=count+1;
        if value7>=value8*(1+ratio/100) then count=count+1;
        if value9>=value10*(1+ratio/100) then count=count+1;
        if count>=4 and close<lowest(close,day)*1.1
        and GetSymbolField("tse.tw","收盤價","D")>average(GetSymbolField("tse.tw","收盤價","D"),10)
        and average(volume,200)>2000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破繼續型態(df: pd.DataFrame, Length: int = 20, Rate: int = 150) -> tuple[bool, str]:
        """
        Original Strategy: 突破繼續型態
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\突破繼續型態.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        Factor = 100/Close[Length];
        if close > open and  close < close[length] then
        begin
        	value1 = linearregslope(high*Factor,Length);
        	value2 = linearregslope(high*Factor,3);
        	if value1 < 0 and  value2-value1 > Rate*0.01 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 站上五根bar高點(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 站上五根bar高點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\站上五根bar高點.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if close > highest(High[1],4)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 第一根漲停(df: pd.DataFrame, Periods: int = 5, Size: int = 1500) -> tuple[bool, str]:
        """
        Original Strategy: 第一根漲停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\第一根漲停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Periods + 3);
        if Periods < 1 then return;
        if q_ask=GetField("漲停價", "D") and q_bestasksize1<Size then 
        begin
        	for value1 = 1 to Periods
        	begin
        		if closeD(value1-1) > closeD(value1) * 1.065 then return;
        	end;
        	ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 籌碼由發散轉收集(df: pd.DataFrame, Length_D: int = 9, Length_W: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 籌碼由發散轉收集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\籌碼由發散轉收集.xs
        XS Logic Reference:
        {@type:sensor}
        SetTotalBar(maxlist(Length_D,6) * 3);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        condition1=false;
        value1=GetField("現股當沖張數","D")[Z];
        value2=GetField("外資買賣超","D")[Z];
        value3=GetField("投信買賣超","D")[Z];
        value4=GetField("自營商買賣超","D")[Z];
        value5=GetField("主力買賣超張數","D")[Z];
        value6=GetField("融資增減張數","D")[Z];
        value7=GetField("融券增減張數","D")[Z];
        value8=volume-value1;//當日淨交易張數
        value9=value2+value3+value4+value5-value6+value7;
        //籌碼收集張數
        if TSELSindex(10,5)[Z]=1 then begin
        	if value8<>0 then 
        		value10=value9/value8*100
        	else
        		value10=value10[1];
        	value11=average(value10,10);
        	if value11 crosses over 10 then condition1=true;
        	stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        	xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);
        	condition2 = kk_d crosses above dd_d;		// 日KD crosses over
        	condition3 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
        	condition4 = kk_d[1] <= 30;							// 日K 低檔
        	condition5 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
        	if condition1 and condition2 and condition3 and condition4 and condition5
        	then ret = 1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 除權前的逆襲(df: pd.DataFrame, Ratio: int = 5, TXT1: str = "僅適用日線", TXT2: str = "需選用逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 除權前的逆襲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\短線操作型\除權前的逆襲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if BarFreq = "D" and Close > Close[2] *(1+Ratio/100) and
           Close > Close[1] and Close[1] > Close[2]
        then
        begin
          if GetField("融券餘額張數")[1] = 0 and  GetField("融券餘額張數")[2] = 0 and 
             GetField("融資餘額張數")[1] >0 {推測是除權前停券} then ret=1; 
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
