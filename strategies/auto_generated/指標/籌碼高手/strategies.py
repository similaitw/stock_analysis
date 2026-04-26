# Auto-generated strategies for: 指標/籌碼高手
import pandas as pd
import numpy as np

class 籌碼高手Strategies:

    @staticmethod
    def CB剩餘張數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: CB剩餘張數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\CB剩餘張數.xs
        XS Logic Reference:
        {@type:indicator}
        if SymbolType <> 6 then RaiseRunTimeError("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if barFreq = "D" then
        	value1 = getField("CB剩餘張數","w")
        else
        	value1 = GetField("CB剩餘張數");
        plot1(value1,"CB剩餘張數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CB轉換溢價率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: CB轉換溢價率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\CB轉換溢價率.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	支援商品：可轉債商品。
        	支援頻率：分鐘以上的頻率。
        	繪圖序列1是「可轉債轉換溢價率」的線條。
        }
        if SymbolType <> 6 then RaiseRunTimeError("不支援此商品");
        if GetSymbolInfo("轉換價格") <> 0 then	//避免分母為0
        	value1 = (100 / GetSymbolInfo("轉換價格")) * GetSymbolField("Underlying", "收盤價");//轉換價值 = (100 / 轉換價格) x 股票現價
        if value1 <> 0 then
        	value2 = (close - value1)/value1;//轉換溢價率(%) = (CB價格 - 轉換價值) / 轉換價值
        plot1(value2,"轉換溢價率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三方買盤(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 三方買盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\三方買盤.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("散戶買張"),"散戶買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        plot2(GetField("實戶買張"),"實戶買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        plot3(GetField("控盤者買張"),"控盤者買進(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三方賣盤(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 三方賣盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\三方賣盤.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("散戶賣張"),"散戶賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        plot2(GetField("實戶賣張"),"實戶賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        plot3(GetField("控盤者賣張"),"控盤者賣出(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力進出(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 主力進出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\主力進出.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition997 = condition999 and (symboltype = 2 or symboltype = 4);//個股+權證+興櫃
        if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Min" then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("主力買進金額");
        	value2 = GetField("主力賣出金額");
        	value3 = value1 - value2;
        	value4 = GetField("主力累計買賣超金額");
        	plot2(value4,"主力累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"主力累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis2
        end else begin
        	if symbolexchange <> "TE" and symboltype <> 1 then begin
        		value1 = GetField("主力買張");
        		value2 = GetField("主力賣張");
        	end;
        	value3 = GetField("主力買賣超張數");
        	plot2(GetField("主力持股"),"主力持股",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"主力持股(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
        	if symbolexchange <> "TE" and symboltype <> 1 then begin
        		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 借券(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 借券
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\借券.xs
        XS Logic Reference:
        {@type:indicator}
        //借券餘額市值公式參考：
        //http://www.twse.com.tw/ch/trading/SBL/TWT72U/TWT72U.php
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 = false and condition996 = false //大盤+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 1 then begin
        	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);			//單位：張
        	plot2(GetField("借券餘額張數"),"借券餘額(張)",axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);				//單位：張
        	//plot3(GetField("借券餘額張數")*1000*close,"借券餘額市值(元)",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);	//單位：元，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end else begin
        	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);			//單位：張
        	plot2(GetField("借券餘額張數"),"借券餘額(張)",axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);				//單位：張
        	plot3(GetField("借券餘額張數")*1000*close,"借券餘額市值(元)",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);	//單位：元，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 借券賣出(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 借券賣出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\借券賣出.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 = false and condition996 = false //大盤+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 1 then begin
        	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot2(GetField("借券賣出張數")+GetField("借券賣出庫存異動張數"),"差額(張)",checkbox:=1,axis:=2);//增減bar，請RD加"借券還券"與"借券調整"
        	plot3(GetField("借券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot4(GetField("借券賣出庫存異動張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//請RD加
        end else begin
        	plot1(GetField("借券賣出餘額張數"),"借券賣出餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	plot2(GetField("借券賣出張數")+GetField("借券賣出庫存異動張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//增減bar，請RD加"借券還券"與"借券調整"
        	plot3(GetField("借券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot4(GetField("借券賣出庫存異動張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//請RD加
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 借券餘額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 借券餘額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\借券餘額.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 = false and condition996 = false //大盤+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 1 then begin
        	plot1(GetField("借券餘額張數"),"借券餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot2(GetField("借券張數") - GetField("還券張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot3(GetField("借券張數"),"借券(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot4(getfield("還券張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end else begin
        	plot1(GetField("借券餘額張數"),"借券餘額(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	plot2(GetField("借券張數") - GetField("還券張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	plot3(GetField("借券張數"),"借券(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot4(getfield("還券張數"),"還券(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內部人持股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內部人持股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\內部人持股.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*Getfield("內部人持股比例","M"),"內部人持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//請RD加
        plot2(Getfield("內部人持股張數","M"),"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內部人持股異動(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內部人持股異動
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\內部人持股異動.xs
        XS Logic Reference:
        {@type:indicator}
        {支援頻率：日、週、月}
        {支援商品：美(股票)}
        if barfreq <> "d" and barfreq <> "w" and barfreq <> "m" then raiseruntimeerror("不支援此頻率");
        exchange = GetSymbolInfo("交易所");
        if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");
        plot1(Getfield("內部人持股異動"),"內部人持股異動",Checkbox:=1);//計算內部人的交易總股數
        plot2(Getfield("內部人持股"),"內部人持股",Checkbox:=0);//計算有持股異動的內部人總股數
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司交易家數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分公司交易家數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\分公司交易家數.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition997 = condition999 and (symboltype = 2 or symboltype = 4);//個股+權證+興櫃
        if condition997 = false //個股+權證+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" 
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value11 = 0 else value11 = GetField("分公司交易家數");
        if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value21 = 0 else value21 = GetField("分公司買進家數");
        if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value31 = 0 else value31 = GetField("分公司賣出家數");
        if GetField("市場總分點數") <> 0 then value1 = value11/GetField("市場總分點數");
        plot1(value11,"交易家數",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家
        plot2(value1,"參與率",checkbox:=0,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot3(value21,"買進家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定) 
        plot4(value31,"賣出家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定)
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司淨買賣金額家數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分公司淨買賣金額家數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\分公司淨買賣金額家數.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition997 = condition999 and (symboltype = 2 or symboltype = 4 or symbolType = 1);//個股+權證+興櫃+類股
        if condition997 = false //個股+權證+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" 
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司淨買超金額家數") and GetField("成交量") = 0 then value1 = 0 else value1 = GetField("分公司淨買超金額家數");
        if getfieldDate("date") <> getfieldDate("分公司淨賣超金額家數") and GetField("成交量") = 0 then value2 = 0 else value2 = GetField("分公司淨賣超金額家數");
        plot1(value2-value1,"分公司淨買賣超金額家數差",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家
        plot2(value1,"分公司淨買超金額家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定) 
        plot3(value2,"分公司淨賣超金額家數",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家，可勾選畫圖選項 (參數設定) 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分公司買進賣出家數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分公司買進賣出家數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\分公司買進賣出家數.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition992 = condition999 and  (symbol <> "TSE.TW" and symbol <> "TWSE.FS" and symbol <> "OTC.TW");//類股+個股+權證+興櫃
        if condition992 = false //類股+個股+權證+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" 
        	then raiseruntimeerror("不支援此頻率");
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1 = 0 else value1 = GetField("分公司買進家數");
        if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2 = 0 else value2 = GetField("分公司賣出家數");
        plot1(value2-value1,"家數差",checkbox:=1,axis:=2);//單位：家
        plot2(value1,"買進",checkbox:=0,axis:=1);//單位：家，可勾選畫圖選項 (參數設定) 
        plot3(value2,"賣出",checkbox:=0,axis:=1);//單位：家，可勾選畫圖選項 (參數設定) 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 券資比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 券資比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\券資比.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 1 then begin
        	plot1(0.01 * GetField("券資比"),"券資比",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：
        	plot2(GetField("融券餘額張數"),"融券餘額",axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot3(GetField("融資餘額"),"融資餘額",axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end else begin
        	plot1(0.01 * GetField("券資比"),"券資比",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：
        	plot2(GetField("融券餘額張數"),"融券餘額",axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        	plot3(GetField("融資餘額"),"融資餘額",axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，新增查價顯示 (繪圖形式->隱藏, 不畫圖)
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 吉尼系數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 吉尼系數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\吉尼系數.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" 
        	then raiseruntimeerror("不支援此頻率");
        plot1(Getfield("吉尼係數","D"),"吉尼係數",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。	
        if getfieldDate("date") <> getfieldDate("分公司交易家數") and GetField("成交量") = 0 then value1 = 0 else value1=GetField("分公司交易家數");
        plot2(value1,"分公司交易家數",axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：家
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 地緣券商買賣超(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 地緣券商買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\地緣券商買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW";//台股
        if condition999 = false //個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("地緣券商買賣超張數");
        value2 += value1;
        plot1(value1,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        plot2(value2,"地緣券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\外資.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("外資買進金額");
        	value2 = GetField("外資賣出金額");
        	value3 = GetField("外資買賣超金額");
        	value4 = value4 + GetField("外資買賣超金額");
        	plot2(value4,"外資累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"外資累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else 
        begin
        	if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
        		value1 = GetField("外資買張");
        		value2 = GetField("外資賣張");
        	end;
        	value3 = GetField("外資買賣超張數");
        	plot2(GetField("外資持股"),"外資持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"外資持股(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	if condition993 = false then begin
        		plot5(0.01*GetField("外資持股比例"),"外資持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	end;
        	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
        	if symbolexchange <> "TE" and condition993 = false then begin
        		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資持股比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資持股比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\外資持股比例.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*GetField("外資持股比例"),"外資持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶持股(df: pd.DataFrame, _input1: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 大戶持股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\大戶持股.xs
        XS Logic Reference:
        {@type:indicator}
        {由集保公司所提供的，「指定級距以上」的持股資料所計算}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symbolType = 1);//個股+興櫃+類股
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        switch (_input1)
        begin
        	case 1:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=1);
        			value2 = Getfield("大戶持股張數","W",param:=1);
        			value3 = Getfield("大戶持股人數","W",param:=1);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=1);
        			value2 = Getfield("大戶持股張數",param:=1);
        			value3 = Getfield("大戶持股人數",param:=1);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 5:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=5);
        			value2 = Getfield("大戶持股張數","W",param:=5);
        			value3 = Getfield("大戶持股人數","W",param:=5);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=5);
        			value2 = Getfield("大戶持股張數",param:=5);
        			value3 = Getfield("大戶持股人數",param:=5);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 10:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=10);
        			value2 = Getfield("大戶持股張數","W",param:=10);
        			value3 = Getfield("大戶持股人數","W",param:=10);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=10);
        			value2 = Getfield("大戶持股張數",param:=10);
        			value3 = Getfield("大戶持股人數",param:=10);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 15:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=15);
        			value2 = Getfield("大戶持股張數","W",param:=15);
        			value3 = Getfield("大戶持股人數","W",param:=15);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=15);
        			value2 = Getfield("大戶持股張數",param:=15);
        			value3 = Getfield("大戶持股人數",param:=15);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 20:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=20);
        			value2 = Getfield("大戶持股張數","W",param:=20);
        			value3 = Getfield("大戶持股人數","W",param:=20);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=20);
        			value2 = Getfield("大戶持股張數",param:=20);
        			value3 = Getfield("大戶持股人數",param:=20);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 30:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=30);
        			value2 = Getfield("大戶持股張數","W",param:=30);
        			value3 = Getfield("大戶持股人數","W",param:=30);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=30);
        			value2 = Getfield("大戶持股張數",param:=30);
        			value3 = Getfield("大戶持股人數",param:=30);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 40:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=40);
        			value2 = Getfield("大戶持股張數","W",param:=40);
        			value3 = Getfield("大戶持股人數","W",param:=40);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=40);
        			value2 = Getfield("大戶持股張數",param:=40);
        			value3 = Getfield("大戶持股人數",param:=40);
        		end;	
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 50:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=50);
        			value2 = Getfield("大戶持股張數","W",param:=50);
        			value3 = Getfield("大戶持股人數","W",param:=50);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=50);
        			value2 = Getfield("大戶持股張數",param:=50);
        			value3 = Getfield("大戶持股人數",param:=50);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 100:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=100);
        			value2 = Getfield("大戶持股張數","W",param:=100);
        			value3 = Getfield("大戶持股人數","W",param:=100);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=100);
        			value2 = Getfield("大戶持股張數",param:=100);
        			value3 = Getfield("大戶持股人數",param:=100);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 200:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=200);
        			value2 = Getfield("大戶持股張數","W",param:=200);
        			value3 = Getfield("大戶持股人數","W",param:=200);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=200);
        			value2 = Getfield("大戶持股張數",param:=200);
        			value3 = Getfield("大戶持股人數",param:=200);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 400:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=400);
        			value2 = Getfield("大戶持股張數","W",param:=400);
        			value3 = Getfield("大戶持股人數","W",param:=400);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=400);
        			value2 = Getfield("大戶持股張數",param:=400);
        			value3 = Getfield("大戶持股人數",param:=400);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 600:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=600);
        			value2 = Getfield("大戶持股張數","W",param:=600);
        			value3 = Getfield("大戶持股人數","W",param:=600);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=600);
        			value2 = Getfield("大戶持股張數",param:=600);
        			value3 = Getfield("大戶持股人數",param:=600);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 800:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=800);
        			value2 = Getfield("大戶持股張數","W",param:=800);
        			value3 = Getfield("大戶持股人數","W",param:=800);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=800);
        			value2 = Getfield("大戶持股張數",param:=800);
        			value3 = Getfield("大戶持股人數",param:=800);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	default:
        		if barFreq = "D" then begin
        			value1 = Getfield("大戶持股比例","W",param:=1000);
        			value2 = Getfield("大戶持股張數","W",param:=1000);
        			value3 = Getfield("大戶持股人數","W",param:=1000);
        		end else begin
        			value1 = Getfield("大戶持股比例",param:=1000);
        			value2 = Getfield("大戶持股張數",param:=1000);
        			value3 = Getfield("大戶持股人數",param:=1000);
        		end;
        		plot1(0.01*value1,"大戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤法人比重(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大盤法人比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\大盤法人比重.xs
        XS Logic Reference:
        {@type:indicator}
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 = false //大盤
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" and
        	barfreq <> "W" and barfreq <> "AW" and
        	barfreq <> "M" and barfreq <> "AM"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.005*(GetField("法人買進比重")+GetField("法人賣出比重")),"交易比重",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot2(0.01*GetField("法人買進比重"),"買進比重",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot3(0.01*GetField("法人賣出比重"),"賣出比重",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 官股券商(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 官股券商
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\官股券商.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 =false and condition998 = false //大盤+個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("官股券商買進金額");
        	value2 = GetField("官股券商賣出金額");
        	value3 = value1 - value2;
        	value4 = GetField("官股券商累計買賣超金額");
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        	plot1(value3,"買賣超"); //bar，axis2
        	plot2(value4,"官股券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	plot3(value1,"買進(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else if condition994 = false then begin
        	value1 = GetField("官股券商買進金額");
        	value2 = GetField("官股券商賣出金額");
        	value3 = GetField("官股券商買賣超張數");
        	value4 = value4 + value3;
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"累計買賣超(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	plot1(value3,"買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        	plot2(value4,"官股券商累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 實戶買賣盤(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 實戶買賣盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\實戶買賣盤.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("實戶買賣超張數")+value1;
        plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        plot2(GetField("實戶買賣超張數"),"實戶買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 實質買賣盤比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 實質買賣盤比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\實質買賣盤比.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*(GetField("實質買盤比")-GetField("實質賣盤比")),"買賣差值",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot2(0.01*GetField("實質買盤比"),"買盤比",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot3(0.01*GetField("實質賣盤比"),"賣盤比",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 庫藏股指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 庫藏股指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\庫藏股指標.xs
        XS Logic Reference:
        {@type:indicator}
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW" or symbolType = 1;//大盤、類股
        if condition994 = false //大盤、類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("庫藏股申請總市值")*1000,"申報總市值",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位:千元
        plot2(GetField("庫藏股申請家數"),"申報家數",checkbox:=0,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:家
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\投信.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("投信買進金額");
        	value2 = GetField("投信賣出金額");
        	value3 = GetField("投信買賣超金額");
        	value4 = value4 + GetField("投信買賣超金額");
        	plot2(value4,"投信累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"投信累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else begin
        	if symbolexchange <> "TE" and condition993 = false then begin
        		value1 = GetField("投信買張");
        		value2 = GetField("投信賣張");
        	end;
        	value3 = GetField("投信買賣超張數");
        	plot2(GetField("投信持股"),"投信持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"投信持股(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	if condition993 = false then begin
        		plot5(0.01*GetField("投信持股比例"),"投信持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	end;
        	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
        	if symbolexchange <> "TE" and condition993 = false then begin
        		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信持股比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信持股比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\投信持股比例.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*GetField("投信持股比例"),"投信持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 控盤者主動買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 控盤者主動買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\控盤者主動買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("主動性交易比重"),"交易比重",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
        plot2(GetField("主動買力"),"主動買力",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
        plot3(GetField("主動賣力"),"主動賣力",checkbox:=0,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 控盤者買賣盤(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 控盤者買賣盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\控盤者買賣盤.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("控盤者買賣超張數")+value1;
        plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        plot2(GetField("控盤者買賣超張數"),"控盤者買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶持股(df: pd.DataFrame, _input1: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 散戶持股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\散戶持股.xs
        XS Logic Reference:
        {@type:indicator}
        {由集保公司所提供的，「指定級距以下」的持股資料所計算}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symbolType = 1);//個股+興櫃+類股
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        switch (_input1)
        begin
        	case 1:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=1);
        			value2 = Getfield("散戶持股張數","W",param:=1);
        			value3 = Getfield("散戶持股人數","W",param:=1);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=1);
        			value2 = Getfield("散戶持股張數",param:=1);
        			value3 = Getfield("散戶持股人數",param:=1);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 5:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=5);
        			value2 = Getfield("散戶持股張數","W",param:=5);
        			value3 = Getfield("散戶持股人數","W",param:=5);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=5);
        			value2 = Getfield("散戶持股張數",param:=5);
        			value3 = Getfield("散戶持股人數",param:=5);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 10:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=10);
        			value2 = Getfield("散戶持股張數","W",param:=10);
        			value3 = Getfield("散戶持股人數","W",param:=10);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=10);
        			value2 = Getfield("散戶持股張數",param:=10);
        			value3 = Getfield("散戶持股人數",param:=10);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 15:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=15);
        			value2 = Getfield("散戶持股張數","W",param:=15);
        			value3 = Getfield("散戶持股人數","W",param:=15);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=15);
        			value2 = Getfield("散戶持股張數",param:=15);
        			value3 = Getfield("散戶持股人數",param:=15);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 20:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=20);
        			value2 = Getfield("散戶持股張數","W",param:=20);
        			value3 = Getfield("散戶持股人數","W",param:=20);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=20);
        			value2 = Getfield("散戶持股張數",param:=20);
        			value3 = Getfield("散戶持股人數",param:=20);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 30:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=30);
        			value2 = Getfield("散戶持股張數","W",param:=30);
        			value3 = Getfield("散戶持股人數","W",param:=30);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=30);
        			value2 = Getfield("散戶持股張數",param:=30);
        			value3 = Getfield("散戶持股人數",param:=30);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 40:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=40);
        			value2 = Getfield("散戶持股張數","W",param:=40);
        			value3 = Getfield("散戶持股人數","W",param:=40);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=40);
        			value2 = Getfield("散戶持股張數",param:=40);
        			value3 = Getfield("散戶持股人數",param:=40);
        		end;	
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 50:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=50);
        			value2 = Getfield("散戶持股張數","W",param:=50);
        			value3 = Getfield("散戶持股人數","W",param:=50);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=50);
        			value2 = Getfield("散戶持股張數",param:=50);
        			value3 = Getfield("散戶持股人數",param:=50);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 100:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=100);
        			value2 = Getfield("散戶持股張數","W",param:=100);
        			value3 = Getfield("散戶持股人數","W",param:=100);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=100);
        			value2 = Getfield("散戶持股張數",param:=100);
        			value3 = Getfield("散戶持股人數",param:=100);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 200:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=200);
        			value2 = Getfield("散戶持股張數","W",param:=200);
        			value3 = Getfield("散戶持股人數","W",param:=200);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=200);
        			value2 = Getfield("散戶持股張數",param:=200);
        			value3 = Getfield("散戶持股人數",param:=200);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 400:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=400);
        			value2 = Getfield("散戶持股張數","W",param:=400);
        			value3 = Getfield("散戶持股人數","W",param:=400);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=400);
        			value2 = Getfield("散戶持股張數",param:=400);
        			value3 = Getfield("散戶持股人數",param:=400);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 600:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=600);
        			value2 = Getfield("散戶持股張數","W",param:=600);
        			value3 = Getfield("散戶持股人數","W",param:=600);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=600);
        			value2 = Getfield("散戶持股張數",param:=600);
        			value3 = Getfield("散戶持股人數",param:=600);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	case 800:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=800);
        			value2 = Getfield("散戶持股張數","W",param:=800);
        			value3 = Getfield("散戶持股人數","W",param:=800);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=800);
        			value2 = Getfield("散戶持股張數",param:=800);
        			value3 = Getfield("散戶持股人數",param:=800);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	default:
        		if barFreq = "D" then begin
        			value1 = Getfield("散戶持股比例","W",param:=1000);
        			value2 = Getfield("散戶持股張數","W",param:=1000);
        			value3 = Getfield("散戶持股人數","W",param:=1000);
        		end else begin
        			value1 = Getfield("散戶持股比例",param:=1000);
        			value2 = Getfield("散戶持股張數",param:=1000);
        			value3 = Getfield("散戶持股人數",param:=1000);
        		end;
        		plot1(0.01*value1,"散戶持股比例",checkbox:=1,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        		plot2(value2,"持股張數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        		plot3(value3,"持股人數",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶指標_量_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 散戶指標(量)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\散戶指標(量).xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        //原始spec要求支援類股，6.30暫不支援，等DB補資料
        //if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        if condition994 =false and condition996 = false //大盤+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then
        	value1 =  GetField("累計成交") - (GetField("資券互抵張數") + GetField("現股當沖張數"))
        else
        	value1 = volume - (GetField("資券互抵張數") + GetField("現股當沖張數"));
        value2 = GetField("融資買進張數") + GetField("融券買進張數");
        value3 = GetField("融資賣出張數") + GetField("融券賣出張數");
        if value1 <> 0 then begin
        	value4 = value2 / value1;
        	value5 = value3 / value1;
        end else begin
        	value4 = 0;
        	value5 = 0;
        end;
        plot1(value4 - value5,"買賣差值",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
        plot2(value4,"買進",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
        plot3(value5,"賣出",checkbox:=0,axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買賣盤(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 散戶買賣盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\散戶買賣盤.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("散戶買賣超張數")+value1;
        plot1(value1,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        plot2(GetField("散戶買賣超張數"),"散戶買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位:張
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本益比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 本益比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\本益比.xs
        XS Logic Reference:
        {@type:indicator}
        //支援商品：台(股票)、美(股票)、美(特別股）
        value1 = GetField("本益比");
        if value1 > 0 then begin
        	plot1(value1);
        	setplotLabel(1,"PE");
        end
        else begin
        	plot1(0);
        	setplotLabel(1,"近4季EPS為負");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 機構持股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 機構持股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\機構持股.xs
        XS Logic Reference:
        {@type:indicator}
        //資料更新頻率：季
        //支援商品：美(股票)
        if barfreq = "Tick" or barfreq = "Min" then raiseruntimeerror("不支援此頻率");
        exchange = GetSymbolInfo("交易所");
        if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");
        plot1(GetField("機構持股比重", "Q")/100,"機構持股比重",Checkbox:=1);//機購持股比重
        plot2(GetField("機構持股", "Q"),"持股數值",Checkbox:=0);//持股數值
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 殖利率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 殖利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\殖利率.xs
        XS Logic Reference:
        {@type:indicator}
        //支援商品：台(股票)、台(ETF)、美(股票)、美(ETF)、美(特別股)。
        value1 = GetField("殖利率");
        if value1 > 0 then begin
        	plot1(value1/100);
        	setplotLabel(1,"殖利率");
        end	
        else begin
        	plot1(0);
        	setplotLabel(1,"無配息紀錄");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法人
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\法人.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition997 = condition999 and (symboltype = 2 or symboltype = 4);//個股+權證+興櫃
        if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("法人買進金額");
        	value2 = GetField("法人賣出金額");
        	value3 = GetField("法人買賣超金額");
        	value4 = value4 + GetField("法人買賣超金額");
        	plot2(value4,"法人累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"法人累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else begin
        	if symbolexchange <> "TE" and symboltype <> 1 and date >= 20110106 then begin
        		value1 = GetField("法人買張");
        		value2 = GetField("法人賣張");
        	end;
        	value3 = GetField("法人買賣超張數");
        	plot2(GetField("法人持股"),"法人持股",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"法人持股(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	if symboltype <> 1 then 
        		value5 = 0.01*GetField("法人持股比例");
        	plot5(value5,"法人持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
        	if symbolexchange <> "TE" and symboltype <> 1 then begin
        		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人持股比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法人持股比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\法人持股比例.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*GetField("法人持股比例"),"法人持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營收
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\營收.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min" or barfreq = "Q" or barfreq = "H" or barfreq = "Y"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("月營收","M") <> 0 then
        	value1 = rateOfChange(GetField("月營收","M"),1) / 100;
        if GetField("月營收","M")[12] <> 0 then
        	value2 = (GetField("月營收","M") - GetField("月營收","M")[12]) / GetField("月營收","M")[12];
        plot1(GetField("月營收","M")*100000000,"月營收",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd2);
        plot2(value1,"月增率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        plot3(value2,"年增率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現股當沖金額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 現股當沖金額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\現股當沖金額.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if symboltype = 1 then begin
        	if volume <> 0 then
        		value1 = (GetField("現股當沖買進金額")+GetField("現股當沖賣出金額"))/(volume*2)
        	else
        		value1 = 0;
        	plot1(value1,"當沖比率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：％
        	plot2(GetField("現股當沖買進金額"),"買進",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
        	plot3(GetField("現股當沖賣出金額"),"賣出",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
        end else begin
        	if GetField("成交金額(元)") <> 0 then
        		value1 = (GetField("現股當沖買進金額")+GetField("現股當沖賣出金額"))/(GetField("成交金額(元)")*2)
        	else
        		value1 = 0;
        	plot1(value1,"當沖比率",checkbox:=1,axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位：％
        	plot2(GetField("現股當沖買進金額"),"買進",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
        	plot3(GetField("現股當沖賣出金額"),"賣出",checkbox:=0,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元，可勾選畫圖選項 (參數設定) 
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 申報轉讓(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 申報轉讓
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\申報轉讓.xs
        XS Logic Reference:
        {@type:indicator}
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition994 =false and condition993 = false //大盤+類股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD" and
        	barfreq <> "W" and barfreq <> "AW" and
        	barfreq <> "M" and barfreq <> "AM"
        	then raiseruntimeerror("不支援此頻率");
        plot1(Getfield("申報總市值"),"申報總市值",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        plot2(Getfield("申報家數"),"申報家數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        plot3(Getfield("申報人數"),"申報人數",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當沖(df: pd.DataFrame, _input1: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 當沖
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\當沖.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        switch (_input1)
        begin
        	case 2:
        		dtVolume = GetField("資券互抵張數");
        	case 3:
        		dtVolume = GetField("現股當沖張數");
        	default:
        		dtVolume = GetField("資券互抵張數") + GetField("現股當沖張數");
        end;
        if condition993 and not condition994 then
        	begin
        		switch (barfreq)
        		begin
        			case "W","AW":
        				value1 = summation(GetField("內盤量","D") + GetField("外盤量","D"),dayofweek(getfielddate("內盤量","D")));
        			case "M","AM":
        				value1 = summation(GetField("內盤量","D") + GetField("外盤量","D"),ceiling(dayofmonth(getfielddate("內盤量","D"))*5/7));
        			case "Q":
        				value1 = summation(GetField("內盤量","D") + GetField("外盤量","D"),mod(month(getfielddate("內盤量","D"))+2,3)*22 + ceiling(dayofmonth(getfielddate("內盤量","D"))*5/7));
        			case "H":
        				value1 = summation(GetField("內盤量","D") + GetField("外盤量","D"),mod(month(getfielddate("內盤量","D"))+5,6)*22 + dayofmonth(getfielddate("內盤量","D"))*5/7);
        			case "Y":
        				value1 = summation(GetField("內盤量","D") + GetField("外盤量","D"),mod(month(getfielddate("內盤量","D"))+11,12)*22 + dayofmonth(getfielddate("內盤量","D"))*5/7);
        			default:
        				value1 = GetField("內盤量","D") + GetField("外盤量","D");
        		end;
        	end
        else if condition994 then
        	begin
        		switch (barfreq)
        		begin
        			case "W","AW":
        				value1 = summation(GetField("累計成交","D"),dayofweek(getfielddate("累計成交","D")));
        			case "M","AM":
        				value1 = summation(GetField("累計成交","D"),ceiling(dayofmonth(getfielddate("累計成交","D"))*5/7));
        			case "Q":
        				value1 = summation(GetField("累計成交","D"),mod(month(getfielddate("累計成交","D"))+2,3)*22 + ceiling(dayofmonth(getfielddate("累計成交","D"))*5/7));
        			case "H":
        				value1 = summation(GetField("累計成交","D"),mod(month(getfielddate("累計成交","D"))+5,6)*22 + ceiling(dayofmonth(getfielddate("累計成交","D"))*5/7));
        			case "Y":
        				value1 = summation(GetField("累計成交","D"),mod(month(getfielddate("累計成交","D"))+11,12)*22 + ceiling(dayofmonth(getfielddate("累計成交","D"))*5/7));
        			default:
        				value1 = GetField("累計成交","D");
        		end;
        	end
        else 
        	value1 = volume;
        if value1 <> 0 then
        	value2 = dtVolume/value1
        else
        	value2 = 0;
        if symboltype = 1 then begin
        	plot1(dtVolume,"當沖張數",axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);	//單位：張
        	plot2(value2,"當沖率",axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	plot3(GetField("資券互抵張數"),"資券互抵(張)",ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        	plot4(GetField("現股當沖張數"),"現股當沖(張)",ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);
        end else begin
        	plot1(dtVolume,"當沖張數",axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);	//單位：張
        	plot2(value2,"當沖率",axis:=2,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	plot3(GetField("資券互抵張數"),"資券互抵(張)",ScaleLabel:=slfull,ScaleDecimal:=sd0);
        	plot4(GetField("現股當沖張數"),"現股當沖(張)",ScaleLabel:=slfull,ScaleDecimal:=sd0);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 累計每股盈餘_發佈值_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 累計每股盈餘(發佈值)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\累計每股盈餘(發佈值).xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if GetField("累計每股盈餘(發佈值)","Q")[4] <> 0 then
        	value1 = (GetField("累計每股盈餘(發佈值)","Q") - GetField("累計每股盈餘(發佈值)","Q")[4]) / GetField("累計每股盈餘(發佈值)","Q")[4]*100;
        plot1(GetField("累計每股盈餘(發佈值)","Q"),"累計每股盈餘(發佈值)");
        plot2(value1,"年增率(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 累計淨利_發佈值_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 累計淨利(發佈值)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\累計淨利(發佈值).xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
        if condition998 = false //個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        if GetField("累計淨利(發佈值)","Q")[4] <> 0 then
        	value1 = (GetField("累計淨利(發佈值)","Q") - GetField("累計淨利(發佈值)","Q")[4]) / GetField("累計淨利(發佈值)","Q")[4]*100;
        plot1(GetField("累計淨利(發佈值)","Q"),"累計淨利(發佈值)");
        plot2(value1,"年增率(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 綜合前十大券商(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 綜合前十大券商
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\綜合前十大券商.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and (symboltype = 2 or symboltype = 1);//個股+興櫃+類股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 =false and condition998 = false //大盤+個股+興櫃+類股
        	then raiseruntimeerror("不支援此商品");
        //if condition994 = false //大盤
        	//then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	value1 = GetField("綜合前十大券商買進金額");
        	value2 = GetField("綜合前十大券商賣出金額");
        	value3 = value1 - value2;
        	value4 = GetField("綜合前十大券商累計買賣超金額");
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
        	plot2(value4,"綜合前十大券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else begin
        	value3 = GetField("綜合前十大券商買賣超張數");
        	value4 = value4 + value3;
        	plot1(value3,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        	plot2(value4,"綜合前十大券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 總持股人數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 總持股人數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\總持股人數.xs
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
    def 自營商(df: pd.DataFrame, _input1: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 自營商
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\自營商.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        if condition999 = false and condition994 = false//大盤, 個股, 權證, 興櫃, 類股指數
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	switch (_input1)
        	begin
        		case 2:
        			value1 = GetField("自營商自行買賣買進金額");
        			value2 = GetField("自營商自行買賣賣出金額");
        			value3 = GetField("自營商自行買賣買賣超金額");
        			value4 = value4 + GetField("自營商自行買賣買賣超金額");
        		case 3:
        			value1 = GetField("自營商避險買進金額");
        			value2 = GetField("自營商避險賣出金額");
        			value3 = GetField("自營商避險買賣超金額");
        			value4 = value4 + GetField("自營商避險買賣超金額");
        		default:
        			value1 = GetField("自營商買進金額");
        			value2 = GetField("自營商賣出金額");
        			value3 = GetField("自營商買賣超金額");
        			value4 = value4 + GetField("自營商買賣超金額");
        	end;
        	plot2(value4,"自營商累計買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis1
        	setplotlabel(1,"買賣超(元)");
        	setplotlabel(2,"自營商累計買賣超(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //bar，axis2
        	plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        	plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto); //line，axis2
        end else begin
        	switch (_input1)
        	begin
        		case 2:
        			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
        				value1 = GetField("自營商自行買賣買張");
        				value2 = GetField("自營商自行買賣賣張");
        			end;
        			value3 = GetField("自營商自行買賣買賣超");
        		case 3:
        			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
        				value1 = GetField("自營商避險買張");
        				value2 = GetField("自營商避險賣張");
        			end;
        			value3 = GetField("自營商避險買賣超");
        		default:
        			if symbolexchange <> "TE" and condition993 = false and date >= 20110106 then begin
        				value1 = GetField("自營商買張");
        				value2 = GetField("自營商賣張");
        			end;
        			value3 = GetField("自營商買賣超張數");
        	end;
        	plot2(GetField("自營商持股"),"自營商持股",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis1
        	setplotlabel(1,"買賣超(張)");
        	setplotlabel(2,"自營商持股(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        	if condition993 = false then begin
        		plot5(0.01*GetField("自營商持股比例"),"自營商持股比例",axis:=12,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        	end;
        	plot1(value3,"買賣超",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0); //bar，axis2
        	if symbolexchange <> "TE" and condition993 = false then begin
        		plot3(value1,"買進",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        		plot4(value2,"賣出",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0); //line，axis2
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商持股比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 自營商持股比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\自營商持股比例.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW" or symbolexchange = "TE";//台股+興櫃
        condition998 = condition999 = true and symboltype = 2;//個股+興櫃
        if condition998 = false //個股+興櫃
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01*GetField("自營商持股比例"),"自營商持股比例",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融券(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 融券
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\融券.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        condition991 = symbolexchange = "SH" and symboltype = 2;//滬股
        condition990 = symbolexchange = "SZ" and symboltype = 2;//深股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	and condition991 = false and condition990 = false //陸股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 then begin
        	plot1(GetField("融券餘額張數"),"融券(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot2(GetField("融券增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot3(GetField("融券買進張數"),"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
        	plot4(GetField("融券賣出張數"),"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
        	plot5(GetField("現券償還張數"),"券償(張)",checkbox:=0,axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張，可勾選畫圖選項 (參數設定) 
        end else begin
        	plot1(GetField("融券餘額張數"),"融券(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	plot2(GetField("融券增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	if condition996 then begin
        		value1 = GetField("融券買進張數");
        		value2 = GetField("融券賣出張數");
        		value3 = GetField("現券償還張數");
        	end;
        	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
        	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
        	plot5(value3,"券償(張)",checkbox:=0,axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張，可勾選畫圖選項 (參數設定) 
        end;
        if condition996 then
        	plot6(GetField("融券使用率")*0.01,"使用率",axis:=13,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%隱藏，不畫圖，僅查價，缺欄位
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融券使用率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 融券使用率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\融券使用率.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        if condition996 = false //個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(0.01 * GetField("融券使用率"),"融券使用率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//請RD加
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資(df: pd.DataFrame, _input1: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 融資
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\融資.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TW" and symboltype = 1;//類股
        condition991 = symbolexchange = "SH" and symboltype = 2;//滬股
        condition990 = symbolexchange = "SZ" and symboltype = 2;//深股
        if condition994 =false and condition993 = false and condition996 = false //大盤+類股+個股
        	and condition991 = false and condition990 = false //陸股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if condition994 and _input1 = 1 then begin
        	plot1(GetField("融資餘額金額"),"融資(元)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot2(GetField("融資增減金額"),"差額(元)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：張
        	plot3(GetField("融資買進金額"),"買進(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
        	plot4(GetField("融資賣出金額"),"賣出(元)",checkbox:=0,axis:=11,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
        	plot5(GetField("現金償還張數"),"現償(張)",checkbox:=0,axis:=12,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//可勾選畫圖選項 (參數設定) 
        	setplotlabel(1,"融資(元)");
        	setplotlabel(2,"差額(元)");
        	setplotlabel(3,"買進(元)");
        	setplotlabel(4,"賣出(元)");
        end else begin
        	plot1(GetField("融資餘額張數"),"融資(張)",checkbox:=1,axis:=1,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	plot2(GetField("融資增減張數"),"差額(張)",checkbox:=1,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	if condition996 then begin
        		value1 = GetField("融資買進張數");
        		value2 = GetField("融資賣出張數");
        		value3 = GetField("現金償還張數");
        	end;
        	plot3(value1,"買進(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
        	plot4(value2,"賣出(張)",checkbox:=0,axis:=11,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
        	plot5(value3,"現償(張)",checkbox:=0,axis:=12,ScaleLabel:=slfull,ScaleDecimal:=sd0);//可勾選畫圖選項 (參數設定) 
        	setplotlabel(1,"融資(張)");
        	setplotlabel(2,"差額(張)");
        	setplotlabel(3,"買進(張)");
        	setplotlabel(4,"賣出(張)");
        end;
        if condition996 then
        	plot6(GetField("融資使用率")*0.01,"使用率",axis:=13,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%，隱藏，不畫圖，僅查價
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資使用率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 融資使用率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\融資使用率.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        if condition996 = false //個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("融資使用率")*0.01,"融資使用率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);//單位%
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資維持率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 融資維持率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\融資維持率.xs
        XS Logic Reference:
        {@type:indicator}
        condition996 = symbolexchange = "TW" = true and symboltype = 2;//個股
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if condition994 = false and condition996 = false //大盤+個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        plot1(GetField("融資維持率")*0.01, "融資維持率",axis:=1,ScaleLabel:=slpercent,ScaleDecimal:=sd2);
        //plot1(1, "融資維持率",checkbox:=1,axis:=1);
        if symboltype = 1 then begin
        	plot2(GetField("融資增減金額"),"融資增減(元)",checkbox:=0,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sdauto);//單位：元
        	setplotlabel(2,"融資增減(元)");
        end else begin
        	plot2(GetField("融資增減張數"),"融資增減(張)",checkbox:=0,axis:=2,ScaleLabel:=slfull,ScaleDecimal:=sd0);//單位：張
        	setplotlabel(2,"融資增減(張)");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 關聯券商買賣超(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 關聯券商買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\關聯券商買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW";//台股
        condition998 = symbolType = 2;//股票
        if condition999 = false or condition998 = false//個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("關聯券商買賣超張數");
        value2 += value1;
        plot1(value1,"買賣超(張)",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        plot2(value2,"累計買賣超(張)",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 關鍵券商買賣超(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 關鍵券商買賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\籌碼高手\關鍵券商買賣超.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TW";//台股
        if condition999 = false //個股
        	then raiseruntimeerror("不支援此商品");
        if barfreq <> "D" and barfreq <> "AD"
        	then raiseruntimeerror("不支援此頻率");
        value1 = GetField("關鍵券商買賣超張數");
        value2 += value1;
        plot1(value1,"買賣超",checkbox:=1,axis:=2,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //bar，axis2
        plot2(value2,"關鍵券商累計買賣超",checkbox:=1,axis:=1,ScaleLabel:=sltypewy,ScaleDecimal:=sd0); //line，axis1
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
