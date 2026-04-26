# Auto-generated strategies for: 警示/3.出場常用警示
import pandas as pd
import numpy as np

class Cat3出場常用警示Strategies:

    @staticmethod
    def DMI賣出訊號(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: DMI賣出訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\DMI賣出訊號.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Length,6) * 13 + 8);
        DirectionMovement(Length, pdi, ndi, adx_value);
        if pdi<pdi[1] and ndi>ndi[1] and ndi crosses over pdi
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KD高檔死亡交叉(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: KD高檔死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\KD高檔死亡交叉.xs
        XS Logic Reference:
        {@type:sensor}
        SetTotalBar(maxlist(Length,6) * 3 + 8);
        Stochastic(Length, RSVt, Kt, rsv, k, _d);
        if k>HighBound and k crosses under _d
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MACD出現賣出訊號(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: MACD出現賣出訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\MACD出現賣出訊號.xs
        XS Logic Reference:
        {@type:sensor}
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 8);
        MACD(weightedclose(), FastLength, SlowLength, MACDLength, difValue, macdValue, oscValue);
        Ret = oscValue Crosses Below 0;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MTM轉負(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: MTM轉負
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\MTM轉負.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Length,6) + 8);
        if momentum(close,Length) crosses under 0 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def OBV退潮(df: pd.DataFrame, Length: int = 15) -> tuple[bool, str]:
        """
        Original Strategy: OBV退潮
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\OBV退潮.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(10);
        value1 = close-close[1];
        if close<> close[1] then 
           OBVolume +=  Volume*(value1)/absvalue(value1);
         if close<highest(high,Length) and
            OBVolume[2]=highest(OBVolume,Length) and 
        	OBVolume=lowest(OBVolume,3)
         then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def RSI高檔死亡交叉(df: pd.DataFrame, Length1: int = 6, Length2: int = 12, HighBound: int = 75) -> tuple[bool, str]:
        """
        Original Strategy: RSI高檔死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\RSI高檔死亡交叉.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(maxlist(Length1,Length2,6) * 8 + 8);
        value1=RSI(close,Length1);
        value2=RSI(close,Length2);
        if value1 crosses under value2 and value1>HighBound
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 一舉跌破多根均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 一舉跌破多根均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\一舉跌破多根均線.xs
        XS Logic Reference:
        {@type:sensor}
        setbarback(maxlist(shortlength,midlength,Longlength,6)+8);
        shortaverage = Average(close,shortlength);
        midaverage = Average(close,midlength) ;
        Longaverage = Average(close,Longlength); 
        if close  crosses under  shortaverage and 
           close  crosses under  midaverage and 
           close  crosses under  Longaverage 
        then ret=1;  
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 一黑破n紅(df: pd.DataFrame, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 一黑破n紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\一黑破n紅.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if high=highest(high[1],Length) and close<lowest(low[1],Length) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三長上影線(df: pd.DataFrame, Percent: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 三長上影線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\三長上影線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        condition1 = (high- maxlist(open,close)) > absvalue(open-close)*3; 
        condition2 = high > maxlist(open, close) * (100 + Percent)/100;
        if trueall( condition1 and condition2, 3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力出貨_(df: pd.DataFrame, RatioThre: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 主力出貨 
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\主力出貨 .xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        if date[1] <> date then 
        begin 
              downvolume  =0; upvolume =0;
        	  uprange =0; downrange=0;
              if close > open then  
        	    begin 
        	      upvolume = volume; 
        		  uprange = close -open;   
        		end
              else 
        	  if close < open then  
        		begin 
        		  downvolume = volume;  
        		  downrange = open -close; 
        		end
        	  else 
        	  if close < close[1] then  
        	    begin 
        		  downvolume = volume;  
        		  downrange = close[1] -close; 
        	    end
        	  else 
        	  if close > close[1] then  
        	    begin 
        		  upvolume = volume; 
        		  uprange = close -close[1]; 
        	    end;
        end;//如果前一個跟Bar跟目前的bar日期不同 今天第一根起算
        if date[1] = date then  //還在同一天
        begin 
              if close > close[1] then  
        	    begin 
        	      upvolume += volume; 
        		  uprange += close -close[1];   
        		end
              else 
        	  if close < close[1] then  
        	    begin 
        		  downvolume += volume;  
        		  downrange += close[1] -close; 
        	    end;
         if upvolume > 0 then DUratio = downvolume/upvolume else DUratio=1;
        end;
        if DUratio crosses over RatioThre and uprange crosses under downrange then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 主力賣超(df: pd.DataFrame, PastDays: int = 3, summ: int = 2000, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 主力賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\主力賣超.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(PastDays + 3);
        if Barfreq = "D" and close< close[1] and
           summation(GetField("LeaderDifference")[1],PastDays) <= summ*-1 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 乖離過大(df: pd.DataFrame, Length: int = 200, Ratio: int = 70) -> tuple[bool, str]:
        """
        Original Strategy: 乖離過大
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\乖離過大.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if close/average(close,Length)>= 1+Ratio/100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘線九連黑(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘線九連黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\分鐘線九連黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if Barfreq ="Min" then 
           if trueall(close < open,Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多日價量背離(df: pd.DataFrame, Length: int = 5, times: int = 3, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 多日價量背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\多日價量背離.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        count = CountIf(close > close[1] and volume < volume[1], Length);
        if count > times then 
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大黑棒(df: pd.DataFrame, Percent: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 大黑棒
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\大黑棒.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if open/close >= 1 + Percent/100  //實體(開盤-收盤)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 天價留上影線後未開高(df: pd.DataFrame, Length: int = 20, P1: int = 2, P2: float = 0.5, P3: float = 0.5, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 天價留上影線後未開高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\天價留上影線後未開高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(Length);
        if  open - close[1] <P2/100*close[1]  and
            high[1]=highest(high,Length)  and 
        	(high[1]-close[1])>= P1/100 *close[1] and
        	high[1] > maxlist(open[1], close[1]) *(1+P3/100)
        then  ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 天量後價量未再創新高(df: pd.DataFrame, XLength: int = 60, Length: int = 3, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 天量後價量未再創新高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\天量後價量未再創新高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(XLength + 3);
        extremes(high,Length,1,value1,PriceHighBar);
        extremes(volume,XLength,1,value1,VolumeHighBar);
        if (PriceHighBar =Length-1) and VolumeHighBar=Length-1  then
        ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 川上三鴉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 川上三鴉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\川上三鴉.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if TrueAll((open-close) > (high-low) * 0.5 and close <close[1],3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 巨量長黑(df: pd.DataFrame, Amount: int = 10000) -> tuple[bool, str]:
        """
        Original Strategy: 巨量長黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\巨量長黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if open > Close * 1.025//實體 
        and close[1] > Close * 1.035 //較前一日大跌
        and volume >=amount 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信外資都賣超(df: pd.DataFrame, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 投信外資都賣超
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\投信外資都賣超.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if Barfreq <> "D" then return;
        if Open < Close[1] and  Close < Close[1] and
           GetField("外資買賣超")[1]<0 and GetField("投信買賣超")[1]<0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買單比例太高且走低(df: pd.DataFrame, ratio: int = 20, TXT: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 散戶買單比例太高且走低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\散戶買單比例太高且走低.xs
        XS Logic Reference:
        {@type:sensor}
        //單筆外盤成交值低於五十萬元稱為散單 //內外盤:內盤-1 外盤1
        settotalbar(3);
        if barfreq ="Min" and currentdate = date then //分鐘線在今天時
        begin
          TimeStamp =currenttime;
          if TimeStamp = TimeStamp[1] then  ACount=0;
          if TimeStamp[1] <= time  then // 盤中開啟 or 換Bar第一個進價
          begin
              if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then
                    ACount = GetField("Volume", "Tick") *Close
         	    else 
        	        ACount=0;
          end
          else
          begin
             if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then ACount+= GetField("Volume", "Tick") *Close;
          end;
          if ACount >= Ratio/100 * volume*close and  
             Close < GetField("RefPrice", "D")*0.985 and GetField("High", "D") < GetField("RefPrice", "D")*1.005 then ret=1;
        end;
        if barfreq ="D" then 
        begin
          if  Date <> currentdate then Acount=0;
          if  GetField("內外盤","Tick") > 0 and GetField("Volume", "Tick") *Close <=500 then ACount+= GetField("Volume", "Tick") *Close;
          if ACount >= Ratio/100 * GetField("Volume", "D") * GetField("均價") and
             Close < GetField("RefPrice", "D")*0.985 and GetField("High", "D") < GetField("RefPrice", "D")*1.005 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 海龜出場法則(df: pd.DataFrame, Length: int = 10, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 海龜出場法則
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\海龜出場法則.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar((Length + 3)*5);
        if barfreq <> "D" and barfreq <> "AD" then Return;
        if close < lowest(getfield("low","W")[1],Length)//近n週最低價
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤中直線下跌(df: pd.DataFrame, SlopeThre: int = 2, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 盤中直線下跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\盤中直線下跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if date<>date[1] then begin KBarOfDay=1; tOpen =Open; end;
        if Length < KBarOfDay and currentbar > maxbarsback and
           Linearregslope(Low/tOpen*1000,Length) < SlopeThre*-1 then 
        ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 竭盡缺口(df: pd.DataFrame, Length: int = 50, Ratio: int = 30, OpenGapRatio: int = 2, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 竭盡缺口
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\竭盡缺口.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if close / lowest(close,Length) >= 1+Ratio/100//區間漲幅夠大
        and open[1]>close[2] //前一日已跳空
        and open/close[1] >= 1+OpenGapRatio/100    //今天又跳空
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價跌破走平後的高壓電線(df: pd.DataFrame, Ratio: int = 10, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 股價跌破走平後的高壓電線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\股價跌破走平後的高壓電線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 8);
        setbarback(72);
        if absvalue(linearregslope(avgprice[1]*Factor,Length))<=0.1 and  //走平
           close crosses under ((average(close,30)+average(close,72))/2 )* (1+Ratio*0.01) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價震盪變大且收最低(df: pd.DataFrame, Length: int = 5, BaseLength: int = 20, Ratio: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 股價震盪變大且收最低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\股價震盪變大且收最低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(8);
        setbackbar(maxlist(Length,BaseLength));
        value1=highest(high,Length)-lowest(low,Length);
        value2=average(value1,BaseLength);
        if	value1 crosses over value2 *(1+ratio/100) and close=low
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 資增券減還收黑(df: pd.DataFrame, V1: int = 1000, V2: int = 500, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 資增券減還收黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\資增券減還收黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if BarFreq <> "D" then return;
        if close < close[1] and 
           GetField("融資增減張數")[1] > V1 and
           GetField("融券增減張數")[1] < V2*-1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌破n日低點(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 跌破n日低點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\跌破n日低點.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if close  < lowest(low[1],Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌破上升趨勢線(df: pd.DataFrame, Length: int = 10, _Angle: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 跌破上升趨勢線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\跌破上升趨勢線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if Close< Close[1] and Close[1] <Close[2] and Close[Length]>0 then begin
        linearreg((high/Close[Length]-1)*100,Length,0,value1,TrendAngle,value3,value4);
        TrendAngleDelta =TrendAngle-TrendAngle[1];
        IF TrendAngleDelta-TrendAngleDelta[1] < -10 and close >Close[Length] THEN RET=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌破均線(df: pd.DataFrame, shortlength: int = 5, midlength: int = 10, Longlength: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 跌破均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\跌破均線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(shortlength,midlength,Longlength));
        shortaverage=Average(close,shortlength);
        midaverage=Average(close,midlength) ;
        Longaverage = Average(close,Longlength); 
        if open > maxlist(shortaverage, midaverage, longaverage) and
           close < minlist(shortaverage, midaverage, longaverage)
        then ret=1;        
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跳空下跌再破底(df: pd.DataFrame, Gapratio: float = 1.5, TXT: str = "僅適用分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 跳空下跌再破底
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\跳空下跌再破底.xs
        XS Logic Reference:
        {@type:sensor}
        //分鐘線
        settotalbar(5);
        if barfreq<>"Min" then return;
        if Close < close[1] and Close < GetField("Open", "D") then 
           if GetField("Open", "D") < GetField("RefPrice", "D")*(100-Gapratio)/100  then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連續n日開高走低收最低(df: pd.DataFrame, Length: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 連續n日開高走低收最低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\連續n日開高走低收最低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if Trueall( Open > Close[1]*1.005 and Close<open and close = low , Length) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 階梯式下跌(df: pd.DataFrame, TXT: str = "5分鐘線以下") -> tuple[bool, str]:
        """
        Original Strategy: 階梯式下跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\階梯式下跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(13);
        if barfreq<> "Min" or barinterval > 5 then return;
        switch (barinterval)
        begin
           case 1,2,5:
             if time =091000 and TrueAll(open=high and close=low and close< close[1],10/barinterval) then ret=1;
             break;
           case 3:
             if time =090900 and TrueAll(open=high and close=low and close< close[1],3) then ret=1;
             break;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高檔出現吊人線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 高檔出現吊人線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\高檔出現吊人線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(33);
        if Close < Close[1] then begin
        	condition1 = 
        		open = High and close < open and
        	   (high -low) > 2 *(high[1]-low[1]) and 
        	   (close-low) > (open-close) *2;
        	condition2= close[1] > highest(High,30)*0.98; //昨日收盤價接近三十日高點
        	if condition1 and condition2 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高檔出現黑暗之星(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 高檔出現黑暗之星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\高檔出現黑暗之星.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if (open-close)>= open *0.025 then //最近一根是長黑棒
        begin
        	value1 = highest(high,length);
        	value2 = lowest(low,length);
        	if value1 = value2 then return;
        	value3 = (value1-close)/(value1-value2)*100;
        	condition1 = value3 < 10; //接近近n日高點
        	condition2 = (close[2]-open[2])/open[2]>=0.03;//一根長陽線
        	condition3 =  open[1]>close[1]  and (high[1]-low[1])<=close[1]*0.02 
        	and close[1]>close[2] - 0.5*(close[1]-open[1]) ; //一根小黑棒且未形成覆蓋線
        	if condition1 and condition2 and condition3 then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高檔覆蓋線(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 高檔覆蓋線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\高檔覆蓋線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(maxlist(Length,42));
        value1 = PercentR(14) - 100;
        value2 = PercentR(28) - 100;
        value3 = PercentR(42) - 100;
        if  value1= 0 and value2=0 and value3 =0 then //用威廉指標來表示股價在高檔
        begin
        HighPoint = highest(high,length);
        LowPoint = Lowest(Low,length);
        if HighPoint > LowPoint then
         RatioThre=(HighPoint-close)/(HighPoint-LowPoint)*100
        else 
         RatioThre=999;
        if RatioThre<10 and 
           close<open and 
           close[1]>open[1] and 
           close<close[1]-1/2*(close[1]-open[1])
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高檔量縮收黑(df: pd.DataFrame, DownPercent: int = 4, Ratio: int = 20, TieDays: int = 3, UpTrendDays: int = 20, RaisingRatio: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 高檔量縮收黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\高檔量縮收黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        setbarback(UpTrendDays+TieDays);
        if Close[TieDays] >  close[UpTrendDays+TieDays-1] * (1+RaisingRatio/100) then
        begin
          if Close< high[TieDays] * (1 - DownPercent/100) and 
             volume[TieDays] > volume *(1+Ratio/100) 
          then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高檔雙死亡交叉(df: pd.DataFrame, FastLength: int = 12, SlowLength: int = 26, MACDLength: int = 9, Shortlength: int = 5, Longlength: int = 10, Length: int = 20, Ratio: int = 20, ReactRatio: int = 5, TXT: str = "建議使用日線") -> tuple[bool, str]:
        """
        Original Strategy: 高檔雙死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\3.出場常用警示\高檔雙死亡交叉.xs
        XS Logic Reference:
        {@type:sensor}
        //近三天內ma及macd都發生過死亡交叉
        SetTotalBar((maxlist(FastLength,SlowLength,6) + MACDLength) * 3 + 11);
        if close >= lowest(close,Length)* (1+ Ratio/100) and
           close >= (1-ReactRatio/100)*highest(close,Length) then
        begin
        price  = WeightedClose();
        Value1 = XAverage(price, FastLength) - XAverage(price, SlowLength);//DIF
        Value2 = XAverage( Value1, MACDLength ) ;//MACD
        Value3 = Value1 - Value2 ;//OSC
        {===============================================================}
        value4=average(close,5);
        value5=average(close,10);
        value6=value4-value5;
        {===============================================================}
        condition1 = TrueAny( value3 crosses under 0 ,3);
        condition2 = TrueAny( value6 crosses under 0 ,3);
        if condition1 and condition2 
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
