# Auto-generated strategies for: 選股/08.財報選股
import pandas as pd
import numpy as np

class Cat08財報選股Strategies:

    @staticmethod
    def N年平均盈餘本益比(df: pd.DataFrame, r1: int = 10, years: int = 8) -> tuple[bool, str]:
        """
        Original Strategy: N年平均盈餘本益比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\N年平均盈餘本益比.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("最新股本");			//單位=億元
        value2=GetField("本期稅後淨利","Y");	//單位=百萬元
        value3=average(GetField("本期稅後淨利","Y"), years);	//稅後淨利平均
        value4=value3/(value1*10);				//每股盈餘
        value6=GetField("收盤價","D");
        if value4 > 0 then
        begin
        	value5 = GetField("收盤價","D") / value4;
        	if value5 < r1 then ret = 1;
        	SetOutputName1("平均盈餘本益比");
        	OutputField1(value5);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N年累計營業利益市值比(df: pd.DataFrame, r1: int = 50, years: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: N年累計營業利益市值比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\N年累計營業利益市值比.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("總市值","D");		//單位億
        value2=summation(GetField("營業利益","y"),years);
        value3=value2/value1;				//單位=百分比
        if value3 < r1
        then ret=1;
        setoutputname1("累計營業利益佔市值比例(%)");
        outputfield1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PB來到近年來低點(df: pd.DataFrame, r1: int = 10, r2: int = 60, TXT: str = "僅適用月資料") -> tuple[bool, str]:
        """
        Original Strategy: PB來到近年來低點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\PB來到近年來低點.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月資料"); setinputname(3,"使用限制");
        setbarfreq("M");
        if barfreq <> "M" then raiseruntimeerror("頻率錯誤");
        settotalbar(3);
        value1=GetField("股價淨值比","M");
        value2=lowest(GetField("股價淨值比","M"),r2);
        value3=average(GetField("股價淨值比","M"),r2);
        if value1 < value3 and value1 < value2*(1+r1/100)
        then ret=1;
        setoutputname1("股價淨值比");
        outputfield1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PEG指標(df: pd.DataFrame, r1: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: PEG指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\PEG指標.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        // PEG指標
        //
        value1 = GetField("本益比","D");
        value2 = GetField("月營收年增率","M"); 
        if value1 > 0 and value2 > 0 and value1 / value2 < r1 then
        ret=1;
        SetOutputName1("PEG指標");
        OutputField1(value1 / value2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ROE漸入佳境(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: ROE漸入佳境
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\ROE漸入佳境.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("股東權益報酬率","Q");
        if GetField("股東權益報酬率","Q")>GetField("股東權益報酬率","Q")[1]
        and GetField("股東權益報酬率","Q")>GetField("股東權益報酬率","Q")[4]
        then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上一季本業賺錢(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上一季本業賺錢
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\上一季本業賺錢.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業利益率","Q");
        if value1>0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上市股可以發行權證的流動性條件(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上市股可以發行權證的流動性條件
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\上市股可以發行權證的流動性條件.xs
        XS Logic Reference:
        {@type:filter}
        {
        	1. 市值超過100億元
        	2. (a or b)
        		a. 最近3個月成交股數佔已發行股份總額比例達20%以上。
        		b. 最近三個月月平均成交股數達1億股以上。
        	3. 最近期經會計師查核或核閱之財務報告無虧損
        }
        settotalbar(3);
        // 近三個月成交股數佔以發行股份比例
        //
        Value1 = Summation(GetField("成交量", "M"), 3) * 100 / (GetField("發行張數","D") * 10000);
        // 最近三個月月平均成交股數
        //
        Value2 = Average(GetField("成交量", "M"), 3) * 1000;
        if GetField("總市值","D") >= 100 and 
           (Value1 >= 20 or Value2 >= 10000000) and 
           GetField("每股稅後淨利(元)","Q") > 0 
        then 
        Ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 上櫃股可以發行權證的流動性條件(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 上櫃股可以發行權證的流動性條件
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\上櫃股可以發行權證的流動性條件.xs
        XS Logic Reference:
        {@type:filter}
        {
        	1. 市值超過40億元
        	2. (a or b)
        		a. 最近3個月成交股數佔已發行股份總額比例達10%以上。
        		b. 最近三個月月平均成交股數達3000萬股以上。
        	3. 最近期經會計師查核或核閱之財務報告無虧損
        }
        settotalbar(3);
        // 近三個月成交股數佔以發行股份比例
        //
        Value1 = Summation(GetField("成交量", "M"), 3) * 100 / (GetField("發行張數","D") * 10000);
        // 最近三個月月平均成交股數
        //
        Value2 = Average(GetField("成交量", "M"), 3) * 1000;
        if GetField("總市值","D") >= 40 and 
           (Value1 > 10 or Value2 > 3000000) and 
           GetField("每股稅後淨利(元)","Q") > 0 
        then 
        Ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 五年內有至少三年營收成長(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 五年內有至少三年營收成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\五年內有至少三年營收成長.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業收入淨額","Y");
        value2=value1-value1[1];
        if countif(value2>0,5)>=3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 企業價值除以自由現金流的倍數低於一水準(df: pd.DataFrame, t1: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 企業價值除以自由現金流的倍數低於一水準
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\企業價值除以自由現金流的倍數低於一水準.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(4);
        value1=GetField("企業價值","Q");//單位百萬
        value2=GetField("來自營運之現金流量","Q");//單位百萬
        value3=GetField("資本支出金額","Q");//單位百萬
        value4=GetField("所得稅費用","Q");//單位百萬
        value5=GetField("利息支出","Q");//單位百萬
        value6=value2-value3-value4-value5;
        //自由現金流量 = 營運現金流量 - 資本支出 - 利息 - 稅金
        value7=summation(value6,4);
        //最近四期現金流量
        if value1<t1*value7 then ret=1;
        outputfield(1,value1,0,"企業價值");
        outputfield(2,value7,0,"近四季自由現金流合計");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 低修正型股價淨值比(df: pd.DataFrame, r1: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 低修正型股價淨值比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\低修正型股價淨值比.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(3);
        value1 = average(GetField("營業利益成長率", "Y"), 6);		// 近六年平均營業利益成長率
        value2 = GetField("每股淨值(元)","Q") * (1 + value1/100);	// 修正後每股淨值
        value3 = close / value2;									// 修正後股價淨值比
        if 0 < value3 and value3 < r1
        then ret=1;
        SetOutputName1("修正後股價淨值比");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 公司官僚化(df: pd.DataFrame, TXT: str = "僅適用季資料") -> tuple[bool, str]:
        """
        Original Strategy: 公司官僚化
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\公司官僚化.xs
        XS Logic Reference:
        {@type:filter}
        // 連續4期[管理費用/營業收入淨額的比例]成長
        //
        //input:TXT("僅適用季資料"); setinputname(1,"使用限制");
        setbarfreq("Q");
        if barfreq <> "Q" then raiseruntimeerror("頻率錯誤");
        settotalbar(3);
        Ret = TrueAll(
        	GetField("管理費用","Q")/GetField("營業收入淨額","Q") > 
        	GetField("管理費用","Q")[1]/GetField("營業收入淨額","Q")[1], 4);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 公司連續N年獲利大於X億(df: pd.DataFrame, lowlimit: int = 1, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 公司連續N年獲利大於X億
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\公司連續N年獲利大於X億.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("本期稅後淨利","Y");//單位百萬
        if trueall(value1>lowlimit*100,period) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 利息支出佔股本比例(df: pd.DataFrame, r1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 利息支出佔股本比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\利息支出佔股本比例.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("最新股本");		//單位億
        value2=GetField("利息支出","Y");	//單位百萬
        value3=value2/(value1*100) * 100;
        if value3 > r1
        then ret=1;
        SetOutputName1("利息支出佔股本比例(%)");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 即將董監改選(df: pd.DataFrame, day: int = 180) -> tuple[bool, str]:
        """
        Original Strategy: 即將董監改選
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\即將董監改選.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        // 董監每三年得改選一次
        //
        lastdate = GetField("董監事就任日期");
        diff = datediff(currentdate, lastdate);
        years_3 = 365*3;
        OutputField(1,lastdate,"董監事就任日期");
        OutputField(2,diff,"改選天數");
        ret = diff < years_3 and diff > years_3 - day;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 可能由虧轉盈(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 可能由虧轉盈
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\可能由虧轉盈.xs
        XS Logic Reference:
        {@type:filter}
        // 計算最新一期月營收的日期(mm=月份)
        //
        mm = datevalue(getfielddate("月營收","M"),"M");
        setbarfreq("M");
        // 預估最新一季的季營收(單位=億)
        //
        if mm=1 or mm=4 or mm=7 or mm=10
        then value1=GetField("月營收","M") * 3;
        if mm=2 or mm=5 or mm=8 or mm=11
        then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
        if mm=3 or mm=6 or mm=9 or mm=12
        then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];
        // 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
        //
        value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");
        if GetField("營業利益","Q")<0
        and value2>0 
        then ret=1;
        outputfield(1,value2 / 100,2,"預估單季本業獲利(億)");
        outputfield(2,GetField("營業利益","Q"),0,"最近一季營業利益");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 固定資產佔股本比率低於N_(df: pd.DataFrame, r1: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 固定資產佔股本比率低於N%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\固定資產佔股本比率低於N%.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("最新股本");//單位億
        value2=GetField("固定資產","Q");
        value3=value2/(value1*100);
        if value3<r1/100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 季營收連N季YOY正成長(df: pd.DataFrame, n: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 季營收連N季YOY正成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\季營收連N季YOY正成長.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(n+4);
        value1=GetField("營業收入淨額","Q");//單位:百萬
        if trueall(value1>value1[4],n)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 市值研發費用比(df: pd.DataFrame, n: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 市值研發費用比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\市值研發費用比.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("總市值");				// 單位=億
        value2=GetField("研發費用","Y");		// 單位=百萬
        value3=value2 / value1;					// % 
        if value3 > n
        then ret=1;
        SetOutputName1("研發費用市值比");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帳上現金少(df: pd.DataFrame, r1: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 帳上現金少
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\帳上現金少.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("現金及約當現金","Q");
        if value1 < r1
        then ret=1;
        SetOutputName1("帳上現金(百萬)");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 年營收成長率超過一定比例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 年營收成長率超過一定比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\年營收成長率超過一定比例.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Y");
        settotalbar(5);
        value1=GetField("營收成長率","Y");
        value2=average(value1,5);
        if trueall(value1>0,5) and value2>=25
        then ret=1;
        OutputField(1,value1,"年度營收成長率");
        OutputField(2,value2,"五年平均營收成長率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最新一季可能虧錢的公司(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 最新一季可能虧錢的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\最新一季可能虧錢的公司.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("M");
        value1=GetField("月營收","M");//單位:億
        value2=value1[2]+value1[3]+value1[4];
        value3=GetField("營業毛利率","Q");
        value4=GetField("營業費用","Q");//單位:百萬
        if value2*value3/100-value4/100<0  
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最近五年ROE平均高於某值(df: pd.DataFrame, r1: int = 15) -> tuple[bool, str]:
        """
        Original Strategy: 最近五年ROE平均高於某值
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\最近五年ROE平均高於某值.xs
        XS Logic Reference:
        {@type:filter}
        if average(GetField("股東權益報酬率","Y"),5)>r1
        then ret=1;
        outputfield(1,GetField("股東權益報酬率","Y"),1,"最近一年");
        outputfield(2,GetField("股東權益報酬率","Y")[1],1,"前一年");
        outputfield(3,GetField("股東權益報酬率","Y")[2],1,"前兩年");
        outputfield(4,GetField("股東權益報酬率","Y")[3],1,"前三年");
        outputfield(5,GetField("股東權益報酬率","Y")[4],1,"前四年");
        outputfield(6,average(GetField("股東權益報酬率","Y"),5),1,"平均");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最近幾季存貨增加的比營收還快(df: pd.DataFrame, r1: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 最近幾季存貨增加的比營收還快
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\最近幾季存貨增加的比營收還快.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(r1+2);
        value1=GetField("營業收入淨額","Q");
        value2=GetField("存貨","Q");
        value3=rateofchange(value1,1);
        value4=rateofchange(value2,1);
        value5=value4-value3;
        if trueall(value5>0,r1)
        and trueall(value5-value5[1]>0,r1)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本業可能轉虧為盈(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 本業可能轉虧為盈
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\本業可能轉虧為盈.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalbar(3);
        // 計算最新一期月營收的日期(mm=月份)
        //
        mm = datevalue(getfielddate("月營收","M"),"M");
        // 預估最新一季的季營收(單位=億)
        //
        if mm=1 or mm=4 or mm=7 or mm=10
        then value1=GetField("月營收","M") * 3;
        if mm=2 or mm=5 or mm=8 or mm=11
        then value1=GetField("月營收","M") * 2 + GetField("月營收","M")[1];
        if mm=3 or mm=6 or mm=9 or mm=12
        then value1=GetField("月營收","M")+GetField("月營收","M")[1]+GetField("月營收","M")[2];
        // 預估獲利(單位=百萬) = 季營收 * 毛利率 - 營業費用
        //
        value2 = value1 * GetField("營業毛利率","Q") - GetField("營業費用","Q");
        if value2 > 0 and GetField("營業利益","Q") < 0 then
        ret = 1;
        SetOutputName1("預估單季營收(億)");
        OutputField1(value1);
        SetOutputName2("預估單季本業獲利(億)");
        OutputField2(value2 / 100);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本業推估本益比低於N(df: pd.DataFrame, epsl: int = 15) -> tuple[bool, str]:
        """
        Original Strategy: 本業推估本益比低於N
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\本業推估本益比低於N.xs
        XS Logic Reference:
        {@type:filter}
        value3= summation(GetField("營業利益","Q"),4); //單位百萬;
        value4= GetField("最新股本");//單位億;
        value5= value3/(value4*10);//每股預估EPS
        if value5>0 and close/value5<=epsl
        then ret=1;
        outputfield(1,close/value5,1,"預估本益比", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 本業獲利佔八成以上(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 本業獲利佔八成以上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\本業獲利佔八成以上.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業利益","Q");//單位百萬
        value2=GetField("稅前淨利","Q");//單位百萬
        if value2>0
        then begin
        if value1/value2*100>80
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 每年本業都獲利且趨勢向上(df: pd.DataFrame, lm: int = 200) -> tuple[bool, str]:
        """
        Original Strategy: 每年本業都獲利且趨勢向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\每年本業都獲利且趨勢向上.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(5);
        value1=GetField("營業利益","Y");//百萬
        if trueall(value1>lm,5)
        //週去五年都賺超過一億
        and linearregslope(value1,5)>0
        //五年的營業利益趨勢往上
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 每股來自營運現金流量(df: pd.DataFrame, r1: int = 25) -> tuple[bool, str]:
        """
        Original Strategy: 每股來自營運現金流量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\每股來自營運現金流量.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("最新股本");				// 單位=億
        value2=GetField("來自營運之現金流量","Q");	// 單位=百萬
        value3=value2/value1;						// 單位=%
        if value3 > r1
        then ret=1;
        setoutputname1("來自營運的現金流量佔股本比率(%)");
        outputfield1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 毛利沒掉營收成長費用減少(df: pd.DataFrame, ratio: int = 10, period1: int = 10, period2: int = 5, count: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 毛利沒掉營收成長費用減少
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\毛利沒掉營收成長費用減少.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(maxlist(period1,period2)+1);
        value1=GetField("營業毛利率","Q");
        value2=GetField("營業收入淨額","Q");//單位百萬
        value3=GetField("營業費用","Q");//單位百萬
        if trueall(value1>value1[1]*(1-ratio/100),period1)
        and countif(value2>value2[1]and value3<value3[1],period2)>=count
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 毛利率上昇月營收成長(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 毛利率上昇月營收成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\毛利率上昇月營收成長.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收月增率","M");
        value2=GetField("營業毛利率","Q");
        if value1>value1[1]
        and value2>value2[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 毛利率沒掉的兇(df: pd.DataFrame, ratio: int = 10, period: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 毛利率沒掉的兇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\毛利率沒掉的兇.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業毛利率","Q");
        if trueall(value1>value1[1]*(1-ratio/100),period)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 法定盈餘公積已提足_配股能力提昇(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 法定盈餘公積已提足，配股能力提昇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\法定盈餘公積已提足，配股能力提昇.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("法定盈餘公積","Q");	//百萬
        value2=GetField("最新股本");			//億
        value3=GetField("本期稅後淨利","Q");	//百萬
        // 稅後淨利 + 法定盈餘公積 > 股本
        //
        if value1 + value3 > value2*100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流動資產市值比(df: pd.DataFrame, r1: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 流動資產市值比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\流動資產市值比.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("流動資產","Q");	// 單位=百萬
        value2=GetField("總市值","D");		// 單位=億
        value3=value1/value2;				// 單位=%
        if value3 < r1
        then ret=1;
        setoutputname1("流動資產市值比%");
        outputfield1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流動資產減負債超過市值N成(df: pd.DataFrame, ratio: int = 80) -> tuple[bool, str]:
        """
        Original Strategy: 流動資產減負債超過市值N成
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\流動資產減負債超過市值N成.xs
        XS Logic Reference:
        {@type:filter}
        if (GetField("流動資產","Q")-GetField("負債總額","Q"))*100>GetField("總市值","D")*ratio/100
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流動資產減負債超過總市值N成(df: pd.DataFrame, ratio: int = 80) -> tuple[bool, str]:
        """
        Original Strategy: 流動資產減負債超過總市值N成
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\流動資產減負債超過總市值N成.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("流動資產","Q");//單位百萬
        value2=GetField("負債總額","Q");//單位百萬
        value3=GetField("總市值","D");//單位億
        if (value1-value2)>=value3*ratio
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 淡季不淡(df: pd.DataFrame, r1: int = 5, r2: int = 0, TXT: str = "僅適用月線") -> tuple[bool, str]:
        """
        Original Strategy: 淡季不淡
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\淡季不淡.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月線"); setinputname(3,"使用限制");
        setbarfreq("M");
        If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");
        settotalbar(3);
        value1=GetField("月營收月增率","M");
        value2=GetField("月營收月增率","M")[12];
        value3=GetField("月營收月增率","M")[24];
        value4=GetField("月營收月增率","M")[36];
        if value2 < -r1 and value3 < -r1 and value4 < -r1 and value1 > r2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收上昇費用降低(df: pd.DataFrame, period: int = 5, count: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 營收上昇費用降低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營收上昇費用降低.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(period+1);
        value1=GetField("營業收入淨額","Q");//單位百萬
        value2=GetField("營業費用","Q");//單位百萬
        if countif(value1>value1[1] and value2<value2[1],period)>=count
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收市值比位於歷史低檔(df: pd.DataFrame, period: int = 60, ratio: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 營收市值比位於歷史低檔
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營收市值比位於歷史低檔.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("M");
        settotalbar(period);
        value1=GetField("總市值","M");//單位:億元
        value2=GetField("月營收","M");//單位:億元
        if value2<>0 then 
        	value3=value1/value2
        else
        	value3=0;
        if value3<lowest(value3,period)*(1+ratio/100)
        //總市值營收比值距離過去一段時間最低點沒有差多遠
        and value3>0
        then ret=1;
        outputfield(1,value3,2,"總市值/月營收");
        outputfield(2,lowest(value3,period),2,"期間最低值");
        outputfield(3,value3/lowest(value3,period),2,"兩者的比率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營業利益均線向上(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營業利益均線向上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營業利益均線向上.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(10);
        value1=GetField("營業利益","Q");
        if linearregslope(average(value1,5),5)>0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營業利益率不曾大幅下滑(df: pd.DataFrame, r1: int = 5, p1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 營業利益率不曾大幅下滑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營業利益率不曾大幅下滑.xs
        XS Logic Reference:
        {@type:filter}
        SetTotalBar(p1 + 4);
        value1=GetField("營業利益率","Q");
        if trueall(value1*(1+r1/100)>value1[1],p1)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營業外收入愈來愈高(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營業外收入愈來愈高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營業外收入愈來愈高.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if trueall(GetField("營業外收入合計","Y") > GetField("營業外收入合計","Y")[1], 3) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營益率由負轉正且持續上揚(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營益率由負轉正且持續上揚
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營益率由負轉正且持續上揚.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        if 
        	GetField("營業利益率","Q")[2]<0 and 
        	GetField("營業利益率","Q")[1]>0 and
        	GetField("營業利益率","Q") > GetField("營業利益率","Q")[1] and
        	GetField("月營收月增率","M") > 0 and 
        	GetField("月營收月增率","M")[1] >0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營運現金流大於稅後盈餘(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營運現金流大於稅後盈餘
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\營運現金流大於稅後盈餘.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("來自營運之現金流量","Q");
        value2=GetField("本期稅後淨利","Q");
        if value1 > value2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 獲利穩定的公司(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 獲利穩定的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\獲利穩定的公司.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Y");
        settotalbar(5);
        value1=GetField("每股稅後淨利(元)","Y");
        if trueall(value1>=2,5)//過去五年每年都賺超過兩元
        and highest(value1,5)<lowest(value1,5)*1.5//獲利的高低差距在忍受範圍
        then ret=1;
        outputfield(1,highest(value1,5),1,"最高EPS");
        outputfield(2,lowest(value1,5),1,"最低EPS");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 獲利追不上固定資本支出(df: pd.DataFrame, r1: int = 3, TXT: str = "僅適用年資料") -> tuple[bool, str]:
        """
        Original Strategy: 獲利追不上固定資本支出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\獲利追不上固定資本支出.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用年資料"); setinputname(2,"使用限制");
        setbarfreq("Y");
        if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");
        settotalbar(3);
        if trueall(
        	GetField("本期稅後淨利","Y") - GetField("本期稅後淨利","Y")[1] <
        	GetField("固定資產","Y") - GetField("固定資產","Y")[1],
        	r1)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現增佔比低(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 現增佔比低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\現增佔比低.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("現金增資佔股本比重","Y");
        if value1<20
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現金不少但股價淨值比低(df: pd.DataFrame, r1: int = 0, r2: int = 10, r3: float = 0.8) -> tuple[bool, str]:
        """
        Original Strategy: 現金不少但股價淨值比低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\現金不少但股價淨值比低.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("來自營運之現金流量","Q");
        value2=GetField("現金及約當現金","Q");
        value3=GetField("股價淨值比","D");
        if value1>r1
        and value2/100>r2
        and value3<r3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現金佔總市值比例(df: pd.DataFrame, r1: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 現金佔總市值比例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\現金佔總市值比例.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("現金及約當現金","Q");	// 單位=百萬
        value2=GetField("總市值","D");			// 單位=億
        value3=value1/value2;					// 單位=%
        if value3 > r1 then ret=1;
        SetoutputName1("現金佔總市值比例%");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現金很多的公司(df: pd.DataFrame, lowlimit: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 現金很多的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\現金很多的公司.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("現金及約當現金","Q");//單位百萬
        value2=GetField("短期投資","Q");//單位百萬
        value3=GetField("短期借款","Q");//單位百萬
        value4=(value1+value2-value3)/100;//單位億之現金及短期投資合計金額
        if value4>=lowlimit
        then ret=1;
        outputfield(1,value4,"償債後現金及短投金額(億)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 現金總市值比(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 現金總市值比
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\現金總市值比.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("現金及約當現金","Q");//單位百萬
        value2=GetField("短期投資","Q");//單位百萬
        value3=(value1+value2)/100;//單位億之現金及短期投資合計金額
        value4=GetField("總市值","D");//單位:億
        if value4<>0
        then value5=value3/value4;//現金總市值比;
        if value5>0.7 and value3>3 //現金總市值比大於0.7且現金及短投合計超過3億
        then ret=1;
        outputfield(1, value5, 1, "現金總市值比", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 總市值接近歷史低點(df: pd.DataFrame, r1: int = 5, TXT: str = "僅適用月資料") -> tuple[bool, str]:
        """
        Original Strategy: 總市值接近歷史低點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\總市值接近歷史低點.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月資料"); setinputname(2,"使用限制");
        setbarfreq("M");
        if barfreq <> "M" then raiseruntimeerror("頻率錯誤");
        settotalbar(3);
        value1=GetField("總市值","M");
        value2=nthlowest(1,GetField("總市值","M"),48);
        value3=nthlowest(1,GetField("總市值","M"),24);
        if absvalue(value2-value3)*100 / value3 < r1
        then 
          begin
        	if (value1-value2) * 100 / value2 < r1 and
        	   (value1-value3) * 100 / value3 < r1 
        	then
        		ret=1;
          end;
        SetOutputName1("最近市值(億)");
        OutputField1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 考慮成長率的股利回推合理股價(df: pd.DataFrame, r: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: 考慮成長率的股利回推合理股價
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\考慮成長率的股利回推合理股價.xs
        XS Logic Reference:
        {@type:filter}
        value1=average(GetField("現金股利","Y"),5);
        if lowest(GetField("現金股利","Y")[1],3)>0 then 
        	s1=lowest(rateofchange(GetField("現金股利","Y"),1),3);
        if value1>1 and r>s1 and s1>0then begin
        	value2=value1/(r-s1)*100;
        	if close<>0 then 
        		value3=(value2-close)/close*100;
        	if value3>10
        	and GetField("現金股利","Y")>GetField("現金股利","Y")[1]
        	then ret=1;
        	outputfield(1,value1,1,"平均現金股利");
        	outputfield(2,s1,1,"近年最低股利成長率");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股價低於N年平均股利的N倍(df: pd.DataFrame, N1: int = 5, N2: int = 16) -> tuple[bool, str]:
        """
        Original Strategy: 股價低於N年平均股利的N倍
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\股價低於N年平均股利的N倍.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("股利合計","Y");
        value2=average(value1,N1);
        if close<value2*N2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股息配發率超過一定比率(df: pd.DataFrame, ratio: int = 60) -> tuple[bool, str]:
        """
        Original Strategy: 股息配發率超過一定比率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\股息配發率超過一定比率.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("每股稅後淨利(元)","Y");
        value2=GetField("現金股利","Y");
        if value1>0
        then value3=value2/value1*100;//股息配發率
        if trueall(value3>ratio,3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股本膨脹營收獲利跟不上(df: pd.DataFrame, TXT: str = "僅適用年資料") -> tuple[bool, str]:
        """
        Original Strategy: 股本膨脹營收獲利跟不上
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\股本膨脹營收獲利跟不上.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用年資料"); setinputname(1,"使用限制");
        setbarfreq("Y");
        if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");
        settotalbar(4);
        value1 = RateOfChange(GetField("普通股股本","Y"), 1);
        value2 = RateOfChange(GetField("營業收入淨額","Y"), 1);
        value3 = GetField("營業利益成長率","Y");
        if 
        	value1 > value2 and
        	value1 > value3 and
        	value1[1] > value2[1] and
        	value1[1] > value3[1]
        then
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股東權益報酬率高且穩定(df: pd.DataFrame, years: int = 5, r1: int = 15, r2: int = 3, fx: str = "資料頻率") -> tuple[bool, str]:
        """
        Original Strategy: 股東權益報酬率高且穩定
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\股東權益報酬率高且穩定.xs
        XS Logic Reference:
        {@type:filter}
        if barfreq <> "Y" then raiseruntimeerror("頻率錯誤");
        settotalbar(3);
        value1=GetField("股東權益報酬率","Y");
        value2=lowest(GetField("股東權益報酬率","Y"), years);
        value3=highest(GetField("股東權益報酬率","Y"), years);
        if (value3 - value2) < r2 and value2 > r1 
        then ret=1;
        setoutputname1("ROE(%)");
        outputfield1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 股魚選股策略(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 股魚選股策略
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\股魚選股策略.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業利益","Q");//單位百萬
        value2=GetField("稅前淨利","Q");//單位百萬
        value3=GetField("來自營運之現金流量","Q");//單位百萬
        value4=GetField("資本支出金額","Q");//單位百萬
        value5=GetField("利息支出","Q");//單位百萬
        value6=GetField("所得稅費用","Q");//單位百萬
        condition1=false;
        condition2=false;
        condition3=false;
        if value2>0 then begin
        	if value1/value2*100>80
        	then condition1=true;  //本業獲利佔八成以上
        end;
        if value3-value4-value5-value6>0 //自由現金流量大於零
        then condition2=true;
        value7=GetField("利息保障倍數","Y");
        value8=GetField("股東權益報酬率","Y");//單位%
        value9=GetField("營業利益率","Q");//單位%
        value10=GetField("本益比","D");
        value11=GetField("殖利率","D");
        value12=GetField("每股淨值(元)","Q");
        value13=value12*value8/8;//獲利能力比率
        if value7>20 and value8>8 and value9>0 and value10<12 and value11>6 and close<value13
        then condition3=true;
        if condition1 and condition2 and condition3
        then ret=1;
        outputfield(1,GetField("股東權益報酬率","Y"),2,"ROE");
        outputfield(2,GetField("殖利率","D"),2,"殖利率", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 葛拉罕的選股兩標準(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 葛拉罕的選股兩標準
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\葛拉罕的選股兩標準.xs
        XS Logic Reference:
        {@type:filter}
        value1=summation(GetField("本期稅後淨利","Q"),4);//單位:百萬
        value2=GetField("負債總額","Q");
        value3=GetField("資產總額","Q");
        value4=GetField("總市值","D");//單位:億
        if value4<value1*7/100
        and value3>value2*2
        then ret=1;
        outputfield(1,value1/100,0,"近四季獲利(億)");
        outputfield(2,value1/100*7,0,"獲利的七倍(億)");
        outputfield(3,value4,0,"總市值");
        outputfield(4,value2,0,"負債");
        outputfield(5,value3,0,"資產");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 說好的好業績一直沒有來(df: pd.DataFrame, r1: int = 5, r2: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 說好的好業績一直沒有來
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\說好的好業績一直沒有來.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1 = 4 * GetField("每股稅後淨利(元)","Q");	// 預估每股盈餘(年)
        if value1 > 0 then
        	value2 = close / value1				//本益比
        else	
        	value2 = 0;	
        if value2 > r2 and 
           trueall(GetField("月營收月增率","M") < r1, 3) 
        then ret = 1;
        setoutputname1("預估每股盈餘(元)");
        outputfield1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 資產報酬率達到一定的水準且沒有明顯下滑(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 資產報酬率達到一定的水準且沒有明顯下滑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\資產報酬率達到一定的水準且沒有明顯下滑.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("資產報酬率","Q");
        value2=average(value1,4);
        value3=linearregslope(value2,5);
        if value3>0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近N年EPS成長率平均大於X_(df: pd.DataFrame, N: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 近N年EPS成長率平均大於X%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\近N年EPS成長率平均大於X%.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Y");
        SetTotalBar(N+3);
        Value1 = Average(RateOfChange(GetField("每股稅後淨利(元)","Y"), 1), N);
        Ret = Value1 > X;
        SetOutputName1("平均EPS成長率(%)");
        OutputField1(Value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近五年至少有一年營業利益超過五億(df: pd.DataFrame, years: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 近五年至少有一年營業利益超過五億
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\近五年至少有一年營業利益超過五億.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Y");
        settotalbar(5);
        value1=GetField("營業利益","Y");//單位: 百萬
        if highest(value1,years)>=500
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近四季EPS合計大於N元(df: pd.DataFrame, n1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 近四季EPS合計大於N元
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\近四季EPS合計大於N元.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("每股稅後淨利(元)","Q");
        value2=summation(value1,4);
        if value2>=n1
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近期有大額資本支出(df: pd.DataFrame, period: int = 20, lm: int = 30, cm: int = 500) -> tuple[bool, str]:
        """
        Original Strategy: 近期有大額資本支出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\近期有大額資本支出.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period+1);
        value1=GetField("資本支出金額","Q");//單位: 百萬
        value2=GetField("資本支出營收比","Q");//單位：%
        value3=average(value1,period);
        value4=average(value2,period);
        if value1>cm//資本支出超過一定金額
        and value1>value3*(1+lm/100)
        and value2>value4*(1+lm/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 過去三年來自營運的現金流量都大於零(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 過去三年來自營運的現金流量都大於零
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\過去三年來自營運的現金流量都大於零.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("來自營運之現金流量","Y");
        if trueall(value1>0,3)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 預估殖利率高的(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 預估殖利率高的
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\預估殖利率高的.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("營業利益","Q");//單位:百萬
        value2=GetField("月營收","M");//單位:億
        value3=GetField("營業利益率","Q");
        value4=SUMMATION(GETFIELD("月營收","M"),3);//近三個月營收
        value5=value4*value3/100;
        //用最近一期營益率去估算的最近一季營業利益
        value6=SUMMATION(GetField("營業利益","Q"),3)+value5*100;
        //前三季營業利益加上最近一季預估營業利益
        value8=GetField("最新股本");//單位億
        value9=value6/(value8*100)*10;
        //估算出來的EPS
        value10=value9/close*100;
        //eps/股價*100: 預估殖利率
        if value10>10 and value3>0 and close>10
        then ret=1;
        outputfield(1,value10,1,"殖利率");
        outputfield(2,value9,1,"預估EPS");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 預期報酬率高的公司(df: pd.DataFrame, tp: int = 150) -> tuple[bool, str]:
        """
        Original Strategy: 預期報酬率高的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\預期報酬率高的公司.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("累計營收年增率","M");
        value2=GetField("月營收","M");//單位:億
        value3=GetField("營業毛利率","Q");
        value4=GetField("營業費用","Q");//單位百萬
        value5=GetField("加權平均股本","Q");//單位億
        {用月營收*毛利率-季營業費用/3來當單月本業獲利，
        乘12當未來一年的本業獲利除以股本為預估的未來一年EPS}
        value6=((value2*value3/100-value4/300)*12/(value5))*10;
        //未來一年預估EPS*累計營收年增率為目標價
        //但若累計營收年增率不到10就以10倍本益比來算目標價
        if value1>10 and value1<20 then value7=value6*value1
        else if value1>=20 then value7=value6*20
        else value7=value6*10;
        //用預估EPS乘上累計營收成長率當成目標價
        if close<>0
        then value8=((value7-close)/close)*100;
        if GetField("月營收月增率","M")<30 and GetField("月營收年增率","M")<50
        then begin
        	if value8 > tp then ret=1;
        	outputfield(1,value8,"預期報酬率");
        	outputfield(2,value7,"目標價");
        	outputfield(3,value6,"預估EPS");
        	outputfield(4,value2,"最近月營收(億)");
        	outputfield(5,value3,"毛利率");
        	outputfield(6,value4,"季營業費用(百萬)");
        	outputfield(7,value5,"加權股本(億)");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高F_Score的股票(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 高F_Score的股票
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高F_Score的股票.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("Q");
        settotalbar(5);
        value1=GetField("資產報酬率","Q");
        value2=GetField("來自營運之現金流量","Q");//單位百萬
        value3=GetField("本期稅後淨利","Q");//單位百萬
        value5=GetField("負債比率","Q");
        value6=GetField("流動比率","Q");
        value7=GetField("現金增資佔股本比重","y");
        value8=GetField("營業毛利率","Q");
        value9=GetField("總資產週轉率(次)","Q");
        if date<>date[1] then score=0;
        if value1>0 then score=score+1;
        if value1-value1[3]>0 then score=score+1;
        if value2>0 then score=score+1;
        if value3>value2 then score=score+1;
        if value5<value5[3] then score=score+1;
        if value6>value6[3] then score=score+1;
        if value7<=value7[3] then score=score+1;
        if value8>value8[3] then score=score+1;
        if value9>value9[3] then score=score+1;
        if score>=8 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高毛利低獲利營收暴衝(df: pd.DataFrame, smr: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 高毛利低獲利營收暴衝
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高毛利低獲利營收暴衝.xs
        XS Logic Reference:
        {@type:filter}
        	smr(5,"月營收月增率"),
        	syr(10,"月營收年增率"),
        	gr(45,"營業毛利率"),
        	epsy(1,"年EPS"),
        	epsq(0.5,"季EPS");
        value1=GetField("月營收月增率","M");
        value2=GetField("月營收年增率","M");
        value3=GetField("營業毛利率","Q");
        if value1> smr //月營收月增率大於10%
        and value2> syr//月營收年增率大於10%
        and value3>= gr//毛利率大於45%
        and GetField("每股稅後淨利(元)","Y")<epsy//最近一年稅後EPS小於1
        and GetField("每股稅後淨利(元)","Q")<epsq//最近一季稅後EPS小於0.5
        and GetField("每股營業額(元)","Y")>10//每股年營收大於10
        then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高現金報酬率(df: pd.DataFrame, r1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 高現金報酬率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高現金報酬率.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        // 自由現金流
        //
        value1 = GetField("來自營運之現金流量","Q") - (GetField("固定資產","Q") - GetField("固定資產","Q")[1]);
        // 淨利息費用
        value2=GetField("利息支出","Q") - GetField("利息收入","Q");				
        // 現金報酬率(%)
        //
        value3 = (value1 + value2) / GetField("企業價值","Q") * 100;
        if value3 > r1 then ret = 1;
        SetOutputName1("現金報酬率(%)");
        OutputField1(value3);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高現金股利政策且營運仍佳(df: pd.DataFrame, peratio: int = 17, ratio: int = 60, epsl: int = 2, rate1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 高現金股利政策且營運仍佳
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高現金股利政策且營運仍佳.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("累計營收年增率","M");//單位%
        value2=GetField("現金股利佔股利比重","Y");
        value3=GetField("營業利益","Q");//單位百萬;
        value4=GetField("最新股本");//單位億;
        value5=summation(value3,4)/(value4*10);//每股預估EPS
        if value1>=rate1 //本業持續成長
        and value2>=ratio //主要以現金股利為主
        and value5>=EPSl //每股推估本業獲利高
        and value5/close<=peratio //本益比低
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高護城河(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 高護城河
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高護城河.xs
        XS Logic Reference:
        {@type:filter}
        condition1=false;
        condition2=false;
        condition3=false;
        if trueall(GetField("營業毛利率","Y") >=10,5)
        then condition1=true;
        if trueall(GetField("來自營運之現金流量","Y")>100,5)
        then condition2=true;
        if trueall(GetField("股東權益報酬率","Y")>20,5)
        then condition3=true;
        if condition1 and condition2 and condition3
        then ret=1;
        outputfield(1,GetField("營業毛利率","Y"),2,"營業毛利率%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高護城河的公司(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 高護城河的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\08.財報選股\高護城河的公司.xs
        XS Logic Reference:
        {@type:filter}
        condition1=false;
        condition2=false;
        condition3=false;
        //每年毛利率都大於10%
        if trueall(GetField("營業毛利率","Y")>=10,4) then condition1=true;
        //每年來自營運的現金流量都大於1億
        if trueall(GetField("來自營運之現金流量","Y")>100,4) then condition2=true;
        //股東權益報酬率大於15%
        if trueall(GetField("股東權益報酬率","Y")>15,4) then condition3=true;
        if condition1 and condition2 and condition3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
