# Auto-generated strategies for: 自動交易/2-下單出場方式
import pandas as pd
import numpy as np

class Cat2下單出場方式Strategies:

    @staticmethod
    def strategy_01_收盤前平倉(df: pd.DataFrame, exit_period: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 01-收盤前平倉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\01-收盤前平倉.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	收盤前平倉
        }
        { 
        	範例:
        	均線穿越時買進1張
        	均線跌破時賣出
        	進場後如果連續下跌3筆時賣出
        	收盤前N分鐘如果還有部位的話賣出(當日部位一定歸0)
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        { 判斷是否已經進入收盤階段 }
        market_close_condition = EnterMarketCloseTime(exit_period);
        if Position = 0 and long_condition and not market_close_condition then begin
        	SetPosition(1);				{ 買進1張: 請注意如果接近收盤時間, 則不進場 }
        end else if Position = 1 and exit_long_condition then begin
        	SetPosition(0);				{ 出場 }
        end else if Position = 1 and market_close_condition then begin
        	SetPosition(0);				{ 進入收盤階段: 出場 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_多單固定停利停損_點_(df: pd.DataFrame, profit_point: int = 10, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 02-多單固定停利停損(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\02-多單固定停利停損(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單停損(點)
        }
        { 
        	範例:
        	均線穿越時以市價買進1張
        	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        if Position = 0 and long_condition then begin
        	SetPosition(1, MARKET);		{ 以市價買進 }
        end;
        if Position = 1 and Filled = 1 then begin
        	{ 依照成本價格設定停損/停利 }
        	if profit_point > 0 and Close >= FilledAvgPrice + profit_point then begin
        		{ 停利 }
        		SetPosition(0);
        	end else if loss_point > 0 and Close <= FilledAvgPrice - loss_point then begin	
        		{ 停損 }
        		SetPosition(0);
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_03_空單固定停利停損_點_(df: pd.DataFrame, profit_point: int = 10, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 03-空單固定停利停損(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\03-空單固定停利停損(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單停損(點)
        }
        { 
        	範例:
        	均線跌破時以市價賣出1張做空
        	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
        }
        short_condition = Average(Close, 5) cross under Average(Close, 20);
        if Position = 0 and short_condition then begin
        	SetPosition(-1, MARKET);		{ 以市價賣出 }
        end;
        if Position = -1 and Filled = -1 then begin
        	{ 依照成本價格設定停損/停利: 請注意當作空時, 判斷是否獲利的方向要改變 }
        	if profit_point > 0 and Close <= FilledAvgPrice - profit_point then begin
        		{ 停利 }
        		SetPosition(0);
        	end else if loss_point > 0 and Close >= FilledAvgPrice + loss_point then begin	
        		{ 停損 }
        		SetPosition(0);
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_04_多單固定停利停損___(df: pd.DataFrame, profit_percent: int = 2, loss_percent: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 04-多單固定停利停損(%)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\04-多單固定停利停損(%).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單停損(%)
        }
        { 
        	範例:
        	均線穿越時以市價買進1張
        	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        if Position = 0 and long_condition then begin
        	SetPosition(1, MARKET);		{ 以市價買進 }
        end;
        if Position = 1 and Filled = 1 then begin
        	{ 依照成本價格設定停損/停利 }
        	if profit_percent > 0 and Close >= FilledAvgPrice*(1+0.01*profit_percent) then begin
        		{ 停利 }
        		SetPosition(0);
        	end else if loss_percent > 0 and Close <= FilledAvgPrice*(1-0.01*loss_percent) then begin	
        		{ 停損 }
        		SetPosition(0);
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_05_空單固定停利停損___(df: pd.DataFrame, profit_percent: int = 2, loss_percent: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 05-空單固定停利停損(%)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\05-空單固定停利停損(%).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單停損(%)
        }
        { 
        	範例:
        	均線跌破時以市價賣出1張做空
        	以成交價為基礎, 設定固定的停損/停利價格, 觸及時出場
        }
        short_condition = Average(Close, 5) cross under Average(Close, 20);
        if Position = 0 and short_condition then begin
        	SetPosition(-1, MARKET);		{ 以市價賣出 }
        end;
        if Position = -1 and Filled = -1 then begin
        	{ 依照成本價格設定停損/停利: 請注意當作空時, 判斷是否獲利的方向要改變 }
        	if profit_percent > 0 and Close <= FilledAvgPrice*(1-0.01*profit_percent) then begin
        		{ 停利 }
        		SetPosition(0);
        	end else if loss_percent > 0 and Close >= FilledAvgPrice*(1+0.01*loss_percent) then begin	
        		{ 停損 }
        		SetPosition(0);
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_06_多單移動停損_點_(df: pd.DataFrame, profit_point: int = 10, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 06-多單移動停損(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\06-多單移動停損(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單移動停損(點)
        	設定停損點, 跟停利點(如果不設定停利的話請把profit_point設定成0)
        	價格碰觸到停損/停利點時出場
        	如果價格上漲時, 停損點會跟著上漲	
        }
        { 
        	範例:
        	均線穿越時買進1張
        	以成交價為基礎, 設定固定停利以及移動停損
        }
        if loss_point = 0 then raiseruntimeerror("請設定停損(點)");
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        if Position = 0 and long_condition then begin
        	SetPosition(1);				{ 買進1張 }
        end;
        if Position = 1 and Filled = 1 then begin
        	{ 依照成本價格設定停損/停利 }
        	{ 計算停損價格 }
        	if stoploss_point = 0 then begin
        		stoploss_point = FilledAvgPrice - loss_point;
        	end;
        	{ 如果價格上漲的話, 則往上挪動停損價格. 停損價格只會越來越高 }
        	if Close > FilledAvgPrice then begin
        		if Close - loss_point > stoploss_point then begin
        			stoploss_point = Close - loss_point;
        		end;	
        	end;	
        	if profit_point > 0 and Close >= FilledAvgPrice + profit_point then begin
        		{ 停利 }
        		SetPosition(0);
        		stoploss_point = 0;
        	end else if Close <= stoploss_point then begin
        		{ 停損 }
        		SetPosition(0);
        		stoploss_point = 0;
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_07_空單移動停損_點_(df: pd.DataFrame, profit_point: int = 10, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 07-空單移動停損(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\07-空單移動停損(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單移動停損(點)
        	設定停損點, 跟停利點(如果不設定停利的話請把profit_point設定成0)
        	價格碰觸到停損/停利點時出場
        	如果價格下跌時, 停損點會跟著下跌	
        }
        { 
        	範例:
        	均線跌破時做空賣出1張
        	以成交價為基礎, 設定固定停利以及移動停損
        }
        if loss_point = 0 then raiseruntimeerror("請設定停損(點)");
        short_condition = Average(Close, 5) cross under Average(Close, 20);
        if Position = 0 and short_condition then begin
        	SetPosition(-1);			{ 做空賣出1張 }
        end;
        if Position = -1 and Filled = -1 then begin
        	{ 依照成本價格設定停損/停利 }
        	{ 計算停損價格 }
        	if stoploss_point = 0 then begin
        		stoploss_point = FilledAvgPrice + loss_point;
        	end;
        	{ 如果價格下跌的話, 則往下挪動停損價格. 停損價格只會越來越低 }
        	if Close < FilledAvgPrice then begin
        		if Close + loss_point < stoploss_point then begin
        			stoploss_point = Close + loss_point;
        		end;	
        	end;	
        	if profit_point > 0 and Close <= FilledAvgPrice - profit_point then begin
        		{ 停利 }
        		SetPosition(0);
        		stoploss_point = 0;
        	end else if Close >= stoploss_point then begin
        		{ 停損 }
        		SetPosition(0);
        		stoploss_point = 0;
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_08_多單移動停利_點_(df: pd.DataFrame, profit_point: int = 10, profit_drawback_point: int = 5, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 08-多單移動停利(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\08-多單移動停利(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單移動停利(點)
        	設定停損點(如果不設定的話, 請把loss_point設定成0), 以及停利點, 跟回跌點數
        	價格下跌到停損時出場
        	價格上漲到停利點後啟動移動停利, 如果價格繼續上漲, 則繼續持有, 如果價格回檔超過回跌點數時, 則停利出場
        }
        { 
        	範例:
        	均線穿越時買進1張
        	以成交價為基礎, 設定固定停損以及移動停利
        }
        if profit_point = 0 then raiseruntimeerror("請設定停利(點)");
        if profit_drawback_point = 0 then raiseruntimeerror("請設定停利回跌(點)");
        if profit_drawback_point > profit_point then raiseruntimeerror("停利(點)需大於停利回跌(點)");
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        if Position = 0 and long_condition then begin
        	SetPosition(1);				{ 買進1張 }
        end;
        if Position = 1 and Filled = 1 then begin
        	if loss_point > 0 and Close <= FilledAvgPrice - loss_point then begin
        		{ 停損 }
        		SetPosition(0);
        		max_profit_point = 0;
        	end else begin
        		{ 判斷是否要啟動停利 }
        		if max_profit_point = 0 and Close >= FilledAvgPrice + profit_point then begin
        			max_profit_point = Close;
        		end;
        		if max_profit_point <> 0 then begin		
        			if Close <= max_profit_point - profit_drawback_point then begin
        				{ 停利 }
        				SetPosition(0);
        				max_profit_point = 0;
        			end else if Close > max_profit_point then begin
        				{ 移動最大獲利點 }
        				max_profit_point = Close;
        			end;	
        		end;		
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_09_空單移動停利_點_(df: pd.DataFrame, profit_point: int = 10, profit_drawback_point: int = 5, loss_point: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 09-空單移動停利(點)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\2-下單出場方式\09-空單移動停利(點).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單移動停利(點)
        	設定停損點(如果不設定的話, 請把loss_point設定成0), 以及停利點, 跟回跌點數
        	價格上漲到停損時出場
        	價格下跌停利點後啟動移動停利, 如果價格繼續下跌, 則繼續持有, 如果價格回檔超過回跌點數時, 則停利出場
        }
        { 
        	範例:
        	均線跌破時做空賣出1張
        	以成交價為基礎, 設定固定停損以及移動停利
        }
        if profit_point = 0 then raiseruntimeerror("請設定停利(點)");
        if profit_drawback_point = 0 then raiseruntimeerror("請設定停利回跌(點)");
        if profit_drawback_point > profit_point then raiseruntimeerror("停利(點)需大於停利回跌(點)");
        short_condition = Average(Close, 5) cross under Average(Close, 20);
        if Position = 0 and short_condition then begin
        	SetPosition(-1);			{ 做空賣出1張 }
        end;
        if Position = -1 and Filled = -1 then begin
        	if loss_point > 0 and Close >= FilledAvgPrice + loss_point then begin
        		{ 停損 }
        		SetPosition(0);
        		max_profit_point = 0;
        	end else begin
        		{ 判斷是否要啟動停利 }
        		if max_profit_point = 0 and Close <= FilledAvgPrice - profit_point then begin
        			max_profit_point = Close;
        		end;
        		if max_profit_point <> 0 then begin		
        			if Close >= max_profit_point + profit_drawback_point then begin
        				{ 停利 }
        				SetPosition(0);
        				max_profit_point = 0;
        			end else if Close < max_profit_point then begin
        				{ 移動最大獲利點 }
        				max_profit_point = Close;
        			end;	
        		end;		
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
