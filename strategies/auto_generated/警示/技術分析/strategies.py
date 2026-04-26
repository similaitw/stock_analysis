# Auto-generated strategies for: 警示/技術分析
import pandas as pd
import numpy as np

class 技術分析Strategies:

    @staticmethod
    def strategy_45度切線突破(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 45度切線突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\45度切線突破.xs
        XS Logic Reference:
        {@type:sensor}
        value1=rateofchange(close,period);
        //計算區間漲跌幅
        value2=arctangent(value1/period*100);
        //計算上漲的角度
        if value2 crosses over 45
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ADX形成上昇趨勢(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: ADX形成上昇趨勢
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\ADX形成上昇趨勢.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Length,6) * 13 + 8);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        value1=GetField("主力買賣超張數")[Z];
        if tselsindex(10,8)[Z]=1
        and value1>300
        and adx_value Crosses Above Threshold
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ADX趨勢成形(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: ADX趨勢成形
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\ADX趨勢成形.xs
        XS Logic Reference:
        {@type:sensor}
        // ADX趨勢成形
        //
        settotalbar(maxlist(Length,6) * 13 + 8);
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        Ret = adx_value Crosses Above Threshold;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ATR通道突破策略(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: ATR通道突破策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\ATR通道突破策略.xs
        XS Logic Reference:
        {@type:sensor}
        value1=average(truerange,period);
        value2=average(close,period)+2*value1;
        if close crosses over value2 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CCI超買(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: CCI超買
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\CCI超買.xs
        XS Logic Reference:
        {@type:sensor}
        // CCI超買
        //
        SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);
        cciValue = CommodityChannel(Length);
        cciMAValue = Average(cciValue, AvgLength);
        Ret = cciMAValue Crosses Above OverBought;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CCI超賣(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: CCI超賣
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\CCI超賣.xs
        XS Logic Reference:
        {@type:sensor}
        // CCI超賣
        //
        SetTotalBar(maxlist(AvgLength + Length + 1,6) + 11);
        cciValue = CommodityChannel(Length);
        cciMAValue = Average(cciValue, AvgLength);
        Ret = cciMAValue Crosses Below OverSold;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DIF_MACD由正轉負(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: DIF-MACD由正轉負
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\DIF-MACD由正轉負.xs
        XS Logic Reference:
        {@type:sensor}
        // DIF-MACD翻負
        //
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        Ret = oscValue Crosses Below 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DIF_MACD由負轉正(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: DIF-MACD由負轉正
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\DIF-MACD由負轉正.xs
        XS Logic Reference:
        {@type:sensor}
        // DIF-MACD翻正
        //
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        Ret = oscValue Crosses Above 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DIF_MACD轉正買進訊號(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: DIF-MACD轉正買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\DIF-MACD轉正買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        {L.J.R. Sep.2014}
        // DIF-MACD翻正
        //
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        value1=GetField("主力買賣超張數")[Z];
        if oscValue Crosses Above 0
        and trueall(value1>300,3)
        and tselsindex(10,8)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MACD死亡交叉(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: MACD死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MACD死亡交叉.xs
        XS Logic Reference:
        {@type:sensor}
        // MACD 死亡交叉 (dif向下穿越macd)
        //
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        Ret = difValue Crosses Below macdValue;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MACD黃金交叉(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: MACD黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MACD黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        // MACD 黃金交叉 (dif向上穿越macd)
        //
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        Ret = difValue Crosses Above macdValue;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MFO資金流震盪指標(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: MFO資金流震盪指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MFO資金流震盪指標.xs
        XS Logic Reference:
        {@type:sensor}
        if range <> 0 and range[1] <> 0 then
        	value1= ((high-low[1])-(high[1]-low))/((high-low[1])+(high[1]-low))*volume;
        if summation(volume,period) <> 0 then
        	value2= summation(value1,period)/summation(volume,period);
        if value2 crosses over -0.5 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM往上穿過0(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM往上穿過0
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MTM往上穿過0.xs
        XS Logic Reference:
        {@type:sensor}
        // MTM往上穿越0軸
        //
        settotalbar(maxlist(Length,6) + 8);
        Ret = Momentum(Close, Length) Crosses Above 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM突破零且投信買超(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: MTM突破零且投信買超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MTM突破零且投信買超.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        if momentum(close,10) crosses over 0
        and GetField("投信買賣超")[Z]>1000 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM背離(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: MTM背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MTM背離.xs
        XS Logic Reference:
        {@type:sensor}
        value1=momentum(close,10);
        if linearregslope(close,6)<0
        and linearregslope(value1,6)>0
        and close*1.2<close[20]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM跌破0(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM跌破0
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\MTM跌破0.xs
        XS Logic Reference:
        {@type:sensor}
        // MTM往下跌破0軸
        //
        settotalbar(maxlist(Length,6) + 8);
        Ret = Momentum(Close, Length) Crosses Below 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Pivot_Point短多策略(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: Pivot Point短多策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\Pivot Point短多策略.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        pivot=(high+low+close)/3;
        value1=2*pivot-low;
        if close=value1
        and tselsindex(10,6)[Z]=1
        and volume>=1000
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI低檔背離(df: pd.DataFrame, RSILength: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: RSI低檔背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\RSI低檔背離.xs
        XS Logic Reference:
        {@type:sensor}
        // RSI由下往上, 與價格趨勢背離
        //
        settotalbar(maxlist(RSILength,6) * 8 + 8);
        RSIValue = RSI(Close, RSILength);
        If RSIValue Crosses Above Threshold and
           RSIValue >= Highest(RSIValue, Region) and 
           Close <= Lowest(Close, Region) then
           Ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI死亡交叉(df: pd.DataFrame, ShortLength: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: RSI死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\RSI死亡交叉.xs
        XS Logic Reference:
        {@type:sensor}
        // RSI短天期往下穿越長天期
        //
        settotalbar(maxlist(ShortLength,6) * 8 + 8);
        Ret = RSI(Close, ShortLength) Crosses Below RSI(Close, LongLength);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI背離(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: RSI背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\RSI背離.xs
        XS Logic Reference:
        {@type:sensor}
        value1=rsi(close,12);
        if linearregslope(close,6)<0
        and linearregslope(value1,6)>0
        and close*1.2<close[20]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI高檔背離(df: pd.DataFrame, RSILength: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: RSI高檔背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\RSI高檔背離.xs
        XS Logic Reference:
        {@type:sensor}
        // RSI由高檔區往下, 與價格趨勢背離
        //
        settotalbar(maxlist(RSILength,6) * 8 + 8);
        RSIValue = RSI(Close, RSILength);
        If RSIValue Crosses Below Threshold and
           RSIValue < Lowest(RSIValue, Region) and 
           Close >= Highest(Close, Region) then
        	Ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI黃金交叉(df: pd.DataFrame, ShortLength: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: RSI黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\RSI黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        // RSI短天期往上穿越長天期
        //
        settotalbar(maxlist(ShortLength,LongLength,6) * 8 + 8);
        Ret = RSI(Close, ShortLength) Crosses Above RSI(Close, LongLength);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def U型底(df: pd.DataFrame, in1: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: U型底
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\U型底.xs
        XS Logic Reference:
        {@type:sensor}
        value1=standarddev(weightedclose,10,2);//計算一定期數標準差
        value2=average(value1,250)*in2;//計算一年標準差
        value3=average(C,5);//MA5
        value4=average(C,10);//MA10
        value5=average(C,20);//MA20
        if value1 crosses over value2 //若標準差向上跨越一年平均標準差
        then begin
        	KP=0;
        	HSV=0;
        end;
        if value1>=value2//在連續變動趨勢中
        then begin
        	if value1>HSV then HSV=value1;//尋找標準差最大點
        	if HSV<>HSV[1] then KP=C;//將標準差最大的點之收盤價視為關鍵價
        end;
        condition2=value1<value2;//標準差小於年均標準差
        condition3=trueall(condition2,in1);//連續20期
        condition4=value4<value4[1];//MA10為下降趨勢
        condition5=trueall(condition4,in3);//連續下降20期
        condition7=trueall(not condition4,in3);//連續20期不下降
        if not condition5 and condition5[1] then condition6=true;//若連續下降
        if C crosses over KP and condition3 and trueall(condition6,round(in3/2,0))
        //若收盤價突破關鍵價且期間內標準差小於年均且下降趨勢結束一段時間
        then begin
        	condition6=false;
        	ret=1;//買進
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def WVAD買進訊號(df: pd.DataFrame, length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: WVAD買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\WVAD買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        //ETF 作多  40天後出場
        value1=close-open;
        value2=high-low;
        if high<>low
        then value3=value1/value2*volume
        else
        value3=value3[1];
        wvad=summation(value3,length);
        if wvad<0
        and linearregslope(wvad,5)>0
        and linearregslope(wvad,15)<0
        and linearregslope(close,20)<0
        and GetSymbolField("tse.tw","收盤價","W")
        >average(GetSymbolField("tse.tw","收盤價","W"),13)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三連陽過前年最高點(df: pd.DataFrame, period: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 三連陽過前年最高點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\三連陽過前年最高點.xs
        XS Logic Reference:
        {@type:sensor}
        //全部  持有二十天
        settotalbar(period);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("強弱指標","D")[Z];
        value2=GetField("主力買賣超張數")[Z];
        if close crosses over highest(close[1],period)
        and trueall(close>close[1],3)
        and trueall(value2>0,3)
        and tselsindex(10,6)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上昇趨勢確立(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 上昇趨勢確立
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\上昇趨勢確立.xs
        XS Logic Reference:
        {@type:sensor}
        //市值適中的股票 20天出場
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        //做收盤價20天線性回歸
        {value1:斜率,value4:預期值}
        value5=rsquare(close,value4,20);//算收盤價與線性回歸值的R平方
        value6=GetField("主力買賣超張數")[Z];
        if value1> 0 and value5 crosses over 0.2
        and trueall(value6>100,3)
        and tselsindex(10,8)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下跌後的吊人線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 下跌後的吊人線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\下跌後的吊人線.xs
        XS Logic Reference:
        {@type:sensor}
        condition1=false;
        condition2=false;
        condition3=false;
        if high<= maxlist(open, close)*1.01	
        //條件1:小紅小黑且上影線很小
        then condition1=true;
        if (close-low)> (open-close)*2 and (close-low)>close*0.02
        //條件2:下影線為實體兩倍以上
        then condition2=true;
        if highest(high,30)>close[1]*1.4
        //條件3:近30日來最高點到昨天跌幅超過40%
        then condition3=true;
        {結果判斷}		
        IF		condition1
        	and	condition2
        	and	condition3
        and average(volume,100)>1000
        //只計算有量的股票
        then ret=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下降趨勢突破(df: pd.DataFrame, in1: int = 70) -> tuple[bool, str]:
        """
        Original Strategy: 下降趨勢突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\下降趨勢突破.xs
        XS Logic Reference:
        {@type:sensor}
        //尋找不同區間大小下目測所認為的高點。
        value1=highest(H,in1);//找出一定區間的高點
        if value1>value1[1] then value2=value1;
        //如果高點變高則保留高點，這樣做的原因是可以找到一波下降之後的高點
        condition1 = value2=value2[1];
        //條件:保留之高點維持(階梯的平台)
        condition2 = trueall(condition1,in1);
        //在計算區間內高點都沒有變 
        if condition2 and not condition2[1]
        then begin
        	value6=value5;
        	value5=value4;
        	value4=value3;
        	value3=value2;
        end;
        condition3 = 
        	value3-value2<value4-value3 
        	and value4-value3<value5-value4 
        	and (value5-value4<value6-value5 or not in2)//嚴格模式多判斷一階
        	and value3-value2>0
        	;//平台的高度一階比一階低
        if condition3[1] and not condition3 then ret=1;
        	//此秩序被打破時進場
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 中小型股趨勢成型(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 中小型股趨勢成型
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\中小型股趨勢成型.xs
        XS Logic Reference:
        {@type:sensor}
        // ADX趨勢成形
        // 用有量的中小型股，5%停利，5%停損
        if GetSymbolField("tse.tw","收盤價")
        > average(GetSymbolField("tse.tw","收盤價"),10) 
        //大盤OK
        then begin
        DirectionMovement(Length, pdi_value, ndi_value, adx_value);
        if adx_value Crosses Above Threshold
        //adx趨勢成形
        and pdi_value>ndi_value
        //+DI>-DI
        and close <close[30]
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力押大注(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力押大注
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\主力押大注.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("主力買賣超張數")[Z];
        if value1=highest(value1,120)
        and trueall(value1>0,3)
        and volume>500
        and close>close[1]*1.03
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力收集完開始拉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力收集完開始拉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\主力收集完開始拉.xs
        XS Logic Reference:
        {@type:sensor}
        //中小型股，持股20天
        //漲幅3%以上
        //爆大量，且一般而言會是月均量1倍以上
        //主力近1日買超要相對過去的買超有成長。
        //買進家數小於賣出家數
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("分公司買進家數","D")[Z];
        value2=GetField("分公司賣出家數","D")[Z];
        value3=GetField("主力買賣超張數")[Z];
        if close>close[1]*1.03
        and value3>average(value3,20)
        and value1<value2
        and volume >2*average(volume,20)
        and tselsindex(10,8)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力累計買超比例過門檻(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上", limit1: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 主力累計買超比例過門檻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\主力累計買超比例過門檻.xs
        XS Logic Reference:
        {@type:sensor}
        //作多  中小型股  持有二十天
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        b1 = summation(GetField("主力買賣超張數")[Z], Length);
        v1 = summation(Volume, Length);
        ratio=b1/v1*100;
        value1=GetField("主力買賣超張數")[Z];
        if v1<>0
        then 
        begin
        if ratio>=limit1 and average(volume,20)>1000
        and trueall(value1>100,3)
        and tselsindex(10,6)[Z]=1
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 乖離反轉作多買進訊號(df: pd.DataFrame, Length: int = 20, Ratio: int = 21, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 乖離反轉作多買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\乖離反轉作多買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        //用週線  四週後出場
        settotalbar((Length+10)*5);
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        if close <= average(getfield("close","W"),Length) * (1-Ratio/100) then KPrice = getfield("high","W");
        value1=GetField("投信買賣超")[Z];
        value2=value1*close*1000;
        if countif(value2>1000000,3)>2
        and close>KPrice and getfield("close","W")[1] < xf_getvalue("W",KPrice,1)
        then ret=1 ;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價值股創近年新高(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 價值股創近年新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\價值股創近年新高.xs
        XS Logic Reference:
        {@type:sensor}
        if close crosses over  highest(close[1],220)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 共振策略(df: pd.DataFrame, shortlength: int = 5, midlength: int = 20, Longlength: int = 60, Percent: int = 5, XLen: int = 6, Length1: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 共振策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\共振策略.xs
        XS Logic Reference:
        {@type:sensor}
        sv = average(close,shortlength);
        mv = average(close,midlength);
        lv = average(close,Longlength);	
        AvgH = maxlist(sv,mv,lv );
        AvgL = minlist(sv,mv,lv );
        if AvgL > 0 then AvgHLp = 100*AvgH/AvgL -100;
        value1 = PercentR(Length1);
        if trueAll(AvgHLp < Percent,XLen)
        and value1>80
        and close>close[1]*1.025
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 布林通道超買訊號(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 布林通道超買訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\布林通道超買訊號.xs
        XS Logic Reference:
        {@type:sensor}
        // 布林通道超買訊號
        //
        settotalbar(Length + 3);
        Ret = High >= bollingerband(Close, Length, UpperBand);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 布林通道超賣訊號(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 布林通道超賣訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\布林通道超賣訊號.xs
        XS Logic Reference:
        {@type:sensor}
        // 布林通道超賣訊號
        //
        settotalbar(Length + 3);
        Ret = Low <= bollingerband(Close, Length, -1 * LowerBand);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量突破均線(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 帶量突破均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\帶量突破均線.xs
        XS Logic Reference:
        {@type:sensor}
        // 帶量突破均線
        //
        settotalbar(3);
        setbarback(Length);
        if close > Average(close, Length) and  close[1] <  Average(close, Length) and
           volume > Average(volume, Length) * VolFactor 
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量跌破均線(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 帶量跌破均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\帶量跌破均線.xs
        XS Logic Reference:
        {@type:sensor}
        // 帶量跌破均線
        //
        settotalbar(3);
        setbarback(Length);
        if close < Average(close, Length) and  close[1] >  Average(close, Length) and
           volume > Average(volume, Length) * VolFactor 
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 底部出大量(df: pd.DataFrame, period: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 底部出大量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\底部出大量.xs
        XS Logic Reference:
        {@type:sensor}
        if close=lowest(close,period)
        and volume=highest(volume,period)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 找起漲點的策略(df: pd.DataFrame, Length: int = 20, UpperBand: int = 2, lowerband: str = "-2") -> tuple[bool, str]:
        """
        Original Strategy: 找起漲點的策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\找起漲點的策略.xs
        XS Logic Reference:
        {@type:sensor}
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1= bollingerband(Close, Length, UpperBand);
        value2= bollingerband(Close, Length, lowerBand);
        value3=value1-value2;
        value4=average(close,20);
        if linearregslope(value4,5)>0
        and value3>average(value3,20)*1.3
        and close[1] crosses over value1
        and close>value1
        and tselsindex(10,6)[Z] = 1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信天天買__股價天天小漲(df: pd.DataFrame, day: int = 8) -> tuple[bool, str]:
        """
        Original Strategy: 投信天天買  股價天天小漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\投信天天買  股價天天小漲.xs
        XS Logic Reference:
        {@type:sensor}
        //中小型股  持有二十天
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("投信買賣超")[Z];
        value2=GetField("主力買賣超張數")[Z];
        if countif(value1>0,day)>=7
        //八天裡至少七天投信買超
        and countif(close>close[1],day)>=5
        //八天裡至少五天上漲
        and average(volume,10)<2000
        and trueall(value2>0,3)
        and tselsindex(10,8)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信近幾日買超比例高的(df: pd.DataFrame, pastDays: int = 5, _BuyRatio: int = 10, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信近幾日買超比例高的
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\投信近幾日買超比例高的.xs
        XS Logic Reference:
        {@type:sensor}
        if BarFreq <> "D" then return;
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("主力買賣超張數")[Z];
        SumForce = Summation(GetField("投信買賣超")[Z], pastDays);
        sumTotalVolume = Summation(Volume, pastDays);
        if SumForce > SumTotalVolume * _BuyRatio/100 
        and tselsindex(10,8)[Z]=1
        then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 景氣循環股操作法(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20, Percent: int = 2, Volpercent: int = 40) -> tuple[bool, str]:
        """
        Original Strategy: 景氣循環股操作法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\景氣循環股操作法.xs
        XS Logic Reference:
        {@type:sensor}
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
        if maxlist(value1,value2,value3)*100 < Percent*Close then Kprice=H;
        end;
        end;
        if C crosses above Kprice
        //and tselsindex(10,8)=1
         then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波動放大(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 波動放大
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\波動放大.xs
        XS Logic Reference:
        {@type:sensor}
        // 波動放大
        //
        settotalbar(3);
        setbarback(Length);
        Ret = Highest(High, Length) / Lowest(Low, Length) -1 > Percent*0.01;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 波動縮小(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 波動縮小
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\波動縮小.xs
        XS Logic Reference:
        {@type:sensor}
        // 波動縮小
        //
        settotalbar(3);
        setbarback(Length);
        Ret = Highest(High, Length) / Lowest(Low, Length) -1 < Percent*0.01;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲幅警示(df: pd.DataFrame, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 漲幅警示
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\漲幅警示.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        Ret = Rateofchange(Close, Length) > Percent;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 潛龍昇天(df: pd.DataFrame, StartDate: int = 20150301, LowMonth: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 潛龍昇天
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\潛龍昇天.xs
        XS Logic Reference:
        {@type:sensor}
        if currentbar =1 and date < startdate then raiseruntimeerror("日期不夠遠");
        if iLow = Low then //觸低次觸與最後一次觸低日期
        begin
        hitlow+=1;
        hitlowdate =date;
        end;
        if DateAdd(hitlowdate,"M",1) < Date and//如果自觸低點那天三個月後都沒有再觸低
        iHigh/iLow < 1.3 and //波動在三成以內
        iHigh = High then
        //來到設定日期以來最高點
        ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤整後跳空走高(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 盤整後跳空走高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\盤整後跳空走高.xs
        XS Logic Reference:
        {@type:sensor}
        //中小型股  停損停利都是5%
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1=highest(high[1],period);
        value2=lowest(low[1],period);
        if value1<value2*1.05
        and open > high[1]*1.025
        and tselsindex(10,7)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 短期均線突破長期均線(df: pd.DataFrame, Shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 短期均線突破長期均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\短期均線突破長期均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(Shortlength,Longlength,6));
        If Average(Close,Shortlength) crosses over Average(Close,Longlength) then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 短期均線跌破長期均線(df: pd.DataFrame, Shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 短期均線跌破長期均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\短期均線跌破長期均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(Shortlength,Longlength,6));
        If Average(Close,Shortlength) crosses under Average(Close,Longlength) then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破投信成本線(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 突破投信成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\突破投信成本線.xs
        XS Logic Reference:
        {@type:sensor}
        //小型股
        if V[1] <> 0 then
        	APrice = GetField("成交金額")[1] / V[1]/1000;
        SumAm = Summation(GetField("投信買賣超")[1]*APrice, pastDays);
        SumForce = Summation(GetField("投信買賣超")[1], pastDays);
        sumTotalVolume = Summation(Volume[1], pastDays);
        if SumAm > 30000 and SumForce > SumTotalVolume * _BuyRatio/100 then
        begin
        Kprice =highest(avgprice,pastDays);
        QDate=Date;
        end;
        if DateDiff(Date,QDate) < pastDays+5 and C > Kprice and C[1] < Kprice then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 第一次站上20週均線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 第一次站上20週均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\第一次站上20週均線.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq<>"W" then return;
        if close crosses over average(close,20)
        and barslast(close crosses over average(close,20))[1]
        >20
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越突破三均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越突破三均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越突破三均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,midlength,Longlength));
        shortaverage=Average(close,shortlength);
        midaverage=Average(close,midlength) ;
        Longaverage = Average(close,Longlength); 
        if close > maxlist(shortaverage, midaverage, longaverage) and
             open < minlist(shortaverage, midaverage, longaverage)
             then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越突破單均線(df: pd.DataFrame, length: int = 5, Price: str = "Close") -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越突破單均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越突破單均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(length);
        avgValue = Average(Price,length);
        if close > avgValue and  open < avgValue  then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越突破雙均線(df: pd.DataFrame, shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越突破雙均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越突破雙均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,Longlength));
        Longaverage = Average(close,Longlength);
        shortaverage=Average(close,shortlength) ;
        if close > maxlist(shortaverage, longaverage) and
             open < minlist(shortaverage, longaverage)
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越跌破三均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越跌破三均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越跌破三均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,midlength,Longlength));
        shortaverage=Average(close,shortlength);
        midaverage=Average(close,midlength) ;
        Longaverage = Average(close,Longlength); 
        if open > maxlist(shortaverage, midaverage, longaverage) and
           close < minlist(shortaverage, midaverage, longaverage)
        then ret=1;        
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越跌破單均線(df: pd.DataFrame, length: int = 5, Price: str = "Close") -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越跌破單均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越跌破單均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(length);
        avgValue = Average(Price,length);
        if close < avgValue and  open > avgValue  then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價穿越跌破雙均線(df: pd.DataFrame, shortlength: int = 5, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價穿越跌破雙均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價穿越跌破雙均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,Longlength));
        Longaverage = Average(close,Longlength);
        shortaverage=Average(close,shortlength) ;
        if open > maxlist(shortaverage, longaverage) and
           close < minlist(shortaverage, longaverage)
         then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價轉趨活躍(df: pd.DataFrame, day: int = 66, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 股價轉趨活躍
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\股價轉趨活躍.xs
        XS Logic Reference:
        {@type:sensor}
        //小型股
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        value1=GetField("總成交次數");
        value2=average(value1,day);
        value3=GetField("強弱指標")[Z];
        value4=average(value3,day);
        value5=GetField("外盤均量")[Z];
        value6=average(value5,day);
        value7=GetField("主動買力")[Z];
        value8=average(value7,day);
        value9=GetField("開盤委買");
        value10=average(value9,day);
        count=0;
        if value1>=value2*(1+ratio/100)
        then count=count+1;
        if value3>=value4*(1+ratio/100)
        then count=count+1;
        if value5>=value6*(1+ratio/100)
        then count=count+1;
        if value7>=value8*(1+ratio/100)
        then count=count+1;
        if value9=value10*(1+ratio/100)
        then count=count+1;
        value11=average(count,5);
        value12=average(count,20);
        if value11 crosses over value12
        and value12<2.2
        and highest(close,20)<lowest(close,20)*1.1
        and tselsindex(10,8)[Z]=1
        and GetField("主力買賣超張數")[Z]>100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌幅警示(df: pd.DataFrame, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 跌幅警示
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\跌幅警示.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(length);
        Ret = RateOfChange(Close, Length) < -1 * Percent;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 進入上昇趨勢(df: pd.DataFrame, period: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 進入上昇趨勢
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\進入上昇趨勢.xs
        XS Logic Reference:
        {@type:sensor}
        //高ROE股持有20天
        value1=countif(low<lowest(low[1],period),period);
        value2=countif(high>highest(high[1],period),period);
        value3=value2-value1;
        if average(GetSymbolField("tse.tw","收盤價","D"),5)
        > average(GetSymbolField("tse.tw","收盤價","D"),20)
        then begin
        if value3 crosses over 4
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過去N日有多日跳空且未拉回(df: pd.DataFrame, day: int = 5, lowlimit: int = 2, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 過去N日有多日跳空且未拉回
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\過去N日有多日跳空且未拉回.xs
        XS Logic Reference:
        {@type:sensor}
        //中小型股  停損停利都是5%
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        value1=highest(high[day],period);
        value2=lowest(low[day],period);
        if value1<value2*1.05
        and countif(high>high[1]
        and low>low[1],day)>=lowlimit
        and tselsindex(10,8)[Z]=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 野百合的春天(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 野百合的春天
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\野百合的春天.xs
        XS Logic Reference:
        {@type:sensor}
        //獲利穩定的公司  20天後出場
        settotalbar(700);
        if getsymbolfield("tse.tw","收盤價")
        > average(getsymbolfield("tse.tw","收盤價"),10)
        then begin
        value4=GetField("總市值");
        value5=average(value4,600);
        if value4[1]<value5[1]*0.7
        and close=highest(close,10)
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開始有人問津(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開始有人問津
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\技術分析\開始有人問津.xs
        XS Logic Reference:
        {@type:sensor}
        if average(truerange/close,20)*100<3
        and truerange crosses over average(truerange,20)*1.2
        and average(volume,30)<600
        and close>close[1]*1.025
        and close<30
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
