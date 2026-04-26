# Auto-generated strategies for: 函數/排行
import pandas as pd
import numpy as np

class 排行Strategies:

    @staticmethod
    def 乖離率排行榜(df: pd.DataFrame, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 乖離率排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\乖離率排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何針對內建函數的回傳值進行排序
        // 使用者可以自行替換成需要使用的函數
        //
        // Length是期數
        //
        	Length(5, numericsimple, "計算期間");
        retval = bias(Length);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資連續買超排行榜(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 外資連續買超排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\外資連續買超排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何依外資連續N期買超的張數進行排序
        // 使用者可以自行替換成需要使用的欄位
        //
        // Length是期數
        //
        	Length(10, numericsimple, "計算期間");
        if TrueAll(GetField("外資買賣超") > 0, Length) Then
           retval = Summation(GetField("外資買賣超"), Length)
        Else
           return;
        { 
        //如果要排序投信連續買超，可以改用"投信買賣超"的欄位:
        if TrueAll(GetField("投信買賣超") > 0, Length) Then
           retval = Summation(GetField("投信買賣超"), Length)
        Else
           return;
        //如果要排序自營商連續買超，可以改用"自營商買賣超"的欄位:
        if TrueAll(GetField("自營商買賣超") > 0, Length) Then
           retval = Summation(GetField("自營商買賣超"), Length)
        Else
           return;
        //可以依需要自行更換欄位
        }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 收盤價排行榜(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 收盤價排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\收盤價排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何針對特定欄位的數值進行排序
        // 使用者可以自行替換成需要使用的欄位
        //
        //
        retval = GetField("收盤價");
        {
        //同理，當日漲跌幅的排行榜就會是：
        retval = GetField("漲跌幅");
        }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 收盤均價排行榜(df: pd.DataFrame, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 收盤均價排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\收盤均價排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何針對特定欄位的N期平均進行排序
        // 使用者可以自行替換成需要使用的欄位
        //
        // Length是期數
        	Length(3, numericsimple, "計算期間");
        retval = Average(GetField("收盤價"),Length);
        {
        //如果想做均量的排行榜，只需要更換欄位為成交量：
        retval = Average(GetField("成交量"),Length);
        }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲幅排行榜(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 漲幅排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\漲幅排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何針對特定欄位的N期增幅進行排序
        // 使用者可以自行替換成需要使用的欄位
        //
        // Length是期數
        	Length(20, numericsimple, "計算期間");
        retval = rateofchange(GetField("收盤價"),Length);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌幅排行榜(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 跌幅排行榜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\排行\跌幅排行榜.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        // 這是一個自訂排行條件的範例
        // 示範如何針對特定欄位的N期減幅進行排序
        // 使用者可以自行替換成需要使用的欄位
        //
        // Length是期數
        	Length(20, numericsimple, "計算期間");
        retval = -rateofchange(GetField("收盤價"),Length);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
