# Auto-generated strategies for: 函數/邏輯判斷
import pandas as pd
import numpy as np

class 邏輯判斷Strategies:

    @staticmethod
    def AverageIF(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: AverageIF
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\AverageIF.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
               thePrice(numericseries),
        	   Length(numericsimple);
        variableA = 0;
        Sum = 0;
        for Value1 = 0 to Length - 1
        begin
            if TrueAndFalse[Value1] then 
        	begin 
        		variableA = variableA + 1;
        		Sum = Sum + thePrice[Value1];		
        	end;	
        end;
        if variableA > 0 then
          AverageIf = Sum/variableA
        else 
          AverageIf = 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CountIF(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: CountIF
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\CountIF.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        variableA = 0;
        for Value1 = 0 to Length - 1
        begin
        	if TrueAndFalse[Value1] then 	
        		variableA = variableA + 1;
        end;
        CountIf = variableA;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CountIfARow(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: CountIfARow
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\CountIfARow.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        CountIfARow = truecount(TrueAndFalse,Length);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CrossOver(df: pd.DataFrame, SeriesA: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: CrossOver
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\CrossOver.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0), idx(0);
        CrossOver  = false;
        posA = 0;
        posB = 0;
        valA = SeriesA[posA];
        valB = SeriesB[posB];
        if valA <= valB then 
        	CrossOver = false
        else begin
        	for idx = 1 to minlist(6, currentbar)
        	begin
        		posA = posA + 1;
        		posB = posB + 1;
        		valA = SeriesA[posA];
        		valB = SeriesB[posB];
        		if valA < valB then
        		begin
        			CrossOver = true;
        			break;
        		end
        		else
        		begin
        			if valA > valB then
        			begin
        				CrossOver = false;
        				break;
        			end;
        		end; 
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CrossUnder(df: pd.DataFrame, SeriesA: str = "numericseries") -> tuple[bool, str]:
        """
        Original Strategy: CrossUnder
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\CrossUnder.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        	SeriesA(numericseries),
        	SeriesB(numericseries);
        	valA(0), valB(0), posA(0), posB(0), idx(0);
        CrossUnder  = false;
        posA = 0;
        posB = 0;
        valA = SeriesA[posA];
        valB = SeriesB[posB];
        if valA >= valB then 
        	CrossUnder = false
        else begin
        	for idx = 1 to minlist(6, currentbar)
        	begin
        		posA = posA + 1;
        		posB = posB + 1;
        		valA = SeriesA[posA];
        		valB = SeriesB[posB];
        		if valA > valB then
        		begin
        			CrossUnder = true;
        			break;
        		end
        		else
        		begin
        			if valA < valB then
        			begin
        				CrossUnder = false;
        				break;
        			end;
        		end; 
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Filter(df: pd.DataFrame, pX: str = "TrueFalseSimple") -> tuple[bool, str]:
        """
        Original Strategy: Filter
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\Filter.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(2);
        If pX Then begin
        	If vCounter < pLength Then begin
        			vCounter = vCounter + 1;
        			Filter = False;
        	end Else begin
        			vCounter = 0;
        			Filter = True;
        	End;
        end Else begin
        	vCounter = vCounter + 1;
        	Filter = False;
        End;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def IFF(df: pd.DataFrame, Logicoperator: str = "truefalsesimple") -> tuple[bool, str]:
        """
        Original Strategy: IFF
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\IFF.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
               TrueReturnV(numericsimple),
               FalseReturnV(numericsimple);
        if Logicoperator then IFF = TrueReturnV
        else IFF = FalseReturnV;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def IsXLOrder(df: pd.DataFrame, pv: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: IsXLOrder
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\IsXLOrder.xs
        XS Logic Reference:
        {@type:function_bool}
        {
        	判斷成交金額是否是特大單
        	級距表請參考:
        	https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/	
        }
        if _last_date <> Date then begin
        	_last_date = Date;
        	_open_price = GetField("Open", "D");
        	if _open_price < 30 then 
        		_threshold = 800000
        	else if _open_price < 50 then 
        		_threshold = 1000000
        	else if _open_price < 100 then 
        		_threshold = 1200000
        	else if _open_price < 200 then 
        		_threshold = 2000000
        	else if _open_price < 500 then 
        		_threshold = 4000000
        	else
        		_threshold = 4000000;
        end;
        if pv > _threshold then retval = true else retval = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def IsXOrder(df: pd.DataFrame, pv: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: IsXOrder
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\IsXOrder.xs
        XS Logic Reference:
        {@type:function_bool}
        {
        	判斷成交金額是否是大單(大單+特大單)
        	級距表請參考:
        	https://www.xq.com.tw/%e5%8f%b0%e8%82%a1%e9%80%90%e7%ad%86%e5%8a%9f%e8%83%bd%e8%a1%8c%e6%83%85%e7%ab%af%e7%9b%b8%e9%97%9c%e7%95%b0%e5%8b%95/	
        }
        if _last_date <> Date then begin
        	_last_date = Date;
        	_open_price = GetField("Open", "D");
        	if _open_price < 30 then 
        		_threshold = 400000
        	else if _open_price < 50 then 
        		_threshold = 500000
        	else if _open_price < 100 then 
        		_threshold = 700000
        	else if _open_price < 200 then 
        		_threshold = 1200000
        	else if _open_price < 500 then 
        		_threshold = 2000000
        	else
        		_threshold = 2500000;
        end;
        if pv > _threshold then retval = true else retval = false;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SummationIF(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: SummationIF
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\SummationIF.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        _Output = 0;
        for Value1 = 0 to Length - 1
        begin
            if TrueAndFalse[Value1] then _Output = _Output + thePrice[Value1];
        end;
        SummationIf = _Output;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TrueAll(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: TrueAll
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\TrueAll.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        TrueAll = True;
        for Value1 = 0 to Length - 1
        begin
            if TrueAndFalse[Value1] = False then
            begin
                TrueAll = False;
                break;
            end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TrueAny(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: TrueAny
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\TrueAny.xs
        XS Logic Reference:
        {@type:function_bool}
        SetBarMode(1);
        TrueAny = False;
        for Value1 = 0 to Length - 1
        begin
            if TrueAndFalse[Value1] then
            begin
                TrueAny = True;
                break;
            end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TrueCount(df: pd.DataFrame, TrueAndFalse: str = "truefalseseries") -> tuple[bool, str]:
        """
        Original Strategy: TrueCount
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\邏輯判斷\TrueCount.xs
        XS Logic Reference:
        {@type:function}
        SetBarMode(1);
        value2 = 0;
        for Value1 = 0 to Length - 1
        begin
            if TrueAndFalse[Value1] = true then
                value2 = value2 +1
            else
             begin
                break;
             end;
        end;
        TrueCount = value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
