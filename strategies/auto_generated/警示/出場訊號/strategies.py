# Auto-generated strategies for: 警示/出場訊號
import pandas as pd
import numpy as np

class 出場訊號Strategies:

    @staticmethod
    def emprical指標賣出訊號(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: emprical指標賣出訊號
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\出場訊號\emprical指標賣出訊號.xs
        XS Logic Reference:
        {@type:sensor}
        ,avgpeak(0),avgvalley(0);
        price=(h+l)/2;
        //透過Z的時間安排來決定現在用的是那一根Bar的資料 
        if GetFieldDate("主力買賣超張數") <> 0 then
        	Z=0 
        else 
        	Z=1;
        beta=cosine(360/period);
        gamma=1/cosine(720*delta/period);
        alpha=gamma-squareroot(gamma*gamma-1);
        BP=0.5*(1-alpha)*(price-price[2])
        +beta*(1+alpha)*BP[1]-alpha*BP[2];
        mean=average(bp,2*period);
        peak=peak[1];
        valley=valley[1];
        if bp[1]>bp and bp[1]>bp[2] then peak=bp[1];
        if bp[1]<bp and bp[1]<bp[2] then valley=bp[1];
        avgpeak=average(peak,50);
        avgvalley=average(valley,50);
        value1=GetField("主力買賣超張數")[Z];
        if mean crosses under avgpeak 
        and trueall(value1<0,3)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近幾日總是收黑K(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 近幾日總是收黑K
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\出場訊號\近幾日總是收黑K.xs
        XS Logic Reference:
        {@type:sensor}
        if countif(close<open,7)>=5
        //過去七天有五天以上收黑
        and lowest(close,90)*1.4<close
        //過去九十天漲幅超過四成
        and lowest(close,10)*1.2<close
        //過去十天有急拉過
        and volume*1.2<average(volume,20)
        //成交量低於二十日均量的兩成
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤委賣暴增(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 開盤委賣暴增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\出場訊號\開盤委賣暴增.xs
        XS Logic Reference:
        {@type:sensor}
        if close>close[90]*1.3 then begin
        //先前有一定的漲幅
        	value1=GetField("開盤委買","D");
        	value2=GetField("開盤委賣","D");
        	value3=value2-value1;
        	if trueall(absvalue(value3[1])<250,10)
        	//近十日開盤委買與開盤委賣張數差不多
        	and value3>=500
        	//今日開盤委賣比開盤委買多出500張以上
        	and close<close[1]
        	//收盤比前一日下跌
        	and close<low*1.01
        	//收盤接近當日最低價
        	then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
