# Auto-generated strategies for: 警示/長線投資
import pandas as pd
import numpy as np

class 長線投資Strategies:

    @staticmethod
    def 多頭趨勢已然確立(df: pd.DataFrame, CountMonth: int = 6, LSP: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 多頭趨勢已然確立
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\長線投資\多頭趨勢已然確立.xs
        XS Logic Reference:
        {@type:sensor}
        if  CurrentDate < DateAdd(Date,"M",CountMonth) then begin
        	pHigh = maxlist(h,pHigh);
        	pLow = minlist(l,pLow);
        end else begin
        	pHigh = C;
        	pLow = C;
        end;
        value1= pHigh-(pHigh-pLow)*LSP/100;
        if close>value1 
        and close[1]<value1[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後的定存股標的(df: pd.DataFrame, Length: int = 200, percent: float = 38.2) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後的定存股標的
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\長線投資\大跌後的定存股標的.xs
        XS Logic Reference:
        {@type:sensor}
        if close < highest(high,Length)*(1- percent/100) then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 獲利穩定的公司來到市值低位區(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 獲利穩定的公司來到市值低位區
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\長線投資\獲利穩定的公司來到市值低位區.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(700);
        if getsymbolfield("tse.tw","收盤價") > average(getsymbolfield("tse.tw","收盤價"),10) then begin
        	value4=GetField("總市值");
        	value5=average(value4,600);
        	if value4[1]<value5[1]*0.7
        	and close=highest(close,10)
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
