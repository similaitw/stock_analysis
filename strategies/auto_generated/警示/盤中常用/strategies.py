# Auto-generated strategies for: 警示/盤中常用
import pandas as pd
import numpy as np

class 盤中常用Strategies:

    @staticmethod
    def strategy_1分鐘K開盤暴量三連陽(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 1分鐘K開盤暴量三連陽
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\盤中常用\1分鐘K開盤暴量三連陽.xs
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
    def 大單敲進(df: pd.DataFrame, atVolume: int = 50, LaTime: int = 10, TXT: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 大單敲進
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\盤中常用\大單敲進.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        //計數器
        Volumestamp =GetField("Volume", "D");
        if time < time[1] 
        or Volumestamp = Volumestamp[1]
        then Xtime =0; //開盤那根要歸0次數
        if GetField("Volume", "Tick") > atVolume
        //單筆tick成交量超過大單門檻
        and GetField("內外盤","Tick")=1
        //外盤成交
        then Xtime+=1; 
        //量夠大就加1次
        if Xtime > LaTime then begin
        	ret=1; 
        	Xtime=0;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤中委買遠大於委賣(df: pd.DataFrame, v1: int = 2000, v2: int = 500, v3: int = 1500, v4: int = 400, v5: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 盤中委買遠大於委賣
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\盤中常用\盤中委買遠大於委賣.xs
        XS Logic Reference:
        {@type:sensor}
        condition1=false;
        condition2=false;
        condition3=false;
        bidtv=q_SumBidSize;//總委買
        asktv=q_SumAskSize;//總委賣
        value1=q_BestBidSize1;//委買一
        value2=q_BestBidSize2;
        value3=q_bestbidsize3;
        value4=q_bestbidsize4;
        value5=q_bestbidsize5;
        value6=q_bestasksize1;//委賣一
        value7=q_bestasksize2;
        value8=q_bestasksize3;
        value9=q_bestasksize4;
        value10=q_bestasksize5;
        tb=bidtv*close/10;
        ta=asktv*close/10;
        if tb>v1 and ta<v2 and tb-ta>v3
        then condition1=true;
        b1=value1*close/10;
        b2=value2*close/10;
        b3=value3*close/10;
        b4=value4*close/10;
        b5=value5*close/10;
        s1=value6*close/10;
        s2=value7*close/10;
        s3=value8*close/10;
        s4=value9*close/10;
        s5=value10*close/10;
        if minlist(b1,b2,b3,b4,b5)>v4
        then condition2=true;
        if maxlist(s1,s2,s3,s4,s5)<v5
        then condition3=true;
        if close<>GetField("漲停價", "D") then begin
        	if  condition1 
        	or (condition2 and condition3)
        	then ret=1; 
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤跳空上漲N_且有量(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開盤跳空上漲N%且有量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\盤中常用\開盤跳空上漲N%且有量.xs
        XS Logic Reference:
        {@type:sensor}
        if open >=close[1]*1.03
        and volume*close>300000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 預估量破均量(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 預估量破均量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\盤中常用\預估量破均量.xs
        XS Logic Reference:
        {@type:sensor}
        value1=GetField("內盤量", "D");//當日內盤量
        value2=GetField("外盤量", "D");//當日外盤量
        if GetField("估計量") > average(volume[1],10)*1.3
        and value2>value1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
