# Auto-generated strategies for: 選股/01.常用過濾條件
import pandas as pd
import numpy as np

class Cat01常用過濾條件Strategies:

    @staticmethod
    def 股本篩選(df: pd.DataFrame, MinCapital: int = 10, MaxCapital: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 股本篩選
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\股本篩選.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Value1 = GetField("最新股本");
        // 介於兩者之間
        Ret = Value1 >= MinCapital and Value1 <= MaxCapital;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股票名稱不含F股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 股票名稱不含F股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\股票名稱不含F股.xs
        XS Logic Reference:
        {@type:filter}
        sn=symbolname;
        if instr(sn,"F")=0
        and instr(sn,"Y")=0 then ret=1;
        outputfield(1,sn,0,"symbolname");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過濾低價股票(df: pd.DataFrame, PriceLimit: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 過濾低價股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\過濾低價股票.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Ret = close > PriceLimit;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過濾低成交量股票(df: pd.DataFrame, Length: int = 5, VolumeLimit: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 過濾低成交量股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\過濾低成交量股票.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Value1 = Average(volume, Length);
        Ret = Value1 > VolumeLimit;
        SetOutputName1("成交均量");
        OutputField1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過濾冷門股票(df: pd.DataFrame, PriceLimit: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 過濾冷門股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\過濾冷門股票.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Value1 = Average(volume,Length);
        if close > PriceLimit and Value1 > VolumeLimit Then
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過濾小型股票(df: pd.DataFrame, MinCapital: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 過濾小型股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\過濾小型股票.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Ret = GetField("最新股本") > MinCapital;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過濾沒賺錢的股票(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 過濾沒賺錢的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\01.常用過濾條件\過濾沒賺錢的股票.xs
        XS Logic Reference:
        {@type:filter}
        // 過去四季每股盈餘加總必須 > 0
        //
        SetTotalbar(3);
        Value1 = summation(GetField("EPS","Q"), 4);
        Ret = Value1 > 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
