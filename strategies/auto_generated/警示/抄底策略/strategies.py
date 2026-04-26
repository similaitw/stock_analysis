# Auto-generated strategies for: 警示/抄底策略
import pandas as pd
import numpy as np

class 抄底策略Strategies:

    @staticmethod
    def 大跌後均線糾結後上漲(df: pd.DataFrame, s1: int = 5, s2: int = 10, s3: int = 20, Percent: int = 2, Volpercent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後均線糾結後上漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\抄底策略\大跌後均線糾結後上漲.xs
        XS Logic Reference:
        {@type:sensor}
        if volume > average(volume,s3) * (1 + volpercent * 0.01)
        //放量25%
        and lowest(volume,s3)<1000
        //區間最低量小於一千張
        and volume>2000
        //今日成交量突破2000張
        then begin
        	Shortaverage = average(close,s1);
        	Midaverage = average(close,s2);
        	Longaverage = average(close,s3);
        	value1= maxlist(Shortaverage,Midaverage,Longaverage) - minlist(Shortaverage,Midaverage,Longaverage);
        	if  value1*100 < Percent*Close
        	and linearregangle(value1,5)<10
        	//均線糾結在一起
        	and close*1.3<close[40]
        	//最近四十個交易日跌了超過三成
        	then ret=1; 
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後的低檔五連陽(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後的低檔五連陽
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\抄底策略\大跌後的低檔五連陽.xs
        XS Logic Reference:
        {@type:sensor}
        if trueall(close>open,5) 
        and close*1.4<close[90]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後的連續跳空上漲(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後的連續跳空上漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\抄底策略\大跌後的連續跳空上漲.xs
        XS Logic Reference:
        {@type:sensor}
        if close*1.5<close[40]
        //過去四十個交易日跌了超過四成
        and countif(open > close[1],5)>=3
        //過去五天有三天以上開盤比前一天收盤高
        and GetSymbolField("tse.tw","收盤價","D")
        >average(GetSymbolField("tse.tw","收盤價","D"),10)
        //指數位於十日均線之上
        and average(volume,5)>2000
        //五日均量大於2000張
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 底部確認(df: pd.DataFrame, period: int = 200) -> tuple[bool, str]:
        """
        Original Strategy: 底部確認
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\抄底策略\底部確認.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        count=0;
        ld=lowest(low,period);
        ldb=lowestbar(low,period);
        hd=highest(high,period);
        hdb=highestbar(high,period);
        x1=GetField("總市值","D")[Z];//單位：億
        if hdb>ldb and hd>ld*1.4 and ld>=ld[1] and x1>20 then begin
        //股價大跌後
        	value1=countif((close-open)/open>1.5,ldb);
        	//自最低點以來的中長紅K棒數
        	if value1>=ldb/5 then count=count+1;
        	value2=summationif(close>close[1],volume,ldb);
        	//自最低點以來的上漲量
        	value3=summationif(close<close[1],volume,ldb);
        	//自最低點以來的下跌量
        	if value2>2*value3 then count=count+1;
        	value4=nthlowestbar(2,low,ldb);
        	//第二個低點的k棒位置
        	value5=nthlowestbar(3,low,ldb);
        	//第三個低點的K棒位置
        	value6=nthlowestbar(4,low,ldb);
        	//第四個低點的K棒位置
        	if value4>value5 and value5>value6 then count=count+1;
        	value7=countif(absvalue(close[1]/close-1)/close[1]*100<1 and close<close[1],ldb);
        	//自低點以來的小黑棒K棒數
        	if value7>0.5*countif(close<close[1],ldb) then count=count+1;
        	//小黑k棒佔下跌k棒超過一半
        	value8=countif(close>low*1.01,ldb);
        	//自低點以來的長下影線天數
        	if value8 >=ldb/5 then count=count+1;
        	value9=countif(close=high,ldb);
        	//自低點以來收最高的天數
        	if value9>=ldb/5 then count=count+1;
        	if ldb>=5 then count=count+1;
        end;
        if count[1]>2 and count crosses over 5 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌深後的反彈(df: pd.DataFrame, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 跌深後的反彈
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\抄底策略\跌深後的反彈.xs
        XS Logic Reference:
        {@type:sensor}
        if open*1.025<close[1]//開盤重挫
        and close>open //收盤比開盤高
        and close*(1+ratio/100)<close[9]
        //近十日跌幅超過N%
        and low*1.01<open
        //開低後又殺低
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
