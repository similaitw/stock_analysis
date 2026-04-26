# Auto-generated strategies for: 選股/09.時機操作
import pandas as pd
import numpy as np

class Cat09時機操作Strategies:

    @staticmethod
    def 即將進入季節性多頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 即將進入季節性多頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\即將進入季節性多頭.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AM");
        settotalbar(3);
        array:m1[7](0);
        avgup = 0;
        for x=1 to 7 begin
        	m1[x]=(close[12*x-1]-close[12*x])/close[12*x];
        end;
        count=0;
        for x=1 to 7 begin
        	if m1[x]>0.02 then begin
        		count=count+1;
        		avgup=avgup+m1[x];
        	end;
        end;
        if count>=6 and close>5 
        and average(volume,20)>10000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 即將進入季節性空頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 即將進入季節性空頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\即將進入季節性空頭.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AM");
        settotalbar(3);
        array:m1[7](0);
        avgdn=0;
        for x=1 to 7 begin
        	m1[x]=(close[12*x-1]-close[12*x])/close[12*x];
        end;
        count=0;
        for x=1 to 7 begin
        	if m1[x]<-0.02 then begin
        		count=count+1;
        		avgdn=avgdn+m1[x];
        	end;
        end;
        if count>=6 and close>10
        and average(volume,20)>20000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 可能有填權行情的股票(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 可能有填權行情的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\可能有填權行情的股票.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("除權日期");
        value2=GetField("每股稅後淨利(元)","Y");
        if value1>date
        and datediff(value1,date)<5
        //除權後五天內
        and trueall(close<close[1]*1.02,3)
        //除權前後未大漲
        and value2>=2
        //每股稅後淨利大於2元
        then ret=1;
        outputfield(1,value1,0,"今年度除權日");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台幣升值受災股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 台幣升值受災股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\台幣升值受災股.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("每股營業額(元)","Y");
        value2=GetField("外銷比率","Y");
        if value1>20 and value2>90
        //每股營收超過20且外銷比率超過九成
        then ret=1;
        outputfield(1,value1,0,"每股營收");
        outputfield(2,value2,0,"外銷比率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信可能會作帳的股票(df: pd.DataFrame, r1: int = 50, day: int = 30, r2: int = 15, r3: int = 5000, r4: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 投信可能會作帳的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\投信可能會作帳的股票.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        settotalbar(50);
        value1=GetField("投信買張","D");
        value2=GetField("最新股本");//單位:億
        condition1=false;
        condition2=false;
        condition3=false;
        if value2<r1
        then condition1=true;//股本小於50億元
        value3=countif(value1>50,day);
        if value3>=r2
        then condition2=true;//近30天裡有超過15天買超
        if summation(value1,day)>r3
        then condition3=true;//近30天合計買超超過5000張
        if condition1 and condition2 and condition3
        and close<close[day-1]*(1+r4/100)
        then ret=1;
        outputfield(1,summation(value1,day),0,"投信累計買進", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 旺季來臨前(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 旺季來臨前
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\旺季來臨前.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(40);
        value1=GetField("月營收","M");//單位:億元
        W1=(value1[12]+value1[13]+value1[14])/3;
        W2=(value1[24]+value1[25]+value1[26])/3;
        W3=(value1[36]+value1[37]+value1[38])/3;
        F1=(value1[11]+value1[10]+value1[9])/3;
        F2=(value1[23]+value1[22]+value1[21])/3;
        F3=(value1[35]+value1[34]+value1[33])/3;
        if F1>=W1*1.25 and F2>=W2*1.25 and F3>=W3*1.25
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 長期都填權的股票(df: pd.DataFrame, N: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 長期都填權的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\09.時機操作\長期都填權的股票.xs
        XS Logic Reference:
        {@type:filter}
        if getfield("除權息日期") = date then
        begin
        value1 = date;
        value2 = c[1];
        value3 = currentbar;
        end;
        if value1 > 0
          AND currentbar - value3 = N - 1
          AND c > value2
        then
        begin
        value4 = date;
        value5 = c;
        condition1 = true;
        end;
        if condition1 then ret=1;
        outputfield(1,value1,0,"除權息日期");
        outputfield(2,value2,2,"除權息前一天收盤");
        outputfield(4,value4,0,"N天後日期");
        outputfield(5,value5,2,"N天後收盤");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
