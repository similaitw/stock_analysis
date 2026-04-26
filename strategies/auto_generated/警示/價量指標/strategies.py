# Auto-generated strategies for: 警示/價量指標
import pandas as pd
import numpy as np

class 價量指標Strategies:

    @staticmethod
    def 今日高點回跌(df: pd.DataFrame, HighBound: int = 2, Reaction: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 今日高點回跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\今日高點回跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if GetField("High", "D") > GetField("RefPrice", "D")*(1+0.01*HighBound) and
           Close <=  GetField("High", "D")*(1-0.01*Reaction) then
           ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價創近期新低量創新高(df: pd.DataFrame, Price: str = "close", Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 價創近期新低量創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\價創近期新低量創新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  Price < lowest(low[1] ,Length) and 
            volume > highest(volume[1],length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價量同創近期新低(df: pd.DataFrame, Price: str = "close", Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 價量同創近期新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\價量同創近期新低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  Price < lowest(low[1] ,Length) and 
            volume < lowest(volume[1],length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價量同創近期新高(df: pd.DataFrame, Price: str = "close", Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 價量同創近期新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\價量同創近期新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  Price > highest(high[1] ,Length) and 
            volume > highest(volume[1],length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 即將漲停(df: pd.DataFrame, Percent: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 即將漲停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\即將漲停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if close > GetField("漲停價", "D")*(1-Percent/100) then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 即將跌停(df: pd.DataFrame, Percent: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 即將跌停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\即將跌停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if close < GetField("跌停價", "D")*(1+Percent/100) then ret =1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多方人氣表態(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多方人氣表態
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\多方人氣表態.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if Close > highD(1) and GetField("Volume", "D")>  GetField("Volume", "D")[1] then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量上影線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量上影線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\帶量上影線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if high - maxlist(open,close) > absvalue(open-close)*2 and
            Volume > maxlist(volume[1],volume[2],volume[3]) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量下影線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量下影線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\帶量下影線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if minlist(open,close) - low > absvalue(open-close)*2 and
            Volume > Maxlist(volume[1],volume[2],volume[3]) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 成交量突破N倍均量(df: pd.DataFrame, length: int = 20, VolumeXtime: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 成交量突破N倍均量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\成交量突破N倍均量.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if volume > Average( volume[1],length)* VolumeXtime then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 成交量突破均量(df: pd.DataFrame, length: int = 20, confirmVolume: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 成交量突破均量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\成交量突破均量.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if volume > Average( volume[1],length) +confirmVolume then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 步步高升(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 步步高升
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\步步高升.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if volume > volume[1]     and 
           volume[1] > volume[2]  and
           close > close[1]       and   
           close[1] > close[2]    and 
           close > open and 
           close[1] > open[1] and 
           close[2] > open[2]
        then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲停回頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 漲停回頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\漲停回頭.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If Close[1] = GetField("漲停價", "D") And q_Last < GetField("漲停價", "D") Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲停鎖住(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 漲停鎖住
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\漲停鎖住.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If Close = GetField("漲停價", "D") And q_AskSize <=0 Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 爆量長紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 爆量長紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\爆量長紅.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if volume >  Average(volume[1],5)  *3    and 
         ( close - open ) >( high -low ) * 0.75  and 
           close > open + (high[1]- low[1])
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 爆量長黑(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 爆量長黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\爆量長黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if volume >  Average(volume[1],5)  *3    and 
         ( open - close ) >( high -low ) * 0.75  and 
           open > close  + (high[1]- low[1])
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日時段區間價突破(df: pd.DataFrame, initialtime: int = 090000, timeline: int = 100000, CloseAtHigh: str = "false", TXT1: str = "限用分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 當日時段區間價突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日時段區間價突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(50);
        if barfreq<> "Min" then return;
        if date <> date[1] then  intervalhigh = 0; 
        if time >= initialtime and time <= timeline then 
        begin
          intervalhigh = maxlist(high,intervalhigh);
        end;
        if time > timeline then
        begin
          if CloseAtHigh then  
            Ret = IFF(close > intervalhigh, 1, 0)
          else  
            Ret = IFF(high > intervalhigh, 1, 0); 
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日時段區間價跌破(df: pd.DataFrame, initialtime: int = 090000, timeline: int = 100000, CloseAtLow: str = "false", TXT1: str = "限用分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 當日時段區間價跌破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日時段區間價跌破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(50);
        if barfreq<> "Min" then return;
        if date <> date[1] then intervallow = 99999999;
        if time >= initialtime and time <= timeline then 
        begin
          intervallow = minlist(low,intervallow);
        end;
        if time >timeline then
        begin
          if CloseAtLow  then  
        	Ret = IFF(close < intervallow, 1, 0)
          else  
        	Ret = IFF(low < intervallow, 1, 0);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日漲幅預警(df: pd.DataFrame, AlertChangeRatio: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 當日漲幅預警
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日漲幅預警.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If q_PriceChangeRatio > AlertChangeRatio Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日跌幅預警(df: pd.DataFrame, AlertChangeRatio: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 當日跌幅預警
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日跌幅預警.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If q_PriceChangeRatio < AlertChangeRatio*-1 Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日量突破(df: pd.DataFrame, initialtime: int = 090000, timeline: int = 100000) -> tuple[bool, str]:
        """
        Original Strategy: 當日量突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日量突破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(50);
        if date <> date[1] then  intervalhighv =0 ; 
        if time >= initialtime and time <= timeline then
        begin 
           intervalhighv = maxlist(volume,intervalhighv ); 
           keyprice =close;
        end;
        if volume > intervalhighv and time >timeline and
           close > keyprice  and close>=open then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日量跌破(df: pd.DataFrame, initialtime: int = 090000, timeline: int = 100000) -> tuple[bool, str]:
        """
        Original Strategy: 當日量跌破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日量跌破.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(50);
        if date <> date[1] then  intervalhighv =0 ; 
        if time >= initialtime and time <= timeline then
        begin 
           intervalhighv = maxlist(volume,intervalhighv ); 
           keyprice =close;
        end;
        if volume > intervalhighv and time >timeline and
           close < keyprice  and close>=open then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日開盤跳空開低(df: pd.DataFrame, UseQuote: str = "True", Gap: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 當日開盤跳空開低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日開盤跳空開低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if UseQuote then 
        	Ret = IFF(100*(GetField("RefPrice", "D") -GetField("Open", "D")) > GetField("RefPrice", "D")*Gap, 1, 0)
        else 
        	Ret = IFF(date <> date[1] and 100*(close[1] -open) > close[1]*Gap, 1, 0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日開盤跳空開高(df: pd.DataFrame, UseQuote: str = "True", Gap: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 當日開盤跳空開高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當日開盤跳空開高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if UseQuote then 
        	Ret = IFF(100*(GetField("Open", "D") -GetField("RefPrice", "D")) > GetField("RefPrice", "D")*Gap, 1, 0)
        else 
        	Ret = IFF(date <> date[1] and 100*(open - close[1]) > close[1]*Gap, 1, 0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當期成交量倍增(df: pd.DataFrame, VolumeXtime: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 當期成交量倍增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\當期成交量倍增.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if volume > volume[1] * VolumeXtime then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭部隊進攻(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭部隊進攻
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\空頭部隊進攻.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(25);
        if low < lowD(1) and GetField("Volume", "D")>  GetField("Volume", "D")[1]  then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價創近期新低(df: pd.DataFrame, Price: str = "close", Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價創近期新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\股價創近期新低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  Price < Lowest(Low[1] ,Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價創近期新高(df: pd.DataFrame, Price: str = "close", Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 股價創近期新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\股價創近期新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  Price > highest(high[1] ,Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌停回頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 跌停回頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\跌停回頭.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If Close[1] = GetField("跌停價", "D") And Close> GetField("跌停價", "D") Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌停鎖住(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 跌停鎖住
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\跌停鎖住.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        If Close = GetField("跌停價", "D") And q_bidsize <=0 Then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌跌不休(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 跌跌不休
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\跌跌不休.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        if volume > volume[1]     and 
           volume[1] > volume[2]  and
           close < close[1]       and   
           close[1] < close[2]    and 
           close < open and 
           close[1] < open[1] and 
           close[2] < open[2]
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續期間上漲(df: pd.DataFrame, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 連續期間上漲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\連續期間上漲.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        If TrueAll(Close > Close[1],Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續期間下跌(df: pd.DataFrame, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 連續期間下跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\連續期間下跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        If TrueAll(Close < Close[1],Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開高帶量走低(df: pd.DataFrame, AmountThre: int = 2000) -> tuple[bool, str]:
        """
        Original Strategy: 開高帶量走低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\價量指標\開高帶量走低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(25);
        if Date > XDate then
          begin
        	XDate = Date;
        	initialAmount = (High+low)/2 * volume/10; //計算K棒成交金額
        	if Open > Close[1] and
               (open - close) > (high -low) * 0.75 and 
        	   initialAmount > AmountThre then ret = 1;
          end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
