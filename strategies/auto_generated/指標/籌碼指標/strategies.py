# Auto-generated strategies for: 指標/籌碼指標
import pandas as pd
import numpy as np

class 籌碼指標Strategies:

    @staticmethod
    def 不明買盤指標(df: pd.DataFrame, period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 不明買盤指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\不明買盤指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("法人買張");
        value2=GetField("當日沖銷張數");
        value3=GetField("散戶買張");
        value4=volume-value1-value2-value3;
        if volume <> 0 then
        	value5=value4/volume;
        value6=average(value5,period);
        plot1(value6,"不明買盤比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力作多成本線(df: pd.DataFrame, period: int = 40) -> tuple[bool, str]:
        """
        Original Strategy: 主力作多成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\主力作多成本線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("主力買張");
        value2=(o+h+l+c)/4;
        value3=value1*value2;//做多金額
        if summation(value1,period)<>0 then
        	value4=summation(value3,period)/summation(value1,period);
        plot1(value4,"主力作多成本線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\主力成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	籌碼指標。
        	支援日以上頻率。支援台股商品。
        }
        plot1(GetField("主力成本"),"主力成本線");//系統估算值。計算主力持股成本。
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 主力累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\主力累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("主力買賣超張數"), Length);
        volTotal = summation(Volume, Length);
        if volTotal <> 0 then
        	_Ratio = _buyTotal * 100 / volTotal
        else
        	_Ratio = 0;
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_Ratio, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力買超佔成交量比重(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 主力買超佔成交量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\主力買超佔成交量比重.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率，僅支援日線以上");
        value4=getField("主力買賣超張數", "D");
        if volume<>0 then 
        value5=(summation(value4,length)/summation(volume,length))*100;
        _strplot1 = text("近 ",numToStr(length,0)," 期，主力買超佔成交量比重");
        plot1(value5,"主力買超佔成交量比重");
        setplotLabel(1,_strplot1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司交易家數差(df: pd.DataFrame, period1: int = 22, period2: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 分公司交易家數差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\分公司交易家數差.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。	
        if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司交易家數");
        value2=average(value1,period1);
        value3=value1-value2;
        value4=average(value3,period2);
        plot1(value3,"分公司家數差");
        plot2(value4,"家數差移動平均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司淨買賣超家數指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分公司淨買賣超家數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\分公司淨買賣超家數指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司淨買超金額家數") and GetField("成交量") = 0 then value1 = 0 else value1 = GetField("分公司淨買超金額家數");
        if getfieldDate("date") <> getfieldDate("分公司淨賣超金額家數") and GetField("成交量") = 0 then value2 = 0 else value2 = GetField("分公司淨賣超金額家數");
        value3=value2-value1;
        plot1(value3,"家數差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司買賣家數指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分公司買賣家數指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\分公司買賣家數指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司買進家數");
        if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2 = 0 else value2=GetField("分公司賣出家數");
        value3=value2-value1;
        plot1(value3,"家數差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\外資成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	籌碼指標。
        	支援日以上頻率。支援台股商品。
        }
        plot1(GetField("外資成本"),"外資成本線");//系統估算值。計算外資持股成本。
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資換手比例(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 外資換手比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\外資換手比例.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("外資買張") + GetField("外資賣張"), Length);
        volTotal = summation(Volume * 2, Length);
        Plot1(_buyTotal, "換手張數");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 外資累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\外資累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("外資買賣超"), Length);
        volTotal = summation(Volume, Length);
        if volTotal <> 0 then
        	_Ratio = _buyTotal * 100 / volTotal
        else
        	_Ratio = 0;
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_Ratio, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資買超佔成交量比重(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 外資買超佔成交量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\外資買超佔成交量比重.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率，僅支援日線以上");
        value4=getField("外資買賣超張數", "D");
        if volume<>0 then 
        value5=(summation(value4,length)/summation(volume,length))*100;
        _strplot1 = text("近 ",numToStr(length,0)," 期，外資買超佔成交量比重");
        plot1(value5,"外資買超佔成交量比重");
        setplotLabel(1,_strplot1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多空淨力場(df: pd.DataFrame, sd: int = 5, ld: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 多空淨力場
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\多空淨力場.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/自訂指標step-by-step/
        }
        H1=HIGH-HIGH[1];
        L1=LOW-LOW[1];
        C1=CLOSE-CLOSE[1];
        if truerange<>0 then begin
        	NF=(H1+L1)/truerange;
        	SNF=average(NF,sd);
        	LNF=average(NF,ld);
        	dd=SNF-LNF;
        end;
        plot1(dd,"多空淨力");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶買張比例(df: pd.DataFrame, period1: int = 5, period2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 大戶買張比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\大戶買張比例.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("主力買張");
        value2=GetField("實戶買張");
        value3=GetField("散戶買張");
        value4=GetField("控盤者買張");
        value5=GetField("法人買張");
        value6=value1+value2+value3+value4+value5;
        //合計的買張數當分母，這有可能超出成交量
        value7=value1+value4+value5;
        //主力+法人+控盤者的買張合計作為大戶的買張
        if value6<>0 then
        	value8=value7/value6*100;
        //計算大戶買張佔各方勢力買張的比例
        value9=average(value8,period1)-average(value8,period2);
        plot1(value9,"大戶買張比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 實戶累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 實戶累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\實戶累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("實戶買賣超張數"), Length);
        volTotal = summation(Volume, Length);
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\投信成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	籌碼指標。
        	支援日以上頻率。支援台股商品。
        }
        plot1(GetField("投信成本"),"投信成本線");//系統估算值。計算投信持股成本。
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 投信累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\投信累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("投信買賣超"), Length);
        volTotal = summation(Volume, Length);
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信買超佔成交量比重(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 投信買超佔成交量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\投信買超佔成交量比重.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率，僅支援日線以上");
        value4=getField("投信買賣超張數", "D");
        if volume<>0 then 
        value5=(summation(value4,length)/summation(volume,length))*100;
        _strplot1 = text("近 ",numToStr(length,0)," 期，投信買超佔成交量比重");
        plot1(value5,"投信買超佔成交量比重");
        setplotLabel(1,_strplot1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 控盤者成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 控盤者成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\控盤者成本線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("控盤者成本線");
        plot1(value1,"控盤者成本線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 放空佔成交均量倍數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 放空佔成交均量倍數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\放空佔成交均量倍數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/借券相關欄位在交易策略上的應用/
        }
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        value1=GetField("借券餘額張數","D");
        value2=GetField("融券餘額張數","D");
        if volume<>0 then 
        	value3=(value1+value2)/average(volume,20);
        plot1(value3,"放空佔成交均量倍數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶作多指標(df: pd.DataFrame, Period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 散戶作多指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\散戶作多指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("融資買進張數");
        value2=GetField("融券買進張數");
        if volume <> 0 then
        	value3=(value1+value2)/volume;
        value4=average(value3,Period);
        plot1(value4,"散戶作多指標");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買進比例(df: pd.DataFrame, Period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 散戶買進比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\散戶買進比例.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("散戶買張");
        if volume<>0 then 
        	value2=value1/volume*100;
        value3=average(value2,Period);
        plot1(value3,"散戶買進比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶賣出比例(df: pd.DataFrame, Period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 散戶賣出比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\散戶賣出比例.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("散戶賣張");
        if volume<>0 then 
        	value2=value1/volume*100;
        value3=average(value2,Period);
        plot1(value3,"散戶賣出比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 整體籌碼收集指標(df: pd.DataFrame, Period: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 整體籌碼收集指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\整體籌碼收集指標.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("現股當沖張數","D");
        value2=GetField("外資買賣超","D");
        value3=GetField("投信買賣超","D");
        value4=GetField("自營商買賣超","D");
        value5=GetField("主力買賣超張數","D");
        value6=GetField("融資增減張數","D");
        value7=GetField("融券增減張數","D");
        value8=volume-value1;//當日淨交易張數
        value9=value2+value3+value4+value5-value6+value7;
        //籌碼收集張數
        if value8<>0 then 
        	value10=value9/value8*100
        else
        	value10=value10[1];
        value11=average(value10,Period);
        plot1(value11,"集中度");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 法人累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\法人累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("法人買賣超張數"), Length);
        volTotal = summation(Volume, Length);
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買超佔成交量比重(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 法人買超佔成交量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\法人買超佔成交量比重.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率，僅支援日線以上");
        value4=getField("法人買賣超", "D");
        if volume<>0 then 
        value5=(summation(value4,length)/summation(volume,length))*100;
        _strplot1 = text("近 ",numToStr(length,0)," 期，法人買超佔成交量比重");
        plot1(value5,"法人買超佔成交量比重");
        setplotLabel(1,_strplot1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買進及賣出比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法人買進及賣出比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\法人買進及賣出比例.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("外資買張");
        value2=GetField("外資賣張");
        value3=GetField("投信買張");
        value4=GetField("投信賣張");
        value5=value1+value3;
        value6=value2+value4;
        if volume <> 0 then begin
        	value7=value5/volume*100;
        	value8=value6/volume*100;
        end;
        plot1(value7,"法人買進比例");
        plot2(value8,"法人賣出比例");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人買進比例(df: pd.DataFrame, length1: int = 5, length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 法人買進比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\法人買進比例.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 326頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("法人買張");
        if volume<>0 then value2=value1/volume*100;
        //法人買張佔成交量比例
        value3 = Average(value2,length1);
        value4 = Average(value2,length2);
        plot1(value3,"短期均線");
        plot2(value4,"長期均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股東人數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 股東人數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\股東人數.xs
        XS Logic Reference:
        {@type:indicator}
        //說明：
        //交易所公布的總持股人數。
        //執行商品為股票時，支援「週」以上的頻率。
        //執行商品為可轉債時，支援「月」以上的頻率。
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symbolType = 1 or symboltype = 6);//個股+類股+可轉債
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 2 or symbolType = 1 then begin
        	if barFreq = "D" then
        		value1 = GetField("總持股人數","W")
        	else
        		value1 = GetField("總持股人數");
        end;
        if symboltype = 6 then begin
        	if barFreq = "D" or barFreq = "W"  then
        		value1 = GetField("總持股人數","M")
        	else
        		value1 = GetField("總持股人數");
        end;
        plot1(value1,"總持股人數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 自營商成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\自營商成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	籌碼指標。
        	支援日以上頻率。支援台股商品。
        }
        plot1(GetField("自營商成本"),"自營商成本線");//系統估算值。計算自營商持股成本。
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商累計買賣超(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 自營商累計買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\自營商累計買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        _buyTotal = summation(GetField("自營商買賣超"), Length);
        volTotal = summation(Volume, Length);
        Plot1(_buyTotal, "累計買賣超");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商買超佔成交量比重(df: pd.DataFrame, length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 自營商買超佔成交量比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\自營商買超佔成交量比重.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率，僅支援日線以上");
        value4=getField("自營商買賣超", "D");
        if volume<>0 then 
        value5=(summation(value4,length)/summation(volume,length))*100;
        _strplot1 = text("近 ",numToStr(length,0)," 期，自營商買超佔成交量比重");
        plot1(value5,"自營商買超佔成交量比重");
        setplotLabel(1,_strplot1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資累計張數(df: pd.DataFrame, Length: int = 5, TXT: str = "僅適用日線以上") -> tuple[bool, str]:
        """
        Original Strategy: 融資累計張數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\融資累計張數.xs
        XS Logic Reference:
        {@type:indicator}
        _buyTotal = summation(GetField("融資增減張數"), Length);
        volTotal = summation(Volume, Length);
        Plot1(_buyTotal, "累計增減");
        Plot2(_buyTotal * 100 / volTotal, "比例%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 資金流向(df: pd.DataFrame, short1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 資金流向
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼指標\資金流向.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 327頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        	short1(5,"短期平均"),
        	mid1(12,"長期平均");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("資金流向");
        value2=average(value1,20);
        value3=value1-value2;
        value4=average(value3,short1);
        value5=average(value3,mid1);
        plot1(value4,"短期均線");
        plot2(value5,"長期均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
