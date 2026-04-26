# Auto-generated strategies for: 指標/期權指標
import pandas as pd
import numpy as np

class 期權指標Strategies:

    @staticmethod
    def Delta(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: Delta
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\Delta.xs
        XS Logic Reference:
        {@type:indicator}
        plot1(GetField("Delta"),"Delta");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Gamma(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: Gamma
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\Gamma.xs
        XS Logic Reference:
        {@type:indicator}
        plot1(GetField("Gamma"),"Gamma");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Theta(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: Theta
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\Theta.xs
        XS Logic Reference:
        {@type:indicator}
        plot1(GetField("Theta"),"Theta");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Vega(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: Vega
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\Vega.xs
        XS Logic Reference:
        {@type:indicator}
        plot1(GetField("Vega"),"Vega");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三大法人交易金額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 三大法人交易金額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\三大法人交易金額.xs
        XS Logic Reference:
        {@type:indicator}
        if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
        if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
        if barFreq<>"d" then raiseRunTimeError("僅支援日線");
        value1 = getField("三大法人交易買進金額");
        value2 = getField("三大法人交易賣出金額");
        value3 = value1 - value2;
        plot1(value1,"三大法人交易買進金額");
        plot2(value2,"三大法人交易賣出金額");
        plot3(value3,"三大法人交易淨額");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價內外(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 價內外
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\價內外.xs
        XS Logic Reference:
        {@type:indicator}
        if symboltype <> 5 then 
        	raiseruntimeerror("僅支援選擇權");
        vRatio = iff(leftstr(getsymbolinfo("買賣權"),1)="C",1,-1)*(100*getsymbolfield("Underlying","收盤價")/getsymbolinfo("履約價")-100);
        plot1(vRatio,"價內外%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價差(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 價差
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\價差.xs
        XS Logic Reference:
        {@type:indicator}
        condition999 = symbolexchange = "TF";//期貨
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        condition993 = symbolexchange = "TF" and symboltype = 5;//選擇權
        if (condition999 = false and condition994 = true) or symbolType = 5	//僅支援期貨
        	then raiseruntimeerror("不支援此商品");
        if symbolexchange = "TF" and symboltype = 3  then	//期貨
        	value1 = GetSymbolField("Underlying", "收盤價");	
        plot1(close-value1,"價差");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台指選Delta(df: pd.DataFrame, iRate100: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 台指選Delta
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\台指選Delta.xs
        XS Logic Reference:
        {@type:indicator}
        	iRate100(2,"無風險利率%"),
        	iVolity100(20,"波動率%"),
        	iHV(false, "波動率", inputkind:=dict(["標的20日歷史波動率",true],["固定波動率",false]));
        if instr(symbol,".TF") = 0 or leftstr(symbol,1) = "F" or instr(symbol,"TX") = 0 then 
        	raiseruntimeerror("僅支援台指選擇權");
        if iHV then 
        	vVolity100 = HVolatility(getsymbolfield("FITX*1.TF","收盤價","D"),20)
        else 
        	vVolity100 = iVolity100;
        vStrikePrice = getsymbolinfo("履約價");
        value1 = bsdelta(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("FITX*1.TF","收盤價"),vStrikePrice,daystoexpirationtf,iRate100,0,vVolity100);
        plot1(value1,"Delta");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台指選IV(df: pd.DataFrame, iRate100: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 台指選IV
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\台指選IV.xs
        XS Logic Reference:
        {@type:indicator}
        	iRate100(2,"無風險利率%");
        if instr(symbol,".TF") = 0 or leftstr(symbol,1) = "F" or instr(symbol,"TX") = 0 then 
        	raiseruntimeerror("僅支援台指選擇權");
        vStrikePrice = getsymbolinfo("履約價");
        value1 = ivolatility(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("FITX*1.TF","收盤價"),vStrikePrice,daystoexpirationtf,iRate100,0,c);
        plot1(value1,"隱含波動率%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台股指數近月外資未平倉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 台股指數近月外資未平倉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\台股指數近月外資未平倉.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = getsymbolfield("FITX*1.TF","外資買方未平倉口數");
        value2 = getsymbolfield("FITX*1.TF","外資賣方未平倉口數");
        value3 = value1 - value2;
        plot1(value1,"外資未平倉買口");
        plot2(value2,"外資未平倉賣口");
        plot3(value3,"外資未平倉淨口");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台股指數近月投信未平倉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 台股指數近月投信未平倉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\台股指數近月投信未平倉.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = getsymbolfield("FITX*1.TF","投信買方未平倉口數");
        value2 = getsymbolfield("FITX*1.TF","投信賣方未平倉口數");
        value3 = value1 - value2;
        plot1(value1,"投信未平倉買口");
        plot2(value2,"投信未平倉賣口");
        plot3(value3,"投信未平倉淨口");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 台股指數近月自營商未平倉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 台股指數近月自營商未平倉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\台股指數近月自營商未平倉.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = getsymbolfield("FITX*1.TF","自營商買方未平倉口數");
        value2 = getsymbolfield("FITX*1.TF","自營商賣方未平倉口數");
        value3 = value1 - value2;
        plot1(value1,"自營商未平倉買口");
        plot2(value2,"自營商未平倉賣口");
        plot3(value3,"自營商未平倉淨口");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資交易金額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外資交易金額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\外資交易金額.xs
        XS Logic Reference:
        {@type:indicator}
        if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
        if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
        if barFreq<>"d" then raiseRunTimeError("僅支援日線");
        value1 = getField("外資交易買進金額");
        value2 = getField("外資交易賣出金額");
        value3 = value1 - value2;
        plot1(value1,"外資交易買進金額");
        plot2(value2,"外資交易賣出金額");
        plot3(value3,"外資交易淨額");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資期權動態(df: pd.DataFrame, length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 外資期權動態
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\外資期權動態.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        value1=GetField("外資交易買口");
        value2=GetField("外資交易賣口");
        value3=GetField("外資買方未平倉口數");
        value4=GetField("外資賣方未平倉口數");
        value5=value1-value2;//外資今日淨買賣口數
        plot1(value5,"外資今日淨買賣口數");
        plot2(average(value5,length),"移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 委買委賣張數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 委買委賣張數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\委買委賣張數.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："口數差 = 委買口數 - 委賣口數"
        支援商品：大盤/期貨/選擇權}
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        if condition994 then begin//大盤
        	value1 = GetField("累計委買");
        	value2 = GetField("累計委賣");
        	value3 = GetField("累計委買") - GetField("累計委賣");
        	plot1(value3,"委買委賣口數差");
        	plot2(value1,"委買口數",checkbox:=0);
        	plot3(value2,"委賣口數",checkbox:=0);
        	setplotlabel(1,"委買委賣張數差");
        	setplotlabel(2,"委買張數");
        	setplotlabel(3,"委賣張數");
        end else begin//期貨與選擇權
        	value1 = GetField("累計委買");
        	value2 = GetField("累計委賣");
        	value3 = GetField("累計委買") - GetField("累計委賣");
        	plot1(value3,"委買委賣口數差");
        	plot2(value1,"委買口數",checkbox:=0);
        	plot3(value2,"委賣口數",checkbox:=0);
        	setplotlabel(1,"委買委賣口數差");
        	setplotlabel(2,"委買口數");
        	setplotlabel(3,"委賣口數");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 委買委賣筆數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 委買委賣筆數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\委買委賣筆數.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義：(委買)筆數 = 交易所資料(開盤到目前累計(委買)筆數)
        for 大盤,  委買委賣資料不含權證, 多一個成交筆數
        支援商品：大盤/期貨/選擇權}
        condition994 = symbol = "TSE.TW" or symbol = "TWSE.FS" or symbol = "OTC.TW";//大盤
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        if condition994 then begin//大盤
        	value1 = GetField("累委買筆");
        	value2 = GetField("累委賣筆");
        	value3 = GetField("累委買筆") - GetField("累委賣筆");
        	value4 = GetField("累成交筆");
        	plot1(value3,"委買委賣筆數差");
        	plot2(value1,"委買筆數",checkbox:=0);
        	plot3(value2,"委賣筆數",checkbox:=0);
        	plot4(value4,"累成交筆");
        end else begin//期貨與選擇權
        	value1 = GetField("累委買筆");
        	value2 = GetField("累委賣筆");
        	value3 = GetField("累委買筆") - GetField("累委賣筆");
        	plot1(value3,"委買委賣筆數差");
        	plot2(value1,"委買筆數",checkbox:=0);
        	plot3(value2,"委賣筆數",checkbox:=0);
        	noplot(4);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信交易金額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投信交易金額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\投信交易金額.xs
        XS Logic Reference:
        {@type:indicator}
        if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
        if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
        if barFreq<>"d" then raiseRunTimeError("僅支援日線");
        value1 = getField("投信交易買進金額");
        value2 = getField("投信交易賣出金額");
        value3 = value1 - value2;
        plot1(value1,"投信交易買進金額");
        plot2(value2,"投信交易賣出金額");
        plot3(value3,"投信交易淨額");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 摩台近月未平倉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 摩台近月未平倉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\摩台近月未平倉.xs
        XS Logic Reference:
        {@type:indicator}
        value1 = getsymbolfield("STW*1.SG","未平倉");
        plot1(value1,"摩台近月未平倉");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 期貨散戶多空比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 期貨散戶多空比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\期貨散戶多空比.xs
        XS Logic Reference:
        {@type:indicator}
        OI_all = getsymbolfield("FITX*1.TF","未平倉","D") 
        	+ getsymbolfield("FITX*2.TF","未平倉","D")
        	+ getsymbolfield("FIMTX*1.TF","未平倉","D") * 0.25 
        	+ getsymbolfield("FIMTX*2.TF","未平倉","D") * 0.25;
        OI_small_bull = OI_all - getsymbolfield("FITX*1.TF","十大交易人未沖銷買口","D");
        OI_small_bear = OI_all - getsymbolfield("FITX*1.TF","十大交易人未沖銷賣口","D");
        if OI_small_bull + OI_small_bear = 0 then
        	OI_small_ratio = 0
        else
        	OI_small_ratio = 100 * OI_small_bull / (OI_small_bull + OI_small_bear) - 50;
        plot1(OI_small_ratio,"散戶");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 溢價率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 溢價率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\溢價率.xs
        XS Logic Reference:
        {@type:indicator}
        if symboltype <> 5 then 
        	raiseruntimeerror("僅支援選擇權");
        vRatio = 100 * (
        iff(leftstr(getsymbolinfo("買賣權"),1)="C",1,-1) * (getsymbolinfo("履約價") - getsymbolfield("Underlying","收盤價")) + close)
        /getsymbolfield("Underlying","收盤價");
        plot1(vRatio,"溢價率%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商交易金額(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 自營商交易金額
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\自營商交易金額.xs
        XS Logic Reference:
        {@type:indicator}
        if symbolType<>3 and symbolType<>5 then raiseRunTimeError("僅支援期權");
        if SymbolExchange <> "TF" then raiseRunTimeError("僅支援台灣市場");
        if barFreq<>"d" then raiseRunTimeError("僅支援日線");
        value1 = getField("自營商交易買進金額");
        value2 = getField("自營商交易賣出金額");
        value3 = value1 - value2;
        plot1(value1,"自營商交易買進金額");
        plot2(value2,"自營商交易賣出金額");
        plot3(value3,"自營商交易淨額");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 買賣成交筆數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 買賣成交筆數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\買賣成交筆數.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："委買委賣成筆差 = 委賣成交筆數 - 委買成交筆數"
        支援商品：期貨/選擇權}
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        value1 = GetField("累買成筆");
        value2 = GetField("累賣成筆");
        value3 = GetField("累賣成筆") - GetField("累買成筆");
        plot1(value3,"委買委賣成筆差");
        plot2(value1,"委買成筆",checkbox:=0);
        plot3(value2,"委賣成筆",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 選擇權理論價(df: pd.DataFrame, iRate100: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 選擇權理論價
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\選擇權理論價.xs
        XS Logic Reference:
        {@type:indicator}
        	iRate100(2,"無風險利率%"),
        	iHV(20,"標的歷史波動率計算期間");
        if symboltype <> 5 then 
        	raiseruntimeerror("僅支援選擇權");
        if iHV > 0 then 
        	vVolity100 = HVolatility(getsymbolfield("Underlying","收盤價","D"),iHV)
        else 
        	vVolity100 = 20;
        vStrikePrice = getsymbolinfo("履約價");
        vTTMdays = DateDiff(GetSymbolInfo("到期日"), Date) + 1;
        value1 = bsprice(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("Underlying","收盤價"),vStrikePrice,vTTMdays,iRate100,0,vVolity100);
        plot1(value1,"理論價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 隱含波動率(df: pd.DataFrame, iRate100: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 隱含波動率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\期權指標\隱含波動率.xs
        XS Logic Reference:
        {@type:indicator}
        	iRate100(2,"無風險利率%");
        if symboltype <> 5 then 
        	raiseruntimeerror("僅支援選擇權");
        vStrikePrice = getsymbolinfo("履約價");
        vTTMdays = DateDiff(GetSymbolInfo("到期日"), Date) + 1;
        value1 = ivolatility(leftstr(getsymbolinfo("買賣權"),1),getsymbolfield("Underlying","收盤價"),vStrikePrice,vTTMdays,iRate100,0,c);
        plot1(value1,"隱含波動率%");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
