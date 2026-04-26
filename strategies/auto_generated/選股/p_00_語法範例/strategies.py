# Auto-generated strategies for: 選股/00.語法範例
import pandas as pd
import numpy as np

class Cat00語法範例Strategies:

    @staticmethod
    def EPS連續N季成長(df: pd.DataFrame, N: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N季成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N季成長.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS","Q") > GetField("EPS","Q")[1],N) then ret=1; 
        SetOutputName1("EPS(元)(季)"); 
        OutputField1(GetField("EPS","Q")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EPS連續N季衰退(df: pd.DataFrame, N: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N季衰退
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N季衰退.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS","Q") < GetField("EPS","Q")[1],N) then ret=1; 
        SetOutputName1("EPS(元)(季)"); 
        OutputField1(GetField("EPS","Q")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EPS連續N季都大於X元(df: pd.DataFrame, N: int = 4, X: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N季都大於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N季都大於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS", "Q") > X,N) then ret=1; 
        SetOutputName1("EPS(元)(季)"); 
        OutputField1(GetField("EPS", "Q")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EPS連續N季都小於X元(df: pd.DataFrame, N: int = 4, X: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N季都小於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N季都小於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS", "Q") < X,N) then ret=1; 
        SetOutputName1("EPS(元)(季)"); 
        OutputField1(GetField("EPS", "Q")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EPS連續N年都大於X元(df: pd.DataFrame, N: int = 4, X: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N年都大於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N年都大於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS", "Y") > X,N) then ret=1; 
        SetOutputName1("EPS(元)(年)"); 
        OutputField1(GetField("EPS", "Y")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EPS連續N年都小於X元(df: pd.DataFrame, N: int = 4, X: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: EPS連續N年都小於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\EPS連續N年都小於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if TrueAll(GetField("EPS", "Y") < X,N) then ret=1; 
        SetOutputName1("EPS(元)(年)"); 
        OutputField1(GetField("EPS", "Y")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N期股價趨勢向上(df: pd.DataFrame, Period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: N期股價趨勢向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\N期股價趨勢向上.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        Condition1 = rateofchange(close, period) >= Period;
        Condition2 = close > close[Period/2];
        Condition3 = close > average(close, period);
        ret = condition1 and condition2 and condition3;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N期股價趨勢向下(df: pd.DataFrame, Period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: N期股價趨勢向下
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\N期股價趨勢向下.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        Condition1 = rateofchange(close, period) <= -1 * Period;
        Condition2 = close < close[Period/2];
        Condition3 = close < average(close, period);
        ret = condition1 and condition2 and condition3;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def _基本範例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: _基本範例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\_基本範例.xs
        XS Logic Reference:
        {@type:filter}
        // 選股範例程式
        //
        // 使用GetField來取得欄位的數值。請按F7或從「編輯」|「插入欄位」選項內啟動插入欄位的畫面。
        // GetField函數的第一個參數是欄位名稱，例如 "每股稅後淨利(元)"，
        // GetField函數的第二個參數是欄位的期別，例如 "Q"代表季資料，"M"代表月資料,"Y"代表年資料。
        //
        Value1 = GetField("每股稅後淨利(元)","Q");
        // 如果GetField函數的第二個參數省略的話，則系統會根據執行這個腳本時所設定的頻率來決定
        // 資料的期別。請務必注意引用腳本時必須設定正確的頻率，否則可能會遇到執行錯誤的情形。
        //
        Value2 = GetField("每股稅後淨利(元)");
        // 可以使用任何XSScript的語法來做運算，如果股票符合預期的話請設定Ret = 1，以下面一行為例
        // 這個腳本會選到最新一年每股稅後淨利 > 5元的股票
        //
        Ret = GetField("每股稅後淨利(元)","Y") > 5;
        // ＊＊　在這個目錄內有更多的程式範本可以參考　＊＊
        //
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 收盤價近N期漲幅大於X_以上(df: pd.DataFrame, N: int = 10, X: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 收盤價近N期漲幅大於X%以上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\收盤價近N期漲幅大於X%以上.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        Value1 = RateOfChange(GetField("收盤價"),N);
        if Value1 > X then ret=1;
        SetOutputName1("近期漲幅%"); 
        OutputField1(Value1); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 收盤價近N期跌幅大於X_以上(df: pd.DataFrame, N: int = 10, X: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 收盤價近N期跌幅大於X%以上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\收盤價近N期跌幅大於X%以上.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        Value1 = RateOfChange(GetField("收盤價"),N);
        if Value1 < -1 * X then ret=1;
        SetOutputName1("近期跌幅%"); 
        OutputField1(Value1); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最近4季EPS合計大於X元(df: pd.DataFrame, X: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 最近4季EPS合計大於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\最近4季EPS合計大於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        Value1 = Summation(GetField("EPS","Q"),N);
        if Value1 > X then ret=1; 
        SetOutputName1("EPS合計"); 
        OutputField1(Value1); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最近4季EPS合計小於X元(df: pd.DataFrame, X: int = 0) -> tuple[bool, str]:
        """
        Original Strategy: 最近4季EPS合計小於X元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\最近4季EPS合計小於X元.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        Value1 = Summation(GetField("EPS","Q"),N);
        if Value1 < X then ret=1; 
        SetOutputName1("EPS合計"); 
        OutputField1(Value1); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收創N期新低(df: pd.DataFrame, N: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: 月營收創N期新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\月營收創N期新低.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if GetField("月營收", "M") <= Lowest(GetField("月營收", "M"),N) then ret=1; 
        SetOutputName1("月營收"); 
        OutputField1(GetField("月營收", "M")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收創N期新高(df: pd.DataFrame, N: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: 月營收創N期新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\月營收創N期新高.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3); 
        if GetField("月營收", "M") >= Highest(GetField("月營收", "M"),N) then ret=1; 
        SetOutputName1("月營收"); 
        OutputField1(GetField("月營收", "M")); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本益比小於X倍(df: pd.DataFrame, X: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 本益比小於X倍
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\本益比小於X倍.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        Value1 = GetField("本益比", "D");
        if Value1 < X then Ret = 1;
        SetOutputName1("本益比(倍)");
        outputfield1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價大於近N期平均(df: pd.DataFrame, N: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價大於近N期平均
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\股價大於近N期平均.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Value1 = Average(GetField("Close"),N);
        if GetField("Close") > Average(GetField("Close"),N) then ret=1; 
        SetOutputName1("均價");
        outputfield1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價小於近N期平均(df: pd.DataFrame, N: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價小於近N期平均
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\股價小於近N期平均.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        Value1 = Average(GetField("Close"),N);
        if GetField("Close") < Value1 then ret=1; 
        SetOutputName1("均價");
        outputfield1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週轉率大於X_(df: pd.DataFrame, X: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 週轉率大於X%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\00.語法範例\週轉率大於X%.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        Value1 = GetField("週轉率","D");
        if Value1 > X then Ret = 1;
        SetOutputName1("週轉率%");
        outputfield1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
