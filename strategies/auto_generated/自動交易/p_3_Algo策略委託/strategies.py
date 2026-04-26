# Auto-generated strategies for: 自動交易/3-Algo策略委託
import pandas as pd
import numpy as np

class Cat3Algo策略委託Strategies:

    @staticmethod
    def strategy_01_定時定量交易(df: pd.DataFrame, order_interval: int = 60, order_qty: int = 1, order_bs: int = 1, order_count: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 01-定時定量交易
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\3-Algo策略委託\01-定時定量交易.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	定時定量: 每隔多久送出一筆委託, 下多少筆之後就停止
        	輸入參數:
        	- 下單間隔 (order_interval: 每隔幾(秒)送出一筆委託)
        	- 下單數量 (order_qty: 每一筆委託的數量)
        	- 買賣方向 (order_bs: 1=買進, -1=賣出)
        	- 委託筆數 (order_count: 總共要送出幾筆)	
        }
        { 
        	範例:
        	策略一啟動就啟動定時定量交易, 全部送完就停止
        }
        if not exec_order_started and GetInfo("TradeMode") = 1 then begin
        	exec_order_started = true;		{ 啟動定時定量委託 }
        	exec_order_count = 0;
        	exec_order_lasttime = 0;
        end;
        { 定時定量的執行邏輯 }
        if exec_order_started and exec_order_count < order_count then begin
        	if exec_order_lasttime = 0 or TimeDiff(CurrentTime, exec_order_lasttime, "S") >= order_interval then begin
        		{ 執行委託 }
        		Print("order_bs=", order_bs, "order_qty=", order_qty);
        		SetPosition(position + order_bs * order_qty);			{ TODO: 請填入委託價格 }
        		exec_order_count = exec_order_count + 1;
        		exec_order_lasttime = CurrentTime;
        	end;
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_時間權重交易_TWAP_(df: pd.DataFrame, order_duration: int = 3600, order_totalqty: int = 100, order_bs: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 02-時間權重交易(TWAP)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\3-Algo策略委託\02-時間權重交易(TWAP).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	時間權重(TWAP): 類似定時定量交易, 差異是傳入的是執行委託總時間以及委託總數量, 由腳本自己反推算委託間隔/每次委託數量.
        	輸入參數:
        	- 下單總時間 (order_duration: 在未來的幾(秒)內要執行完畢)
        	- 下單總數量 (order_totalqty: 委託的總數量)
        	- 買賣方向 (order_bs: 1=買進, -1=賣出)
        	把預期委託數量平均分配在指定的時間範圍內, 例如指定在未來的60分鐘內買進100張
        }
        { 
        	範例:
        	策略一啟動就啟動定時定量交易, 全部送完就停止
        }
        if not exec_order_started and GetInfo("TradeMode") = 1 then begin
        	exec_order_started = true;		{ 啟動定時定量委託 }
        	exec_order_starttime = CurrentTime;
        	exec_order_startposition = Position;
        	exec_order_endposition = Position + order_bs * order_totalqty;
        end;
        { 時間權重的執行邏輯 }
        if exec_order_started and Position <> exec_order_endposition then begin
        	duration = TimeDiff(CurrentTime, exec_order_starttime, "S");
        	target_position = order_bs * Floor(order_totalqty * duration / order_duration) + exec_order_startposition;
        	if Position <> target_position then begin
        		SetPosition(target_position);		{ TODO: 請填入委託價格 }
        	end;	
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_03_分量權重交易_VWAP_(df: pd.DataFrame, vwap_days: int = 1, start_hhmm: int = 0905, end_hhmm: int = 1000, order_totalqty: int = 1000, order_bs: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 03-分量權重交易(VWAP)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\3-Algo策略委託\03-分量權重交易(VWAP).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	分量權重(VWAP): 把預期委託數量依照歷史成交量分布, 在指定的時間範圍送出內, 預期成交均價可以接近歷史均價
        	輸入參數:
        	- 統計天數 (vwap_days: 決定要用前幾天的成交量統計)
        	- 開始交易時間 (start_hhmm: 交易開始時間, 格式為hhmm, 例如0905, 表示從09:05開始進行交易)
        	- 結束交易時間 (end_hhmm: 交易結束時間, 格式為hhmm, 例如1300, 表示交易到1300就停止)
        	- 交易數量 (order_totalqty: 預計交易的數量)
        	- 交易方向 (order_bs: 1=買進, -1=賣出)
        	執行邏輯:
        	- 策略起動時根據vwap_days統計出每分鐘的成交數量分佈比例(從09:00~13:30),
        	- 依照指定的交易區間(start_hhmm ~ end_hhmm), 以及預期交易數量, 決定每分鐘的委託數量,
        	- 舉例
        		- start_hhmm = 09:10, end_hhmm = 10:00
        		- 依照歷史統計, 09:10的成交量=1%, 09:11的成交量=0.8%, .. 09:59的成交量=1.5%
        		- 假設order_totalqty = 500, 則
        		- 在09:11(09:10結束時), 送出500 * 1% / (1% + 0.8% + .. + 1.5%), 
        		- 在09:12(09:11結束時), 送出500 * 0.8% / (1% + 0.8% + .. + 1.5%),
        		- 在10:00(09:59結束時), 送出500 * 1.5% / (1% + 0.8% + .. + 1.5%),
        		- 也就是說, 在指定時間範圍內, 依照歷史成交量的分佈, 每分鐘送出委託,
        }
        if start_hhmm >= end_hhmm then raiseruntimeerror("開始時間必須 < 結束時間");
        { 請確認Backbar有足夠的空間可以讀入vwap_days的資料 }
        array: intrabarpersist vwap_dist[](0);		// N日統計分佈, 總共有total_minute格, 每一格是到目前為止的百分比
        if not vwap_started and GetInfo("TradeMode") = 1 then begin
        	// 如果使用者指定 09:01 ~ 10:00, 因為分K是標在時間起點, 
        	// 所以我們要統計的是09:01 ~ 09:59這些分K的成交量分佈 (所以end_hhmm會-1分鐘)
        	start_hhmmss = start_hhmm * 100;
        	end_hhmmss = TimeAdd(end_hhmm * 100, "M", -1);
        	CalcVWAPDistribution(vwap_days, start_hhmmss, end_hhmmss, vwap_dist);
        	vwap_totalminutes = Array_GetMaxIndex(vwap_dist);
        	vwap_started = true;
        	vwap_base_position = Position;
        	vwap_time_index = 0;
        end;
        { VWAP的執行邏輯 }
        if vwap_started and Position <> vwap_base_position + order_bs * order_totalqty then begin
        	if CurrentTime >= start_hhmmss then begin
        		{ 計算目前時間是開始時間後的第幾分鐘 }
        		value1 = IntPortion(TimeDiff(CurrentTime, start_hhmmss, "M"));
        		if value1 > vwap_time_index then begin
        			{ 預期的成交量比例  = vwap_dist[value1] }
        			if value1 >= vwap_totalminutes then 
        				value2 = 100				{ 超過時間 => 100% }
        			else	
        				value2 = vwap_dist[value1];
        			value3 = value2	* order_totalqty * order_bs / 100;
        			if Position <> vwap_base_position + value3 then begin
        				{ 送出委託單 }
        				SetPosition(vwap_base_position + value3);	{ TODO: 請填入委託價格 }
        			end;	
        			vwap_time_index = value1;
        		end;
        	end;
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_04_網格交易(df: pd.DataFrame, grid_gap: int = 20, grid_maxcount: int = 3, stoploss_point: int = 100) -> tuple[bool, str]:
        """
        Original Strategy: 04-網格交易
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\3-Algo策略委託\04-網格交易.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	網格交易: 每當價格跌破一個網格時就買進, 上漲一個網格時則賣出
        	輸入參數:
        	- 網格間隔 (grid_gap: 定義網格的間距)
        	- 網格數目 (grid_maxcount: 往上/往下分別設定的網格數目)
        	- 停損點 (stoploss_point: 當價格超過停損點時, 執行停損. 停損點通常布置在最大網格之外)
        	執行邏輯:
        	- 系統啟動時, 以當時的價格為中心點,
        	- 當市價下跌超過一個網格時, 買進1張,
        	- 當市價上漲超過一個網格時, 賣出1張, 也就是低買高賣,
        	- 如果市價上漲/下跌超過最大網格數目時, 就暫停交易,
        	- 如果價格持續上漲/下跌, 當超過停損點的話, 則全部平倉停損 (通常停損點會設定在最大網格數目之外)
        	舉例:
        	- 每格100點
        	- 共3格
        	- 停損點=500
        	如果在10000點時啟動, 那麼
        	- 當價格跌破9900時買進1口, 接下來如果漲回10000時賣出1口, 
        	- 如果沒有漲回10000, 而是繼續跌到9800時, 則再買進1口 (漲回9900時則賣出1口),
        	- 如果持續下跌, 每100點就買進1口, 可是最低就到9700(3格=300點), 再往下跌就不買了,
        	- 如果很不幸的, 一直往下跌, 那麼當跌破9500時(10000-500=停損點), 則全部停損,
        	- 同理, 如果價格一開始就往上走, 例如漲到10100點時, 就賣出1口, 如果跌回10000點, 則買進1口,
        	- 如果繼續上漲, 到了10200點時, 再賣出1口 (跌回10100時則買進1口),
        	- 如果很不幸的, 一直往上漲, 那麼當漲到10500時(10000+500=停損點), 則全部停損,
        	- 交易邏輯是低買高賣, 預期價格會在區間震盪, 賺取價格在網格之間穿越時的買賣差額	
        	Note: 以下程式碼假設商品一開始的部位 = 0
        }
        { 
        	範例:
        	策略一啟動就以當時收盤價為基礎啟動網格交易, 一直跑到停損點觸發為止
        }
        if not grid_started and GetInfo("TradeMode") = 1 then begin
        	grid_started = true;
        	grid_base = Close;
        	grid_current_base = Close;
        	grid_current_ord = 0;
        	grid_buycount = 0;
        	grid_sellcount = 0;
        	Print("=>啟動網格中心點:", numtostr(grid_current_base, 0));
        end;
        { 網格交易邏輯 }
        if grid_base <> 0 then begin
        	if Close >= grid_base + stoploss_point or Close <= grid_base - stoploss_point then begin
        		SetPosition(0, label:="網格:停損出場");	{ 全部平倉, 停止網格交易(TODO:請填入委託價格) }
        		grid_base = 0;							{ 停止網格交易 }
        	end else begin
        		{ 
        			比對目前價格與current_grid_base, 看價格是否穿越網格跳過幾格
        			請注意以下的邏輯有處理一次跳過多格的情形 
        		}
        		if Close >= grid_current_base + grid_gap then begin
        			value1 = grid_current_ord + IntPortion((Close - grid_current_base) / grid_gap);
        			if value1 >= grid_maxcount then value1 = grid_maxcount;
        			value1 = value1 - grid_current_ord;		{ 往上移動的格數 }
        			if value1 > 0 then begin
        				{ 往上移動網格 }
        				grid_current_base = grid_current_base + value1 * grid_gap;
        				grid_current_ord = grid_current_ord + value1;
        				grid_sellcount = grid_sellcount + value1;
        				SetPosition(Position - value1, label:="網格:上漲賣出");	{ 賣出 (TODO:請填入委託價格) }
        			end;
        		end else if Close <= grid_current_base - grid_gap then begin
        			value1 = grid_current_ord - IntPortion((grid_current_base - Close) / grid_gap);
        			if value1 <= -1 * grid_maxcount then value1 = -1 * grid_maxcount;
        			value1 = grid_current_ord - value1;		{ 往下移動的格數 }
        			if value1 > 0 then begin
        				{ 往下移動網格 }
        				grid_current_base = grid_current_base - value1 * grid_gap;
        				grid_current_ord = grid_current_ord - value1;
        				grid_buycount = grid_buycount + value1;
        				SetPosition(Position + value1, label:="網格:下跌買進");	{ 買進 (TODO:請填入委託價格) }
        			end;
        		end;
        	end;	
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_05_冰山委託單_Iceberg_(df: pd.DataFrame, ice_maxprice: int = 14000, ice_below: int = 10, ice_bs: int = 1, ice_totalqty: int = 100, ice_batchqty: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 05-冰山委託單(Iceberg)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\3-Algo策略委託\05-冰山委託單(Iceberg).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	冰山單(Iceberg): 把要買進的數量分批低掛
        	輸入參數:
        	- 最高價格 (ice_maxprice: 當市價超過這個價格時, 就暫停交易)
        	- 委託價差 (ice_below: 目前市價=X時, 委託價格=X-ice_below(for buying), 也就是低買的價格位置, 目前是定義成絕對值)
        	- 委託方向 (ice_bs: 1=買進, -1=賣出)
        	- 委託總數量 (ice_totalqty: 預期總成交數量)
        	- 每次委託數量 (ice_batchqty: 每一次委託單的大小)
        	執行邏輯(for買進)
        	- 當目前價格 = X時, 如果X <= ice_maxprice, 送出一筆委託單, 價格 = X - ice_below, 數量 = ice_batchqty,
        	- 如果成交的話, 依照目前的價格送出下一筆委託單,
        	- 如果目前的價格Y >= X + 2 * ice_below, and Y <= ice_maxprice, 則取消剩餘委託, 用目前的市場價格重新送出
        	- Buy the dip => 低接
        	Note: 以下程式碼假設商品一開始的部位 = 0
        }
        if not ice_started and GetInfo("TradeMode") = 1 then begin
        	ice_started = true;
        	ice_lastorderprice = 0;
        end;
        { 冰山交易邏輯 }
        if ice_started and Filled <> ice_bs * ice_totalqty then begin
        	{ 如果目前市場價格超過最大值, 則不處理. 已經送出的委託就維持不動 }
        	if (ice_bs = 1 and Close > ice_maxprice) or 
        	   (ice_bs = -1 and Close < ice_maxprice) then 
        	   return;
        	if Position = 0 then begin
        		{ 送出第一次委託 }
        		ice_lastorderprice = Close - ice_bs * ice_below;
        		SetPosition(ice_bs * ice_batchqty, ice_lastorderprice);
        	end else if Position = Filled then begin
        		{ 送出下一批次委託 }
        		ice_lastorderprice = Close - ice_bs * ice_below;
        		SetPosition(Position + ice_bs * ice_batchqty, ice_lastorderprice);
        	end else if ice_bs = 1 and Close > ice_lastorderprice + 2 * ice_below then begin
        		{ 價格移動, 追價 }
        		ice_lastorderprice = Close - ice_bs * ice_below;
        		SetPosition(Position, ice_lastorderprice);
        	end else if ice_bs = -1 and Close < ice_lastorderprice - 2 * ice_below then begin
        		{ 價格移動, 追價 }
        		ice_lastorderprice = Close - ice_bs * ice_below;
        		SetPosition(Position, ice_lastorderprice);
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
