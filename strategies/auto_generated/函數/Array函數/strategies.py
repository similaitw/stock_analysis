# Auto-generated strategies for: 函數/Array函數
import pandas as pd
import numpy as np

class Array函數Strategies:

    @staticmethod
    def ArrayLinearRegSlope(df: pd.DataFrame, Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: ArrayLinearRegSlope
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\Array函數\ArrayLinearRegSlope.xs
        XS Logic Reference:
        {@type:function}
        {
        	傳入Array來計算LinearRegression的Slope
        	最新一期的資料放在ThePriceArray[1]
        }
        if DataLength < Length then RaiseRunTimeError("Array的長度不能小於Length");
              SumX2(0), //平方和
              SumY(0),
              SumXY(0);
        SumX = Length * (Length+1)/2;
        SumX2 = Length * (Length+1)*(2*Length+1)/6;
        SumXY=0; SumY=0;
        for Xi = 1 to Length
        Begin
           SumXY += Xi* ThePriceArray[Length-Xi+1];
           SumY  += ThePriceArray[Length-Xi+1];
        End;
        retval = IFF((Length*SumX2 - Square(SumX)) <> 0,
                     (Length*SumXY - SumX*SumY) / (Length*SumX2 - Square(SumX)),
        			 0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ArrayMASeries(df: pd.DataFrame, TheSeries: str = "numericseries", MALength: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: ArrayMASeries
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\Array函數\ArrayMASeries.xs
        XS Logic Reference:
        {@type:function}
        {
        	把某個數值序列的MA轉成Array
        	範例:
        	Array: MAArray[](0);
        	ArrayMASeries(Close, 10, MAArray);
            // Array_GetMaxIndex(MAArray) = 10	
        	// MAArray[1] = MA(Close, 10), 
        	// MAArray[2] = MA(Close[1], 10),
        	// MAArray[3] = MA(Close[2], 10),
        	// ...
        }
        Array_SetMaxIndex(TargetArray, MALength);
        acc = 0;
        for idx = 0 to MALength-1 begin
        	acc = acc + TheSeries[idx];
        end;
        for idx = 0 to MALength-1 begin
        	TargetArray[idx+1] = acc / MALength;
        	acc = acc - TheSeries[idx];
        	acc = acc + TheSeries[MALength + idx];
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ArraySeries(df: pd.DataFrame, TheSeries: str = "numericseries", Length: str = "numericsimple") -> tuple[bool, str]:
        """
        Original Strategy: ArraySeries
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\Array函數\ArraySeries.xs
        XS Logic Reference:
        {@type:function}
        {
        	把某個數值序列轉成Array
        	範例:
        	Array: CloseArray[](0);
        	ArraySeries(Close, 10, CloseArray);
            // Array_GetMaxIndex(CloseArray) = 10	
        	// CloseArray[1] = Close, CloseArray[2] = Close[1], CloseArray[3] = Close[2], ..
        }
        Array_SetMaxIndex(TargetArray, Length);
        for idx = 0 to Length - 1 begin
        	TargetArray[idx+1] = TheSeries[idx];
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ArrayXDaySeries(df: pd.DataFrame, TheSeries: str = "numericseries", SBB_length: str = "NumericSimple") -> tuple[bool, str]:
        """
        Original Strategy: ArrayXDaySeries
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\Array函數\ArrayXDaySeries.xs
        XS Logic Reference:
        {@type:function}
        {
        	以Array儲存跨頻率的序列值，傳入一個序列
        	範例:
        	Array: CloseArray[](0);
        	ArrayXDaySeries(GetField("收盤價","D"),SBB_length,_DayValue);
        }
        _length = GetBarBack("D");
        _xf_CurrentBar = xf_GetCurrentBar("D");
        if _length < SBB_length then raiseRunTimeError("新上市櫃商品資料引用筆數不足，所以不允計算");
        if currentBar = 1 then begin
        	Array_SetMaxIndex(TargetArray, _length);
        	for idx = 0 to _length - 1 begin
        		TargetArray[idx + 1] = TheSeries[idx];
        	end;
        end else begin
        	if _xf_CurrentBar > _xf_CurrentBar[1] then begin
        		Array_Copy(TargetArray, 1, TargetArray, 2, _length - 1);
        	end;
        	TargetArray[1] = TheSeries[0];
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
