# Auto-generated strategies for: 警示/1.籌碼監控
import pandas as pd
import numpy as np

class Cat1籌碼監控Strategies:

    @staticmethod
    def 主力切入見真章(df: pd.DataFrame, pastDays: int = 3, UpRatio: float = 3.5, _buyAmount: int = 3000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 主力切入見真章
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\主力切入見真章.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        if BarFreq <> "D" then return;
        if   close > close[1]*(1 + UpRatio/100) then
        begin
        	// 過去N日 主力買賣超的成交金額的總和
            //	
            SumForce = Summation((AvgPrice * GetField("主力買賣超張數")/10)[1], pastDays);
        	if SumForce > _buyAmount  then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力認賠再追賣(df: pd.DataFrame, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 主力認賠再追賣
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\主力認賠再追賣.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(15);
        if BarFreq <> "D" then return;
        if close < lowest(low[1] ,pastDays) and
           volume > volume[1]*0.5 and
           GetField("主力買賣超張數")[1] < average(volume[1],pastDays)/-7 and
           Summation(GetField("主力買賣超張數")[2],pastDays) > Average(volume[2],pastDays)/7
         then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 券增價漲再推升(df: pd.DataFrame, pastDays: int = 10, UpRatio: float = 3.5, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 券增價漲再推升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\券增價漲再推升.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        if BarFreq <> "D" then return;
        if  close > high[1] and close > close[1]*(1 + UpRatio/100) and
        	Getfield("融券餘額張數")[1] = highest(Getfield("融券餘額張數")[1] ,pastDays)  
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資增持收新高(df: pd.DataFrame, pastDays: int = 3, _buyAmount: int = 3000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 外資增持收新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\外資增持收新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        if BarFreq <> "D" then return;
        if close > highest(high[1],pastDays) then 
        begin
        	// 過去N日外資買超金額
            //	
            SumForce = Summation((AvgPrice * GetField("外資買賣超")/10)[1], pastDays);
        	if SumForce > _buyAmount   then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資拉抬上攻(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 25, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 外資拉抬上攻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\外資拉抬上攻.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        if BarFreq <> "D" then return;
        if Close > High[1] then
        begin
        	SumTotalVolume = Summation(volume[1], pastDays);
        	SumForce = Summation(GetField("外資買賣超")[1], pastDays);
        	if SumForce > SumTotalVolume * _BuyRatio / 100 then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資換手再創高(df: pd.DataFrame, Percent: int = 30, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 外資換手再創高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\外資換手再創高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if BarFreq <> "D" then return;
        if close > high[1] and FB-FS > 0 and (FB+FS) > 2 * volume[1] * Percent / 100  then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 實戶潛進終抬頭(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 20, length: int = 20, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 實戶潛進終抬頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\實戶潛進終抬頭.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        MonthLine = average(close[1],length);
        if BarFreq <> "D" then return;
        if Close crosses over MonthLine then
        begin
            counter = summationif(close[1] < MonthLine, 1, pastDays);
        	if counter  = pastDays then 
        	begin
        	// 最近一段時間在月線底下的吃貨量
             	SumForce = summationif(close[1] < MonthLine, GetField("實戶買賣超張數")[1], pastDays);
            	SumTotalVolume = Summationif(close[1] < MonthLine, Volume[1], pastDays);
        	if SumForce > SumTotalVolume * _BuyRatio / 100  then ret =1;
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信加持卻遇襲(df: pd.DataFrame, pastDays: int = 5, _buyAmount: int = 1000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信加持卻遇襲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\投信加持卻遇襲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastdays + 3);
        if BarFreq <> "D" then return;
        if close < lowest(low[1], pastdays) then
        begin
        	sumForce = Summation(GetField("投信買賣超")[1], pastDays);
        	if sumForce > _buyAmount then ret=1;
        end;        
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信存股連拉升(df: pd.DataFrame, HoldRatio: int = 50, Length: int = 25, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信存股連拉升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\投信存股連拉升.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if BarFreq <> "D" then return;
        if  GetField("投信持股比例")[1]> holdratio and
            GetField("投信持股比例")[1]=highest(GetField("投信持股比例")[1], Length) and
            close > close[1] and close[1] > close[2] and close[2] > close[3]
            then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信拉抬上攻(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 25, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信拉抬上攻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\投信拉抬上攻.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastDays + 3);
        if BarFreq <> "D" then return;
        if Close > High[1] then
        begin
        	SumForce = Summation(GetField("投信買賣超")[1], pastDays);
        	sumTotalVolume = Summation(Volume[1], pastDays);
        	if SumForce > SumTotalVolume * _BuyRatio/100 then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶下車股價漲(df: pd.DataFrame, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 散戶下車股價漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\散戶下車股價漲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D" then return;
        if close > high[1] and 
        	GetField("散戶買賣超張數")[1] < volume[1] * -0.1  then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶撿到出貨後創低(df: pd.DataFrame, ChangeKshares: int = 1000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 散戶撿到出貨後創低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\散戶撿到出貨後創低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D" then return;
        if close < low[1] and
        	GetField("主力買賣超張數")[1] < ChangeKshares*-1 and 
        	GetField("散戶買賣超張數")[1] > ChangeKshares
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法人主攻漲升(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 25, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 法人主攻漲升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\法人主攻漲升.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastDays + 3);
        if BarFreq <> "D" then return;
        if Close > High[1] and close[1] > close[2] then
        begin
        	SumForce = Summation(
        		(GetField("外資買賣超")+GetField("自營商買賣超")+GetField("投信買賣超"))[1], 
        		pastDays);
        	SumTotalVolume = Summation(Volume[1], pastDays);
        	if SumForce > SumTotalVolume * _BuyRatio / 100  then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商增持收新高(df: pd.DataFrame, pastDays: int = 3, _buyAmount: int = 3000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 自營商增持收新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\自營商增持收新高.xs
        XS Logic Reference:
        {@type:sensor}
        if BarFreq <> "D" then return;
        if close > highest(high[1],pastDays) then 
        begin
        	SumForce = Summation((AvgPrice * GetField("自營商買賣超")/10)[1], pastDays);
        	if SumForce > _buyAmount   then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商拉抬上攻(df: pd.DataFrame, pastDays: int = 3, _BuyRatio: int = 25, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 自營商拉抬上攻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\自營商拉抬上攻.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastDays + 3);
        if BarFreq <> "D" then return;
        if Close > High[1] then
        begin
        	SumForce = Summation(GetField("自營商買賣超")[1], pastDays);
        	SumTotalVolume = Summation(Volume[1], pastDays);
        	if SumForce > SumTotalVolume * _BuyRatio / 100 then ret =1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資追捧戰新高(df: pd.DataFrame, pastDays: int = 10, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 融資追捧戰新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\融資追捧戰新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(pastDays + 3);
        if BarFreq <> "D" then return;
        if Getfield("融資餘額張數")[1] = highest(Getfield("融資餘額張數")[1] ,pastDays) and
           close >= highest(high[1],pastDays)  
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連日外盤攻擊創新高(df: pd.DataFrame, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 連日外盤攻擊創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\1.籌碼監控\連日外盤攻擊創新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D" then return;
        if Close > maxlist(high[1],high[2]) and GetField("內盤量","D")>0 and GetField("外盤量") > GetField("內盤量","D") * 1.2  then
        begin
        	if TrueAll(Getfield("外盤量")[1] > 1.1 * Getfield("內盤量")[1], 3) then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
