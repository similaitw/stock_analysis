# Auto-generated strategies for: 指標/跨頻率指標
import pandas as pd
import numpy as np

class 跨頻率指標Strategies:

    @staticmethod
    def 分鐘與日DMI_Osc(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日DMI-Osc
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日DMI-Osc.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率DMI-Osc指標，預設跨頻率為30分鐘
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘DMI-Osc技術指標。
        //
        		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        xfMin_DirectionMovement(FreqType, Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value - ndi_value, "分鐘與日DMI-Osc");
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		setplotlabel(1, "1分DMI-Osc");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		setplotlabel(1, "5分DMI-Osc");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		setplotlabel(1, "10分DMI-Osc");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		setplotlabel(1, "15分DMI-Osc");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		setplotlabel(1, "30分DMI-Osc");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		setplotlabel(1, "60分DMI-Osc");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		setplotlabel(1, "日DMI-Osc");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		setplotlabel(1, "還原日DMI-Osc");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘與日DMI(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日DMI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日DMI.xs
        XS Logic Reference:
        {@type:indicator}
        // 分頻率DMI指標，預設跨分頻率為30分鐘
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘DMI技術指標。
        //
        		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        xfMin_DirectionMovement(FreqType, Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value, "分鐘與日+DI");
        Plot2(ndi_value, "分鐘與日-DI");
        Plot3(adx_value, "分鐘與日ADX");
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		setplotlabel(1, "1分+DI");
        		setplotlabel(2, "1分-DI");
        		setplotlabel(3, "1分ADX");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		setplotlabel(1, "5分+DI");
        		setplotlabel(2, "5分-DI");
        		setplotlabel(3, "5分ADX");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		setplotlabel(1, "10分+DI");
        		setplotlabel(2, "10分-DI");
        		setplotlabel(3, "10分ADX");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		setplotlabel(1, "15分+DI");
        		setplotlabel(2, "15分-DI");
        		setplotlabel(3, "15分ADX");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		setplotlabel(1, "30分+DI");
        		setplotlabel(2, "30分-DI");
        		setplotlabel(3, "30分ADX");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		setplotlabel(1, "60分+DI");
        		setplotlabel(2, "60分-DI");
        		setplotlabel(3, "60分ADX");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		setplotlabel(1, "日+DI");
        		setplotlabel(2, "日-DI");
        		setplotlabel(3, "日ADX");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		setplotlabel(1, "還原日+DI");
        		setplotlabel(2, "還原日-DI");
        		setplotlabel(3, "還原日ADX");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘與日KD(df: pd.DataFrame, Length: int = 9) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日KD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日KD.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率KD指標，預設跨頻率為30分
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘KD技術指標。
        //
        		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        xfMin_stochastic(FreqType, Length, RSVt, Kt, rsv, k, _d);
        Plot1(k, "分鐘與日K(%)");
        Plot2(_d, "分鐘與日D(%)");
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		setplotlabel(1, "1分K(%)");
        		setplotlabel(2, "1分D(%)");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		setplotlabel(1, "5分K(%)");
        		setplotlabel(2, "5分D(%)");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		setplotlabel(1, "10分K(%)");
        		setplotlabel(2, "10分D(%)");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		setplotlabel(1, "15分K(%)");
        		setplotlabel(2, "15分D(%)");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		setplotlabel(1, "30分K(%)");
        		setplotlabel(2, "30分D(%)");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		setplotlabel(1, "60分K(%)");
        		setplotlabel(2, "60分D(%)");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		setplotlabel(1, "日K(%)");
        		setplotlabel(2, "日D(%)");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		setplotlabel(1, "還原日K(%)");
        		setplotlabel(2, "還原日D(%)");		
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘與日MACD(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日MACD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日MACD.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率MACD指標，預設跨頻率為30分
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘MACD技術指標。
        //
        		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        xfMin_macd(FreqType,xfMin_weightedclose(FreqType),FastLength,SlowLength,MACDLength,value1,value2,value3);
        // 前面區段資料變動較大, 先不繪出
        //
        if CurrentBar <= SlowLength then
        begin
        	Value1 = 0;
        	Value2 = 0;
        	Value3 = 0;
        end;
        Plot1(Value1, "分鐘與日DIF");
        Plot2(Value2, "分鐘與日MACD");
        Plot3(Value3, "分鐘與日Osc");
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		setplotlabel(1, "1分DIF");
        		setplotlabel(2, "1分MACD");
        		setplotlabel(3, "1分Osc");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		setplotlabel(1, "5分DIF");
        		setplotlabel(2, "5分MACD");
        		setplotlabel(3, "5分Osc");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		setplotlabel(1, "10分DIF");
        		setplotlabel(2, "10分MACD");
        		setplotlabel(3, "10分Osc");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		setplotlabel(1, "15分DIF");
        		setplotlabel(2, "15分MACD");
        		setplotlabel(3, "15分Osc");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		setplotlabel(1, "30分DIF");
        		setplotlabel(2, "30分MACD");
        		setplotlabel(3, "30分Osc");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		setplotlabel(1, "60分DIF");
        		setplotlabel(2, "60分MACD");
        		setplotlabel(3, "60分Osc");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		setplotlabel(1, "日DIF");
        		setplotlabel(2, "日MACD");
        		setplotlabel(3, "日Osc");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		setplotlabel(1, "還原日DIF");
        		setplotlabel(2, "還原日MACD");
        		setplotlabel(3, "還原日Osc");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘與日RSI(df: pd.DataFrame, Length1: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日RSI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日RSI.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率RSI指標，預設跨頻率為30分
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘RSI技術指標。
        //
        		FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        // 因 Getfield 第二個參數不支援動態變數字串，故使用以下語法表達跨分鐘頻率的RSI
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		value1 = xfMin_RSI("1", GetField("Close","1"), Length1);
        		value2 = xfMin_RSI("1", GetField("Close","1"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "1分RSI");
        		setplotlabel(2, "1分RSI");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		value1 = xfMin_RSI("5", GetField("Close","5"), Length1);
        		value2 = xfMin_RSI("5", GetField("Close","5"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "5分RSI");
        		setplotlabel(2, "5分RSI");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		value1 = xfMin_RSI("10", GetField("Close","10"), Length1);
        		value2 = xfMin_RSI("10", GetField("Close","10"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "10分RSI");
        		setplotlabel(2, "10分RSI");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		value1 = xfMin_RSI("15", GetField("Close","15"), Length1);
        		value2 = xfMin_RSI("15", GetField("Close","15"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "15分RSI");
        		setplotlabel(2, "15分RSI");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		value1 = xfMin_RSI("30", GetField("Close","30"), Length1);
        		value2 = xfMin_RSI("30", GetField("Close","30"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "30分RSI");
        		setplotlabel(2, "30分RSI");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		value1 = xfMin_RSI("60", GetField("Close","60"), Length1);
        		value2 = xfMin_RSI("60", GetField("Close","60"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "60分RSI");
        		setplotlabel(2, "60分RSI");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		value1 = xfMin_RSI("D", GetField("Close","D"), Length1);
        		value2 = xfMin_RSI("D", GetField("Close","D"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "日RSI");
        		setplotlabel(2, "日RSI");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		value1 = xfMin_RSI("AD", GetField("Close","AD"), Length1);
        		value2 = xfMin_RSI("AD", GetField("Close","AD"), Length2);
        		Plot1(value1, "分鐘與日RSI1");
        		Plot2(value2, "分鐘與日RSI2");
        		setplotlabel(1, "還原日RSI");
        		setplotlabel(2, "還原日RSI");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘與日威廉指標(df: pd.DataFrame, Length1: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 分鐘與日威廉指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\分鐘與日威廉指標.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率威廉指標，預設跨頻率為30分
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率60分鐘，跨頻率計算30分鐘威廉技術指標。
        //
        	Length1(14, "天數一"), Length2(28, "天數二"), Length3(42, "天數三"),
        	FreqType("30", "跨頻率週期", inputkind:=dict(["1分鐘","1"],["5分鐘","5"],["10分鐘","10"],["15分鐘","15"],["30分鐘","30"],["60分鐘","60"],["日","D"],["還原日","AD"]));
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("此範例僅支援分鐘、日與還原日頻率");
        value1 = xfMin_PercentR(FreqType, Length1) - 100;
        value2 = xfMin_PercentR(FreqType, Length2) - 100;
        value3 = xfMin_PercentR(FreqType, Length3) - 100;
        Plot1(value1, "分鐘與日威廉指標1");
        Plot2(value2, "分鐘與日威廉指標2");
        Plot3(value3, "分鐘與日威廉指標3");
        // 防呆，大頻率跨小頻率時，在線圖秀不支援
        //
        switch (FreqType)
        begin
        	case  "1":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		if barinterval <> 1 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於1分鐘");
        		setplotlabel(1, "1分威廉指標1");
        		setplotlabel(2, "1分威廉指標2");
        		setplotlabel(3, "1分威廉指標3");
        	case  "5":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於5分鐘");
        		setplotlabel(1, "5分威廉指標1");
        		setplotlabel(2, "5分威廉指標2");
        		setplotlabel(3, "5分威廉指標3");
        	case "10":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於10分鐘");
        		setplotlabel(1, "10分威廉指標1");
        		setplotlabel(2, "10分威廉指標2");
        		setplotlabel(3, "10分威廉指標3");
        	case "15":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於15分鐘");
        		setplotlabel(1, "15分威廉指標1");
        		setplotlabel(2, "15分威廉指標2");
        		setplotlabel(3, "15分威廉指標3");
        	case "30":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於30分鐘");
        		setplotlabel(1, "30分威廉指標1");
        		setplotlabel(2, "30分威廉指標2");
        		setplotlabel(3, "30分威廉指標3");
        	case "60":
        		if barfreq <> "Tick" and barfreq <> "Min" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		if barinterval <> 1 and barinterval <> 2 and barinterval <> 3 and barinterval <> 5 and barinterval <> 10 and barinterval <> 15 and barinterval <> 20 and barinterval <> 30 and barinterval <> 45 and barinterval <> 60 then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於60分鐘");
        		setplotlabel(1, "60分威廉指標1");
        		setplotlabel(2, "60分威廉指標2");
        		setplotlabel(3, "60分威廉指標3");
        	case "D":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於日");
        		setplotlabel(1, "日威廉指標1");
        		setplotlabel(2, "日威廉指標2");
        		setplotlabel(3, "日威廉指標3");
        	case "AD":
        		if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then raiseruntimeerror("不支援大頻率跨小頻率：主頻率大於還原日");
        		setplotlabel(1, "還原日威廉指標1");
        		setplotlabel(2, "還原日威廉指標2");
        		setplotlabel(3, "還原日威廉指標3");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週DMI_Osc(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 週DMI-Osc
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週DMI-Osc.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週DMI-Osc指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日DMI-Osc技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        xf_DirectionMovement("W", Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value - ndi_value, "週DMI-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週DMI(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 週DMI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週DMI.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週DMI指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日DMI技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        xf_DirectionMovement("W", Length, pdi_value, ndi_value, adx_value);
        // 初始區波動較大, 先不繪出
        //
        if CurrentBar < Length then
         begin
        	pdi_value = 0;
        	ndi_value = 0;
        	adx_value = 0;
         end;
        Plot1(pdi_value, "週+DI");
        Plot2(ndi_value, "週-DI");
        Plot3(adx_value, "週ADX");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週KD(df: pd.DataFrame, Length: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 週KD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週KD.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週KD指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日KD技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        xf_stochastic("W", Length, RSVt, Kt, rsv, k, _d);
        Plot1(k, "週K(%)");
        Plot2(_d, "週D(%)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週MACD(df: pd.DataFrame, FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 週MACD
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週MACD.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週MACD指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日MACD技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        xf_macd("W",xf_weightedclose("W"),FastLength,SlowLength,MACDLength,value1,value2,value3);
        // 前面區段資料變動較大, 先不繪出
        //
        if CurrentBar <= SlowLength then
        begin
        	Value1 = 0;
        	Value2 = 0;
        	Value3 = 0;
        end;
        Plot1(Value1, "週DIF");
        Plot2(Value2, "週MACD");
        Plot3(Value3, "週Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週RSI(df: pd.DataFrame, Length1: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: 週RSI
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週RSI.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週RSI指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日RSI技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        Plot1(xf_RSI("W", GetField("Close","W"), Length1), "週RSI1");
        Plot2(xf_RSI("W", GetField("Close","W"), Length2), "週RSI2");        
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 週威廉指標(df: pd.DataFrame, Length1: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: 週威廉指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\跨頻率指標\週威廉指標.xs
        XS Logic Reference:
        {@type:indicator}
        // 跨頻率週威廉指標
        // 不支援大頻率跨小頻率，例如：
        // 不支援主頻率週資料，跨頻率計算日威廉技術指標。
        //
        if barfreq <> "Tick" and barfreq <> "Min" and barfreq <> "D" and barfreq <> "W" and barfreq <> "AD" and barfreq <> "AW" then raiseruntimeerror("不支援大頻率跨小頻率");
        	Length1(14, "天數一"), 
        	Length2(28, "天數二"), 
        	Length3(42, "天數三");
        value1 = xf_PercentR("W", Length1) - 100;
        value2 = xf_PercentR("W", Length2) - 100;
        value3 = xf_PercentR("W", Length3) - 100;
        Plot1(value1, "週威廉指標1");
        Plot2(value2, "週威廉指標2");
        Plot3(value3, "週威廉指標3");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
