# Auto-generated strategies for: 指標/財報指標/基本面指標
import pandas as pd
import numpy as np

class 基本面指標Strategies:

    @staticmethod
    def strategy_10年EPS預估之10倍本益比線(df: pd.DataFrame, _setalign: int = 0, pe: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 10年EPS預估之10倍本益比線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\10年EPS預估之10倍本益比線.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        _EPSSum1 = 0;
        _count1 = 0;
        for value1 = 0 to 10 begin
            if CheckField("每股稅後淨利(元)", "Y")[value1] then begin
        	    _EPSSum1 += getField("每股稅後淨利(元)", "Y")[value1];
        		_count1 += 1;
        		//print(currentBar, date, getFielddate("每股稅後淨利(元)", "Y")[value1], getField("每股稅後淨利(元)", "Y")[value1]);
        		end;
        	if _count1 = 10 then break;
        	end;
        _EPSSum2 = 0;
        _count2 = 0;
        for value1 = 0 to 5 begin
            if CheckField("每股稅後淨利(元)", "Q")[value1] then begin 
        	    _EPSSum2 += getField("每股稅後淨利(元)", "Q")[value1];
        		_count2 += 1;
        		print(currentBar, date, getFielddate("每股稅後淨利(元)", "Q")[value1], getFielddate("每股稅後淨利(元)", "Q")[value1]);
        		end;
        	if _count2 = 4 then break;
        	end;
        if _count1 > 0 then value3=((_EPSSum1 / _count1)+_EPSSum2)/2;
        value4=value3*pe;
        plot1(value4,"10倍長期PE線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PB倍數線(df: pd.DataFrame, _setalign: int = 0, ratio1: float = 0.8, ratio2: int = 1, ratio3: float = 1.2, ratio4: float = 1.5, ratio5: float = 1.8) -> tuple[bool, str]:
        """
        Original Strategy: PB倍數線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\PB倍數線.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1 = getField("每股淨值(元)", "Q", default := value1[1]);
        if value1 <> 0 then value2 = close / value1;
        plot1(value2*ratio1, "0.8倍");
        plot2(value2*ratio2, "1.0倍");
        plot3(value2*ratio3, "1.2倍");
        plot4(value2*ratio4, "1.5倍");
        plot5(value2*ratio5, "1.8倍");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 員工人數(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 員工人數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\員工人數.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1 = getField("員工人數", "Q", default:=value1[1]);
        plot1(value1,"員工人數");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 季營收年增率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 季營收年增率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\季營收年增率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        if checkfield("營業收入淨額", "Q")[4] and checkField("營業收入淨額", "Q") and getField("營業收入淨額", "Q")[4] <> 0 then 
            value1 = 100 * (getField("營業收入淨額", "Q") - getField("營業收入淨額", "Q")[4]) / getField("營業收入淨額", "Q")[4];
        plot1(value1, "季營收年增率");
        value2 = getField("營業收入淨額", "Q", default := value2[1]);
        plot2(value2, "季營收(百萬)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 年營收年增率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 年營收年增率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\年營收年增率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        if CheckField("營業收入淨額", "Y") and CheckField("營業收入淨額", "Y")[1] and getField("營業收入淨額", "Y")[1] <> 0 then begin
            value1 = (getField("營業收入淨額", "Y") - getField("營業收入淨額", "Y")[1]) / getField("營業收入淨額", "Y")[1] * 100;
        	end;
        plot1(value1, "年營收年增率");
        value2=getField("營業收入淨額", "Y", default := value2[1]);
        plot2(value2,"年營收(百萬)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 應收帳款週轉率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 應收帳款週轉率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\應收帳款週轉率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("應收帳款週轉率(次)", "Q", default:= value1[1]);
        plot1(value1,"應收帳款週轉率(次)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收年增率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 月營收年增率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\月營收年增率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("月營收年增率", "M", default := value1[1]);
        plot1(value1,"月營收年增率");
        value2 = getfield("月營收", "M", default:= value2[1]);
        plot2(value2*100, "月營收(百萬)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收長期移動平均線(df: pd.DataFrame, _setalign: int = 0, period: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 月營收長期移動平均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\月營收長期移動平均線.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        _sum = 0;
        _count = 0;
        for value1 = 0 to (period + 5) begin
            if CheckField("月營收年增率", "M")[value1] then begin
        	    _sum += getField("月營收年增率", "M")[value1];
        		_count += 1;
        		end;
        	if _count = period then break;
        	end;
        if _count > 0 then value1 = _sum / _count;
        plot1(value1, "月營收年增率移動平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 殖利率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 殖利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\殖利率.xs
        XS Logic Reference:
        {@type:indicator}
        value1=getField("殖利率", "D", default := value1[1]);
        plot1(value1,"殖利率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 每股淨值(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 每股淨值
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\每股淨值.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("每股淨值(元)", "Q", default := value1[1]);
        plot1(value1,"每股淨值(元)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 每股營收(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 每股營收
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\每股營收.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        _sum = 0;
        _count = 0;
        for value1 = 0 to 17 begin
            if checkfield("月營收", "M")[value1] then begin
        	    _sum += getField("月營收", "M")[value1];
        		_count += 1;
        		end;
        	if _count = 12 then break;
        	end;
        value2 = getField("普通股股本", "Q", default:= 0);
        if value2 <> 0 then value3 = _sum / value2 * 10;
        plot1(value3, "每股營收(元)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流動比率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 流動比率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\流動比率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("流動比率", "Q", default := value1[1]);
        plot1(value1,"流動比率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營業利益率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 營業利益率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\營業利益率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("營業利益率", "Q", default := value1[1]);
        plot1(value1,"營業利益率");
        if checkfield("營業利益率", "Q")[4] and checkField("營業利益率", "Q") and getField("營業利益率", "Q")[4] <> 0 then 
            value2 = 100 * (getField("營業利益率", "Q") - getField("營業利益率", "Q")[4]) / getField("營業利益率", "Q")[4];
        plot2(value2, "營業利益率年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營業毛利率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 營業毛利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\營業毛利率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("營業毛利率", "Q", default := value1[1]);
        plot1(value1,"營業毛利率");
        if checkfield("營業毛利率", "Q")[4] and checkField("營業毛利率", "Q") and getField("營業毛利率", "Q")[4] <> 0 then 
            value2 = 100 * (getField("營業毛利率", "Q") - getField("營業毛利率", "Q")[4]) / getField("營業毛利率", "Q")[4];
        plot2(value2, "營業毛利率年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盈轉佔股本比重(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 盈轉佔股本比重
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\盈轉佔股本比重.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("盈餘轉增資佔股本比重", "Y", default:=value1[1]);
        plot1(value1,"盈餘轉增資佔股本比重" );
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 研發費用(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 研發費用
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\研發費用.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("研發費用", "Q", default:=value1[1]);
        value2=getField("研發費用率", "Q", default:=value2[1]);
        plot1(value1,"研發費用(百萬)");
        plot2(value2,"研發費用率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 稅前淨利率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 稅前淨利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\稅前淨利率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("稅前淨利率", "Q", default := value1[1]);
        plot1(value1,"稅前淨利率");
        if checkfield("稅前淨利率", "Q")[4] and checkField("稅前淨利率", "Q") and getField("稅前淨利率", "Q")[4] <> 0 then 
            value2 = 100 * (getField("稅前淨利率", "Q") - getField("稅前淨利率", "Q")[4]) / getField("稅前淨利率", "Q")[4];
        plot2(value2, "稅前淨利率年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 稅後淨利率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 稅後淨利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\稅後淨利率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("稅後淨利率", "Q", default := value1[1]);
        plot1(value1,"稅後淨利率");
        if checkfield("稅後淨利率", "Q")[4] and checkField("稅後淨利率", "Q") and getField("稅後淨利率", "Q")[4] <> 0 then 
            value2 = 100 * (getField("稅後淨利率", "Q") - getField("稅後淨利率", "Q")[4]) / getField("稅後淨利率", "Q")[4];
        plot2(value2, "稅後淨利率年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自由現金流量(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 自由現金流量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\自由現金流量.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        _sum1 = 0;
        _count1 = 0;
        _sum2 = 0;
        _count2 = 0;
        for value1 = 0 to 5 begin
            if checkField("自由現金流量", "Q")[value1] then begin
        	    _sum1 += getField("自由現金流量", "Q")[value1];
        		_count1 += 1;
        		end;
        	if _count1 = 4 then break;
        	end;
        for value1 = 0 to 5 begin
        	if checkField("自由現金流量營收比", "Q")[value1] then begin
        	    _sum2 += getField("自由現金流量營收比", "Q")[value1];
        		_count2 += 1;
        		end;
        	if _count2 = 4 then break;
        	end;
        if _count1 <> 0 then value2 = _sum1 / _count1;
        if _count2 <> 0 then value3 = _sum2 / _count2;
        plot1(value2,"自由現金流量(百萬)");
        plot2(value3,"自由現金流量營收比");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 行銷費用(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 行銷費用
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\行銷費用.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("推銷費用", "Q", default := value1[1]);
        value2=getField("銷售費用比", "Q", default := value2[1]);
        plot1(value1,"推銷費用(百萬)");
        plot2(value2,"銷售費用比");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 資本支出長期走勢(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 資本支出長期走勢
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\資本支出長期走勢.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        _sum = 0;
        _count = 0;
        for value1 = 0 to 5 begin
            if checkField("資本支出金額", "Q")[value1] then begin
        	    _sum += getField("資本支出金額", "Q")[value1];
        		_count += 1;
        		end;
        	if _count = 4 then break;
        	end;
        plot1(_sum, "資本支出(百萬)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 速動比率(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 速動比率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\速動比率.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1=getField("速動比率", "Q", default := value1[1]);
        plot1(value1,"速動比率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 預收款(df: pd.DataFrame, _setalign: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 預收款
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\財報指標\基本面指標\預收款.xs
        XS Logic Reference:
        {@type:indicator}
        setalign("營收財報", _setalign);
        value1 = GetField("預收款項", "Q", default:= value1[1]);
        if checkfield("預收款項", "Q") and checkfield("預收款項", "Q")[4] and GetField("預收款項", "Q")[4] <> 0 then 
            value2 = (GetField("預收款項", "Q") - GetField("預收款項", "Q")[4]) / GetField("預收款項", "Q")[4];
        plot1(value1,"預收款(百萬)");
        plot2(value2,"預收款年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
