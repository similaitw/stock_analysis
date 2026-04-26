# Auto-generated strategies for: 指標/主圖指標
import pandas as pd
import numpy as np

class 主圖指標Strategies:

    @staticmethod
    def BBand軌道線(df: pd.DataFrame, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: BBand軌道線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\BBand軌道線.xs
        XS Logic Reference:
        {@type:indicator}
        	Length(20, "MA的天數"), 
        	UpperBand(2, "上通道標準差倍數"), 
        	LowerBand(2, "下通道標準差倍數");
        up = bollingerband(Close, Length, UpperBand);
        mid = average(close, Length);
        down = bollingerband(Close, Length, -1 * LowerBand);
        plot1(up, "UB");
        plot2(mid, "BBandMA");
        plot3(down, "LB");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CDP(df: pd.DataFrame, plotLen: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: CDP
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\CDP.xs
        XS Logic Reference:
        {@type:indicator}
        {
            PlotLine(PlotIndex, x1, y1, x2, y2, add:=0);
        	    PlotIndex為 1 ~ 999，作用如同 Plot 的序列編號
        		x1 為起點的 Bar Number (可用 CurrentBar 確認)
        		y1 為起點的 Y 軸數值 (ex. 價格)
        		x2 為終點的 Bar Number
        		add 為非必要參數，預設為 0，執行後會先清除之前的趨勢線，若不希望清除的話則可以設為 1。
            CDP指標
            CDP＝(H[1] + L[1] + 2C[1])/4
            AH = CDP + (H[1]-L[1])
        	NH = 2*CDP - L[1]
        	NL = 2*CDP - H[1]
            AL = CDP - (H[1]-L[1])
        	只支援分鐘線
        }
        if BarFreq <> "Min" then RaiseRunTimeError("請跑分鐘頻率");
        //換日時計算當日的CDP數值
        if GetFieldDate("Date") <> GetFieldDate("Date")[1] then begin
            bar_count = 0;
            x1_bar = CurrentBar;
            HH = GetField("High", "D")[1];
            LL = GetField("Low", "D")[1];
            CC = GetField("Close", "D")[1];
            CDP = (HH + LL + 2*CC) / 4;
            AH = CDP + HH - LL;
        	NH = 2*CDP - LL;
        	NL = 2*CDP - HH;
            AL = CDP - (HH - LL);
        end;
        if plotLen = 1 then begin
        	if x1_bar <> 0 then begin
        		PlotLine(1, x1_bar, CDP, CurrentBar, CDP, "CDP", add:=1);
        		PlotLine(2, x1_bar, NH, CurrentBar, NH, "NH", add:=1);
        		PlotLine(3, x1_bar, NL, CurrentBar, NL, "NL", add:=1);
        		PlotLine(4, x1_bar, AH, CurrentBar, AH, "AH", add:=1);
        		PlotLine(5, x1_bar, AL, CurrentBar, AL, "AL", add:=1);
        	    end;
        	end
        else if plotLen = 2 then begin
        	if islastBar then begin
        		PlotLine(1, x1_bar, CDP, CurrentBar, CDP, "CDP");
        		PlotLine(2, x1_bar, NH, CurrentBar, NH, "NH");
        		PlotLine(3, x1_bar, NL, CurrentBar, NL, "NL");
        		PlotLine(4, x1_bar, AH, CurrentBar, AH, "AH");
        		PlotLine(5, x1_bar, AL, CurrentBar, AL, "AL");
        	    end;
        	end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EMA(df: pd.DataFrame, Period1: int = 50, Period2: int = 120, Period3: int = 240) -> tuple[bool, str]:
        """
        Original Strategy: EMA
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\EMA.xs
        XS Logic Reference:
        {@type:indicator}
        Plot1(EMA(Close, Period1), "EMA1");
        Plot2(EMA(Close, Period2), "EMA2");
        Plot3(EMA(Close, Period3), "EMA3");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def SAR(df: pd.DataFrame, AFInitial: float = 0.02) -> tuple[bool, str]:
        """
        Original Strategy: SAR
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\SAR.xs
        XS Logic Reference:
        {@type:indicator}
        	AFInitial(0.02, "加速因子起始值"), 
        	AFIncrement(0.02, "加速因子累加值"), 
        	AFMax(0.2, "加速因子最高值");
        plot1(SAR(AFInitial, AFIncrement, AFMax), "SAR");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def ZigZag(df: pd.DataFrame, zz_deviation: int = 10, zz_depth: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: ZigZag
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\ZigZag.xs
        XS Logic Reference:
        {@type:indicator}
        {
            PlotLine(PlotIndex, x1, y1, x2, y2, add:=0);
        	    PlotIndex為 1 ~ 999，作用如同 Plot 的序列編號
        		x1 為起點的 Bar Number (可用 CurrentBar 確認)
        		y1 為起點的 Y 軸數值 (ex. 價格)
        		x2 為終點的 Bar Number
        		add 為非必要參數，預設為 0，執行後會先清除之前的趨勢線，若不希望清除的話則可以設為 1。
        	繪製zigzag指標
        	指標參數:
        	zz_deviation: 單位是%, 代表每一個波段的滿足幅度, 也就是當某個低點到某個高點的價差%大於這個數值時, 這個就視為一個完整的上漲/下跌波段
        	zz_depth: 多少根bar. 這個數值代表指標區間的高點/低點必須比他的左邊/右邊各zz_depth根bar都來的大/小, 才可以視為一個區間高點/低點
        	一個ZigZag指標, 就是連結區間高點/低點的波段, 且每一個波段的價差必須滿足指定的價差%
        }
        // 底下pv_開頭的這幾個變數, 用來紀錄已經找到的波段
        //
        array: maxmin[2](0);		// 紀錄每根bar所找到的區間高點/低點的bar的位置, maxmin[1]是高點, maxmin[2]是低點
        pivot_updated = false;
        // 找最近一個區間高點/區間低點
        //
        maxmin[1] = SwingHighBar(High, zz_depth + 1, zz_depth, zz_depth, 1);
        maxmin[2] = SwingLowBar(Low, zz_depth + 1, zz_depth, zz_depth, 1);
        // 當遇到一個新的區間高點/低點時, 判斷這個點跟目前的波段(pivot)的關係, 更新pivot, 或是產生新的pivot
        //
        for _i = 1 to 2 begin
        	if maxmin[_i] >= 0 then begin
        		if _i = 1 then is_high = true else is_high = false;
        		if is_high then 
        			p_price = High[maxmin[_i]]
        		else
        			p_price = Low[maxmin[_i]];
        		p_index = CurrentBar - maxmin[_i];    // 轉換成1-based的barIndex
        		// Print("(FindPoint)", NumToStr(Date[maxmin[_i]], 0), NumToStr(p_price, 2), is_high);
        		if pv_count = 0 then begin
        			// 目前還沒有pivot: 先產生一個只有一個點的pivot, 這是第一個pivot
        			//
        			pv_count = 1;
        			pv_start_index = p_index;
        			pv_start_price = p_price;
        			pv_end_index = p_index;
        			pv_end_price = p_price;
        			pv_is_high = is_high;
        			pivot_updated = true;
        		end	else begin		
        			if pv_is_high = is_high then begin
        				// 如果同方向, 而且新的點的價格比上一個pivot的價格更高/更低, 就更新pivot(延伸pivot的長度)
        				//
        				if (is_high and p_price > pv_end_price) or (not is_high and p_price < pv_end_price) then begin
        					if pv_count = 1 then begin
        						// 如果是第一個pivot, 而且還只有一個點, 則讓start/end都挪到新的那個點
        						//
        						pv_start_index = p_index;
        						pv_start_price = p_price;
        					end;
        					pv_end_index = p_index;
        					pv_end_price = p_price;
        					pivot_updated = true;
        				end;
        			end else begin
        				// 如果反方向, 而且新的點產生了價格的轉折, 則產生一個新的pivot(波段)
        				//
        				dev = 100 * (p_price - pv_end_price) / pv_end_price;
        				if (not pv_is_high and dev >= zz_deviation) or (pv_is_high and dev <= -1 * zz_deviation) then begin
        					// 產生新的pivot
        					//
        					pv_count = pv_count + 1;
        					pv_start_index = pv_end_index;
        					pv_start_price = pv_end_price;
        					pv_end_index = p_index;
        					pv_end_price = p_price;
        					pv_is_high = is_high;
        					pivot_updated = true;
        				end;
        			end;       
        			if pivot_updated then begin
        				//Print(
        				//	Text("PLOT(", NumToStr(pv_count, 0), ")"),
        				//	"from",	NumToStr(Date[CurrentBar - pv_start_index], 0), NumToStr(pv_start_price, 2),
        				//	"to", NumToStr(Date[CurrentBar - pv_end_index], 0), NumToStr(pv_end_price, 2),
        				//	pv_is_high
        				//);
        				// 畫出最新一段pivot
        				//
        				if pv_start_index <> pv_end_index then
        					PlotLine(1, pv_start_index, pv_start_price, pv_end_index, pv_end_price, "ZigZag", add:=1);
        				// 只要有更新pivot, 就不再處理另一個方向的區間高點/低點
        				//
        				break;
        			end;
        		end;
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 一目均衡表(df: pd.DataFrame, ConvPeriod: int = 9, BasePeriod: int = 26, LagPeriod: int = 52) -> tuple[bool, str]:
        """
        Original Strategy: 一目均衡表
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\一目均衡表.xs
        XS Logic Reference:
        {@type:indicator}
        // 轉換線
        Value1 = (Highest(High, ConvPeriod) + Lowest(Low, ConvPeriod)) / 2;
        // 樞紐線
        Value2 = (Highest(High, BasePeriod) + Lowest(Low, BasePeriod)) / 2;
        // 先行帶 A
        Value3 = (Value1 + Value2) / 2;
        // 先行帶 B
        Value4 = (Highest(High, LagPeriod) + Lowest(Low, LagPeriod)) / 2;  
        Plot(1, value1, "轉換線");
        Plot(2, value2, "樞紐線");
        Plot(3, Close, "後行時間", shift:=-BasePeriod);
        Plot(4, Value3, "先行時間(1)", shift:=BasePeriod);
        Plot(5, Value4, "先行時間(2)", shift:=BasePeriod);
        if value3 > value4 then begin 
            PlotFill(6, Value3, Value4, shift:=BasePeriod);
        	noplot(7);
        	end
        else begin 
            plotfill(7, Value3, Value4, shift:=BasePeriod);	
        	noplot(6);
        	end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 修正式移動平均線(df: pd.DataFrame, n: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 修正式移動平均線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\修正式移動平均線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min" then
        begin
        	value1=GetField("內盤量");//單位:元
        	value2=GetField("外盤量");//單位:元
        end else begin
        	value1=GetField("內盤量","D");//單位:元
        	value2=GetField("外盤量","D");//單位:元
        end;
        //計算內外盤比
        if value2<>0 then
        	value3=value1/value2*100
        else
        	value3=100;
        if close>close[1] then begin
        	if value3>130 then 
        		w=2.5
        	else if value3>120 then
        		w=2.2
        	else if value3>110 then
        		w=2.1
        	else if value3>100 then
        		w=1.9
        	else
        		w=1.8;
        end else if value3<70 then 
        		w=2.5
        	else if value3<80 then 
        		w=2.2
        	else if value3<90 then 
        		w=2.1
        	else if value3<100 then 
        		w=1.9
        	else
        		w=1.8;
        value4=(w/(n+1))*close+(n-1)/(n+1)*value4[1];
        value5=average(close,n);
        plot2(value5,"移動平均線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 個股儀表板(df: pd.DataFrame, _TEXT1: str = "===============", Length_D: int = 9, _TEXT2: str = "===============", period2: int = 10, _TEXT3: str = "===============", FastLength: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: 個股儀表板
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\個股儀表板.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/打造個股儀表板/
        收錄於「三週學會程式交易：打造你的第一筆自動化交易」 330頁
        https://www.ipci.com.tw/books_in.php?book_id=724
        }
        if barfreq <> "D" then raiseruntimeerror("不支援此頻率");
        condition1=false;
        condition2=false;
        condition3=false;
        condition4=false;
        condition5=false;
        condition6=false;
        condition7=false;
        condition8=false;
        condition9=false;
        condition10=false;
        switch(close)
        begin
        	case >150: value5=low*0.9;
        	case <50 : value5=low*0.98;
        	default: value5=low*0.95;
        end;
        //==========日KD黃金交叉================
        stochastic(Length_D, 3, 3, rsv_d, kk_d, dd_d);
        c5=barslast(kk_d crosses over dd_d);
        if c5=0 and c5[1]>20 then 
        	condition1=true;
        if condition1 then
        	plot1(value5,"月KD高檔鈍化且日KD黃金交叉");
        //============內外盤量比差====================
        value6=GetField("內盤量");//單位:元
        value7=GetField("外盤量");//單位:元
        if volume<>0 then begin
        	value8=value7/volume*100;//外盤量比
        	value9=value6/volume*100;//內盤量比
        end;
        value10=average(value8,5);
        value11=average(value9,5);
        value7=value10-value11+5;
        c3=barslast(value7 crosses over 0);
        if c3=0 and c3[1]>20 then
        	condition2=true;
        if condition2 then
        	plot2(value5*0.99,"內外盤量比差");
        //===========淨力指標==============
        value12=summation(high-close,period2);//上檔賣壓
        value13=summation(close-open,period2); //多空實績
        value14=summation(close-low,period2);//下檔支撐
        value15=summation(open-close[1],period2);//隔夜力道
        if close<>0 then
        	value16=(value13+value14+value15-value12)/close*100;
        c4=barslast(value16 crosses over -4);
        if c4=0 and c4[1]>20 then
        	condition3=true;
        if condition3 then
        	plot3(value5*0.98,"淨力指標");
        //===========多頭起漲前的籌碼收集================
        //狀況1.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量=0，則交易家數相關指標回傳0。
        //狀況2.：如果 K線日期與交易家數相關資料欄位日期不同，並且成交量<>0，則交易家數相關指標正常運算。
        if getfieldDate("date") <> getfieldDate("分公司買進家數") and GetField("成交量") = 0 then value1=GetField("分公司買進家數");
        if getfieldDate("date") <> getfieldDate("分公司賣出家數") and GetField("成交量") = 0 then value2=GetField("分公司賣出家數");
        value3=value2-value1;
        value4=countif(value3>20,10);
        c2=barslast(value4>6);
        if c2=0 and c2[1]>20 then
        	condition4=true;
        if condition4=true then
        	plot4(value5*0.97,"籌碼收集");
        //===========法人同步買超====================
        v1=GetField("外資買賣超");
        v2=GetField("投信買賣超");
        v3=GetField("自營商買賣超");
        c1= barslast(maxlist2(v1,v2,v3)>100);
        if c1=0 and c1[1]>20 then
        	condition5=true;
        if condition5=true then
        	plot5(value5*0.96,"法人同步買超");
        //========DIF-MACD 翻正=============
        MACD(weightedclose(), FastLength, SlowLength,MACDLength, difValue, macdValue, oscValue);
        c6=barslast(oscValue Crosses Above 0);
        if c6=0 and c6[1]>20 then
        	condition6=true;
        if condition6 then
        	plot6(value5*0.95,"DIF-MACD 翻正");
        //========資金流向======================
        m1=GetField("資金流向");
        ma1=average(m1,20)*1.5;
        c7=barslast(m1 crosses over ma1 and close>close[1]);
        if c7=0 and c7[1]>20 then
        	condition7=true;
        if condition7 then
        	plot7(value5*0.94,"資金流向");
        //=========總成交次數================
        t1=GetField("總成交次數","D");
        mat1=average(t1,20)*1.5;
        c8=barslast(t1 crosses over mat1 and close>close[1]);
        if c8=0 and c8[1]>20 then
        	condition8=true;
        if condition8 then 
        	plot8(value5*0.93,"成交次數");
        //=========強弱指標==================
        s1=GetField("強弱指標","D");
        c9=barslast(trueall(s1>0,3));
        if c9=0 and c9[1]>20 then
        	condition9=true;
        if condition9 then
        	plot9(value5*0.92,"強弱指標");
        //============開盤委買================
        b1=GetField("主力買張");
        mab1=average(b1,10);
        c10=barslast(b1 crosses over mab1);
        if c10=0 and c10[1]>10 then
        	condition10=true;
        if condition10 then 
        	plot10(value5*0.91,"主力買張");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內盤成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內盤成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\內盤成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {內盤成本線 = 累計當日賣出金額(元) / 累計當日賣出量*1000, 就是特大+大+中+小, 不分大小單
        支援商品：台股}
        value91 = GetField("買進特大單金額");
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D") + GetField("賣出中單金額","D") + GetField("賣出小單金額","D");
        value2 = GetField("賣出特大單量","D") + GetField("賣出大單量","D") + GetField("賣出中單量","D") + GetField("賣出小單量","D");
        if value2 <> 0 then
        	value3 = value1 / (value2 * 1000)
        else
        	value3 = value3[1];
        plot1(value3,"內盤成本線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 唐奇安通道(df: pd.DataFrame, Period: int = 13) -> tuple[bool, str]:
        """
        Original Strategy: 唐奇安通道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\唐奇安通道.xs
        XS Logic Reference:
        {@type:indicator}
        {
        指標說明
        https://www.xq.com.tw/xstrader/唐奇安通道/
        }
        value1 = Highest(H, period);
        value2 = Lowest(L, period);
        plot1(value1[1],"通道上緣");
        plot2((value1+value2)/2,"通道中線");
        plot3(value2[1],"通道下緣" );
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外盤成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外盤成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\外盤成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {外盤成本線 = 累計當日買進金額(元) / 累計當日買進量*1000, 就是特大+大+中+小, 不分大小單
        支援商品：台股}
        value91 = GetField("買進特大單金額");
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        value1 = GetField("買進特大單金額","D") + GetField("買進大單金額","D") + GetField("買進中單金額","D") + GetField("買進小單金額","D");
        value2 = GetField("買進特大單量","D") + GetField("買進大單量","D") + GetField("買進中單量","D") + GetField("買進小單量","D");
        if value2 <> 0 then
        	value3 = value1 / (value2 * 1000)
        else
        	value3 = value3[1];
        plot1(value3,"外盤成本線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外資均價線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 外資均價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\外資均價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("Volume") > 0 then 
        begin
        	Value5 = GetField("外資買張")*GetField("成交金額")/(GetField("Volume")*1000);
        	Value6 = GetField("外資賣張")*GetField("成交金額")/(GetField("Volume")*1000);
        end else begin
        	Value5 = 0;
        	Value6 = 0;
        end;
        Value1 = summation(Value5, period);
        Value2 = summation(GetField("外資買張"), period);
        Value3 = summation(Value6, period);
        Value4 = summation(GetField("外資賣張"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
        if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;
        Plot1(avg_b, "外資買進均價");
        Plot2(avg_s, "外資賣出均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大戶成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\大戶成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {大戶成本線有兩個線圖, 可以分開勾選, 
        一個是買進成本線, 計算方式都是累計當日大單+特大單的買進金額/買進量
        一個是賣出成本線, 計算方式都是累計當日大單+特大單的賣出金額/買進量
        支援商品：台股}
        value91 = GetField("買進特大單金額");
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        //買進成本
        value1 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
        value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
        if value2 <> 0 then
        	value3 = value1 / (value2*1000)
        else
        	value3 = value3[1];
        //賣出成本
        value11 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
        value21 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
        if value21 <> 0 then 
        	value31 = value11 / (value21*1000)
        else
        	value31 = value31[1];
        plot1(value3,"大戶買進成本線",checkbox:=1);
        plot2(value31,"大戶賣出成本線",checkbox:=1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 寶塔線(df: pd.DataFrame, _len: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 寶塔線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\寶塔線.xs
        XS Logic Reference:
        {@type:indicator}
        SetBackBar(_len);
        if _reversal = 1 then begin
            value1 = highest(high[1], _len);
            value2 = lowest(low[1], _len);
        	end
        else if _reversal = 2 then begin
            value1 = highest(value3[1], _len);
            value2 = lowest(value4[1], _len);
        	end;
        value3 = maxlist(close, close[1]);
        value4 = minlist(close, close[1]);
        if close cross over value1 then begin
            condition1 = True;
        	condition2 = False;
        	end
        else if close cross under value2 then begin
            condition1 = False;
        	condition2 = True;
        	end;
        if currentbar > _len then begin
            if not condition1[1] and condition1 then
        	    _name = "翻紅"
        	else if condition1 then
        	    _name = "續紅"
        	else if not condition2[1] and condition2 then
        	    _name = "翻黑"
        	else if condition2 then
        	    _name = "續黑";
        	if condition1 then 
        	    plotk(1, value4, value3, value4, value3)
        	else if condition2 then
        	    plotk(1, value3, value3, value4, value4);
        	end;
        setplotLabel(1, text(_name));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平均K線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 平均K線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\平均K線.xs
        XS Logic Reference:
        {@type:indicator}
        if currentbar = 1 then
          ha_open = (open + close) / 2
        else
          ha_open = (ha_open[1] + ha_close[1]) / 2;
        ha_close = (open + high + low + close) / 4;
        ha_high = maxlist(high, ha_open, ha_close);
        ha_low = minlist(low, ha_open, ha_close);
        PlotK(1, ha_open, ha_high, ha_low, ha_close, "平均K線");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 平均波幅通道(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 平均波幅通道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\平均波幅通道.xs
        XS Logic Reference:
        {@type:indicator}
        input : length(5);			setinputname(1, "天期");
        input : atrlength(15);		setinputname(2, "ATR天期");
        input : k(1.35);			setinputname(3, "通道常數");
        variable : hband(0),lband(0);  
        hband = average(close,length)+average(truerange,atrlength)*k;  
        lband = average(close,length)-average(truerange,atrlength)*k;  
        plot1(hband, "通道上限");  
        plot2(lband, "通道下限");   
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投信均價線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 投信均價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\投信均價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("Volume") > 0 then 
        begin
        	Value5 = GetField("投信買張")*GetField("成交金額")/(GetField("Volume")*1000);
        	Value6 = GetField("投信賣張")*GetField("成交金額")/(GetField("Volume")*1000);
        end else begin
        	Value5 = 0;
        	Value6 = 0;
        end;
        Value1 = summation(Value5, period);
        Value2 = summation(GetField("投信買張"), period);
        Value3 = summation(Value6, period);
        Value4 = summation(GetField("投信賣張"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
        if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;
        Plot1(avg_b, "投信買進均價");
        Plot2(avg_s, "投信賣出均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投資建議目標價(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投資建議目標價
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\投資建議目標價.xs
        XS Logic Reference:
        {@type:indicator}
        //支援頻率：不定期
        //支援商品 ：美(股票)
        exchange = GetSymbolInfo("交易所");
        if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");
        plot1(getField("投資建議目標價"),"目標價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 散戶成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\散戶成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {散戶成本線內有兩個線圖, 可以分開勾選, 
        一個是散戶買進成本線, 計算方式都是累計當日小單的買進金額/買進量
        一個是散戶賣出成本線, 計算方式都是累計當日小單的賣出金額/買進量
        支援商品：台股}
        value91 = GetField("買進小單金額");
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        //買進成本
        value1 = GetField("買進小單金額","D");
        value2 = GetField("買進小單量","D");
        if value2 <> 0 then
        	value3 = value1 / (value2*1000)
        else
        	value3 = value3[1];
        //賣出成本
        value11 = GetField("賣出小單金額","D");
        value21 = GetField("賣出小單量","D");
        if value21 <> 0 then 
        	value31 = value11 / (value21*1000)
        else
        	value31 = value31[1];
        plot1(value3,"散戶買進成本線",checkbox:=1);
        plot2(value31,"散戶賣出成本線",checkbox:=1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 樂活五線譜(df: pd.DataFrame, period: int = 720) -> tuple[bool, str]:
        """
        Original Strategy: 樂活五線譜
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\樂活五線譜.xs
        XS Logic Reference:
        {@type:indicator}
        array: line_diff[](0);
        Array_SetMaxIndex(line_diff, period);
        linearreg(close,period,0,value2,value3,value4,value5);
        {計算(收盤-迴歸)標準差}
        //先計算區間內的 收盤 - 迴歸 值
        _sum = 0;
        for value1 = 1 to period begin
            line_diff[value1] = close[period - value1] - (value2 * value1 + value4);
        	_sum += close[period - value1] - (value2 * value1 + value4);
        	end;
        // 收盤-迴歸的平均	
        diff_avg = _sum / period;
        //計算標準差
        _sum = 0;
        for value1 = 1 to period begin
            _sum += power((line_diff[value1] - diff_avg), 2);
        	end;
        value6 = squareroot(_sum / period);
        value7=value5+value6;
        value8=value5+2*value6;
        value9=value5-value6;
        value10=value5-2*value6;
        plot1(value8,"+2SD");
        plot2(value7,"+1SD");
        plot3(value5,"TL");
        plot4(value9,"-1SD");
        plot5(value10,"-2SD");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 樂活五線譜_趨勢線(df: pd.DataFrame, length: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 樂活五線譜_趨勢線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\樂活五線譜_趨勢線.xs
        XS Logic Reference:
        {@type:indicator}
        {
            PlotLine(PlotIndex, x1, y1, x2, y2, add:=0);
        	    PlotIndex為 1 ~ 999，作用如同 Plot 的序列編號
        		x1 為起點的 Bar Number (可用 CurrentBar 確認)
        		y1 為起點的 Y 軸數值 (ex. 價格)
        		x2 為終點的 Bar Number
        		add 為非必要參數，預設為 0，執行後會先清除之前的趨勢線，若不希望清除的話則可以設為 1。
        	樂活五線譜是由「股息現金流被動收入理財的心路歷程」已故的版主 Allan Lin（艾倫）醫師改良曾淵滄博士的曾氏通道，
        	以原始價格取代對數值，同樣以 5 條平衡線作參考，分別為極度樂觀線（95% 樂觀線），過度樂觀線（75% 樂觀線），
        	中線（長期走勢線），過度悲觀線（75% 悲觀線）和極度悲觀線（95% 悲觀線）。
        	樂活五線譜的形成，是以統計學的方法來計算一段時間（預設為 3.5 年）的平均價格，並畫出一條股價趨勢線，
        	然從趨勢線的上方和下方各加上一個標準差以及兩個標準差而形成的五條線。
        	在這個腳本範例內，使用者可以指定統計天期（從最新一期往回統計N筆K線資料)，之後會畫出從統計起點到最新一根K線
        	所算出來的5條樂活通道線，分別是：
        	TL = 從統計起點到最新一根K線的線性回歸線(以每根K棒的Close價格統計)
            SDP1 = 往上一個標準差 
        	SDP2 = 往上兩個標準差
            SDM1 = 往下一個標準差
        	SDM2 = 往下兩個標準差 
        }
        array: diff_array[](0);
        if CurrentBar = GetTotalBar() and CurrentBar >= length then begin
            LinearReg(Close, length, length, lr_slope, lr_deg, lr_intercept, lr_forecast);
        	// 統計每個收盤價到回歸線的距離並計算平均值
        	//
            Array_SetMaxIndex(diff_array, length);
        	diff_avg = 0;
            for idx = 1 to length begin
                diff_array[idx] = Close[length - idx] - (lr_intercept + lr_slope * idx);
        		diff_avg = diff_avg + diff_array[idx];
            end;
        	diff_avg = diff_avg / length;
        	// 計算回歸線與收盤價差距的標準差
        	//
        	Value1 = 1;
            for idx = 1 to length begin
        		Value1 += power((diff_array[idx] - diff_avg), 2);	
        	end;	
        	std = SquareRoot(Value1 / length);
            // 每次價格更新時會重畫, 產生新的bar時也會重畫
            //
        	last_y = Close - diff_array[length];
            PlotLine(1, 
               CurrentBar-length, lr_forecast, 
               CurrentBar, last_y, "TL");
            PlotLine(2,
               CurrentBar-length, lr_forecast+std, 
               CurrentBar, last_y+std, "SDP1");
            PlotLine(3,
               CurrentBar-length, lr_forecast+2*std, 
               CurrentBar, last_y+2*std, "SDP2");
            PlotLine(4,
               CurrentBar-length, lr_forecast-std, 
               CurrentBar, last_y-std, "SDM1");
            PlotLine(5,
               CurrentBar-length, lr_forecast-2*std, 
               CurrentBar, last_y-2*std, "SDM2");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 權益線分析(df: pd.DataFrame, Update: str = "-1") -> tuple[bool, str]:
        """
        Original Strategy: 權益線分析
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\權益線分析.xs
        XS Logic Reference:
        {@type:indicator}
        array:peak[300,5](0);
        if currentbar = 1 then begin 
        	iHigh =high; 
        	iDate =Date; 
        	value1=open; 
        end;
        hHigh = maxlist(high,hHigh); 
        if hHigh > iHigh  then begin
        	if iHigh <> iLow then begin
        		peak[pc,0] = date;
        		peak[pc,1] = iHigh;
        		peak[pc,2] = iLow;
        		peak[pc,3] = (iHigh- iLow)/iHigh*100;
        		peak[pc,4] = datediff(date,iDate);
        		if pc > 0  and peak[pc-1,2] <> 0 then peak[pc,5] = (iHigh/ peak[pc-1,2]-1)*100;
        		pc+=1;
        	end;
        	iHigh =hHigh;
        	iLOw = hHigh;
        	iDate =Date;
        end else 
        	iLow =minlist(Low,iLow);
        if  DateDiff(currentdate,date) > update and value1 > 0 and pc > 1 then begin
        	summ=0; 
        	for value2 = 1 to pc -1  
        		summ += peak[value2,3]; 
        	avg=summ/(pc-1);
        	summeans=0;
        	for value2 = 1 to pc -1 begin
        		summeans += square(peak[value2,3]-avg);
        	end;
        	if pc-1 > 0 then 
        		stdev = squareroot( summeans/(pc-1)) 
        	else 
        		stdev=0;
        	poLow = iHigh*(1- (avg+stdev)/100);
        	if Close < PoLow then msg ="Sell";
        end;
        if date <>currentdate then ALow =Polow;
        if C > alow and ALow > 0 then  plot1(Alow,"95%CF");  //95%信心水準回檔最大值
        if C > iHigh*0.86 then begin
        	plot3(iHigh*0.92,"N1D"); //第1減碼線
        	plot4(iHigh*0.86,"N2D"); //第2減碼線
        end;
        plot5(Close,"現價");
        plot6(V,"成交量");
        ND=100*(average(H/L-1,20)+standarddev(H/L-1,20,1)*3);
        if ND < 3 and trueall(ND[1]> 3,5) then  EP=h;
        if ND < 5 and trueall(ND[1]> 5,5) then EP=h;
        if c > EP and c[1] < EP then plot8(v,"作多點量");
        if EP > 0 then plot9(EP,"關鍵價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日成本線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 當日成本線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\當日成本線.xs
        XS Logic Reference:
        {@type:indicator}
        {均線 = 當日所有成交Tick的平均價格(sum(pv)/sum(v)), 也就是當日的成本
        支援商品：台股/期貨/選擇權/陸股/港股/美股/大盤/類股}
        if barfreq <> "Min" and barfreq <> "D" then 
        	raiseruntimeerror("僅支援分鐘與日頻率");
        plot1(GetField("均價"),"均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 肯特納通道(df: pd.DataFrame, Length: int = 20, UpperBand: int = 2, LowerBand: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 肯特納通道
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\肯特納通道.xs
        XS Logic Reference:
        {@type:indicator}
        variable : hband(0),lband(0),midline(0); 
        midline = XAverage(close, Length);
        hband = midline + ATR(Length) * UpperBand;
        lband = midline - ATR(Length) * LowerBand;
        Plot1(hband, "UB");
        Plot2(midline, "KeltnerMA");
        Plot3(lband, "LB");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自營商均價線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 自營商均價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\自營商均價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("Volume") > 0 then 
        begin
        	Value5 = GetField("自營商買張")*GetField("成交金額")/(GetField("Volume")*1000);
        	Value6 = GetField("自營商賣張")*GetField("成交金額")/(GetField("Volume")*1000);
        end else begin
        	Value5 = 0;
        	Value6 = 0;
        end;
        Value1 = summation(Value5, period);
        Value2 = summation(GetField("自營商買張"), period);
        Value3 = summation(Value6, period);
        Value4 = summation(GetField("自營商賣張"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg_b = Value1 / Value2;
        if Value4 > 0 and Value4 <> Value4[1]  then avg_s = Value3 / Value4;
        Plot1(avg_b, "自營商買進均價");
        Plot2(avg_s, "自營商賣出均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 處置期間(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 處置期間
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\處置期間.xs
        XS Logic Reference:
        {@type:indicator}
        if BarFreq <> "d" and BarFreq <> "ad" then raiseruntimeerror("僅支援日與還原日頻率");
        value1 = GetField("處置開始日期");
        value2 = GetField("處置結束日期");
        value3 = getField("Date");
        if value1 = 0 then raiseruntimeerror("無處置的歷史紀錄");
        //用點顯示處置區間
        if value3 >= value1 and value3 <= value2 then plot1(value1,"處置中") //尚在處置中
        else noplot(1);
        //用來顯示處置相關的日期數值
        if value1 <> value1[1] or (value3 >= value1 and value3 <= value2) then begin
        	plot3(value1,"開始日期");
        	plot4(value2,"結束日期");
        end else begin
        	noplot(3);
        	noplot(4);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融券均價線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 融券均價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\融券均價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("Volume") > 0 then 
        	Value3 = GetField("融券賣出張數")*GetField("成交金額")/(GetField("Volume")*1000)
        else
        	Value3 = 0;
        Value1 = summation(Value3, period);
        Value2 = summation(GetField("融券賣出張數"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg = Value1 / Value2;
        Plot1(avg, "融券賣出均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 融資均價線(df: pd.DataFrame, period: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 融資均價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\融資均價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq = "Tick" or barfreq = "Min"
        	then raiseruntimeerror("不支援此頻率");
        if GetField("Volume") > 0 then 
        	Value3 = GetField("融資買進張數")*GetField("成交金額")/(GetField("Volume")*1000)
        else
        	Value3 = 0;
        Value1 = summation(Value3, period);
        Value2 = summation(GetField("融資買進張數"), period);
        if Value2 > 0 and Value2 <> Value2[1] then avg = Value1 / Value2;
        Plot1(avg, "融資買進均價");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 趨勢線(df: pd.DataFrame, periods: int = 30, startyear: int = 2017) -> tuple[bool, str]:
        """
        Original Strategy: 趨勢線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\趨勢線.xs
        XS Logic Reference:
        {@type:indicator}
        // 起始年之前的資料不計算
        if year(date) < startyear then return;
        // 如果已經有趨勢線的話, 檢查是否突破
        if base_bar > 0 then begin
        	temp_y = line_a * (currentbar - base_bar) + line_b;
        	if high > temp_y then 
        		plot1(high) 
        	else 
        		noplot(1);	
        end;
        // 計算過去N期的趨勢線
        maxh_bar = nthhighestbar(1, high, periods);
        base_bar = 0;	// 用來追蹤最近一個趨勢線的x=0的位置
        idx = maxh_bar-1;
        while idx >= 0 begin
        	// 畫一條曲線從maxh_bar to idx, 假設maxh_bar的位置x=0
        	//
        	// x0 = 0, y0 = high[maxh_bar] == b
        	// x1 = maxh_bar - idx, y1 = high[idx]
        	//
        	line_b = high[maxh_bar];
        	line_a = (high[idx] - line_b) / (maxh_bar - idx);
        	x_bar = idx;
        	// 檢查是否所有的點都落在這條切線底下
        	//
        	condition1 = false;
        	for idx2 = maxh_bar - 1 downto 0 begin
        		// x = maxh_bar - idx2
        		//
        		temp_y = line_a * (maxh_bar - idx2) + line_b;
        		if high[idx2] > temp_y then begin
        			condition1 = true;
        			break;
        		end;
        	end;
        	if not condition1 then begin
        		base_bar = currentbar - maxh_bar;
        		break; 
        	end;
            idx = idx - 1;	
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開盤第N根的每日高低價線(df: pd.DataFrame, Length: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 開盤第N根的每日高低價線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\主圖指標\開盤第N根的每日高低價線.xs
        XS Logic Reference:
        {@type:indicator}
        if barfreq <> "Min" then raiseRunTimeError("僅支援分鐘頻率");
        if Length = 0 then raiseRunTimeError("參數請設定大於0的合理數值");
        if gettotalBar = currentBar and Length - 1 > _MaxCDN then raiseRunTimeError("參數設定超過每日分鐘K棒數");
        if getfieldDate("date") <> getfieldDate("date")[1] then 
        	_ChageDNum = 0
        else begin
        	_ChageDNum += 1;
        end;
        if _ChageDNum > _MaxCDN then _MaxCDN = _ChageDNum;
        if _ChageDNum < Length - 1  then begin
        	NoPlot(1);
        	NoPlot(2);
        	NoPlot(3);
        end else if _ChageDNum = Length - 1  then begin
        	_MH = GetField("最高價", "D");
        	_ML = GetField("最低價", "D");
        	_HHMMSS = time;
        	plot1(_HHMMSS,"時間");
        	plot2(_MH,"最高價");
        	plot3(_ML,"最低價");
        end else begin
        	plot1(_HHMMSS,"時間");
        	plot2(_MH,"最高價");
        	plot3(_ML,"最低價");
        end;
        setplotLabel(1,Text("第",NumToStr(Length, 0),"根時間"));
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
