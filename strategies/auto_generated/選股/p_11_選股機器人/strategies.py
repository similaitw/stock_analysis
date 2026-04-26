# Auto-generated strategies for: 選股/11.選股機器人
import pandas as pd
import numpy as np

class Cat11選股機器人Strategies:

    @staticmethod
    def 上游價格指標趨勢向上(df: pd.DataFrame, Period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 上游價格指標趨勢向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\上游價格指標趨勢向上.xs
        XS Logic Reference:
        {@type:filter}
        Condition1 = rateofchange(GetField("上游股價指標"), period) >= Period; 
        Condition2 = GetField("上游股價指標") > GetField("上游股價指標")[Period/2]; 
        Condition3 = GetField("上游股價指標") > average(GetField("上游股價指標"), period); 
        ret = condition1 and condition2 and condition3; 
        outputfield(1,rateofchange(GetField("上游股價指標","D"),period),2,"上游漲幅%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下游價格指標趨勢向上(df: pd.DataFrame, Period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 下游價格指標趨勢向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\下游價格指標趨勢向上.xs
        XS Logic Reference:
        {@type:filter}
        Condition1 = rateofchange(GetField("下游股價指標"), period) >= Period; 
        Condition2 = GetField("下游股價指標") > GetField("下游股價指標")[Period/2]; 
        Condition3 = GetField("下游股價指標") > average(GetField("下游股價指標"), period); 
        ret = condition1 and condition2 and condition3; 
        outputfield(1,rateofchange(GetField("下游股價指標","D"),Period),2,"下游漲幅%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 中小型股整理結束(df: pd.DataFrame, Periods: int = 20, Ratio: int = 3, Direction: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 中小型股整理結束
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\中小型股整理結束.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        //盤整後噴出
        condition1 = false;
        if (highest(high[1],Periods-1) - lowest(low[1],Periods-1))/close[1] <= ratio*0.01 
        then condition1=true//近期波動在?%以內
        else return;
        if condition1 and Direction > 0 and high = highest(high, Periods)
        and close>close[1]*1.02
        then ret=1;//盤整後往上突破
        outputfield(1,highest(high[1],Periods-1),2,"整理區高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 創百日新高但距低點不遠(df: pd.DataFrame, day: int = 200, day1: int = 20, percents: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 創百日新高但距低點不遠
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\創百日新高但距低點不遠.xs
        XS Logic Reference:
        {@type:filter}
        //說明：今天的收盤價創百日的收盤價新高，但收盤價距離區間低點不遠
        value1=lowest(close,day1);
        if close=highest(close,day)
        and value1*(1+percents/100)>=close
        and close >= value1*1.05
        and volume >= average(volume[1], 5)
        then ret=1;
        outputfield(1, value1, 2, "區間低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 可能由盈轉虧(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 可能由盈轉虧
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\可能由盈轉虧.xs
        XS Logic Reference:
        {@type:filter}
        // 計算最新一期月營收的日期(mm=月份)
        //
        mm = datevalue(getfielddate("月營收","M"),"M");
        // 預估最新一季的季營收(單位=億)
        //
        if mm=1 or mm=4 or mm=7 or mm=10
        then value1=GetField("月營收","M") * 3;
        if mm=2 or mm=5 or mm=8 or mm=11
        then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
        if mm=3 or mm=6 or mm=9 or mm=12
        then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];
        // 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
        //
        value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");
        ret = 1;
        outputfield(1,value2 / 100,2,"預估單季本業獲利(億)", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 可能轉虧為盈(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 可能轉虧為盈
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\可能轉虧為盈.xs
        XS Logic Reference:
        {@type:filter}
        // 計算最新一期月營收的日期(mm=月份)
        //
        mm = datevalue(getfielddate("月營收","M"),"M");
        // 預估最新一季的季營收(單位=億)
        //
        if mm=1 or mm=4 or mm=7 or mm=10
        then value1=GetField("月營收","M") * 3;
        if mm=2 or mm=5 or mm=8 or mm=11
        then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
        if mm=3 or mm=6 or mm=9 or mm=12
        then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];
        // 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
        //
        value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");
        if value2 > 0 and GetField("營業利益","Q") < 0 then
        ret = 1;
        outputfield(1,value1,2,"預估單季營收(億)", order := 1);
        outputfield(2, value2 / 100,2, "預估單季本業獲利(億)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資先前沒買_突然連買三天(df: pd.DataFrame, _period: int = 20, _ratio: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 外資先前沒買，突然連買三天
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\外資先前沒買，突然連買三天.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1 = trueall(GetField("外資買賣超","D")[3]=0, _period);
        condition2 = trueall(GetField("外資買賣超","D")*100/volume>=_ratio,3);
        if condition1 and condition2 
        then ret=1;
        value1 = Summation(GetField("外資買賣超","D"), 3) / Summation(Volume, 3) * 100;
        outputfield(1,value1,2,"外資買超%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多次到頂而破(df: pd.DataFrame, HitTimes: int = 3, RangeRatio: int = 2, Length: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 多次到頂而破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\多次到頂而破.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        //找到過去其間的最高點
        theHigh = Highest(High[1],Length);
        value1=highestbar(high[1],length);
        // 設為瓶頸區間上界
        HighLowerBound = theHigh *(100-RangeRatio)/100;
        //回算在此區間中 進去瓶頸區的次數
        TouchRangeTimes = CountIF(High[1] > HighLowerBound, Length-value1);
        Condition1 = TouchRangeTimes >= HitTimes;
        Condition2 = close > theHigh;
        Condition3 = close[length]*1.2<thehigh;
        condition4=false;
        if Condition1 and Condition2 and condition3
        then condition4=true;
        if barslast(condition4=true)=1
        then ret=1;
        outputfield(1, theHigh, 2, "區間高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭下起漲前的籌碼收集(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭下起漲前的籌碼收集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\多頭下起漲前的籌碼收集.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("分公司買進家數");
        value2=GetField("分公司賣出家數");
        value3=value2-value1;
        value4=countif(value3>20,10);
        if value4>6 and close[30]>close*1.1
        then ret=1;
        outputfield(1,value1,0,"買進家數", order := -1);
        outputfield(2,value2,0,"賣出家數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 天價上影線賣出訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 天價上影線賣出訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\天價上影線賣出訊號.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        if H > O*1.03 and C <O and H = highest(H,255) then Kprice = L;
        condition1 = c crosses below Kprice;
        condition2 = average(volume[1], 5) >= 500;
        ret = condition1 and condition2;
        outputfield(1,Kprice,2,"關卡價", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信初介入(df: pd.DataFrame, day: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 投信初介入
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\投信初介入.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1 = summation(GetField("投信買賣超")[1], day); 
        value2 = summation(volume[2], day);
        condition1 = value1 < value2 * 0.02;
        //先前投信不怎麼買這檔股票
        condition2 = GetField("投信買賣超")>= volume[1] * 0.15;
        //投信開始較大買超
        condition3 = H > H[1];
        //買了股價有往上攻
        condition4 = C > C[1];
        //今天收盤有往上走
        condition5=close<close[10]*1.05;
        RET = condition1 and condition2 and condition3 and condition4 and condition5;
        outputfield(1,GetField("投信買賣超","D"),0,"投信買超", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信掃貨(df: pd.DataFrame, pastDays: int = 5, _BuyRatio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 投信掃貨
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\投信掃貨.xs
        XS Logic Reference:
        {@type:filter}
        SumForce = Summation(GetField("投信買賣超"), pastDays);
        sumTotalVolume = Summation(Volume, pastDays);
        value1 = SumForce / SumTotalVolume * 100;
        if value1 > _BuyRatio then ret =1;
        outputfield(1,value1,2,"投信買超%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信第一天大買(df: pd.DataFrame, v1: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 投信第一天大買
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\投信第一天大買.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("投信持股","D");
        value2=GetField("投信買賣超","D");
        if value1 < v1 and value2 > VOLUME*0.2
        then ret=1;
        outputfield(1,GetField("投信買賣超","D"),0,"投信買超", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收年增率移動平均黃金交叉b(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 月營收年增率移動平均黃金交叉b
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\月營收年增率移動平均黃金交叉b.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收年增率","M");
        if average(value1,4) crosses over average(value1,12)
        and value1 > 0
        then ret=1;
        outputfield(1,value1,2,"月營收年增率%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 殺過頭(df: pd.DataFrame, day: int = 5, period: int = 20, r1: int = 20, r2: int = 10, r3: int = 2, v1: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 殺過頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\殺過頭.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1=false;
        condition2=false;
        condition3=false;
        if highest(high,period)>=close[1]*(1+r1/100)
        then condition1=true;
        if highest(high,day)>=close[1]*(1+r2/100)
        then condition2=true;
        if close>=close[1]*(1+r3/100) and v1>=1000
        then condition3=true;
        if condition1 and condition2 and condition3
        then ret=1;
        outputfield(1,lowest(low,period),2,"前波低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 毛利率創一年新高(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 毛利率創一年新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\毛利率創一年新高.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業毛利率","Q");
        if value1=highest(value1,12)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 毛利率沒掉的兇(df: pd.DataFrame, ratio: int = 10, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 毛利率沒掉的兇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\毛利率沒掉的兇.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業毛利率","Q");
        if trueall(value1>value1[1]*(1-ratio/100),period)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 烏龜交易法則之買進訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 烏龜交易法則之買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\烏龜交易法則之買進訊號.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1=false;
        condition2=false;
        if high=highest(high,100)and barslast(high=highest(high,100))[1]>100
        then condition1=true; 
        //創百日新高且上一次發生時是在100個交易日之前
        if average(volume[1], 5) >= 1000
        then condition2=true;
        //五日移動平均量大於千張
        if condition1 and condition2
        then ret=1;
        outputfield(1,highest(high,100),2,"突破高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 烏龜交易法則之賣出訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 烏龜交易法則之賣出訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\烏龜交易法則之賣出訊號.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1=false;
        condition2=false;
        if L=lowest(L,100)and barslast(L=lowest(L,100))[1]>100
        then condition1=true; 
        //創百日新低且上一次發生時是在100個交易日之前
        if average(volume[1], 5) >= 1000
        then condition2=true;
        //五日移動平均量大於千張
        if condition1 and condition2
        then ret=1;
        outputfield(1,lowest(L,100),2,"跌破低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破糾結均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, Percent: int = 5, XLen: int = 20, Volpercent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 突破糾結均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\突破糾結均線.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        shortaverage = average(close,shortlength);
        midaverage = average(close,midlength);
        Longaverage = average(close,Longlength);
        AvgH = maxlist(shortaverage,midaverage,Longaverage);
        AvgL = minlist(shortaverage,midaverage,Longaverage);
        if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;
        condition1 = trueAll(AvgHLp < Percent,XLen);
        condition2 = V > average(V[1],XLen)*(1+Volpercent/100) ;
        condition3 = C > AvgH *(1.02) and H > highest(H[1],XLen);
        condition4 = average(volume[1], 5) >= 1000; 
        ret = condition1 and condition2 and condition3 and condition4;
        outputfield(1,AvgH,2,"均線上緣", order := -1);
        outputfield(2,AvgL,2,"均線下緣");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 總市值位於歷史低檔區(df: pd.DataFrame, period: int = 1250, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 總市值位於歷史低檔區
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\總市值位於歷史低檔區.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("總市值");
        value2=lowest(GetField("總市值"),period);
        if value1<value2*(1+ratio/100)
        //總市值距離過去一段時間最低點沒有差多遠
        then begin
        	if close=highest(close,20)
        	and close<close[19]*1.07
        	and close crosses over average(close,20)
        	and close<=15
        	then ret=1;
        end;
        outputfield(1, value1, 2, "總市值(億)", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價領先大盤創新高(df: pd.DataFrame, Length: int = 20, BandRange: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 股價領先大盤創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\股價領先大盤創新高.xs
        XS Logic Reference:
        {@type:filter}
        Condition1 = GetSymbolField("TSE.TW","收盤價","D") > average(GetSymbolField("TSE.TW","收盤價","D"),10);
        Condition2 = average(GetSymbolField("TSE.TW","收盤價","D"),5) > average(GetSymbolField("TSE.TW","收盤價","D"),20);
        value1=close/GetSymbolField("TSE.TW","收盤價","D");
        up = bollingerband(value1, Length, BandRange);
        Condition3 = TrueAll(value1 >= up, 3);
        // 成交量判斷
        Condition99 = Average(Volume[1], 100) >= 1000;
        if Condition1 And Condition2 And Condition3 And Condition99 then ret=1;
        outputfield(1, rateofchange(c,5), 2, "5日漲幅%", order := 1);
        outputfield(2, rateofchange(GetSymbolField("TSE.TW","收盤價","D"),5), 2, "大盤5日漲幅%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週轉率高點買進(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 週轉率高點買進
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\週轉率高點買進.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("成交金額");
        value2=GetField("總成交次數","D");
        if value2>0 then value3=value1/value2;
        if value3=highest(value3,200)
        and close>close[1]*1.025
        and close[2]<close[12]*1.05
        and volume>2000
        then ret=1;
        outputfield(1, GetField("週轉率","D"), 2, "週轉率%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 除權後的填權行情(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 除權後的填權行情
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\11.選股機器人\除權後的填權行情.xs
        XS Logic Reference:
        {@type:filter}
        if  close[1]*1.1<close[20]
        and close>close[1]*1.025
        and volume>average(volume,20)
        then ret=1;
        value1=getbaroffset(dateadd(GetField("除權息日期"),"D",-1));
        outputfield(1,close[value1],2,"除權參考價");
        outputfield(2,-RateOfChange(c,value1),2,"貼權率%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
