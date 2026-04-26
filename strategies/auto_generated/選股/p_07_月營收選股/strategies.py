# Auto-generated strategies for: 選股/07.月營收選股
import pandas as pd
import numpy as np

class Cat07月營收選股Strategies:

    @staticmethod
    def 可預期的營收成長股(df: pd.DataFrame, years: int = 3, growrate: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 可預期的營收成長股
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\可預期的營收成長股.xs
        XS Logic Reference:
        {@type:filter}
        // 找出過去幾年這個月的營收都會成長的股票
        //
        settotalbar(1);
        // 最新一期營收月份
        //
        mm = Month(getfielddate("月營收", "M"));
        // 下一期營收月份
        mm = mm + 1;
        if mm > 12 then mm = 1;
        while count < years begin
        	if Month(getfielddate("月營收", "M")[idx]) = mm then begin
        		// 看同月份的營收YOY是否符合標準, 不符合的話就不用再找了
        		if getfield("月營收年增率", "M")[idx] < growrate then return;
        		count = count + 1;
        	end;
        	idx = idx + 1;	
        end;
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 旺季不旺(df: pd.DataFrame, r1: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 旺季不旺
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\旺季不旺.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("M");
        settotalbar(3);
        value1=GetField("月營收月增率","M");
        value2=GetField("月營收月增率","M")[12];
        value3=GetField("月營收月增率","M")[24];
        value4=GetField("月營收月增率","M")[36];
        value5=(value2+value3+value4)/3;
        if value2 > r1 and value3 > r1 and value4 > r1 and value1 < value5
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 最近三個月營收明顯成長(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 最近三個月營收明顯成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\最近三個月營收明顯成長.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("月營收月增率","M");
        value2=GetField("月營收年增率","M");
        condition1=false;
        condition2=false;
        if average(value1,3)>10 and average(value2,3)>10
        and value1>value1[1]
        and value2>value2[1] 
        then condition1=true;
        if trueall(value1>5 and value2>5,3)
        then condition2=true;
        if condition1 and condition2 then ret=1;
        outputfield(1,value1,1,"月營收月增率");
        outputfield(2,value1[1],1,"上個月營收月增率");
        outputfield(3,value2,1,"月營收年增率");
        outputfield(4,value2[1],1,"上個月營收年增率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收YOYN月移動平均大於X(df: pd.DataFrame, lowlimit: int = 10, period: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 月營收YOYN月移動平均大於X
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收YOYN月移動平均大於X.xs
        XS Logic Reference:
        {@type:filter}
        if average(GetField("月營收年增率","M"),period) >= lowlimit
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收出現死亡交叉(df: pd.DataFrame, shortterm: int = 4, longterm: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 月營收出現死亡交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收出現死亡交叉.xs
        XS Logic Reference:
        {@type:filter}
        if average(GetField("月營收","M"),shortterm)*1.1
        < average(GetField("月營收","M"),longterm)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收創新低(df: pd.DataFrame, period: int = 36) -> tuple[bool, str]:
        """
        Original Strategy: 月營收創新低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收創新低.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period + 5);
        value1=GetField("月營收","M");
        value2=lowest(GetField("月營收","M"),period);
        if value1=value2
        and value1[1]=value2[1]
        then ret=1;
        outputfield(1, value1,2,"月營收(億)", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收創新高股價離高點有些距離(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 月營收創新高股價離高點有些距離
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收創新高股價離高點有些距離.xs
        XS Logic Reference:
        {@type:filter}
        value1=highest(getfield("月營收","M"),48);
        value2=highest(GetField("總市值","D"),500);
        if getfield("月營收","M")=value1
        and value2>GetField("總市值","D")*1.2
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收大成長的公司(df: pd.DataFrame, lowlimit: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 月營收大成長的公司
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收大成長的公司.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收","M");//億
        value2=GetField("營業利益率","Q");
        value3=value1*12*value2/100;
        value4=GetField("最新股本");//億
        FEPS=value3/value4*10;
        if feps<>0 then value5=close/feps;
        condition1 = value5<12 and value5>0;
        value6=GetField("月營收月增率","M");
        value7=GetField("月營收年增率","M");
        condition2 = value6>=lowlimit and value7>=lowlimit and value6[1]>0;
        if condition1 and condition2 then ret=1;
        setoutputname1("用月營收預估的本業EPS");
        outputfield1(FEPS);
        setoutputname2("用月營收預估的本益比");
        outputfield2(value5);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收年增率移動平均黃金交叉(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 月營收年增率移動平均黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收年增率移動平均黃金交叉.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收年增率","M");
        if average(value1,4) crosses over average(value1,12)
        and value1 > 0
        then ret=1;
        outputfield(1,value1,2,"月營收年增率%", order := 1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 月營收成長動能加快(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 月營收成長動能加快
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\月營收成長動能加快.xs
        XS Logic Reference:
        {@type:filter}
        setbarfreq("M");
        value1=average(GetField("月營收年增率","M"),3);
        //月營收年增率三個月平均
        value2=average(GetField("月營收年增率","M"),12);
        //月營收年增率十二個月平均
        if value1 crosses over value2
        //黃金交叉
        and value1>5
        and value1-value2>5
        and value2>=1
        then ret=1;
        outputfield(1,value1,0,"3個月平均");
        outputfield(2,value2,0,"12個月平均");
        outputfield(3,(close-close[1])/close[1]*100,1,"本月漲跌幅");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收再起飛(df: pd.DataFrame, TXT: str = "僅適用月線") -> tuple[bool, str]:
        """
        Original Strategy: 營收再起飛
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營收再起飛.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月線"); setinputname(1,"使用限制");
        setbarfreq("M");
        If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");
        settotalbar(23);
        value1=GetField("月營收年增率","M");
        value2=average(GetField("月營收年增率","M"), 3);
        value3=linearregslope(value2,20);
        value4=linearregslope(value2,5);
        if value3 < 0 and value4 crosses above 0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收年增率由負轉正_且至少連續3個月(df: pd.DataFrame, period: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 營收年增率由負轉正，且至少連續3個月
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營收年增率由負轉正，且至少連續3個月.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收年增率","M");
        if trueall(value1>0,period) and value1[3]<0
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收月增率優於平均(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 營收月增率優於平均
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營收月增率優於平均.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("月營收月增率","M");
        value2=average(GetField("月營收月增率","M"),36);
        if value1>10
        and value1>value2*1.3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收月增率比歷年突出(df: pd.DataFrame, r1: int = 5, TXT: str = "僅適用月線") -> tuple[bool, str]:
        """
        Original Strategy: 營收月增率比歷年突出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營收月增率比歷年突出.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月線"); setinputname(2,"使用限制");
        setbarfreq("M");
        If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");
        value1 = GetField("月營收月增率","M");
        value2 = average(GetField("月營收月增率","M"),3);
        value3 = average(GetField("月營收月增率","M")[12],3);
        value4 = average(GetField("月營收月增率","M")[24],3);
        value5 = average(GetField("月營收月增率","M")[36],3);
        value6 = (value3 + value4 + value5) / 3;
        if (value2 - value6) > r1 then
        ret = 1;
        SetOutputName1("近3月月營收增幅平均");
        OutputField1(value2);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營收高於預期(df: pd.DataFrame, r1: int = 10, TXT: str = "僅適用月線") -> tuple[bool, str]:
        """
        Original Strategy: 營收高於預期
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營收高於預期.xs
        XS Logic Reference:
        {@type:filter}
        //input:TXT("僅適用月線"); setinputname(2,"使用限制");
        setbarfreq("M");
        If barfreq <> "M" then raiseruntimeerror("頻率設定有誤");
        settotalbar(3);
        value1=GetField("月營收年增率","M");
        value2=average(GetField("月營收年增率","M")[1],3);
        if value1-value2 > r1
        then ret=1;
        setoutputname1("月營收年增率(%)");
        outputfield1(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 營運趨緩(df: pd.DataFrame, months: int = 24, quarters: int = 16) -> tuple[bool, str]:
        """
        Original Strategy: 營運趨緩
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\營運趨緩.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(3);
        value1=GetField("月營收年增率","M");
        value2=GetField("營業毛利率","Q");
        if value1 = lowest(GetField("月營收年增率","M"), months) and
           value2 = lowest(GetField("營業毛利率","Q"), quarters) then
        ret = 1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 累計月營收年增率連續N月成長(df: pd.DataFrame, period: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: 累計月營收年增率連續N月成長
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\累計月營收年增率連續N月成長.xs
        XS Logic Reference:
        {@type:filter}
        settotalbar(period+1);
        value1=GetField("累計營收年增率","M");
        if trueall(value1>value1[1],period)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 累計營收年增率黃金交叉(df: pd.DataFrame, r1: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 累計營收年增率黃金交叉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\選股\07.月營收選股\累計營收年增率黃金交叉.xs
        XS Logic Reference:
        {@type:filter}
        value1=GetField("累計營收年增率","M");
        if average(value1,r1) crosses over average(value1,r2)+5
        and value1>10
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
