# Auto-generated strategies for: 警示/ETF策略
import pandas as pd
import numpy as np

class Etf策略Strategies:

    @staticmethod
    def BBand翻多(df: pd.DataFrame, Length: int = 20, Up: int = 1, Down: int = 1, Threshold: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: BBand翻多
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\BBand翻多.xs
        XS Logic Reference:
        {@type:sensor}
        up1 = bollingerband(Close, Length, absvalue(Up));
        down1 = bollingerband(Close, Length, -1 * absvalue(Down));
        mid1 = (up1 + down1) / 2;
        bbandwidth = 100 * (up1 - down1) / mid1;
        if bbandwidth crosses above Threshold then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ETF乖離反轉作多買進訊號(df: pd.DataFrame, Length: int = 20, Ratio: int = 21) -> tuple[bool, str]:
        """
        Original Strategy: ETF乖離反轉作多買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\ETF乖離反轉作多買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        if close/average(close,Length)<= 1-Ratio/100 then KPrice = H;
        if Close crosses over KPrice
        then ret=1 ;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KO買進訊號(df: pd.DataFrame, Length1: int = 34, Length2: int = 55) -> tuple[bool, str]:
        """
        Original Strategy: KO買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\KO買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        ko = callfunction("KO成交量擺盪指標", Length1, Length2);
        value1=average(ko,3);
        value2=average(ko,13);
        if value1 crosses over value2
        and linearregangle(close,5)>20
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def KST趨勢確認策略(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: KST趨勢確認策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\KST趨勢確認策略.xs
        XS Logic Reference:
        {@type:sensor}
        kst=callfunction("KST確認指標");
        if kst crosses over -50 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def OBV買進訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: OBV買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\OBV買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        if CurrentBar = 1 then
        	obvolume = 0
        else begin	
        	if close > close[1] then
        		obvolume = obvolume[1] + volume
        	else begin
        		if close < close[1] then
        			obvolume = obvolume[1] - volume
        		else
        			obvolume = obvolume[1];
        	end;		
        end;
        value1=average(obvolume,20);
        if obvolume crosses over value1*1.3 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def Q指標買進訊號(df: pd.DataFrame, t1: int = 10, t2: int = 5, t3: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: Q指標買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\Q指標買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        Qindicator=callfunction("Q指標",t1,t2,t3);
        if linearregangle(Qindicator,5)>40
        and barslast(linearregangle(Qindicator,5)>45)[1]>20
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三下影線反轉直上買進訊號(df: pd.DataFrame, Percent: float = 0.5) -> tuple[bool, str]:
        """
        Original Strategy: 三下影線反轉直上買進訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\三下影線反轉直上買進訊號.xs
        XS Logic Reference:
        {@type:sensor}
        condition1 = (minlist(open,close)-Low) > absvalue(open-close)*2; 
        condition2 =  minlist(open, close)  > low* (100 + Percent)/100;
        if trueall( condition1 and condition2, 3) then begin
        	OCDate = Date;
        	Kprice = average(H,3);
        end;
        if DateDiff(Date,OCDate) <3 and Close crosses over Kprice then ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 中長線均線糾結後突破(df: pd.DataFrame, Shortlength: int = 10, Midlength: int = 20, Longlength: int = 40, Percent: int = 2, Volpercent: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 中長線均線糾結後突破
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\中長線均線糾結後突破.xs
        XS Logic Reference:
        {@type:sensor}
        if volume > average(volume,Longlength) * (1 + volpercent * 0.01) and volume > 1000 then
        begin
        	shortaverage = average(close,Shortlength);
        	midaverage = average(close,Midlength);
        	Longaverage = average(close,Longlength);
        	value2=  maxlist(shortaverage,midaverage,Longaverage );
        	value3=  minlist(shortaverage,midaverage,Longaverage );
        	if close crosses over value2
        	and (value2-value3)*100 < Percent*close 
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 基金投資大跌後的止跌訊號(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 基金投資大跌後的止跌訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\基金投資大跌後的止跌訊號.xs
        XS Logic Reference:
        {@type:sensor}
        if (open[2] - close[2] ) > (high[2] -low[2]) * 0.75
        //前前期出黑K棒
        and close[2] < close[3]-(high[3]-low[3])
        //跌勢擴大
        and ( close - open ) > (high -low) * 0.75
        //當期收紅K棒
        and close> close[2]					
        //收復黑棒收盤價
        and close[1] <= close[2] and close[1] < open
        //前低收盤為三期低點
        and close[40] > close[1]*1.05
        //近四十日跌幅超過5%
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大盤MFI多頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大盤MFI多頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\大盤MFI多頭.xs
        XS Logic Reference:
        {@type:sensor}
        if TSEMFI=1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大碗底(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大碗底
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\大碗底.xs
        XS Logic Reference:
        {@type:sensor}
        value1=lowestbar(low,100);
        value2=lowest(low,100);
        value3=highestbar(high,100);
        value4=highest(high,100);
        if value4>value2*1.15
        and value3-value1>15
        then begin
        	if value1>15
        	and value2*1.05>close[1]
        	and close>close[1]*1.01
        	and volume>average(volume[1],15)*1.2
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌三成之後(df: pd.DataFrame, n: int = 30, period: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 大跌三成之後
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\大跌三成之後.xs
        XS Logic Reference:
        {@type:sensor}
        if close*(1+n/100) < close[period-1] then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後均線黃金交叉(df: pd.DataFrame, Length1: int = 5, Length2: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後均線黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\大跌後均線黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        value1=highest(high,100);
        if value1 > close*1.2
        and average(close,Length1) crosses over average(close,Length2)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大跌後的價量背離(df: pd.DataFrame, period: int = 10, times: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 大跌後的價量背離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\大跌後的價量背離.xs
        XS Logic Reference:
        {@type:sensor}
        if close[1]*1.2<close[40] //大跌
        and countif(c>c[1] xor v>v[1],period) >= times //價漲量縮、價跌量增
        and close=highest(close,period) //收近期最高
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月KD高檔鈍化且日KD黃金交叉(df: pd.DataFrame, Length_D: int = 9, Length_M: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 月KD高檔鈍化且日KD黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\月KD高檔鈍化且日KD黃金交叉.xs
        XS Logic Reference:
        {@type:sensor}
        stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        xf_stochastic("M", Length_M, 3, 3, rsv_m, kk_m, dd_m);
        if xf_getvalue("M", kk_m, 1) >= 85 and kk_d crosses over dd_d then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 烏龜進場法則(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 烏龜進場法則
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\烏龜進場法則.xs
        XS Logic Reference:
        {@type:sensor}
        if average(close,3) crosses above average(close,55)
        and volume> average(volume,5)
        and atr(3) > atr(20)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 理專DBCD交易法則(df: pd.DataFrame, length1: int = 10, Threshold: str = "-2") -> tuple[bool, str]:
        """
        Original Strategy: 理專DBCD交易法則
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\理專DBCD交易法則.xs
        XS Logic Reference:
        {@type:sensor}
        value1=bias(length1);
        value2=bias(length2);
        value3=value2-value1;
        value4=average(value3,length3);
        if value4 crosses over Threshold
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 理專之雙KD向上(df: pd.DataFrame, Length_D: int = 9, Length_W: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 理專之雙KD向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\理專之雙KD向上.xs
        XS Logic Reference:
        {@type:sensor}
        stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        xf_stochastic("W", Length_W, 3, 3, rsv_w, kk_w, dd_w);
        condition1 = kk_d crosses above dd_d;		// 日KD crosses over
        condition2 = xf_GetBoolean("W",xf_crossover("W", kk_w, dd_w),1);	// 周KD crosses over
        condition3 = kk_d <= 30;							// 日K 低檔
        condition4 = xf_getvalue("W", kk_w, 1) <= 50;		// 周K 低檔
        ret = condition1 and condition2 and condition3 and condition4;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 趨勢翻多(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 趨勢翻多
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\趨勢翻多.xs
        XS Logic Reference:
        {@type:sensor}
        LinearReg(close, Length, 0, value1, value2, value3, value4);
        //做收盤價20天線性回歸
        //value1:斜率、value4:預期值
        value5=rsquare(close,value4,20);//算收盤價與線性回歸值的R平方
        if value1>0 and value1[1]<0 and value5>0.2 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週線二連紅之後(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 週線二連紅之後
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\週線二連紅之後.xs
        XS Logic Reference:
        {@type:sensor}
        if rateofchange(close,2)[1]>0 
        and rateofchange(close,2)[2]>0
        and close<close[2]*1.07
        and close[10]>close*1.15
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週線反轉法則(df: pd.DataFrame, rate1: int = 5, rate2: int = 3, TXT: str = "僅適用日線") -> tuple[bool, str]:
        """
        Original Strategy: 週線反轉法則
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\ETF策略\週線反轉法則.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(20);
        if getfield("high","W")[2]>=getfield("close","W")[3]*(1+rate1/100) 
        and low < getfield("close","W")[1]*(1-rate2/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
