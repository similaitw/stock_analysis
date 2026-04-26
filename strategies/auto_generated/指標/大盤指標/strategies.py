# Auto-generated strategies for: 指標/大盤指標
import pandas as pd
import numpy as np

class 大盤指標Strategies:

    @staticmethod
    def ALF亞歷山大過濾指標(df: pd.DataFrame, length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: ALF亞歷山大過濾指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\ALF亞歷山大過濾指標.xs
        XS Logic Reference:
        {@type:indicator}
        Value1 = close / close[length-1];
        plot1(Value1, "亞歷山大過濾指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def BBand寬度指標(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: BBand寬度指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\BBand寬度指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/bband-width/
        }
        	Length(20, "MA的天數"), 
        	UpperBand(2, "上通道標準差倍數"), 
        	LowerBand(2, "下通道標準差倍數");
        up = bollingerband(Close, Length, UpperBand);
        down = bollingerband(Close, Length, -1 * LowerBand);
        mid = (up + down) / 2;
        bbandwidth = 100 * (up - down) / mid;
        Plot1(bbandwidth , "BBand width(%)");
        plot2(4,"低檔");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ETF成交量統計指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: ETF成交量統計指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\ETF成交量統計指標.xs
        XS Logic Reference:
        {@type:indicator}
        array:ETF[50](0);
        etf[1]=GetSymbolField("0050.tw","成交金額");
        etf[2]=GetSymbolField("0051.tw","成交金額");
        etf[3]=GetSymbolField("0052.tw","成交金額");
        etf[4]=GetSymbolField("0053.tw","成交金額");
        etf[5]=GetSymbolField("0054.tw","成交金額");
        etf[6]=GetSymbolField("0055.tw","成交金額");
        etf[7]=GetSymbolField("0056.tw","成交金額");
        etf[8]=GetSymbolField("0057.tw","成交金額");
        etf[9]=GetSymbolField("0058.tw","成交金額");
        etf[10]=GetSymbolField("0059.tw","成交金額");
        etf[11]=GetSymbolField("0061.tw","成交金額");
        etf[12]=GetSymbolField("006201.tw","成交金額");
        etf[13]=GetSymbolField("006203.tw","成交金額");
        etf[14]=GetSymbolField("006204.tw","成交金額");
        etf[15]=GetSymbolField("006205.tw","成交金額");
        etf[16]=GetSymbolField("006206.tw","成交金額");
        etf[17]=GetSymbolField("006207.tw","成交金額");
        etf[18]=GetSymbolField("006208.tw","成交金額");
        etf[19]=GetSymbolField("00631L.tw","成交金額");
        etf[20]=GetSymbolField("00632R.tw","成交金額");
        etf[21]=GetSymbolField("00633L.tw","成交金額");
        etf[22]=GetSymbolField("00634R.tw","成交金額");
        etf[23]=GetSymbolField("00635U.tw","成交金額");
        etf[24]=GetSymbolField("00636.tw","成交金額");
        etf[25]=GetSymbolField("00637L.tw","成交金額");
        etf[26]=GetSymbolField("00638R.tw","成交金額");
        etf[27]=GetSymbolField("00639.tw","成交金額");
        etf[28]=GetSymbolField("00640L.tw","成交金額");
        etf[29]=GetSymbolField("00641R.tw","成交金額");
        etf[30]=GetSymbolField("00642U.tw","成交金額");
        etf[31]=GetSymbolField("00643.tw","成交金額");
        etf[32]=GetSymbolField("00645.tw","成交金額");
        etf[33]=GetSymbolField("00646.tw","成交金額");
        etf[34]=GetSymbolField("00647L.tw","成交金額");
        etf[35]=GetSymbolField("00648R.tw","成交金額");
        etf[36]=GetSymbolField("00649.tw","成交金額");
        etf[37]=GetSymbolField("00650L.tw","成交金額");
        etf[38]=GetSymbolField("00651R.tw","成交金額");
        etf[39]=GetSymbolField("00652.tw","成交金額");
        etf[40]=GetSymbolField("00653L.tw","成交金額");
        etf[41]=GetSymbolField("00654R.tw","成交金額");
        etf[42]=GetSymbolField("00655L.tw","成交金額");
        etf[43]=GetSymbolField("00656R.tw","成交金額");
        etf[44]=GetSymbolField("00657.tw","成交金額");
        etf[45]=GetSymbolField("00658L.tw","成交金額");
        etf[46]=GetSymbolField("00659R.tw","成交金額");
        etf[47]=GetSymbolField("00660.tw","成交金額");
        etf[48]=GetSymbolField("00661.tw","成交金額");
        etf[49]=GetSymbolField("00662.tw","成交金額");
        etf[50]=GetSymbolField("008201.tw","成交金額");
        value1=array_sum(etf,1,50);
        if volume<>0 then 
        	value3=value1/volume*100;
        plot1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KST確認指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: KST確認指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\KST確認指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=average(rateofchange(close,12),10);
        value2=average(rateofchange(close,20),10);
        value3=average(rateofchange(close,30),8);
        value4=average(rateofchange(close,40),15);
        kst=value1+value2*2+value3*3+value4*4;
        plot1(kst,"KST確認指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def OTC佔大盤成交量比(df: pd.DataFrame, Period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: OTC佔大盤成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\OTC佔大盤成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/otc跟上市成交量比值是股市多空指標/
        }
        value1=GetSymbolField("tse.tw","成交量");
        value2=GetSymbolField("otc.tw","成交量");
        value3=value2/value1*100;
        value4=average(value3,Period);
        plot1(value4,"OTC/TSE(%)");
        Plot2(value2,"OTC成交量");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Q指標(df: pd.DataFrame, t1: int = 10, t2: int = 5, t3: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: Q指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\Q指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=close-close[1];			//價格變化
        value2=summation(value1,t1);	//累積價格變化
        value3=average(value2,t2);
        value4=absvalue(value2-value3);	//雜訊
        value5=average(value4,t3);		//把雜訊移動平均
        if value5 = 0 then 
        	Qindicator = 0
        else
        	Qindicator = value3 / value5*5;
        plot1(Qindicator,"Q-indicator");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲下跌家數差RSI指標(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 上漲下跌家數差RSI指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲下跌家數差RSI指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/上漲下跌家數差RSI指標/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 256頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        value1=getfield("上漲家數");
        value2=getfield("下跌家數");
        value3=value1-value2;
        value4=summation(value3,period);
        value5=rsi(value4,period);
        plot1(value5,"上漲家數RSI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲下跌量差(df: pd.DataFrame, period1: int = 3, period2: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 上漲下跌量差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲下跌量差.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/進場點一目了然的大盤儀表板/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 244頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("上漲量");
        	value2=getfield("下跌量");
        end else begin
        	value1=GetField("上漲量","D");
        	value2=getfield("下跌量","D");
        end;
        value3=average(value1,period1);
        value4=average(value2,period1);
        value5=value3-value4;//上漲量與下跌量比例
        value6=average(value5,period2);
        plot1(value6,"上漲下跌量差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲佔比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上漲佔比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲佔比.xs
        XS Logic Reference:
        {@type:indicator}
        value1=GetField("上漲家數");
        value2=GetField("下跌家數");
        value3=value1+value2;
        if value3 = 0 then value4 = 0 else value4=value1/value3*100;
        plot1(value4,"上漲佔比");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲家數(df: pd.DataFrame, shortterm: int = 5, midterm: int = 15) -> tuple[bool, str]:
        """
        Original Strategy: 上漲家數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲家數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/大盤多空轉換點之探討系列一-上漲的股票有沒有200/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 252頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        value1=GetField("上漲家數");
        value2=lowest(value1,shortterm);
        value3=average(value2,midterm);
        plot1(value3,"平均上漲家數");
        plot2(200,"多");
        plot3(100,"空");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲家數佔比指標(df: pd.DataFrame, period1: int = 5, period2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 上漲家數佔比指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲家數佔比指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=GetField("上漲家數");
        value2=GetField("下跌家數");
        value3=value1+value2;
        if value3 = 0 then 
        	value4 = 0 
        else
        	value4=value1/value3*100;
        value5=average(value4,period1);
        value6=average(value4,period2);
        plot1(value5,"上漲佔比短期平均");
        plot2(value6,"上漲佔比長期平均");
        plot3(value5-value6,"長短天期差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上漲量比重(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上漲量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\上漲量比重.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/盤上成交是否真的是重要指標/
        }
        if barfreq = "Tick" or barfreq = "Min" then 
        begin
        	value1=GetField("上漲量");
        end else begin
        	value1=GetField("上漲量","D");
        end;
        if volume<>0 then
        	value2=value1/volume;
        plot1(average(value2,5),"上漲量比重");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力買賣超佔市場成交量比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力買賣超佔市場成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\主力買賣超佔市場成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {市場成交量定義
        加權成交量 GetSymbolField("TSE.TW", "成交量"):
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        總計(1~15)欄位的成交金額(元)
        上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
        https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
        股票合計(1~3)欄位的成交金額(元)
        }
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");
        value1 = GetSymbolField("TSE.TW", "主力買進金額") - GetSymbolField("TSE.TW", "主力賣出金額") 
        		+ GetSymbolField("OTC.TW", "主力買進金額") - GetSymbolField("TSE.TW", "主力賣出金額");
        value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
        if value2 = 0 then value3 = 0 else value3 = value1/value2*100;
        plot1(value3,"佔比(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 估波指標_Coppock_Indicator_(df: pd.DataFrame, length1: int = 14, length2: int = 11, length3: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 估波指標(Coppock Indicator)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\估波指標(Coppock Indicator).xs
        XS Logic Reference:
        {@type:indicator}
        { 一般適用於大盤月線資料 }
        Value1=rateofchange(close,length1);   
        Value2=rateofchange(close,length2);   
        coppock=xaverage(Value1+Value2,length3);   
        plot1(coppock,"Coppock Indicator");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 作多意願指標(df: pd.DataFrame, length1: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 作多意願指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\作多意願指標.xs
        XS Logic Reference:
        {@type:indicator}
        count1=0;
        for x1=1 to length2-1 begin
        	if high < close*1.01 then 
        		count1=count1+1;
        	if open > close[1]*1.005 then
        		count1=count1+1;
        	if close > close[1] and volume>volume[1] then
        		count1=count1+1;
        	if GetField("外盤量") > GetField("內盤量") then
        		count1=count1+1;
        end;
        value2=average(count1,length1);
        value3=average(count1,length2);
        plot1(value2,"長期意願");
        plot2(value3,"短期意願");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內外盤量差(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內外盤量差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\內外盤量差.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/內外盤量比在預測大盤後市上的應用/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」242頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq = "Tick" or barfreq = "Min" then 
        begin
        	value1=GetField("內盤量");//單位:元
        	value2=GetField("外盤量");//單位:元
        end else begin
        	value1=GetField("內盤量","D");//單位:元
        	value2=GetField("外盤量","D");//單位:元
        end;
        if volume <> 0 then begin
        	value3=value2/volume*100;//外盤量比
        	value4=value1/volume*100;//內盤量比
        end else begin
        	value3=value3[1];
        	value4=value4[1];
        end;
        value5=average(value3,5);
        value6=average(value4,5);
        value7=value5-value6+5;
        plot1(value7,"內外盤量比差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內盤長短期累積量比值差(df: pd.DataFrame, length1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 內盤長短期累積量比值差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\內盤長短期累積量比值差.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min" then 
        begin
        	value1=GetField("內盤量");//單位:元
        	value2=GetField("外盤量");//單位:元
        end else begin
        	value1=GetField("內盤量","D");//單位:元
        	value2=GetField("外盤量","D");//單位:元
        end;
        value3=summation(value1,length1);
        value4=summation(value2,length1);
        value5=summation(value1,length2);
        value6=summation(value2,length2);
        value7=summation(volume,length1);
        value8=summation(volume,length2);
        ac=value4/value7*100;//外盤短期積量比值
        ds=value3/value7*100;//內盤短期積量比值
        ac1=value6/value8*100;//外盤長期積量比值
        ds1=value5/value8*100;//內盤長期積量比值
        value11=ds1-ds;
        plot1(value11,"內盤長短期積量比值差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 反脆弱指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 反脆弱指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\反脆弱指標.xs
        XS Logic Reference:
        {@type:indicator}
        array:ValueArray[21](0);
        valuearray[1]=GetSymbolField("1477.tw","總市值");
        valuearray[2]=GetSymbolField("1536.tw","總市值");
        valuearray[3]=GetSymbolField("1702.tw","總市值");
        valuearray[4]=GetSymbolField("2231.tw","總市值");
        valuearray[5]=GetSymbolField("2207.tw","總市值");
        valuearray[6]=GetSymbolField("2355.tw","總市值");
        valuearray[7]=GetSymbolField("2377.tw","總市值");
        valuearray[8]=GetSymbolField("2379.tw","總市值");
        valuearray[9]=GetSymbolField("2383.tw","總市值");
        valuearray[10]=GetSymbolField("2492.tw","總市值");
        valuearray[11]=GetSymbolField("2905.tw","總市值");
        valuearray[12]=GetSymbolField("3023.tw","總市值");
        valuearray[13]=GetSymbolField("3552.tw","總市值");
        valuearray[14]=GetSymbolField("4938.tw","總市值");
        valuearray[15]=GetSymbolField("4958.tw","總市值");
        valuearray[16]=GetSymbolField("5347.tw","總市值");
        valuearray[17]=GetSymbolField("5871.tw","總市值");
        valuearray[18]=GetSymbolField("5904.tw","總市值");
        valuearray[19]=GetSymbolField("8016.tw","總市值");
        valuearray[20]=GetSymbolField("9910.tw","總市值");
        valuearray[21]=GetSymbolField("9938.tw","總市值");
        value1=array_sum(valuearray,1,21);
        plot1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台指選倉P_C(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 台指選倉P／C
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\台指選倉P／C.xs
        XS Logic Reference:
        {@type:indicator}
        value1=getsymbolfield("txo00.tf","買賣權未平倉量比率");
        plot1(value1,"台指選倉P／C");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 噪音指標(df: pd.DataFrame, n1: int = 5, n2: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 噪音指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\噪音指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=absvalue(close-close[n1-1]);  
        value2=summation(range,n1);  
        if value1 <> 0 then  
        begin
        	value3 = value2 / value1;  
        	value4 = average(value3,n2);  
        end;
        plot1(value4,"噪音指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資買賣超佔市場成交量比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資買賣超佔市場成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\外資買賣超佔市場成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {市場成交量定義
        加權成交量 GetSymbolField("TSE.TW", "成交量"):
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        總計(1~15)欄位的成交金額(元)
        上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
        https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
        股票合計(1~3)欄位的成交金額(元)
        }
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");
        value1 = GetSymbolField("TSE.TW", "外資買賣超金額") + GetSymbolField("OTC.TW", "外資買賣超金額");
        value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
        if value2 = 0 then value3 = 0 else value3 = value1/value2*100;
        plot1(value3,"佔比(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空點數指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多空點數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\多空點數指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/多空點數指標/
        }
        Lscore=0;
        Sscore=0;
        for i = 1 to 100 begin
        	if C> H[i] then 
        		Lscore += 1 
        	else if C < L[i] then 
        		Sscore += 1;
        end;
        PLOT1(LSCORE-SSCORE,"多空點數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤儀表板(df: pd.DataFrame, _TEXT1: str = "===============", period: int = 10, _TEXT2: str = "===============", p1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 大盤儀表板
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\大盤儀表板.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/進場點一目了然的大盤儀表板/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 260頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        condition1=false;
        condition2=false;
        condition3=false;
        condition4=false;
        condition5=false;
        //==========OTC 佔大盤成交量比================
        value1=GetSymbolField("tse.tw","成交量");
        value2=GetSymbolField("otc.tw","成交量");
        value3=value2/value1*100;
        value4=average(value3,5);
        value5=low*0.98;
        if value4 crosses over 20 then
        	condition1=true;
        if condition1 then
        	plot1(value5,"OTC 進場訊號");
        //============內外盤量比差====================
        value6=GetField("內盤量");//單位:元
        value7=GetField("外盤量");//單位:元
        value8=value7/volume*100;//外盤量比
        value9=value6/volume*100;//內盤量比
        value10=average(value8,5);
        value11=average(value9,5);
        value7=value10-value11+5;
        if value7 crosses over 0 then 
        	condition2=true;
        if condition2 then 
        	plot2(value5*0.98,"內外盤量比差");
        //===========上漲下跌家數 RSI 指標==============
        value12=GetField("上漲家數");
        value13=GetField("下跌家數");
        value14=value12-value13;
        value15=summation(value14,period);
        value16=rsi(value15,period);
        if value16 crosses over 50 then
        	condition3=true;
        if condition3 then
        	plot3(value5*0.97,"上漲下跌家數 RSI");
        //===========上漲家數突破 200 檔================
        value17=lowest(value12,5);
        value18=average(value17,15);
        if value18 crosses over 200 then
        	condition4=true;
        if condition4=true then
        	plot4(value5*0.96,"上漲家數突破 200 家");
        //==========上漲下跌量指標=====================
        value19=GetField("上漲量");
        value20=GetField("下跌量");
        value21=average(value19,period);
        value22=average(value20,period);
        value23=value21-value22;
        value24=average(value23,5);
        if value24 crosses over 0 then
        	condition5=true;
        if condition5=true then
        	plot5(value5*0.95,"上漲量突破下跌量");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤六度空間切割法(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大盤六度空間切割法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\大盤六度空間切割法.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/多空六大階段指標/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 259頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        m50=average(close,50);
        m200=average(close,200);
        if close > m50 and c< m200 and m50<m200
        then value1=10
        else value1=0;
        if close > m50 and c> m200 and m50<m200
        then value2=20
        else value2=0;
        if close > m50 and c> m200 and m50 > m200
        then value3=30
        else value3=0;
        if close < m50 and c>m200 and m50>m200
        then value4=-10
        else value4=0;
        if close < m50 and c <m200
        then value5=-20
        else value5=0;
        if close < m50 and c <m200 then value6=-30
        else value6=0;
        plot1(value1,"復甦期");
        plot2(value2,"收集期");
        plot3(value3,"多頭");
        plot4(value4,"警示期");
        plot5(value5,"發散期");
        plot6(value6,"空頭");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤多空對策判斷分數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大盤多空對策判斷分數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\大盤多空對策判斷分數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/大盤多空對策訊號/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 265頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq <> "D" then raiseruntimeerror("僅支援日頻率");
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if currenttime > 180000 
        or currenttime < 083000 then 
        	Z =0 
        else 
        	Z=1;
        //每天的分數都先歸零
        if date <> date[1] then 
        	count=0;
        //外資買超
        XData = GetField("外資買賣超金額")[Z];
        if xdata > 0 then 
        	count=count+1;
        //投信買超
        YData = GetField("投信買賣超金額")[Z];
        if ydata > 0 then
        	count=count+1;
        //自營商買超
        ZData = GetField("自營商買賣超金額")[Z];
        if zdata > 0 then 
        	count=count+1;
        //上漲量超過一半
        value6 = GetField("上漲量");
        if value6/volume > 0.5 then
        	count=count+1;
        //外盤量超過一半
        value7 = GetField("外盤量");
        if value7/volume>0.5 then
        	count=count+1;
        //RSI多頭
        value8=rsi(close,5);
        value9=rsi(close,10);
        if value8 > value9 and value8 < 90 then
        	count=count+1;
        //MACD 多頭
        MACD(Close, 12, 26, 9, Dif_val, MACD_val, Osc_val);
        if osc_val > 0 then
        	count=count+1;
        //MTM  多頭
        value10=mtm(10);
        if value10 > 0 then
        	count=count+1;
        //KD多頭
        stochastic(9,3,3,rsv1,k1,d1);
        if k1 > d1 and k1 < 80 then
        	count=count+1;
        //+DI>-DI
        DirectionMovement(14,pdi_value,ndi_value,adx_value);
        if pdi_value > ndi_value then
        	count=count+1;
        //AR趨勢向上
        value14=ar(26);
        value15=linearregslope(value14,5);
        if value15 > 0 then 
        	count=count+1;
        //ACC大於零
        value16=acc(10);
        if value16 > 0 then 
        	count=count+1;
        //TRIX多頭
        value17=trix(close,9);
        value18=trix(close,15);
        if value17 > value18 then
        	count=count+1;
        //SAR多頭
        value19=SAR(0.02, 0.02, 0.2);
        if close > value19 then
        	count=count+1;
        //週線大於月線
        if average(close,5) > average(close,20) then
        	count=count+1;
        //計算平均分數
        value11=average(count,10);
        plot1(value11,"分數");
        Plot2(10,"多");
        plot3(5,"空");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤多空指標(df: pd.DataFrame, Length: int = 7, LowLimit: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 大盤多空指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\大盤多空指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/打造自己的大盤多空函數/
        }
        plot1(tselsindex(Length,LowLimit));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 委買委賣均張差額(df: pd.DataFrame, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 委買委賣均張差額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\委買委賣均張差額.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 246頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq = "Tick" or barfreq = "Min" then begin
        	value1=GetField("委買均");
        	value2=GetField("委賣均");
        end else begin
        	value1=GetField("委買均","D");
        	value2=GetField("委賣均","D");
        end;
        value3=value1-value2;
        value4=average(value3,period);
        plot1(value4,"委買賣均張差額的移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 實質買賣盤比指標(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 實質買賣盤比指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\實質買賣盤比指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("實質買盤比");
        value2=GetField("實質賣盤比");
        value3=average(value1,length)-80;
        plot1(value3,"實質買賣盤比");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 尼古斯指標(df: pd.DataFrame, length: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 尼古斯指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\尼古斯指標.xs
        XS Logic Reference:
        {@type:indicator}
        value1=GetField("上漲家數");
        value2=GetField("下跌家數");
        value3=average(value1,length);
        value4=average(value2,length);
        if value4 <> 0 then value5=value3/value4;
        plot1(value5, "尼古斯指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信買賣超佔市場成交量比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信買賣超佔市場成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\投信買賣超佔市場成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {市場成交量定義
        加權成交量 GetSymbolField("TSE.TW", "成交量"):
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        總計(1~15)欄位的成交金額(元)
        上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
        https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
        股票合計(1~3)欄位的成交金額(元)
        }
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");
        value1 = GetSymbolField("TSE.TW", "投信買賣超金額") + GetSymbolField("OTC.TW", "投信買賣超金額");
        value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
        if value2 = 0 then value3 = 0 else value3 = value1/value2*100;
        plot1(value3,"佔比(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本土天王平均(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 本土天王平均
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\本土天王平均.xs
        XS Logic Reference:
        {@type:indicator}
        array:ValueArray[12](0);
        valuearray[1]=GetSymbolField("1216.tw","收盤價");
        valuearray[2]=GetSymbolField("2201.tw","收盤價");
        valuearray[3]=GetSymbolField("2412.tw","收盤價");
        valuearray[4]=GetSymbolField("1707.tw","收盤價");
        valuearray[5]=GetSymbolField("2207.tw","收盤價");
        valuearray[6]=GetSymbolField("2905.tw","收盤價");
        valuearray[7]=GetSymbolField("2912.tw","收盤價");
        valuearray[8]=GetSymbolField("5530.tw","收盤價");
        valuearray[9]=GetSymbolField("8454.tw","收盤價");
        valuearray[10]=GetSymbolField("1507.tw","收盤價");
        valuearray[11]=GetSymbolField("9933.tw","收盤價");
        valuearray[12]=GetSymbolField("9941.tw","收盤價");
        value1=array_sum(valuearray,1,12);
        plot1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買賣超佔市場成交量比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法人買賣超佔市場成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\法人買賣超佔市場成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {市場成交量定義
        加權成交量 GetSymbolField("TSE.TW", "成交量"):
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        總計(1~15)欄位的成交金額(元)
        上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
        https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
        股票合計(1~3)欄位的成交金額(元)
        }
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");
        value1 = GetSymbolField("TSE.TW", "法人買賣超金額") + GetSymbolField("OTC.TW", "法人買賣超金額");
        value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
        if value2 = 0 then value3 = 0 else value3 = value1/value2*100;
        plot1(value3,"佔比(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買進賣出比重指標(df: pd.DataFrame, period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 法人買進賣出比重指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\法人買進賣出比重指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("法人買進比重");
        value2=GetField("法人賣出比重");
        value3=value1-value2;
        value4=average(value3,period);
        plot1(value4,"法人買賣比重差額的移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲跌停家數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 漲跌停家數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\漲跌停家數.xs
        XS Logic Reference:
        {@type:indicator}
        value1=GetField("漲停家數");
        value2=GetField("跌停家數");
        plot1(value1,"漲停家數");
        plot2(value2,"跌停家數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日沖銷張數(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 當日沖銷張數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\當日沖銷張數.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("當日沖銷張數");
        value2=average(value1,length);
        plot1(value2,"當日沖銷張數的移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 移動平均線再平均指標(df: pd.DataFrame, Period1: int = 5, Period2: int = 5, Period3: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 移動平均線再平均指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\移動平均線再平均指標.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/移動平均線再平均指標/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 257頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        value1=average(close,Period1);
        value2=average(value1,Period2);
        value3=value1-value2;
        value4=summation(value3,Period3);
        plot1(value4,"多空");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商買賣超佔市場成交量比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 自營商買賣超佔市場成交量比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\自營商買賣超佔市場成交量比.xs
        XS Logic Reference:
        {@type:indicator}
        {市場成交量定義
        加權成交量 GetSymbolField("TSE.TW", "成交量"):
        https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html
        總計(1~15)欄位的成交金額(元)
        上櫃成交量 GetSymbolField("OTC.TW", "成交量"):
        https://www.tpex.org.tw/web/stock/aftertrading/market_statistics/statistics.php?l=zh-tw
        股票合計(1~3)欄位的成交金額(元)
        }
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("只支援日線以上");
        value1 = GetSymbolField("TSE.TW", "自營商買賣超金額") + GetSymbolField("OTC.TW", "自營商買賣超金額");
        value2 = GetSymbolField("TSE.TW", "成交量") + GetSymbolField("OTC.TW", "成交量");
        if value2 = 0 then value3 = 0 else value3 = value1/value2*100;
        plot1(value3,"佔比(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 軍火商指數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 軍火商指數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\軍火商指數.xs
        XS Logic Reference:
        {@type:indicator}
        array:ValueArray[6](0);
        valuearray[1]=GetSymbolField("LMT.US","收盤價");
        valuearray[2]=GetSymbolField("BA.US","收盤價");
        valuearray[3]=GetSymbolField("RTN.US","收盤價");
        valuearray[4]=GetSymbolField("GD.US","收盤價");
        valuearray[5]=GetSymbolField("NOC.US","收盤價");
        valuearray[6]=GetSymbolField("UTX.US","收盤價");
        value1=array_sum(valuearray,1,6);
        plot1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤委買委賣差(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 開盤委買委賣差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\開盤委買委賣差.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 245頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        value1=GetField("開盤委買", "D");
        value2=GetField("開盤委賣", "D");
        value3=value1-value2;
        value4=average(value3,length);
        plot1(value4,"開盤委買賣差之移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 麥克連震盪指標(df: pd.DataFrame, length1: int = 19) -> tuple[bool, str]:
        """
        Original Strategy: 麥克連震盪指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\大盤指標\麥克連震盪指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("上漲量");
        	value2=getfield("下跌量");
        end else begin
        	value1=GetField("上漲量","D");
        	value2=getfield("下跌量","D");
        end;
        value3=value1-value2;
        value4=Xaverage(value3,length1)-Xaverage(value3,length2);
        plot1(value4,"麥克連震盪指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
