# Auto-generated strategies for: 指標/即時籌碼
import pandas as pd
import numpy as np

class 即時籌碼Strategies:

    @staticmethod
    def 分時大戶買賣力_金額_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時大戶買賣力(金額)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時大戶買賣力(金額).xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："大戶單=特大單+大單資料為分鐘統計金額"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出特大單金額");
        value1 = GetField("賣出特大單金額") + GetField("賣出大單金額");
        value2 = GetField("買進特大單金額") + GetField("買進大單金額");
        value3 = value2 - value1;
        plot1(value3,"大戶買賣力(金額)");
        plot2(value2,"大戶外盤量(金額)",checkbox:=0);
        plot3(value1,"大戶內盤量(金額)",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分時大戶買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時大戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時大戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："大戶單=特大單+大單資料為分鐘統計張數"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value1 = GetField("賣出特大單量") + GetField("賣出大單量");
        value2 = GetField("買進特大單量") + GetField("買進大單量");
        value3 = value2 - value1;
        plot1(value3,"大戶買賣力");
        plot2(value2,"大戶外盤量",checkbox:=0);
        plot3(value1,"大戶內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分時散戶買賣力_金額_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時散戶買賣力(金額)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時散戶買賣力(金額).xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："散戶單=小單資料為分鐘統計金額"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出小單金額");
        value1 = GetField("賣出小單金額");
        value2 = GetField("買進小單金額");
        value3 = value2 - value1;
        plot1(value3,"散戶買賣力(金額)");
        plot2(value2,"散戶外盤量(金額)",checkbox:=0);
        plot3(value1,"散戶內盤量(金額)",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分時散戶買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時散戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時散戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："散戶單=小單資料為分鐘統計張數"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出小單量");
        value1 = GetField("賣出小單量");
        value2 = GetField("買進小單量");
        value3 = value2 - value1;
        plot1(value3,"散戶買賣力"); 
        plot2(value2,"散戶外盤量",checkbox:=0); 
        plot3(value1,"散戶內盤量",checkbox:=0); 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分時漲跌成交量(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時漲跌成交量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時漲跌成交量.xs
        XS Logic Reference:
        {@type:indicator}
        {支援商品類型：台股/期權/選擇權/大盤/類股指數}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value1 = GetField("上漲量");
        value2 = GetField("下跌量");
        value3 = value1 - value2;
        plot1(value3,"漲跌成交(分時)");
        plot2(value1,"上漲量",checkbox:=0);
        plot3(value2,"下跌量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分時買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 分時買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\分時買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {支援商品：指數/台股/期貨/選擇權}
        if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
        if SymbolType <> 1 and SymbolType <> 2 and SymbolType <> 3 and SymbolType <> 5 then raiseruntimeerror("不支援此商品");
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value1 = GetField("外盤量");
        value2 = GetField("內盤量");
        value3 = value1 - value2;
        plot1(value3,"買賣力");
        plot2(value1,"外盤量",checkbox:=0);
        plot3(value2,"內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶散戶籌碼流向_金額_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大戶散戶籌碼流向(金額)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\大戶散戶籌碼流向(金額).xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："大戶=特大單+大單, 散戶=小單 
        資料為大戶/散戶從開盤累計到現在的(外盤-內盤)金額"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出特大單金額");
        value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
        value2 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
        value3 = value2 - value1;
        value11 = GetField("賣出小單金額","D");
        value21 = GetField("買進小單金額","D");
        value31 = value21 - value11;
        plot1(value3,"大戶買賣力(金額)");
        plot2(value31,"散戶買賣力(金額)");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶散戶籌碼流向(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大戶散戶籌碼流向
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\大戶散戶籌碼流向.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："大戶=特大單+大單, 散戶=小單 
        資料為大戶/散戶從開盤累計到現在的(外盤-內盤)張數"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出特大單量");
        value1 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
        value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
        value3 = value2 - value1;
        value11 = GetField("賣出小單量","D");
        value21 = GetField("買進小單量","D");
        value31 = value21 - value11;
        plot1(value3,"大戶買賣力");
        plot2(value31,"散戶買賣力");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶買賣力_金額_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大戶買賣力(金額)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\大戶買賣力(金額).xs
        XS Logic Reference:
        {@type:indicator}
        {大戶買賣力(金額)是特大單金額+大單金額，資料為開盤迄今的累計
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出特大單金額");
        value1 = GetField("賣出特大單金額","D") + GetField("賣出大單金額","D");
        value2 = GetField("買進特大單金額","D") + GetField("買進大單金額","D");
        value3 = value2 - value1;
        plot1(value3,"大戶買賣力(金額)");
        plot2(value2,"大戶外盤金額",checkbox:=0);
        plot3(value1,"大戶內盤金額",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大戶買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 大戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\大戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {"大戶=特大單+大單，資料為開盤迄今的累計張數"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出特大單量");
        value1 = GetField("賣出特大單量","D") + GetField("賣出大單量","D");
        value2 = GetField("買進特大單量","D") + GetField("買進大單量","D");
        value3 = value2 - value1;
        plot1(value3,"大戶買賣力");
        plot2(value2,"大戶外盤量",checkbox:=0);
        plot3(value1,"大戶內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買賣力_金額_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 散戶買賣力(金額)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\散戶買賣力(金額).xs
        XS Logic Reference:
        {@type:indicator}
        {散戶買賣力(金額)是小單金額，資料為開盤迄今的累計
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出小單金額");
        value1 = GetField("賣出小單金額","D");
        value2 = GetField("買進小單金額","D");
        value3 = value2 - value1;
        plot1(value3,"散戶買賣力(金額)"); //bar，axis2
        plot2(value2,"散戶外盤金額",checkbox:=0); //line，axis11
        plot3(value1,"散戶內盤金額",checkbox:=0); //line，axis11
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 散戶買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 散戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\散戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義："散戶單=小單資料為開盤迄今的累計張數"
        支援商品：台(股票)}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("賣出小單量");
        value1 = GetField("賣出小單量","D");
        value2 = GetField("買進小單量","D");
        value3 = value2 - value1;
        plot1(value3,"散戶買賣力"); //bar，axis2
        plot2(value2,"散戶外盤量",checkbox:=0); //line，axis11
        plot3(value1,"散戶內盤量",checkbox:=0); //line，axis11
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 流動大戶買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 流動大戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\流動大戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {近15分鐘累計的(買進大單量+買進特大單量)-(賣出大單量+賣出特大單量)
        抓近15分鐘的目的是希望可以看到最近的買賣力。}
        array:_ArrayLarge[15](0),_ArraySmall[15](0);
        if barfreq <> "Min" or barinterval <> 1 then 
        	raiseruntimeerror("僅支援 1 分鐘頻率");
        //初始化
        if getfieldDate("Date") <> getfieldDate("Date")[1] then begin
        	_Count = 0;
        	Array_SetValRange(_ArrayLarge, 1, 15, 0);
        	Array_SetValRange(_ArraySmall, 1, 15, 0);
        	value3 = 0;
        	value99 = 0;
        end else begin
        	_Count += 1;
        end;
        value99 = mod(_count,15) + 1;
        _ArrayLarge[value99] = GetField("買進大單量", "1") + GetField("買進特大單量", "1");
        _ArraySmall[value99] = GetField("賣出大單量", "1") + GetField("賣出特大單量", "1");
        value1 = Array_Sum(_ArrayLarge, 1, 15);
        value2 = Array_Sum(_ArraySmall, 1, 15);
        value3 = value1 - value2;
        plot1(value3,"流動大戶買賣力");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 漲跌成交量(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 漲跌成交量
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\漲跌成交量.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義：(上漲)量 = 開盤累計到目前比前一價(上漲)的成交量的加總
        支援商品：台股,大盤,類股,期貨,選擇權}
        if barfreq <> "Min" and barfreq <> "D" and barfreq <> "AD" then 
        	raiseruntimeerror("僅支援分鐘與日頻率（含還原）");
        value91 = GetField("上漲量");
        value1 = GetField("上漲量","D");
        value2 = GetField("下跌量","D");
        value3 = value1 - value2;
        plot1(value3,"漲跌成交");
        plot2(value1,"上漲量",checkbox:=0);
        plot3(value2,"下跌量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自訂大戶買賣力(df: pd.DataFrame, threshold: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 自訂大戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\自訂大戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義：主力 = 成交單量 >= X的委託由Tick資料去累積計算
        支援商品：台(股票)、台(期貨)}
        value91 = GetField("上漲量");
        if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
        if SymbolType <> 2 and SymbolType <> 3 then raiseruntimeerror("不支援此商品");
        if barfreq <> "Min" then 
        	raiseruntimeerror("僅支援分鐘頻率");
        {
        	顯示開盤迄今的累計外盤大單 - 累計內盤大單, 也就是盤中大戶的買賣力趨勢
        	大單定義: 成交單量 > X
        }
        if getfielddate("date") <> _last_date then begin
        	_last_date = getfielddate("date");
        	_v_buy_acc = 0;
        	_v_sell_acc = 0;
        	_last_seq = 0;
        end;
        // 抓洗價當時最新一筆Tick的位置跟日期
        //
        _cur_seq = GetField("SeqNo", "Tick");
        _curbar_date = GetField("Date", "Tick");
        if symbolexchange = "TW" and SymbolType = 2 then begin	//台(股票)
        	if _curbar_date <> date then begin
        		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
        		//
        		_cur_seq = 0;
        	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
        		// _last_seq是上一次畫圖時最後一筆Tick的位置
        		//
        		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
        		//
        		_i = _last_seq + 1;	
        		while _i <= _cur_seq begin
        			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
        			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
        			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
        			//-------------------------------------------------
        			// multitick的處理
        			//
        			// TickGroup回傳以下數值
        			//  -1 = 集合競價(每天第一盤, 最後一盤, 包含暫緩之後的搓合, etc.) 
        			//	0 = 逐筆搓合單筆
        			//	1 = 逐筆搓合開始
        			//  2 = 逐筆搓合中間
        			//  3 = 逐筆搓合結束
        			//
        			value5 = GetField("TickGroup", "Tick")[_cur_seq - _i];
        			tv = value3;
        			_complete = 0;
        			if value5 = -1 then begin
        				// 集合競價: 不列入統計
        				_i = _i + 1;
        				tv = 0;
        			end else if value5 = 0 then begin
        				// 獨立一筆: 列入統計
        				_i = _i + 1;
        			end else if value5 = 1 then begin
        				// 把連續撮合的所有資料合併成一筆統計
        				// 連續撮合的第一筆 = 1, 中間 = 2, 最後 = 3
        				_first = _i;
        				_i = _i + 1;
        				while _i <= _cur_seq and _complete = 0 begin
        					value99 = GetField("Time", "Tick")[_cur_seq - _i];			// 價格
        					value22 = GetField("Close", "Tick")[_cur_seq - _i];			// 價格
        					value33 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        					value44 = GetField("SeqNo", "Tick")[_cur_seq - _i];			// Seq
        					value55 = GetField("TickGroup", "Tick")[_cur_seq - _i];
        					tv = tv + value33;
        					_i = _i + 1;
        					if value55 = 3 then _complete = 1;
        				end;
        				if _complete = 0 then begin
        					// 有可能交易所還沒有傳送完整的連續撮合Ticks, 所以等下一次洗價時再處理
        					//
        					_cur_seq = _first;
        					break;
        				end;
        			end else begin	
        				// 異常狀況: 跳過
        				_i = _i + 1;
        			end;	
        			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
        			//
        			if tv > threshold then begin
        				if value1 = 1 then _v_buy_acc = _v_buy_acc + tv;
        				if value1 = -1 then _v_sell_acc = _v_sell_acc + tv;
        			end;	
        		end;
        	end;
        end;
        if symbolexchange = "TF" and SymbolType = 3 then begin	//台(期貨)
        	if _curbar_date <> date then begin
        		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
        		//
        		_cur_seq = 0;
        	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
        		// _last_seq是上一次畫圖時最後一筆Tick的位置
        		//
        		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
        		//
        		_i = _last_seq + 1;	
        		while _i <= _cur_seq begin
        			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
        			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
        			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
        			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
        			//
        			if value3 >= threshold then begin
        				if value1 = 1 then _v_buy_acc = _v_buy_acc + value3;
        				if value1 = -1 then _v_sell_acc = _v_sell_acc + value3;
        			end;	
        			_i = _i + 1;
        		end;
        	end;
        end;
        _last_seq = _cur_seq;
        plot1(_v_buy_acc - _v_sell_acc, "大戶買賣力(自訂)");
        plot2(_v_buy_acc, "大戶(自訂)外盤量",checkbox:=0);
        plot3(_v_sell_acc, "大戶(自訂)內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 自訂散戶買賣力(df: pd.DataFrame, threshold: int = 30) -> tuple[bool, str]:
        """
        Original Strategy: 自訂散戶買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\自訂散戶買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義：散戶 = 成交單量 < X的委託由Tick資料去累計計算
        支援商品：台(股票)、台(期貨)}
        if symbolexchange <> "TW" and symbolexchange <> "TF" then raiseruntimeerror("不支援此商品");
        if SymbolType <> 2 and SymbolType <> 3 then raiseruntimeerror("不支援此商品");
        if barfreq <> "Min" then 
        	raiseruntimeerror("僅支援分鐘頻率");
        value91 = GetField("上漲量");
        {
        	顯示開盤迄今的累計外盤小單 - 累計內盤小單, 也就是盤中散戶的買賣力趨勢
        	小單定義: 成交單量 <= X
        }
        if getfielddate("date") <> _last_date then begin
        	_last_date = getfielddate("date");
        	_v_buy_acc = 0;
        	_v_sell_acc = 0;
        	_last_seq = 0;
        end;
        // 抓洗價當時最新一筆Tick的位置跟日期
        //
        _cur_seq = GetField("SeqNo", "Tick");
        _curbar_date = GetField("Date", "Tick");
        if symbolexchange = "TW" and SymbolType = 2 then begin	//台(股票)
        	if _curbar_date <> date then begin
        		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
        		//
        		_cur_seq = 0;
        	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
        		// _last_seq是上一次畫圖時最後一筆Tick的位置
        		//
        		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
        		//
        		_i = _last_seq + 1;	
        		while _i <= _cur_seq begin
        			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
        			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
        			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
        			//-------------------------------------------------
        			// multitick的處理
        			//
        			// TickGroup回傳以下數值
        			//  -1 = 集合競價(每天第一盤, 最後一盤, 包含暫緩之後的搓合, etc.) 
        			//	0 = 逐筆搓合單筆
        			//	1 = 逐筆搓合開始
        			//  2 = 逐筆搓合中間
        			//  3 = 逐筆搓合結束
        			//
        			value5 = GetField("TickGroup", "Tick")[_cur_seq - _i];
        			tv = value3;
        			_complete = 0;
        			if value5 = -1 then begin
        				// 集合競價: 不列入統計
        				_i = _i + 1;
        				tv = 0;
        			end else if value5 = 0 then begin
        				// 獨立一筆: 列入統計
        				_i = _i + 1;
        			end else if value5 = 1 then begin
        				// 把連續撮合的所有資料合併成一筆統計
        				// 連續撮合的第一筆 = 1, 中間 = 2, 最後 = 3
        				_first = _i;
        				_i = _i + 1;
        				while _i <= _cur_seq and _complete = 0 begin
        					value99 = GetField("Time", "Tick")[_cur_seq - _i];			// 價格
        					value22 = GetField("Close", "Tick")[_cur_seq - _i];			// 價格
        					value33 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        					value44 = GetField("SeqNo", "Tick")[_cur_seq - _i];			// Seq
        					value55 = GetField("TickGroup", "Tick")[_cur_seq - _i];
        					tv = tv + value33;
        					_i = _i + 1;
        					if value55 = 3 then _complete = 1;
        				end;
        				if _complete = 0 then begin
        					// 有可能交易所還沒有傳送完整的連續撮合Ticks, 所以等下一次洗價時再處理
        					//
        					_cur_seq = _first;
        					break;
        				end;
        			end else begin	
        				// 異常狀況: 跳過
        				_i = _i + 1;
        			end;	
        			// 如果小於門檻, 則依照外盤/內盤分別累計(成交量)
        			//
        			if tv <= threshold then begin
        				if value1 = 1 then _v_buy_acc = _v_buy_acc + tv;
        				if value1 = -1 then _v_sell_acc = _v_sell_acc + tv;
        			end;	
        		end;
        	end;	
        end;
        if symbolexchange = "TF" and SymbolType = 3 then begin	//台(期貨)
        	if _curbar_date <> date then begin
        		// 如果開盤到有某些分鐘沒有成交, 此時會對到昨日之前的Tick => 這些分鐘不要計算
        		//
        		_cur_seq = 0;
        	end else if _cur_seq > 0 and _cur_seq > _last_seq then begin
        		// _last_seq是上一次畫圖時最後一筆Tick的位置
        		//
        		// 所以就統計 _cur_seq .. _last_seq之間的Tick的成交資料
        		//
        		_i = _last_seq + 1;	
        		while _i <= _cur_seq begin
        			value1 = GetField("BidAskFlag", "Tick")[_cur_seq - _i];	// 外盤=1, 內盤=-1
        			value2 = GetField("Close", "Tick")[_cur_seq - _i];		// 價格
        			value3 = GetField("Volume", "Tick")[_cur_seq - _i];		// 單量
        			value4 = GetField("SeqNo", "Tick")[_cur_seq - _i];		// Tick編號
        			// 如果超過門檻, 則依照外盤/內盤分別累計(成交量)
        			//
        			if value3 < threshold then begin
        				if value1 = 1 then _v_buy_acc = _v_buy_acc + value3;
        				if value1 = -1 then _v_sell_acc = _v_sell_acc + value3;
        			end;	
        			_i = _i + 1;
        		end;
        	end;
        end;
        _last_seq = _cur_seq;
        plot1(_v_buy_acc - _v_sell_acc, "散戶買賣力(自訂)");
        plot2(_v_buy_acc, "大戶(自訂)外盤量",checkbox:=0);
        plot3(_v_sell_acc, "大戶(自訂)內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 買賣力(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 買賣力
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\即時籌碼\買賣力.xs
        XS Logic Reference:
        {@type:indicator}
        {指標數值定義：(外盤)量 = 開盤累計到目前的(外盤)成交量
        支援商品：台股/期貨/選擇權}
        value91 = GetField("外盤量");
        value1 = GetField("外盤量","D");
        value2 = GetField("內盤量","D");
        value3 = value1 - value2;
        plot1(value3,"買賣力");
        plot2(value1,"外盤量",checkbox:=0);
        plot3(value2,"內盤量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
