# Auto-generated strategies for: 選股/10.價值投資
import pandas as pd
import numpy as np

class Cat10價值投資Strategies:

    @staticmethod
    def PB跌到歷年低點區且低於0_8(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: PB跌到歷年低點區且低於0.8
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\PB跌到歷年低點區且低於0.8.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("股價淨值比","Y");
        value2=lowest(value1,4);
        if value1<value2*1.3 and value1<=0.8
        then ret=1;
        outputfield(1, GetField("股價淨值比","Y"),2, "PB比", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低PB股的逆襲(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 低PB股的逆襲
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\低PB股的逆襲.xs
        XS Logic Reference:
        {@type:filter}
        if close<15
        and H = highest(H,20)
        and close<lowest(low,20)*1.07
        and highest(h,40)>close*1.1
        then ret=1;
        outputfield(1, GetField("股價淨值比","D"),2, "PB比", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低本益比低PB高殖利率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 低本益比低PB高殖利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\低本益比低PB高殖利率.xs
        XS Logic Reference:
        {@type:filter}
        {本益比小於 15 倍 股價淨值比小於 2 倍 殖利率大於 3%}
        if GetField("本益比","D") < 10 and
           GetField("股價淨值比","D") <1.5 and
           GetField("殖利率","D") > 3  and
           GetField("營收成長率","Q") >0 
           then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低預估本益比攻勢發動(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 低預估本益比攻勢發動
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\低預估本益比攻勢發動.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收","M");//單位:億元
        value2=GetField("稅後淨利率","Q");
        value3=GetField("最新股本");//單位:億元
        if value3<>0 then
        value6=(value1*value2*12)/(value3*10);//單月營收推估的本業EPS
        if value6<>0 then 
        value7=close/value6;
        value4=GetField("總市值");
        value5=average(GetField("總市值"),600);
        if value4<value5*0.7
        and close=highest(close,10)
        then ret=1;
        outputfield(1,value7,2,"推估本益比", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 價值雪球股(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 價值雪球股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\價值雪球股.xs
        XS Logic Reference:
        {@type:filter}
        if GetField("本益比","D") < 15 and
           GetField("股價淨值比","D") <2 and
           GetField("殖利率","D") > 3  and
           GetField("營收成長率","Q") >0 and
           GetField("營業利益","Q") >GetField("營業利益","Q")[1] and
           C > Lowest(L,255) + (highest(h,255)-Lowest(L,255))*0.5
           then ret=1;
        outputfield(1,GetField("本益比","D"),1,"本益比");
        outputfield(2,GetField("股價淨值比","D"),1,"PB比");
        outputfield(3,GetField("殖利率","D"),2, "殖利率", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 新一代金牌定存股(df: pd.DataFrame, lowlimit: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 新一代金牌定存股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\新一代金牌定存股.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("本期稅後淨利","Y");//單位:百萬
        value2=lowest(value1,5);//五年獲利低點
        value3=average(value1,5);//五年來平均獲利
        if value1/100> lowlimit//獲利超過年度獲利下限
        and value1/100<50//獲利沒有超過五十億元
        and value1>value1[1]*0.9
        and value1[1]>value1[2]*0.9//年度獲利連續兩年未衰退超過一成
        and value2*1.3>value3
        //五年來獲利最差的時候比平均值沒有掉超過三成
        then ret=1;
        outputfield(1, value1/100, 1, "稅後淨利(億)", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收推估出的低本益比股(df: pd.DataFrame, peraito: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 月營收推估出的低本益比股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\月營收推估出的低本益比股.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收","M");//單位:億元
        value3=GetField("本期稅後淨利","Q");//單位百萬
        value4=GetField("營業利益率","Q");
        value5=GetField("最新股本");//單位:億元
        condition1=false;
        condition2=false;
        if value5<>0 then
        value6=(value1*value4*12)/(value5*100)*10;//單月營收推估的本業EPS
        if value6<>0 then 
        value7=close/value6;
        if value7<peraito and value7>0 and value3>200
        then ret=1;
        outputfield(1,value7,0,"推估本益比", order := -1);
        outputfield(2,value6,2,"推估EPS");
        outputfield(3,value1,2,"月營收");
        outputfield(4,value4,2,"營業利益率");
        outputfield(5,value5,2,"最新股本");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本業推估本益比低於N(df: pd.DataFrame, peuplimit: int = 15) -> tuple[bool, str]:
        """
        Original Strategy: 本業推估本益比低於N
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\本業推估本益比低於N.xs
        XS Logic Reference:
        {@type:filter}
        value3= summation(GetField("營業利益","Q"),4); //單位百萬;
        value4= GetField("最新股本");//單位億;
        value5= value3/(value4*10);//每股預估EPS
        if value5>0 and close/value5<=peuplimit
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 每股流動資產遠大於股價(df: pd.DataFrame, percent: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 每股流動資產遠大於股價
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\每股流動資產遠大於股價.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("現金及約當現金","Q");//百萬;
        value2=GetField("短期投資","Q");//百萬
        value3=GetField("應收帳款及票據","Q");//百萬
        value4=GetField("長期投資","Q");//百萬
        value5=GetField("負債總額","Q");//百萬
        value6=GetField("最新股本");//單位: 億
        value7=(value1+value2+value3+value4-value5)/(value6*10);
        if value7>close*(1+percent/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營運現金流量的持續積累(df: pd.DataFrame, ratio: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 營運現金流量的持續積累
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\營運現金流量的持續積累.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("來自營運之現金流量","q");//單位百萬
        value2=GetField("總市值","D");//單位億
        value3=summation(value1,8);//最近八季的營運現金流總和
        value4=value3*5;//以最近兩年來推未來十年營運現金流總和
        nv=GetField("股東權益總額","Q");//單位百萬
        if value2*100-nv<value4*ratio/100
        then ret=1;
        outputfield(1, 100*value2/value4,1, "市值/現金流", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價距離合理價值很遠(df: pd.DataFrame, r1: int = 3, r2: int = 2, r3: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 股價距離合理價值很遠
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\股價距離合理價值很遠.xs
        XS Logic Reference:
        {@type:filter}
        // 計算未來10年的營業利益折現值
        value1=GetField("營業利益","Y");		//單位:百萬
        value2=GetField("最新股本");			//單位:億
        value3=GetField("每股淨值(元)","y");
        value11 = maxlist(GetField("營業利益","Y"),GetField("營業利益","Y")[1],GetField("營業利益","Y")[2],GetField("營業利益","Y")[3],GetField("營業利益","Y")[4]);
        value12 = minlist(GetField("營業利益","Y"),GetField("營業利益","Y")[1],GetField("營業利益","Y")[2],GetField("營業利益","Y")[3],GetField("營業利益","Y")[4]);
        if trueall(value1>0,5) and (value11-value12)/value11<0.5 then begin
        	t = 0;
        	for idx =1 to 10 begin
        		t = t + value1 * power(1+r1/100,idx)/power(1+r2/100,idx);
        	end;
        	// t=百萬,value2=億,換成每股
        	value5 = t / value2 / 100;
        	value6=close/(value3+value5);
        	if value6<r3/100
        	then ret=1;
        end;
        outputfield(1, value5, 2, "估算每股營業利益");
        outputfield(2, value6, 1, "市價/淨值比", order := -1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 跌不下去的高殖利率股(df: pd.DataFrame, N: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 跌不下去的高殖利率股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\10.價值投資\跌不下去的高殖利率股.xs
        XS Logic Reference:
        {@type:filter}
        condition1 = L = Lowest(L,N);
        condition2 = H = Highest(H,N);
        if condition2
        //股價創區間以來高點
        and	TrueAll(Condition1=false,N)
        //這段區間都未破底
        and close<close[N-1]*1.05
        and volume>600
        //區間股價漲幅不大
        then ret=1;
        outputfield(1, GetField("股東權益報酬率","Q"),2, "股東權益%", order := 1);
        outputfield(2, GetField("現金股利","Y"),2, "現金股利");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
