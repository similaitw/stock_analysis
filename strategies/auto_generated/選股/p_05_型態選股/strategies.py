# Auto-generated strategies for: 選股/05.型態選股
import pandas as pd
import numpy as np

class Cat05型態選股Strategies:

    @staticmethod
    def 三次到頂而破(df: pd.DataFrame, BoxRangePercents: int = 7, HighAreaPercents: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 三次到頂而破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\三次到頂而破.xs
        XS Logic Reference:
        {@type:filter}
        period = 10;
        while period < Maxperiod and
        	highest(high[1],period) < lowest(low[1],period) *(1+BoxRangePercents/100)
        begin period +=1; end;
        if period < MaxPeriod then
        begin
        	BoxHigh = highest(High[1],period); {區間高點}
        	if Close > BoxHigh   and  {突破整理區間高點}
        	   NthHighest(3,High[1],period) > BoxHigh*(1-HighAreaPercents/100)
        	   {昨天以前第3個高點也在高檔區間,即曾經攻高3次}
        	   then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上昇旗形(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 上昇旗形
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\上昇旗形.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        value2=nthhighest(1,high[1],period);//最高價
        value3=nthhighest(2,high[1],period);//第二高價
        value4=nthhighest(3,high[1],period);//第三高價
        value5=nthhighestbar(1,high[1],period);//最高價距今幾根bar
        value6=nthhighestbar(2,high[1],period);//第二高價距今幾根bar
        value7=nthhighestbar(3,high[1],period);//第三高價距今幾根bar
        condition1=false;
        condition2=false;
        if value6-value5>3 and value7-value6>3
        then condition1=true;//三個高點沒有連在一起，且是愈來愈高
        if maxlist(value2,value3,value4)<minlist(value2,value3,value4)*1.07
        then condition2=true;//三個高點沒有差多少
        if condition1 and condition2  
        and close crosses over value2
        and close[period]*1.05<value2
        then ret=1;
        outputfield(1, value2, 2, "前波高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下跌後的吊人線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 下跌後的吊人線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\下跌後的吊人線.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1=false;
        condition2=false;
        condition3=false;
        if high<= maxlist(open, close)*1.01	
        //狀況1:小紅小黑且上影線很小
        then condition1=true;
        if (close-low)> absvalue(open-close)*2 and (close-low)>close*0.02
        //狀況2:下影線為實體兩倍以上
        then condition2=true;
        if highest(high,30)>close[1]*1.4
        //狀況3:近30日來最高點到昨天跌幅超過40%
        then condition3=true;
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        outputfield(1,high,2,"K棒高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下降趨勢改變(df: pd.DataFrame, Length: int = 20, VolLimit: int = 1000) -> tuple[bool, str]:
        """
        Original Strategy: 下降趨勢改變
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\下降趨勢改變.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(maxlist(length, 5) + 3);
        If CurrentBar = 1 then
        	kk = 0
        else
        	kk = kk[1] + (close - close[1])/close[1] * Volume;
        value1 = linearregslope(kk, Length);
        value2 = linearregslope(kk, 5);
        IF value1 < 0 and value2 > 0 AND VOLUME > VolLimit then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 下降趨勢明確(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 下降趨勢明確
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\下降趨勢明確.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(20);
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        //做收盤價20天線性回歸
        {value1:斜率,value4:預期值}
        value5=rsquare(close,value4,20);
        //算收盤價與線性回歸值的R平方
        if value1<0 and value5>0.2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 做M頭的股票(df: pd.DataFrame, day: int = 60, GP: int = 30, pc: int = 2, rg: int = 30, bc: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 做M頭的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\做M頭的股票.xs
        XS Logic Reference:
        {@type:filter}
        value1=highest(high,day);//找出波段最高點
        value2=lowest(low,day);//找出波段最低點
        value3=nthhighest(2,high,day);//波段第二高點
        value4=nthhighestbar(1,high,day);//最高價在距今第幾根bar
        value5=nthlowestbar(1,low,day);//最低價在距今第幾根bar
        value6=nthhighestbar(2,high,day);//第二價在距今第幾根bar
        value7=lowest(low,maxlist(value4,value6));//從第一個M頭以來的最低點
        value8=nthlowestbar(1,low,maxlist(value4,value6));//谷底距今第幾根bar
        condition1=false;
        condition2=false;
        condition3=false;
        condition4=false;
        if value1>value2*(1+gp/100) then condition1=true;//波段漲幅超過30%
        if value5>maxlist(value4,value6)+rg then condition2=true;//低點在圖左邊
        if value1<=value3*(1+pc/100) then condition3=true;//兩個高點之間的價差不大
        if value8>minlist(value4,value6) and value8<minlist(value4,value6)
        then condition4=true;//谷底在兩頭之間
        if condition1 and condition2 and condition3 and condition4  
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 在上昇趨勢中的股票(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 在上昇趨勢中的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\在上昇趨勢中的股票.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(20);
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        //做收盤價20天線性回歸
        {value1:斜率,value4:預期值}
        value5=rsquare(close,value4,20);
        //算收盤價與線性回歸值的R平方
        if value1>0 and value5>0.2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平台整理後突破(df: pd.DataFrame, Period: int = 20, ratio: int = 10, ratio1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 平台整理後突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\平台整理後突破.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        h1=nthhighest(1,high[1],period);
        h2=nthhighest(4,high[1],period);
        l1=nthlowest(1,low[1],period);
        l2=nthlowest(4,low[1],period);
        if (h1-l1)/l1<=ratio/100
          and (h1-h2)/h2<=ratio1/100
          and (l2-l1)/l1<=ratio1/100
          and close crosses over h1
          and close[period+30]*1.1<h1
          and volume> average(volume,period)
        then ret=1;
        outputfield(1, h1, 2, "區間高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平台整理後跌破(df: pd.DataFrame, Period: int = 15, ratio: int = 7, ratio1: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 平台整理後跌破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\平台整理後跌破.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        h1=nthhighest(1,high[1],period);
        h2=nthhighest(4,high[1],period);
        l1=nthlowest(1,low[1],period);
        l2=nthlowest(4,low[1],period);
        if (h1-l1)/l1<=ratio/100
        and (h1-h2)/h2<=ratio1/100
        and (l2-l1)/l1<=ratio1/100
        and close crosses below l1
        and close[period+30]>l1*1.1
        then ret=1;
        outputfield(1, l1, 2, "區間低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破下降旗型(df: pd.DataFrame, Length: int = 100, UpRatio: int = 2, VolLimit: int = 300) -> tuple[bool, str]:
        """
        Original Strategy: 突破下降旗型
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\突破下降旗型.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(Length + 3);
        if high = highest(high,Length) then hDate = date;
        day = datediff(date,hdate);
        if day =0 and day[1] > 0 then KeyPrice = Close;
        if day >0 and day[1] = 0 then HighPrice = High;
        if KeyPrice > 0 and HighPrice > 0 and day > 2 and day <= Length / 2 and 
        	Close > Open * (1 + 0.01 * UpRatio) and 
        	Close >= highest(High,3) and
        	volume > VolLimit and 
        	Close > KeyPrice and 
        	Close < HighPrice  
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破整理格局(df: pd.DataFrame, limit1: int = 7, limit2: int = 2, rangemax: int = 30, vollimit: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 突破整理格局
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\突破整理格局.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(rangemax + 3);
        period = 5;
        repeat
         begin
        	value1=simplehighest(high[1],period);
        	value2=simplelowest(low[1],period);
        	period=period+1;
         end;	
        until period >= rangemax or (value1 > value2 * (1 + limit1/100));
        if period < rangemax
        then
          begin
        	value3=nthhighest(1, high[1], period);
        	value4=nthhighest(3, high[1], period);
        	if value3 <= value4 * (1 + limit2/100) and 
        	   close crosses over value3 and
        	   volume > vollimit
        	then ret=1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破箱型(df: pd.DataFrame, period: int = 20, rangeratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 突破箱型
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\突破箱型.xs
        XS Logic Reference:
        {@type:filter}
        h1=nthhighest(1,high,period);
        h2=nthhighest(2,high,period);
        l1=nthlowest(1,low,period);
        l2=nthlowest(2,low,period);
        hd1=nthhighestbar(1,high,period);
        hd2=nthhighestbar(2,high,period);
        ld1=nthlowestbar(1,low,period);
        ld2=nthlowestbar(2,low,period);
        if absvalue(hd1[1]-hd2[1])>=4 and absvalue(ld1[1]-ld2[1])>=4
        and h1[1]-h2[1]<=h1[1]*0.02
        and l2[1]-l1[1]<=l1[1]*0.02
        and h1[1]<=l1[1]*(1+rangeratio/100)
        then begin
        if close crosses over h1[1]
        and volume >=average(volume,period)*1.3
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破繼續型態(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 突破繼續型態
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\突破繼續型態.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        //觸低次觸與最後一次觸低日期
        if iLow = Low then begin
        	hitlow+=1;
        	hitlowdate =date;
        end;
        if DateAdd(hitlowdate,"M",2) < Date and//如果自觸低點那天1個月後都沒有再觸低
        iHigh/iLow < 1.3 and //波動在三成以內
        iHigh = High
        //來到設定日期以來最高點
        then ret =1;
        outputfield(1, highest(high[1],100), 2, "前波高點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破股票箱(df: pd.DataFrame, length: int = 12, boxrange: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 突破股票箱
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\突破股票箱.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);	
        value1=NthHighest(1,high,length);
        value3=nthhighest(3,high,length);
        value4=Nthlowest(1,low,length);
        value5=nthlowest(3,low,length);
        if 
          value1[1] <= 1.03 * value3[1] and 
          value5[1] <= 1.03 * value4[1] and 
          value1[1] <= (1 + 0.01 * boxrange) * value4[1] and 
          close > value1[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌勢後的內困三日翻紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 跌勢後的內困三日翻紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\跌勢後的內困三日翻紅.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        If close[4]=lowest(close,20)
        and close[4]*1.2<=close[24]
        and open[3]>close[3]*0.01
        And close[2]>open[2]*0.01
        And close[1]>open[1]*0.01
        And close>high[4]
        and volume>average(volume,5)
        and average(volume,100)>=1000
        Then
        ret=1;
        outputfield(1,close[4],2,"前波低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近期漲幅不大(df: pd.DataFrame, period: int = 20, ratio: int = 7) -> tuple[bool, str]:
        """
        Original Strategy: 近期漲幅不大
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\近期漲幅不大.xs
        XS Logic Reference:
        {@type:filter}
        if close[period-1]<>0
        and (close/close[period-1]-1)*100<ratio
        then ret=1;
        outputfield(1,GetField("法說會日期"),0,"法說會日期", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 長時間未破底後創新高(df: pd.DataFrame, period: int = 90, percent: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 長時間未破底後創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\長時間未破底後創新高.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("AD");
        condition1=false;
        condition2=false;
        value1=lowest(low,period);
        if value1=low[period-1]
        then condition1=true;
        if highest(high[1],period)<=value1*(1+percent/100)
        then condition2=true;
        if condition1 and condition2 and close crosses over highest(close[1],period)
        then ret=1;
        outputfield(1,value1,2,"前波低點", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 長紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 長紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\05.型態選股\長紅.xs
        XS Logic Reference:
        {@type:filter}
        if close>=open*1.035
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
