# Auto-generated strategies for: 自動交易/0-基本語法
import pandas as pd
import numpy as np

class Cat0基本語法Strategies:

    @staticmethod
    def strategy_01_SetPosition(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 01-SetPosition
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\01-SetPosition.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	Position代表的是這個商品在這個策略內的’預期部位’, Position是一個整數, 可以大於0, 也可以小於0.
        	**請注意: 一個交易策略內可以跑多個商品，每個商品的Position是獨立的**
        	當我們想要執行交易時, 就呼叫SetPosition這一個函數, 傳入我們預期的部位(同時也可以傳入委託價格).
        	腳本開始執行時, 商品的Position預設數值是0, 當我們想要買進時, 就透過SetPosition把Position變大, 想要賣出時, 就透過
        	SetPosition把Position變小.
        	系統收到了SetPosition()的呼叫之後, 就會依照目前的Position, 目前委託/成交的執行狀態, 決定如何送單, 來讓你的策略可以達到(成交)
        	這個新的預期的部位.
        	SetPosition()可以接受兩個參數:
        	第一個參數是預期的部位,
        	第二個參數是委託的價格, 這個參數如果不傳的話, 則會採用策略的預設買進/賣出價格
        	請看以下範例
        }
        {
        	把部位(Position)變成1, 如果原先部位是0的話, 則等於買進1張
        	第二個參數(委託價格)如果不傳的話, 則使用策略設定內的預設價格	
        }
        SetPosition(1);	
        {
        	第二個參數可以傳入價格, MARKET是系統保留字, 代表是'市價'(期貨的話則會是'範圍市價')
        }
        SetPosition(1, MARKET);
        {
        	也可以傳入K棒的價格, 例如Close
        }
        SetPosition(1, Close);
        {
        	也可以傳入數值運算式
        }
        SetPosition(1, Close + 1.0);
        {
        	也可以傳入絕對值, 例如100.0
        }
        SetPosition(1, 100.0);
        {
        	支援檔位換算功能(AddSpread), 
        	AddSpread(Close, 1)表示是Close價格往上加1檔, AddSpread(Close, 2)表示加2檔
        	AddSpread(Close, -1)表示是Close價格往下減1檔
        	AddSpread也可以用在警示腳本, 以及指標腳本
        }
        SetPosition(1, AddSpread(Close, 1));
        {
        	Position也可以是負的, 如果原先部位是0的話, 則等於賣出1張
        }
        SetPosition(-1);
        {
        	除了可以SetPosition之外, 也可以讀到目前的Position
        	SetPosition(Position+1)表示是加碼1張
        }
        value1 = Position;
        SetPosition(Position+1);
        {	
        	SetPosition的價格如果不符合商品的交易規則的話, 系統會自動轉換,
        	例如: 如果超過漲停價, 則只會送出漲停價,
        	例如: 如果不符合跳動點的話, 則會自動轉換到符合跳動點價格
        }
        SetPosition(1, 123.1);		{ 如果是買進台積電的話, 則會送出委託價格=123元 }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_SetPosition範例_1_多單1口_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 02-SetPosition範例#1(多單1口)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\02-SetPosition範例#1(多單1口).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	範例: 
        	當發生做多情境時, 買進1口
        	做多後發生出場情境時, 多單出場(變成空手)
        }
        	long_condition(false), 		{ 是否做多 }
        	exit_long_condition(false); { 是否多單出場 }
        { 
        	Position=0時判斷是否要做多, 
        	Position=1時判斷是否要出場 
        }
        if Position = 0 and long_condition then SetPosition(1);
        if Position = 1 and exit_long_condition then SetPosition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_SetPosition範例_2_空單1口_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 02-SetPosition範例#2(空單1口)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\02-SetPosition範例#2(空單1口).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	範例: 
        	當發生做空情境時, 賣出1口(做空)
        	做空後發生出場情境時, 空單出場(變成空手)
        }
        	short_condition(false), 		{ 是否做空 }
        	exit_short_condition(false);	{ 是否空單出場 }
        { 
        	Position=0時判斷是否要做空, 
        	Position=-1時判斷是否要回補 
        }
        if Position = 0 and short_condition then SetPosition(-1);
        if Position = -1 and exit_short_condition then SetPosition(0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_02_SetPosition範例_3_多單1口_空單1口_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 02-SetPosition範例#3(多單1口+空單1口)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\02-SetPosition範例#3(多單1口+空單1口).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	範例
        	當發生做多情境時, 把部位變成做多1口(如果此時是空手的話, 買進1口, 如果此時是做空1口的話, 回補這一口,同時買進1口)
        	當發生做空情境時, 把部位變成做空1口(如果此時是空手的話, 賣出1口, 如果此時是做多1口的話, 賣出這一口,同時做空1口)
        	做多後發生出場情境時, 多單出場(變成空手)
        	做空後發生出場情境時, 空單出場(變成空手)
        	這個是範例#1跟範例#2的綜合體, 可是包含了部位翻轉的邏輯(Position可能從-1變成1, 或是從1變成-1)
        }
        	long_condition(false), 			{ 是否做多 }
        	exit_long_condition(false), 	{ 是否多單出場 }
        	short_condition(false), 		{ 是否做空 }
        	exit_short_condition(false);	{ 是否空單出場 }
        if Position <> 1 and long_condition then begin
        	{ 如果符合做多情境(long_condition), 則把部位變成1 (可能是0->1 or -1->1) }
        	SetPosition(1);
        end else if Position <> -1 and short_condition then begin
        	{ 如果符合做空情境(short_condition), 則把部位變成-1 (可能是0->-1 or 1->-1) }
        	SetPosition(-1);
        end else if Position = 1 and exit_long_condition then begin
        	{ 如果已經做多, 且發生多方出場情形時(exit_long_condition), 則把部位變成0 }
        	SetPosition(0);
        end else if Position = -1 and exit_short_condition then begin
        	{ 如果已經做空, 且發生空方出場情形時(exit_short_condition), 則把部位變成0 }
        	SetPosition(0);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_03_Filled(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 03-Filled
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\03-Filled.xs
        XS Logic Reference:
        {@type:autotrade}
        {
            Filled是Position的另外一個朋友, 代表這個策略內/這個執行商品的成交部位
            假設剛開始執行時, 腳本的Position是0的話, 此時Filled也會是0
            接下來當腳本執行SetPosition(1)後, 會送出一筆買進1張的委託
            如果此時尚未成交的話, Position會等於1, 可是Filled會等於0
            如果這一筆委託單成交的話, 則Position會等於1, Filled也會等於1    
            如果腳本內想要判斷目前成交狀態的話, 就可以透過讀取Filled這個變數來判斷.
        }
        { 以下假設策略啟動時商品的Postion = 0 }
        if Position = 1 and Filled = 0 then begin
            { 已經送出一筆買進1張的委託, 可是還沒有成交}
        end;
        if Position = 1 and Filled = 1 then begin
            { 已經送出一筆買進1張的委託, 而且這一筆委託已經成交 }
        end;
        if Position = -1 and Filled = 0 then begin
            { 已經送出一筆賣出1張的委託, 可是還沒有成交 }
        end;
        if Position = -1 and Filled = -1 then begin
            { 已經送出一筆賣出1張的委託, 而且這一筆委託已經成交 }
            { Filled跟Position一樣, 可能會大於0, 也可能會小於0 }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_04_SetPosition範例_4_追價_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 04-SetPosition範例#4(追價)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\04-SetPosition範例#4(追價).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	範例: 透過Filled來判斷是否需要追價
        	當發生做多情境時, 買進1口
        	如果發生出場情境時, 多單出場(變成空手)
        	如果買進委託沒有成交的話, 則追價
        }
        {
        	當腳本呼叫SetPosition的話, 系統會依照目前委託/成交的情形, 決定如何送出委託單.
            以下情境假設一開始執行時Position = 0. 
        	情境#1
        	腳本呼叫SetPosition(1)時, 系統送出一筆買進1口的委託單
        	經過一段時間後, 腳本呼叫SetPosition(0), 此時會發生以下的情形
        	- 如果剛剛那一筆委託單已經成交(Position=1, Filled=1), 接下來SetPosition(0), 就會送出一筆賣出1口的委託
        	- 如果剛剛那一筆委託單還沒有成交(Position=1, Filled=0), 接下來SetPosition(0), 就會**刪除買進的那一筆委託**
        	  (這樣子的話, 使用者的部位就剛好是0)
        	情境#2
        	腳本呼叫SetPosition(1)時, 系統送出一筆買進1口的委託單
        	經過一段時間後, 腳本又呼叫SetPosition(1), 此時會發生以下的情形
        	- 如果剛剛那一筆委託單已經成交(Position=1, Filled=1), 接下來SetPosition(1), 不會送出任何委託
        	- 如果剛剛那一筆委託單還沒有成交(Position=1, Filled=0), 接下來SetPosition(1), 系統會執行以下的邏輯
        		- 如果新的SetPosition(1)的委託價格跟先前的委託價格**不一樣**的話, 則刪除剛剛的委託, 
        		  然後送出一筆買進1口的委託單(使用新的委託價格)
        		- 如果新的SetPosition(1)的委託價格跟先前的委託價格一樣的話, 則不會做任何動作
        	情境#3
        	腳本呼叫SetPosition(2)時, 送出一筆買進2口的委託單
        	經過一段時間後, 腳本又呼叫SetPosition(3), 此時會發生以下的情形
        	- 如果剛剛那一筆委託單已經完全成交(Position=2, Filled=2)
        		- 接下來SetPosition(3), 就會送出一筆買進1口的委託
        	- 如果剛剛那一筆委託單都沒有成交(Position=2, Filled=0)
        		- 接下來SetPosition(3), 就會刪除先前的委託, 然後送出一筆買進3口的委託
        	- 如果剛剛那一筆委託單部分成交(Position=2, Filled=1)
        		- 接下來SetPosition(3), 就會刪除先前的委託, 然後送出一筆買進2口的委託
        	小結:
        	如果Position跟Filled一樣的話, 這個表示先前送出的委託都已經完全成交, 或是已經被取消. 
        	此時如果收到新的SetPosition()的話, 系統的動作是送出一筆買進或是賣出的委託
        	如果Position跟Filled不一樣的話, 這個表示目前應該有一筆[尚未完全成交的委託], 如果此時收到新的SetPosition()的話,
        	系統會先刪除目前這一筆委託, 確認這一筆委託的成交數量之後, 再依照新的需求決定如何送單.
        }
        	long_condition(false), 		{ 是否做多 }
        	exit_long_condition(false); { 是否多單出場 }
        if Position = 0 and long_condition then begin
        	{ 如果目前是空手, 且符合做多情境(long_condition), 則以目前收盤價買進1口, }
        	SetPosition(1, Close);
        end else if Position = 1 and exit_long_condition then begin
        	SetPosition(0);
        	{ 多單出場: 如果已經買到了, 就賣出剛剛買到的1口, 如果還沒有買到, 就取消買進的委託單 }
        end else if Position = 1 and Filled = 0 then begin
        	{ 如果已經送出買進委託, 可是還沒有成交的話, 則追價(系統會刪除先前委託, 然後再送出買進1張) }
        	SetPosition(1, Close);
        	{ 為了確保委託單排隊的順序, 如果新的委託價跟先前委託價格一樣的話, 系統就不會執行委託異動的動作 }
        end;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_04_SetPosition範例_5_加碼_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 04-SetPosition範例#5(加碼)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\04-SetPosition範例#5(加碼).xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	範例: 透過Filled來判斷是否要加碼
        	當發生做多情境時, 買進1口
        	買進成交後, 如果發生加碼情境時, 再買進1口,
        	如果發生出場情境時, 多單出場(變成空手, 部位=0)
        }
        	long_condition(false), 			{ 是否做多 }
        	raise_long_condition(false),	{ 是否多單加碼 }
        	exit_long_condition(false); 	{ 是否多單出場 }
        if Position = 0 and long_condition then begin
        	{ 目前Position=0, 而且發生做多情境, 買進1口 }
        	SetPosition(1);
        end else if Position <> 0 and exit_long_condition then begin
        	{ 已經買進, 而且發生多單出場情境, 賣出所有部位 }
        	{ 請注意, Position可能是1 or 2, 所以用 <> 0 來判斷 }
        	SetPosition(0);
        end else if Position = 1 and Filled = 1 and raise_long_condition then begin
        	{ 已經買進1口, 而且也成交了, 此時發生加碼情境, 所以再買進1口}
        	SetPosition(2);
        	{ 也可以寫成 SetPosition(position + 1) }
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_05_FilledAvgPrice以及停損停利範例(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 05-FilledAvgPrice以及停損停利範例
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\05-FilledAvgPrice以及停損停利範例.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	除了可以使用Filled來知道目前的成交部位之外, 
        	也可以透過FilledAvgPrice這個函數來取得目前"未平倉"部位的成本	
        }
        {
        	範例: 多單1口進場後, +1.5%停利, -1.5%停損
        }
        	long_condition(false); 		{ 是否做多 }
        if Position = 0 and long_condition then SetPosition(1);
        if Position = 1 and Filled = 1 then begin		
        	{ 多單已經買進1口 }
        	{ 計算損益% }
        	{ 
        		請注意: 不管Filled是大於0還是小於0, FilledAvgPrice的數值都是'正數'(>0) 
        	}
        	plratio = 100 * (Close - FilledAvgPrice) / FilledAvgPrice;
        	if plratio >= 1.5 then SetPosition(0);		{ 停利 }
        	if plratio <= -1.5 then SetPosition(0);		{ 停損 }
        end;	
        {
        	目前計算未平倉成本的方式是採用**先進先出的沖銷方式**來計算, 以下是沖銷順序的範例:
        	範例#1
        	假設策略執行過程總共產生三筆成交, 依照時間先後順序, 資料分別為
        	- 第一筆: 買進1張, 成交價100元,
        	- 第二筆: 買進1張, 成交價102元,
        	- 第三筆: 賣出1張, 成交價101元
        	在第一筆成交時, Filled = 1, FilledAvgPrice = 100
        	在第二筆成交時, Filled = 2, FilledAvgPrice = (100 + 102) / 2 = 101
        	在第三筆成交時, Filled = 1, FilledAvgPrice = 102 (第三筆-1沖銷第一筆+1, 所以未平倉剩下第二筆1張, 未平倉成本=102)
        	範例#2
        	假設策略執行過程總共產生四筆成交, 依照時間先後順序, 資料分別為
        	- 第一筆: 買進2張, 成交價100元,
        	- 第二筆: 買進2張, 成交價101元,
        	- 第三筆: 買進2張, 成交價102元,
        	- 第四筆: 賣出3張, 成交價101元,
        	在第一筆成交時, Filled = 2, FilledAvgPrice = 100
        	在第二筆成交時, Filled = 4, FilledAvgPrice = (100*2 + 101*2) / 4 = 100.5
        	在第三筆成交時, Filled = 6, FilledAvgPrice = (100*2 + 101*2 + 102*2) / 6 = 101
        	在第四筆成交時, Filled = 3, FilledAvgPrice = (101*1 + 102 * 2) / 3 = 101.66666
        	(第一筆成交的2張被沖銷, 第二筆成交的1張被沖銷)
        }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_06_FilledRecord函數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 06-FilledRecord函數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\06-FilledRecord函數.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	除了Filled跟FilledAvgPirce之外, 系統也提供FilledRecord相關的函數, 讓腳本可以取得每一筆成交的詳細資料
        }
        {
        	FilledRecordCount: 取得商品執行迄今的成交筆數
        	請注意:
        	成交筆數會對應到真實的交易紀錄, 例如買進5張, 如果分三次成交, 分別成交2張, 2張, 1張, 
        	那麼FilledRecordCount會是3	
        }	
        value1 = FilledRecordCount;		{ 回傳成交筆數 }
        {
        	取得成交筆數之後, 就可以一筆一筆把成交紀錄資料讀出來
        	FilledRecordDate(n): 回傳第n筆成交紀錄的日期, 格式是YYYYMMDD, 例如20200727 (2020年7月27日)
        	FilledRecordTime(n): 回傳第n筆成交紀錄的時間, 格式是HHMMSS, 例如103000 (10點30分0秒)
        	FilledRecordBS(n):   回傳第n筆成交紀錄的買賣別, 買進的話是1, 賣出的話是-1
        	FilledRecordPrice(n):回傳第n筆成交紀錄的成交價格, 請注意這個數值的正負跟買進/賣出無關(以台股來說都會 > 0)
        	FilledRecordQty(n):  回傳第n筆成交紀錄的成交數量, 請注意不管是買進或是賣出, 這個數值都是 > 0的整數	
        	FilledRecordIsRealtime(n): 回傳第n筆成交紀錄是否是在即時區間成交的, 如果是的話回傳1, 否則回傳0
        	n的範圍從1到FilledRecordCount
        }
        for idx = 1 to FilledRecordCount begin
        	value2 = FilledRecordDate(idx);
        	value3 = FilledRecordTime(idx);
        	value4 = FilledRecordBS(idx);
        	value5 = FilledRecordPrice(idx);
        	value6 = FilledRecordQty(idx);	
        	value7 = FilledRecordIsRealtime(idx);
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_07_Position跟Filled的異動時機點(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 07-Position跟Filled的異動時機點
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\07-Position跟Filled的異動時機點.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	系統在什麼時候會更新Position以及Filled ?
        	系統洗價(執行腳本)的邏輯如下:
        	- 當成交價異動時(逐筆洗價)或是K棒完成時(非逐筆洗價)執行腳本,
        	- 要執行腳本前, 先決定當時的Position以及Filled的數值,
        	- 執行腳本的邏輯,
        	- 如果執行時腳本呼叫SetPosition的話, 則紀錄"第一次"呼叫SetPosition的狀態,
        	- 接下來腳本如果又呼叫其他的SetPosition的話, 則[不予理會], 也就是說洗價過程內如果腳本呼叫了
        	  很多個SetPosition的話, 系統只會執行第一個,
        	- 在洗價過程內, Position跟Filled的數值都會維持不變, 就算洗價到一半時突然收到成交的話, Filled也不會更動(不然的話腳本的計算
              邏輯可能會因為Filled的異動而亂掉)	
        	- 等到腳本洗價完畢, 依照委託/執行的狀態, 決定要如何送單,
        	- 同時也會更新Position的數值(所以下一次洗價時Position的數值會異動)
        	- 如果在下一次洗價前收到任何成交的話, 也會更新Filled的數值(所以下一次洗價時Filled的數值會是洗價前的成交狀態)	
        }
        {
        	範例#1: 說明多個SetPosition時的執行邏輯, 以及Position何時異動
        }
        if currentbar = 1 then begin
        	print(Position);			{ 印出 0 }
        	SetPosition(1);				{ 這是第一次呼叫的SetPosition(), 系統會執行這一個 }
        	print(Position);			{ 印出 0, 要等到下一次洗價時Position才會變成1 }
        	SetPosition(2);				{ 這次呼叫會被忽略, 因為line#33已經呼叫了SetPosition() }
        	print(Position);			{ 印出 0, 要等到下一次洗價時Position才會變成1 }
        end else if currentbar = 2 then begin
        	print(Position);			{ 印出 1, 因為currentbar=1的時候執行了line#33的SetPosition(1) }
        	SetPosition(2);				{ 這是這一次洗價第一次呼叫的SetPosition(), 系統會執行這一個 }
        	print(Position);			{ 印出 1, 要等到下一次洗價時Position才會變成2 }
        end;
        {
        	範例#2: 因為每一次洗價只會執行一個SetPosition, 所以如果系統希望可以依照不同情境決定部位的數量, 那該怎麼設計 ? 
        }
        { 
        	如果long_condition成立時買1張, 
        	如果strong_condition成立時就買2張
        }
        // 寫法#1 => 有問題!! 如果long_condition跟strong_condition都成立時, 只會買1張
        //
        if long_condition then SetPosition(1);
        if strong_condition then SetPosition(2);
        // 寫法#2 => OK, 因為會先判斷strong_condition(買比較多的先判斷, 設計時要小心先後順序)
        //
        if strong_condition then SetPosition(2);
        if long_condition then SetPosition(1);
        // 寫法#3 => OK(推薦) 依照不同情形計算預期部位, 最後再一次呼叫SetPosition
        //
        if long_condition then value1 = 1;
        if strong_condition then value1 = 2;
        if value1 <> 0 then SetPosition(value1);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_08_Alert(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 08-Alert
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\08-Alert.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        	Alert語法
        	在交易腳本內也可以透過Alert語法產生'通知'. 	
        }
        if alert_condition then begin
        	{ 呼叫Alert函數, 傳入要通知的訊息 }
        	alert("這是我想要顯示的通知訊息");
        	{ 也可以一次傳入多個參數, 系統會把這些參數串連成一個字串, 用空白字元來分隔 }
        	alert("目前Bar時間=", FormatTime("HH:mm", Time));
        end;
        { 
        	Alert的通知會出現在以下的畫面內
        	a. 自動交易中心, 策略執行記錄內(類別為警示)
        	b. 即時監控畫面(請記得來源要勾選'自動交易')
        	c. 警示提示視窗(請記得來源要勾選'自動交易')
        	如果自動交易策略啟動推播的話, Alert也會傳送到手機端		
        }
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_09_CancelAllOrders(df: pd.DataFrame, _n: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 09-CancelAllOrders
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\自動交易\0-基本語法\09-CancelAllOrders.xs
        XS Logic Reference:
        {@type:autotrade}
        {
        此為 CancelAllOrders 的範例腳本
        腳本將會在啟動時直接下出委託價為跌停價的買進委託 (只會委託一次)，若委託未成交的話則在N分鐘以後刪除委託。
        需注意會依照策略設定和商品洗價而有所差異，並不一定會準時在N分鐘後刪除
        }
        if _n < 0 then RaiseRunTimeError("設定分鐘需要大於0");
        //啟動後進入交易指令可執行的區間後下單並計算出場時間
        Once(Position = 0 and Filled = 0 and GetInfo("TradeMode") = 1) begin   
            SetPosition(1, GetField("跌停價", "D"), label:="跌停價買進委託");
            _time = TimeAdd(CurrentTime, "M", _n);
        	end;    
        //當洗價時
        if CurrentTime > _time and Position <> Filled then CancelAllOrders(label:="刪除跌停價買進委託");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
