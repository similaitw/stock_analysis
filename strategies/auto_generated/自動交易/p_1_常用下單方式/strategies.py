# Auto-generated strategies for: 自動交易/1-常用下單方式
import pandas as pd
import numpy as np

class Cat1常用下單方式Strategies:

    @staticmethod
    def strategy_01_市價交易(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 01-市價交易
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\01-市價交易.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	市價交易
        }
        { 
        	範例:
        	均線穿越時以市價買進1張
        	均線跌破時以市價賣出(1張)
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        if Position = 0 and long_condition then begin
        	SetPosition(1, MARKET);		{ 以市價買進 }
        end;
        if Position = 1 and exit_long_condition then begin
        	SetPosition(0, MARKET);		{ 以市價賣出 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_金額換算(df: pd.DataFrame, ordersize_w: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 02-金額換算
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\02-金額換算.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	以金額計算交易數量
        }
        { 
        	範例:
        	均線穿越時以指定金額換算張數買進
        	均線跌破時以市價賣出全部數量
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        if Position = 0 and long_condition then begin
        	order_price = AddSpread(Close, 1);	
        	order_qty = (ordersize_w * 10000) / (order_price * 1000);
        								{ 計算出來的數值如果不是整數, 傳入SetPosition時會自動捨去小數位數 }
        								{ 例如 SetPosition(2.5) 執行時會被轉成 SetPosition(2) }
        	SetPosition(order_qty, order_price);		{ 以指定價格買入指定數量 }
        end;
        if Position <> 0 and exit_long_condition then begin
        	SetPosition(0, MARKET);		{ 以市價賣出全部數量 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_03_全部賣出(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 03-全部賣出
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\03-全部賣出.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單全部賣出
        }
        { 
        	範例:
        	多單進場: 每次遇到均線穿越或是連續上漲3筆時就買進1張(可以買進很多張, 沒有限制)
        	均線跌破時賣出全部
        }
        long_condition = 
        	Average(Close, 5) cross over Average(Close, 20) or
        	TrueAll(Close > Close[1], 3);
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        if long_condition then begin
        	SetPosition(Position + 1);		{ 多單+1: 使用預設買進價格 }
        									{ SetPosition(Position+1)的意思就是比目前部位多買1筆 }
        									{ 也可以使用 Buy(1), 代表多單加碼1張 }
        end;
        if Position > 0 and exit_long_condition then begin
        	SetPosition(0);					{ 多單全部出場: 把Position調成0, 使用預設賣出價格 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_04_全部回補(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 04-全部回補
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\04-全部回補.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單全部回補
        }
        { 
        	範例:
        	空單做空: 每次遇到均線跌破或是連續下跌3筆時就賣出1張(可以做空很多張, 沒有限制)
        	均線穿越時回補全部空單
        }
        short_condition = 
        	Average(Close, 5) cross under Average(Close, 20) or
        	TrueAll(Close < Close[1], 3);
        exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	
        if short_condition then begin
        	SetPosition(Position - 1);		{ 空單+1: 使用預設賣出價格 }
        									{ SetPosition(Position-1)的意思就是比目前部位多賣1筆 }
        									{ 也可以使用Short(1), 代表空單加碼1張 }
        end;
        if Position < 0 and exit_short_condition then begin
        	SetPosition(0);					{ 空單全部回補: 把Position調成0, 使用預設買進價格 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_05_多單減碼(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 05-多單減碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\05-多單減碼.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單減碼
        }
        { 
        	範例:
        	多單進場: 每次連續上漲3筆時就買進1張(可以買進很多張, 沒有限制)
        	多單減碼: 每次連續下跌3筆時就減碼1張(最多減碼到0)
        	均線跌破時賣出全部
        }
        add_one_condition = TrueAll(Close > Close[1], 3);
        reduce_one_condition = TrueAll(Close < Close[1], 3);	
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        if add_one_condition then begin
        	Buy(1);							{ 多單+1: 使用預設買進價格 }
        end;
        if Position > 0 then begin
        	{ 請注意: 因為可能同時會符合多單出場以及多單減碼的情形, 所以邏輯上要依照優先順序檢查. }
        	if exit_long_condition then begin
        		SetPosition(0);				{ 多單全部出場: 把Position調成0, 使用預設賣出價格 }
        	end else if reduce_one_condition then begin
        		Sell(1);					{ 多單賣出1張, 使用預設的賣出價格 }
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_06_空單減碼(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 06-空單減碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\06-空單減碼.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	空單減碼
        }
        { 
        	範例:
        	空單進場: 每次連續下跌3筆時就賣出1張(可以賣出很多張, 沒有限制)
        	空單減碼: 每次連續上漲3筆時就減碼(回補)1張(最多減碼到0)
        	均線穿越時回補全部
        }
        short_one_condition = TrueAll(Close < Close[1], 3);
        reduce_one_condition = TrueAll(Close > Close[1], 3);	
        exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	
        if short_one_condition then begin
        	Short(1);						{ 空單+1: 使用預設賣出價格 }
        end;
        if Position < 0 then begin
        	{ 請注意: 因為可能同時會符合空單出場以及空單減碼的情形, 所以邏輯上要依照優先順序檢查. }
        	if exit_short_condition then begin
        		SetPosition(0);				{ 空單全部出場: 把Position調成0, 使用預設買進價格 }
        	end else if reduce_one_condition then begin
        		Cover(1);					{ 空單回補1張, 使用預設的買進價格 }
        	end;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_07_多單加碼(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 07-多單加碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\07-多單加碼.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單加碼
        }
        { 
        	範例:
        	多單進場: 均線穿越做多1張(部位最多=1)
        	多單加碼: 如果已經做多, 又連續上漲3筆, 則加碼1張
        	均線跌破時賣出全部
        }
        long_condition = Average(Close, 5) cross over Average(Close, 20);
        add_one_condition = TrueAll(Close > Close[1], 3);	
        exit_long_condition = Average(Close, 5) cross under Average(Close, 20);	
        if Position = 0 and long_condition then begin
        	SetPosition(1);					{ 多單1張: 使用預設買進價格 }
        end;
        if Position = 1 and add_one_condition then begin
        	SetPosition(2);					{ 加碼1張變成2張 }
        end;
        if Position > 0 and exit_long_condition then begin
        	SetPosition(0);					{ 多單全部出場: 把Position調成0, 使用預設賣出價格 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_08_空單加碼(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 08-空單加碼
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\08-空單加碼.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	多單加碼
        }
        { 
        	範例:
        	空單進場: 均線跌破時做空1張(部位最多=-1)
        	空單加碼: 如果已經做空, 又連續下跌3筆, 則加碼1張
        	均線突破時全部回補
        }
        short_condition = Average(Close, 5) cross under Average(Close, 20);
        add_one_condition = TrueAll(Close < Close[1], 3);	
        exit_short_condition = Average(Close, 5) cross over Average(Close, 20);	
        if Position = 0 and short_condition then begin
        	SetPosition(-1);				{ 空單1張: 使用預設賣出價格 }
        end;
        if Position = -1 and add_one_condition then begin
        	SetPosition(-2);				{ 空單加碼1張變成-2 }
        end;
        if Position < 0 and exit_short_condition then begin
        	SetPosition(0);					{ 空單全部出場: 把Position調成0, 使用預設買進價格 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_09_刪單(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 09-刪單
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\09-刪單.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	刪除尚未完全成交的委託
        }
        { 
        	範例:
        	均線穿越時以長天期的均線價格買進1張
        	如果等了三根K棒都沒有成交則取消委託
        	均線跌破時多單全部平倉
        }
        value1 = Average(Close, 5);
        value2 = Average(Close, 20);
        long_condition = value1 cross over value2;
        exit_long_condition = value1 cross under value2;	
        if Position = 0 and long_condition then begin
        	SetPosition(1, value2);		{ 以20日均線的價格買進 }
        end;
        if Position = 1 and exit_long_condition then begin
        	SetPosition(0);				{ 多單全部平倉 }
        end else if Position = 1 and TrueAll(Position <> Filled, 3) then begin
        	{ 
        		送出買進委託後, Position = 1, 如果成交了, Filled = 1,
        		Position <> Filled 在這裡則代表著委託已經送出, 可是還沒有成交,
        		Position, Filled, 跟value1, value2, Close一樣, 都是一個"序列",
        		所以Position[1]是上一根K棒最後的Position, Filled[1]是上一根K棒最後的Filled,
        		所以TrueAll(Position <> Filled, 3) 代表著連續三根K棒都沒有成交 			
        	}
        	SetPosition(0);				{ 取消買進的委託 }
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_10_改價(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 10-改價
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\1-常用下單方式\10-改價.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	修改尚未完全成交的委託的價格
        }
        { 
        	範例:
        	均線穿越時以短天期的均線價格買進1張
        	如果等了三根K棒都沒有成交則以目前的市場價格追價
        	均線跌破時多單全部平倉
        }
        value1 = Average(Close, 5);
        value2 = Average(Close, 20);
        long_condition = value1 cross over value2;
        exit_long_condition = value1 cross under value2;	
        if Position = 0 and long_condition then begin
        	SetPosition(1, value1);		{ 以5日均線的價格買進 }
        end;
        if Position = 1 and exit_long_condition then begin
        	SetPosition(0);				{ 多單全部平倉 }
        end else if Position = 1 and TrueAll(Position <> Filled, 3) then begin
        	{ 
        		送出買進委託後, Position = 1, 如果成交了, Filled = 1,
        		Position <> Filled 在這裡則代表著委託已經送出, 可是還沒有成交,
        		Position, Filled, 跟value1, value2, Close一樣, 都是一個"序列",
        		所以Position[1]是上一根K棒最後的Position, Filled[1]是上一根K棒最後的Filled,
        		所以TrueAll(Position <> Filled, 3) 代表著連續三根K棒都沒有成交 			
        	}
        	SetPosition(1, Close);		{ 修改委託價格為目前成交價 }
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
