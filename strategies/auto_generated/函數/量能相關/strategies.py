# Auto-generated strategies for: 函數/量能相關
import pandas as pd
import numpy as np

class 量能相關Strategies:

    @staticmethod
    def DiffBidAskVolumeLxL(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: DiffBidAskVolumeLxL
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\量能相關\DiffBidAskVolumeLxL.xs
        XS Logic Reference:
        {@type:function}
        {
        	DiffBidAskVolumeLxL為近15分鐘大戶買賣超的函數，
        	該函數運算出來的數值，與XS指標的「流動大戶買賣力」指標相同。
        }
        array:_ArrayLarge[15](0),_ArraySmall[15](0);
        if barfreq <> "Min" or barinterval <> 1 then 
        	raiseruntimeerror("僅支援 1 分鐘頻率");
        //初始化
        if getfieldDate("Date") <> getfieldDate("Date")[1] then begin
        	_Count = 0;
        	Array_SetValRange(_ArrayLarge, 1, 15, 0);
        	Array_SetValRange(_ArraySmall, 1, 15, 0);
        	value3 = 0;
        	value99 = 0;
        end else begin
        	_Count += 1;
        end;
        value99 = mod(_count,15) + 1;
        _ArrayLarge[value99] = GetField("買進大單量", "1") + GetField("買進特大單量", "1");
        _ArraySmall[value99] = GetField("賣出大單量", "1") + GetField("賣出特大單量", "1");
        value1 = Array_Sum(_ArrayLarge, 1, 15);
        value2 = Array_Sum(_ArraySmall, 1, 15);
        DiffBidAskVolumeLxL = value1 - value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DiffBidAskVolumeXL(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: DiffBidAskVolumeXL
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\量能相關\DiffBidAskVolumeXL.xs
        XS Logic Reference:
        {@type:function}
        {
        	DiffBidAskVolumeXL為近15分鐘特大單買賣超的函數。
        	計算方式為「近15分鐘累計的買進特大單量－賣出特大單量」
        }
        array:_ArrayLarge[15](0),_ArraySmall[15](0);
        if barfreq <> "Min" or barinterval <> 1 then 
        	raiseruntimeerror("僅支援 1 分鐘頻率");
        //初始化
        if getfieldDate("Date") <> getfieldDate("Date")[1] then begin
        	_Count = 0;
        	Array_SetValRange(_ArrayLarge, 1, 15, 0);
        	Array_SetValRange(_ArraySmall, 1, 15, 0);
        	value3 = 0;
        	value99 = 0;
        end else begin
        	_Count += 1;
        end;
        value99 = mod(_count,15) + 1;
        _ArrayLarge[value99] = GetField("買進特大單量", "1");
        _ArraySmall[value99] = GetField("賣出特大單量", "1");
        value1 = Array_Sum(_ArrayLarge, 1, 15);
        value2 = Array_Sum(_ArraySmall, 1, 15);
        DiffBidAskVolumeXL = value1 - value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DiffTradeVolumeAtAskBid(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: DiffTradeVolumeAtAskBid
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\量能相關\DiffTradeVolumeAtAskBid.xs
        XS Logic Reference:
        {@type:function}
        {
        	DiffTradeVolumeAtAskBid為分時買賣力的函數，
        	該函數運算出來的數值，與XS指標的「分時買賣力」指標相同。
        }
        value1 = GetField("外盤量");
        value2 = GetField("內盤量");
        DiffTradeVolumeAtAskBid = value1 - value2;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def DiffUpDownVolume(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: DiffUpDownVolume
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\函數\量能相關\DiffUpDownVolume.xs
        XS Logic Reference:
        {@type:function}
        {
        	DiffUpDownVolume為分時漲跌成交量的函數，
        	該函數運算出來的數值，與XS指標的「分時漲跌成交量」指標相同。
        }
        DiffUpDownVolume = GetField("上漲量") - GetField("下跌量");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
