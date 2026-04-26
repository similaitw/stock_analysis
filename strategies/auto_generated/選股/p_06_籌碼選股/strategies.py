# Auto-generated strategies for: 選股/06.籌碼選股
import pandas as pd
import numpy as np

class Cat06籌碼選股Strategies:

    @staticmethod
    def N日以來投信曾大買過(df: pd.DataFrame, period: int = 250, days: int = 5, amount: int = 3000) -> tuple[bool, str]:
        """
        Original Strategy: N日以來投信曾大買過
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\N日以來投信曾大買過.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(period+days);
        value1=GetField("投信買張");
        value2=summation(value1,days);
        if countif(value2>=amount,period)>=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N日內三大法人曾同步買超(df: pd.DataFrame, days: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: N日內三大法人曾同步買超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\N日內三大法人曾同步買超.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(days+1);
        value1=GetField("外資買賣超","D");
        value2=GetField("投信買賣超","D");
        value3=GetField("自營商自行買賣買賣超","D");
        condition1=value1>0 and value2>0 and value3>0;
        if barslast(condition1)<days
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 不明買盤介入(df: pd.DataFrame, period: int = 5, ratio: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 不明買盤介入
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\不明買盤介入.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period + 7);
        value1=GetField("法人買張","D");
        value2=GetField("資券互抵張數","D");
        value3=GetField("散戶買張","D");
        value4=volume - value1 - value2 - value3;
        value5=value4*100/volume;	// 不明買盤的比重
        value6=average(value5,period);
        if value6 crosses over ratio
        then ret=1;
        SetOutputName1("不明買盤比重(%)");
        OutputField1(value5);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力偷偷調節後下殺(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 主力偷偷調節後下殺
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力偷偷調節後下殺.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        Value1=GetField("分公司買進家數","D");
        value2=GetField("分公司賣出家數","D");
        value3=(value1-value2);
        //買進家數減去賣出家數，代表籌碼發散的情況
        value4=average(close,5);
        //計算發散程度的五日移動平均
        if period<>0 then begin
        	if countif(value3>10, period)/period >0.6
        	//區間裡超過六成以上的日子主力都是站在出貨那一邊
        	and linearregslope(value4,5)>0
        	//發散程度之五日移動平均線短期趨勢是向上
        	then ret=1;
        end;
        outputfield(1, countif(value3>10, period), 0, "出貨天數", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力公司派可能出貨中(df: pd.DataFrame, Period: int = 5, Rate1: int = 1000, Rate2: int = 5000, Ratio: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 主力公司派可能出貨中
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力公司派可能出貨中.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        if Close < Close[Period] and  {近期股價累計為下跌}
           Close < Lowest(Low,Period)* (1+Ratio/100) and {接近期間低點}
           Average(Volume,Period) > Rate2    {偏弱期間均量大於成交量下限}
        then 
          begin  
        	value1= GetField("法人持股","D") - GetField("法人持股","D")[Period]; {期間法人累計買賣超}
        	value2= GetField("融資餘額張數","D") - GetField("融資餘額張數","D")[Period] ; {期間融資累計增減}
        	value3= GetField("融券餘額張數","D") - GetField("融券餘額張數","D")[Period];{期間融券累計增減}
        	if value1 + value2 -value3 >  Rate1 * -1 then ret=1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力慢慢收集籌碼後攻堅(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 主力慢慢收集籌碼後攻堅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力慢慢收集籌碼後攻堅.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        Value1=GetField("分公司買進家數","D");
        value2=GetField("分公司賣出家數","D");
        value3=(value2-value1);
        //賣出的家數比買進家數多的部份
        value4=average(close,5);
        if period<>0 then begin
           if countif(value3>30, period)/period >0.7
           then ret=1;
        end;
        outputfield(1, countif(value3>30, period), 0, "進貨天數", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力發動股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力發動股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力發動股.xs
        XS Logic Reference:
        {@type:filter}
        //成交量 連續 3 日遞減
        //股價 > 20日均線 10%
        if volume<volume[1] 
        and volume[1]<volume[2]
        and close>average(close,20)*1.1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力買超超過門檻(df: pd.DataFrame, Length: int = 5, limit1: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 主力買超超過門檻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力買超超過門檻.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        r1 = summation(GetField("主力買賣超張數"), Length);
        volTotal = summation(Volume, Length);
        if voltotal<>0 then 
          begin
        	ratio = r1 / voltotal * 100;
            if ratio >= limit1 and average(volume,20) > 500 then ret=1;
        	setoutputname1("主力買賣超比重(%)");
        	outputfield1(ratio);
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力長期收集(df: pd.DataFrame, period: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 主力長期收集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主力長期收集.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(period);
        value1=GetField("分公司買進家數","D");
        value2=GetField("分公司賣出家數","D");
        condition1=false;
        if countif(value1<value2,period)>period/2
        then condition1=true;
        if condition1
        and close>open*1.035
        and GetField("主力買賣超張數","D")>0
        and summation(GetField("主力買賣超張數","D"),5)>0
        and summation(GetField("主力買賣超張數","D"),20)>0
        and summation(GetField("主力買賣超張數","D"),60)>0
        and summation(GetField("主力買賣超張數","D"),120)>0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主流股蓄勢待發(df: pd.DataFrame, days: int = 10, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 主流股蓄勢待發
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\主流股蓄勢待發.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(100);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        if absvalue((average(close,20)-close)/close)*100<2
        and absvalue((average(close,60)-close)/close)*100<2
        and close=highest(close,days)
        and macdvalue>macdvalue[1]
        and macdvalue>0
        and difvalue>0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 交易家數暴增(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 交易家數暴增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\交易家數暴增.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("分公司交易家數","D");
        value2=highest(GetField("分公司交易家數","D")[1],20);
        if value1-value2>150
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 借券增(df: pd.DataFrame, lowlimit: int = 200, days: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 借券增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\借券增.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(3);
        value1=GetField("借券賣出餘額張數","D")-GetField("借券賣出餘額張數","D")[days];//借券賣出餘額張數增加數
        if value1>=lowlimit
        then ret=1;
        outputfield(1,value1,"借券賣出餘額張數增加數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 借券賣出餘額張數大減(df: pd.DataFrame, amount: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 借券賣出餘額張數大減
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\借券賣出餘額張數大減.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1 = GetField("借券賣出餘額張數");
        if value1[1] - value1 > amount
        then ret=1;
        setoutputname1("借券賣出減少張數");
        outputfield1(value1[1] - value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 再跌就有斷頭賣壓的股票(df: pd.DataFrame, period: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 再跌就有斷頭賣壓的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\再跌就有斷頭賣壓的股票.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value2=nthhighestbar(1,close,period);//波段高點在第幾根Bar
        if GetField("融資餘額張數","D")>average(volume,5)
        //融資餘額大於五日均量
        and GetField("融資餘額張數","D")[value2]>10000
        //融資餘額大於一萬張
        and GetField("融資餘額張數","D")[value2]>10000
        //最高點時融資餘額也大於一萬張
        and close*1.2<=close[value2]//波段跌幅超過兩成
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 券增價漲(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5) -> tuple[bool, str]:
        """
        Original Strategy: 券增價漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\券增價漲.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio and
        	Getfield("融券餘額張數") > 0 and
        	Getfield("融券餘額張數") = highest(Getfield("融券餘額張數"), Length)  
        then ret=1;
        SetOutputName1("融券餘額張數");
        OutputField1(Getfield("融券餘額張數"));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 券補力道超過一定值(df: pd.DataFrame, lowlimit: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 券補力道超過一定值
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\券補力道超過一定值.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("融券餘額張數","D");
        if value1/average(volume,5)*100>lowlimit
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 千張大戶增加而散戶減少(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 千張大戶增加而散戶減少
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\千張大戶增加而散戶減少.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("W");
        settotalbar(3);
        condition1 = GetField("大戶持股人數","W",param:=1000)>GetField("大戶持股人數","W",param:=1000)[1];
        condition2 = GetField("散戶持股人數","W",param:=400)<GetField("散戶持股人數","W",param:=400)[1];
        if condition1 and condition2 then ret=1;
        outputfield(1,GetField("大戶持股人數","W",param:=1000),0,"本週大戶人數");
        outputfield(2,GetField("大戶持股人數","W",param:=1000)[1],0,"上週大戶人數");
        outputfield(3,GetField("大戶持股人數","W",param:=1000)-GetField("大戶持股人數","W",param:=1000)[1],0,"大戶增加數");
        outputfield(4,GetField("散戶持股人數","W",param:=400),0,"本週散戶人數");
        outputfield(5,GetField("散戶持股人數","W",param:=400)[1],0,"上週散戶人數");
        outputfield(6,GetField("散戶持股人數","W",param:=400)-GetField("散戶持股人數","W",param:=400)[1],0,"散戶減少數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 千張大戶增持(df: pd.DataFrame, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 千張大戶增持
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\千張大戶增持.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("W");
        settotalbar(3);
        if GetField("大戶持股比例","W",param:=1000) > (GetField("大戶持股比例","W",param:=1000)[1] * (1 + ratio/100)) then ret=1;
        outputfield(1, GetField("大戶持股比例","W",param:=1000), 2, "大戶比例");
        outputfield(2, GetField("大戶持股比例","W",param:=1000)[1], 2, "大戶比例[1]");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 千張大戶減少而散戶增加(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 千張大戶減少而散戶增加
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\千張大戶減少而散戶增加.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("W");
        settotalbar(3);
        condition1 = GetField("大戶持股人數","W",param:=1000)<GetField("大戶持股人數","W",param:=1000)[1];
        condition2 = GetField("散戶持股人數","W",param:=400)>GetField("散戶持股人數","W",param:=400)[1];
        if condition1 and condition2 then ret=1;
        outputfield(1,GetField("大戶持股人數","W",param:=1000),0,"本週大戶人數");
        outputfield(2,GetField("大戶持股人數","W",param:=1000)[1],0,"上週大戶人數");
        outputfield(3,GetField("大戶持股人數","W",param:=1000)-GetField("大戶持股人數","W",param:=1000)[1],0,"大戶減少數");
        outputfield(4,GetField("散戶持股人數","W",param:=400),0,"本週散戶人數");
        outputfield(5,GetField("散戶持股人數","W",param:=400)[1],0,"上週散戶人數");
        outputfield(6,GetField("散戶持股人數","W",param:=400)-GetField("散戶持股人數","W",param:=400)[1],0,"散戶增加數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 增資股即將出籠(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 增資股即將出籠
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\增資股即將出籠.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("現增新股上市日");
        value2=GetField("現增比率");//每千股可認股數
        value3=GetField("現增價格");
        value4=GetField("融券餘額張數","D");
        value5=GetField("普通股股本","Q");//單位:億
        if value1>date and datediff(value1,date)<10//增資股快上市了
        and value5*10000*value2/1000>2000//增資張數大於5000張
        and value4[30]>value4-1000//近一個月融券增加沒有超過1000張
        and value3*1.1<close//股價仍比現增價格高超過一成
        then ret=1;
        outputfield(1,value1,0,"新股上市日", order := -1);
        outputfield(2,value2,2,"現增比率");
        outputfield(3,close-value3,2,"現增價差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資完全不碰的股票有人在收籌碼(df: pd.DataFrame, period: int = 5, investorLimit: int = 2000, ratio: int = 50, volLimit: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 外資完全不碰的股票有人在收籌碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\外資完全不碰的股票有人在收籌碼.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        // 主力買張比重
        value1 = summation(GetField("主力買張","D"), period);
        value2 = summation(volume, period);
        value3 = value1 / value2 * 100;
        if GetField("外資持股","D") < investorLimit and value3 > ratio and value2 > volLimit * period  
        then ret=1;
        SetOutputName1("主力買張比重(%)");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資拉抬(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5, VolumeRatio: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 外資拉抬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\外資拉抬.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio then
        begin
        	SumTotalVolume = Summation(volume, Length);
        	SumForce = Summation(GetField("外資買賣超"), Length);
        	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
        end;
        SetOutputName1("外資累計買超張數");
        OutputField1(SumForce);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資由空翻多(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資由空翻多
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\外資由空翻多.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(3);
        if summation(GetField("外資買賣超","D"),20)<0
        and trueall(GetField("外資買賣超","D")>200,3)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資買超後隔天會漲的機率很高的股票(df: pd.DataFrame, n: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 外資買超後隔天會漲的機率很高的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\外資買超後隔天會漲的機率很高的股票.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(n);
        value1=GetField("外資買賣超","D");
        if value1[1]>200 
        then begin
        x1=1;
        c1=c1+1;
        //外資買超的次數
        end
        else x1=0;
        if close>open
        then begin
        y=1;
        c2=c2+1;
        //上漲的次數
        end
        else y=0;
        if value1[1]>200
        and close>open
        then c3=c3+1;
        //上漲且外資買超的次數
        value2=c1/n; //外資買超的機率
        value3=c2/n; //上漲的機率
        value4=c3/c2;//收紅且外資買超的機率
        value5=value4*value3/value2;
        if countif(value1[1]>200,n)>20
        then ret=1;
        outputfield(1,value5*100,0,"外資前一日買超隔天收高的機率");
        outputfield(2,c1,0,"上漲次數");
        outputfield(3,c2,"外資買超次數");
        outputfield(4,c3,0,"上漲且外資買超");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後法人散戶清浮額(df: pd.DataFrame, period: int = 10, percent1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後法人散戶清浮額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\大跌後法人散戶清浮額.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("法人買賣超張數");
        value2=GetField("融資增減張數");
        if close[period-1] >= close*(1+percent1/100) and 
           value1 < 0 and 
           value2 < 0 and 
           close > close[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 官股買超比重(df: pd.DataFrame, lowlimit: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 官股買超比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\官股買超比重.xs
        XS Logic Reference:
        {@type:filter}
        value1 = getfield("官股券商買賣超張數", "D");
        if value1 > 0 then begin
        	value2 = value1 * 100 / volume;
        	if value2 >= lowlimit then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信從空手到開始佈局(df: pd.DataFrame, r1: int = 500, r2: int = 5000, length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 投信從空手到開始佈局
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信從空手到開始佈局.xs
        XS Logic Reference:
        {@type:filter}
        setTotalBar(3);
        if trueall(GetField("投信買賣超","D")[1] < r1, length) and 
           GetField("投信買賣超","D") * close > r2 * 10
        then ret=1;
        SetOutputName1("投信買賣超(張)");
        OutputField1(GetField("投信買賣超","D"));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信拉抬(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5, VolumeRatio: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 投信拉抬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信拉抬.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio then
        begin
        	SumTotalVolume = Summation(volume, Length);
        	SumForce = Summation(GetField("投信買賣超"), Length);
        	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
        end;
        SetOutputName1("投信累計買超張數");
        OutputField1(SumForce);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信持股從無到有(df: pd.DataFrame, v1: int = 2000, v2: int = 300) -> tuple[bool, str]:
        """
        Original Strategy: 投信持股從無到有
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信持股從無到有.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("投信持股","D");
        value2=GetField("投信買賣超","D");
        if value1 < v1 and value2 > v2
        then ret=1;
        SetOutputName1("投信買賣超(張)");
        OutputField1(value2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信掃貨(df: pd.DataFrame, pastDays: int = 5, _BuyRatio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 投信掃貨
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信掃貨.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        SumForce = Summation(GetField("投信買賣超"), pastDays);
        sumTotalVolume = Summation(Volume, pastDays);
        value1 = SumForce / SumTotalVolume * 100;
        if value1 > _BuyRatio then ret =1;
        SetOutputName1("買超佔比例(%)");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信爭買的小型成長股(df: pd.DataFrame, miniratio: int = 10, lv: int = 5000, holdratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 投信爭買的小型成長股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信爭買的小型成長股.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1=GetField("投信買張");			//投信買張
        value2=GetField("投信持股");			//投信持股
        value3=GetField("投信持股比例");		//投信持股比例 
        if  
           value1 > volume * miniratio*0.01 and //買進張數/成交量 >= minratio
           value2 < lv and 						//原來庫存低
           value3 < holdratio and 				//原來庫存低
           GetField("公司類別","M") = "小型股" 	//小型股
        then ret=1;
        SetOutputName1("投信買張");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信第一天大買進(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信第一天大買進
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\投信第一天大買進.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("最新股本");//單位:億
        value2=GetField("投信買張","D");
        value3=value2*close/10;  //單位:萬}
        condition1=value3>200 and value1<80;
        condition2=filter(condition1,5);
        if condition2 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買進比例上揚(df: pd.DataFrame, r1: int = 50, r2: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 散戶買進比例上揚
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\散戶買進比例上揚.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(28);
        value1=GetField("散戶買張");
        value2=value1/volume*100;		// 散戶買張比例
        value3=average(value2,5);		// 短期散戶比例
        value4=average(value2,20);		// 長期散戶比例
        if value2 > r1 and
           value3 crosses above value4 and
           average(volume,5) > r2
        then ret=1;
        SetOutputName1("散戶買進比例(%)");
        OutputField1(value2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 斷頭後的止跌(df: pd.DataFrame, Length: int = 4, DVOL: int = 3000, R1: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 斷頭後的止跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\斷頭後的止跌.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        if Close > Close[1] and 
           RateOfChange(Close, Length) < -1 * R1 and
           GetField("融資餘額張數")[Length] - GetField("融資餘額張數") > DVOL 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人主力敢買又敢拉的股票(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法人主力敢買又敢拉的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人主力敢買又敢拉的股票.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("法人買賣超張數");
        value2=GetField("主力買賣超張數");
        value3=value1+value2;
        value4=GetField("內外盤比","D");//外盤量/內盤量*100
        condition1=false;
        condition2=false;
        condition3=false;
        if countif(value3>300,5)>=4 or countif(value3>300,4)>=3
        then condition1=true; 
        if value3>volume*0.3 and value4>50
        then condition2=true;
        if high<=close*1.02
        then condition3=true;
        if condition1 and condition2 and condition3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人大出籌碼(df: pd.DataFrame, r1: int = 45) -> tuple[bool, str]:
        """
        Original Strategy: 法人大出籌碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人大出籌碼.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("外資賣張","D");
        value2=GetField("投信賣張","D");
        value3=GetField("自營商賣張","D");
        if volume<>0 then 
        value4=(value1+value2+value3)/volume;
        if value4*100>r1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人大買而股價尚未發動(df: pd.DataFrame, day: int = 10, amount: int = 100, percent1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 法人大買而股價尚未發動
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人大買而股價尚未發動.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        if trueall(GetField("法人買賣超張數") > amount, day) and 
           RateOfChange(Close, day) < percent1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人淨買超比例高(df: pd.DataFrame, ratio: int = 30, period: int = 3, volLimit: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 法人淨買超比例高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人淨買超比例高.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1 = Summation(Volume - GetField("資券互抵張數"), period);
        value2 = Summation(GetField("法人買賣超張數"), period);
        value3 = value2 / value1 * 100;
        if value3 > ratio and volume > volLimit then
        ret = 1;
        SetOutputName1("近日法人淨買超比例(%)");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買超(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5, VolumeRatio: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 法人買超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人買超.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio then
        begin
        	SumTotalVolume = Summation(volume, Length);
        	SumForce = Summation(GetField("法人買賣超張數"), Length);
        	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
        end;
        SetOutputName1("三大法人累計買超張數");
        OutputField1(SumForce);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買超減融資佔成交量比重增加(df: pd.DataFrame, r1: int = 15, volLimit: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 法人買超減融資佔成交量比重增加
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人買超減融資佔成交量比重增加.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1 = (GetField("法人買賣超張數") - GetField("融資買進張數")) / Volume * 100;
        if value1 > r1 and volume > volLimit then
        ret = 1;
        setoutputname1("法人籌碼收集比例(%)");
        outputfield1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買進佔成交量超過25_(df: pd.DataFrame, r1: int = 45) -> tuple[bool, str]:
        """
        Original Strategy: 法人買進佔成交量超過25%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人買進佔成交量超過25%.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("外資買張","D");
        value2=GetField("投信買張","D");
        value3=GetField("自營商買張","D");
        if volume<>0 then 
        value4=(value1+value2+value3)/volume;
        if value4*100>r1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人逢低買超破億元(df: pd.DataFrame, day: int = 5, lowlimit: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 法人逢低買超破億元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人逢低買超破億元.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(day);
        value1=GetField("法人買賣超張數","D");
        value2=summation(value1,day);
        value3=value1*value2/10000;
        if value3>=1 
        and close*1.1<close[30]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人連續買進達一定標準(df: pd.DataFrame, day: int = 5, ratio1: int = 40, times: int = 2, volLimit: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 法人連續買進達一定標準
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\法人連續買進達一定標準.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(day + 3);
        value1 = (GetField("外資買張") + GetField("投信買張"))/Volume * 100;
        value2 = countif(value1 > ratio1, day);
        if value2 >= times and average(volume, day) > volLimit then
        ret = 1;
        SetOutputName1("近日法人買進比例(%)");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流通在外股數不多(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 流通在外股數不多
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\流通在外股數不多.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("最新股本");//單位:億
        value2=GetField("董監持股佔股本比例","D");
        value3=GetField("法人持股比例","D");
        if value1*(1-value2/100-value3/100)<50
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 籌碼安定比率(df: pd.DataFrame, r1: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 籌碼安定比率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\籌碼安定比率.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1=GetField("投信持股比例","D");
        value2=GetField("外資持股比例","D");
        value3=GetField("董監持股佔股本比例","D");
        value4=value1+value2+value3;
        if value4 > r1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 籌碼從散戶手裡被收集(df: pd.DataFrame, ratio: int = 200, volLimit: int = 2000) -> tuple[bool, str]:
        """
        Original Strategy: 籌碼從散戶手裡被收集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\籌碼從散戶手裡被收集.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("控盤者買張");
        value2=GetField("散戶買張");
        value3=value1/value2 * 100;
        if volume > volLimit and value3 > ratio and value3[1] > ratio
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 籌碼被發散(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 籌碼被發散
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\籌碼被發散.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value1=GetField("分公司賣出家數");
        value2=GetField("分公司買進家數");
        if linearregslope(value1,period)<0
        //賣出的家數愈來愈少
        and linearregslope(value2,period)>0
        //買進的家數愈來愈多 
        and value2>300
        and close>close[period]*1.05
        //但這段期間股價在漲
        and close>close[1]*1.025
        //今天又漲超過2.5%
        then ret=1;
        outputfield(1,value2,0,"買進家數", order := 1);
        outputfield(2,value1,0,"賣出家數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 籌碼集中度超過兩成的股票(df: pd.DataFrame, day: int = 10, ratio: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 籌碼集中度超過兩成的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\籌碼集中度超過兩成的股票.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(day+3);
        value1=GetField("主力買賣超張數","D");
        if volume<>0 then 
        	value2=summation(value1,day)/summation(volume,day)*100;
        if value2>=ratio then 
        	ret=1;
        outputfield(1,value2,0,"籌碼集中度");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價突破外資成本線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價突破外資成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\股價突破外資成本線.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("D");
        settotalbar(period+7);
        if GetField("Volume") > 0 then 
        	Value5 = GetField("外資買張")*GetField("成交金額")*100000/GetField("Volume")
        else
        	Value5 = 0;
        Value1 = summation(Value5, period);
        Value2 = summation(GetField("外資買張"), period);
        if Value2 > 0 then avg_b = Value1 / Value2;
        if close cross over avg_b then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價突破投信成本線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價突破投信成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\股價突破投信成本線.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period + 5);
        if GetField("Volume") > 0 then 
        	Value5 = GetField("投信買張")*GetField("成交金額(元)")/(GetField("Volume")*1000)	 
        else 
        	Value5 = 0;
        Value1 = summation(Value5, period);
        Value2 = summation(GetField("投信買張"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
        if close cross over avg_b then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商拉抬(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5, VolumeRatio: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 自營商拉抬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\自營商拉抬.xs
        XS Logic Reference:
        {@type:filter}
        // 
        //
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio then
        begin
        	SumTotalVolume = Summation(volume, Length);
        	SumForce = Summation(GetField("自營商買賣超"), Length);
        	if SumForce > SumTotalVolume * VolumeRatio / 100 then ret =1;
        end;
        SetOutputName1("自營商累計買超張數");
        OutputField1(SumForce);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資大減後轉強(df: pd.DataFrame, period: int = 80, v1: int = 3000) -> tuple[bool, str]:
        """
        Original Strategy: 融資大減後轉強
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\融資大減後轉強.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1 = highestbar(close,period);
        value2 = GetField("融資餘額張數")[value1] - GetField("融資餘額張數");
        if  value2 > v1 and 
        	trueall(close > close[1],3)
        then ret=1;
        SetOutputName1("融資減少張數");
        OutputField1(value2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資追捧(df: pd.DataFrame, Length: int = 10, UpRatio: float = 3.5) -> tuple[bool, str]:
        """
        Original Strategy: 融資追捧
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\融資追捧.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if RateOfChange(Close, 1) >= UpRatio and
        	Getfield("融資餘額張數") > 0 and
        	Getfield("融資餘額張數") = highest(Getfield("融資餘額張數"), Length)  
        then ret=1;
        SetOutputName1("融資餘額張數");
        OutputField1(Getfield("融資餘額張數"));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近N日主力合計買超大於M張(df: pd.DataFrame, days: int = 5, lowmit: int = 200) -> tuple[bool, str]:
        """
        Original Strategy: 近N日主力合計買超大於M張
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\近N日主力合計買超大於M張.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("主力買賣超張數","D");
        if summation(value1,days)>=lowmit
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續兩日籌碼在收集(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 連續兩日籌碼在收集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\連續兩日籌碼在收集.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("分公司買進家數","D");
        value2=GetField("分公司賣出家數","D");
        value3=value2-value1;
        if trueall(value3>30,2)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續大戶進散戶出(df: pd.DataFrame, periods: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 連續大戶進散戶出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\連續大戶進散戶出.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("W");
        settotalbar(periods+2);
        condition1 = trueall(getfield("大戶持股比例", "W", param:=1000) > getfield("大戶持股比例", "W", param:=1000)[1], periods);
        condition2 = trueall(getfield("散戶持股比例", "W", param:=400) < getfield("散戶持股比例", "W", param:=400)[1], periods);
        ret= condition1 and condition2;
        outputfield(1, getfield("大戶持股比例", "W", param:=1000), 2, "大戶比例");
        outputfield(2, getfield("散戶持股比例", "W", param:=400), 2, "散戶比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 集保張數減少中(df: pd.DataFrame, n: int = 3, Amount: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 集保張數減少中
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\06.籌碼選股\集保張數減少中.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        // 單位=萬張
        Value1 = (GetField("集保張數","W")[n] - GetField("集保張數","W")) * 10000;
        if Value1 > Amount then
        ret = 1;
        setoutputname1("減少張數(張)");
        OutputField1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
