# Auto-generated strategies for: 警示/A股用語
import pandas as pd
import numpy as np

class A股用語Strategies:

    @staticmethod
    def 九陰白骨爪(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 九陰白骨爪
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\九陰白骨爪.xs
        XS Logic Reference:
        {@type:sensor}
        // 連續9筆K線收黑
        //
        settotalbar(10);
        Ret = TrueAll(close < open, 9);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 九陽神功(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 九陽神功
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\九陽神功.xs
        XS Logic Reference:
        {@type:sensor}
        // 連續9筆上漲
        settotalbar(10);
        Ret = TrueAll(Close > Close[1], 9);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 出水芙蓉(df: pd.DataFrame, Length: int = 66, downLength: int = 100, ratio: int = 25, VLength: int = 20, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 出水芙蓉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\出水芙蓉.xs
        XS Logic Reference:
        {@type:sensor}
        {股價長期低於季線 今日帶量突破季線 [僅適用日線] }
        settotalbar(downLength + 8);
        setbarback(maxlist(Length + vLength));
        if barfreq <> "D" then return;
        value1=average(close,Length);//季線值
        value2=average(volume,VLength);//均量值
        condition1 = TrueAll(high[1] < value1[1], downLength);
        if condition1 and close crosses over value1 and volume > value2* (100+ratio)/100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 回頭高飛(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 回頭高飛
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\回頭高飛.xs
        XS Logic Reference:
        {@type:sensor}
        //開高5%以上，拉回又再拉漲停
        settotalbar(3);
        condition1  =  (Close  =  GetField("漲停價", "D"));
        condition2  =  (GetField("Open", "D") > GetField("RefPrice", "D") *1.05);
        condition3  =  (GetField("Low", "D") < GetField("Open", "D"));
        condition4  =   close > close[1];
        if condition1 and condition2 and condition3 and condition4 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 斷頭鍘刀(df: pd.DataFrame, ShortLength: int = 5, MidLength: int = 20, LongLength: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 斷頭鍘刀
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\斷頭鍘刀.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(ShortLength,MidLength,LongLength));
        value1=average(close,ShortLength);
        value2=average(close,MidLength);
        value3=average(close,LongLength);
        if close crosses below value1 and 
           close crosses below value2 and 
           close crosses below value3 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 死蜘蛛(df: pd.DataFrame, ShortLength: int = 5, MidLength: int = 20, LongLength: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 死蜘蛛
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\死蜘蛛.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(ShortLength,MidLength,LongLength));
        value1=average(close,ShortLength);
        value2=average(close,MidLength);
        value3=average(close,LongLength);
        condition1  = value1>close;
        condition2  = close[1]>value3;
        value4=maxlist(value1,value2,value3);
        value5=minlist(value1,value2,value3);
        value6=(value4-value5)/value4;
        condition3 =  value6<0.02;
        if condition1 and condition2 and condition3 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 殺跌波型(df: pd.DataFrame, TXT: str = "請使用1分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 殺跌波型
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\殺跌波型.xs
        XS Logic Reference:
        {@type:sensor}
        //黑三兵
        settotalbar(5);
        if    ( open - close ) > (high -low) * 0.75 and 
              ( open[1] - close[1] ) > (high[1] -low[1]) * 0.75 and
              ( open[2] - close[2] ) > (high[2] -low[2]) * 0.75 and
              close < close[1] and close[1] < close[2] 
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 池塘底(df: pd.DataFrame, Length: int = 40, inter: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 池塘底
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\池塘底.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbarback(maxlist(Length,inter));
        value1=absvalue(close-close[inter]);
        value2=value1/close;
        value3=average(value2,length);//本日收盤價與前第inter日之收盤價之差的移動平均
        value4=average(volume,20);
        condition1 = value3<0.01;
        condition2 =  close crosses above highest(high[1],length) ;
        condition3 =  volume/value4>1.2;
        if condition1 and condition2 and condition3 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 瀑布波型(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 瀑布波型
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\瀑布波型.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(30);
        if close[1] > lowest(close,30) * 1.2 and 
           (high-low)> close * 0.035 and 
           (close-low)> close * 0.01 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 火箭攻擊(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 火箭攻擊
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\火箭攻擊.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        IF CLOSE >=  CLOSE[1] * 1.015 and close=high and volume>volume[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 螞蟻功(df: pd.DataFrame, Length: int = 10, Length1: int = 5, Ratio: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 螞蟻功
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\A股用語\螞蟻功.xs
        XS Logic Reference:
        {@type:sensor}
        //延著均線前進
        settotalbar(maxlist(Length,Length1) + 3);
        value1=average(close,Length);
        for x=Length-1 downto 0
        begin
        	if value1[x] >= close[x]  and value1[x]*100 <=  (100+ratio) *Close
        	then count += 1;
        end;
        if count >= Length1 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
