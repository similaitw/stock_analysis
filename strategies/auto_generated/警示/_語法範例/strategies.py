# Auto-generated strategies for: 警示/!語法範例
import pandas as pd
import numpy as np

class 語法範例Strategies:

    @staticmethod
    def strategy_1_基本語法(df: pd.DataFrame, shortlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 1.基本語法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\1.基本語法.xs
        XS Logic Reference:
        {@type:sensor}
        //基本語法共有以下幾個元素
        //1.宣告參數
        //2.宣告變數
        //3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
        //4.運用函數
        //5.條件判斷：例如使用cross over這樣的關係因子
        //6.設定警示條件：if.. then ret=1;
        //在這邊我們用一個警示來示範這幾個基本語法的使用方式。
        //=================範例：平均漲跌幅變大========================================
        //1.宣告參數：利用input宣告輸入的參數。
        //宣告後的參數，可以直接在警示中進場數值的調整，而不需要調整腳本內容
        //參數的名稱，可以用setinputname來指定中文的說明
        //指定後再設定警示參數時，就可以直接看到中文，而非參數英文名稱
        //我們在這邊故意只指定第一個參數的中文名，讓大家看看效果
        //2.宣告變數，利用variable
        //這是宣告一個變數叫xi，其初始值為0
        //3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
        //系統也提供value1~value99共99個不必宣告就可直接用的變數名稱
        value1=close-close[1];//close[1]代表前一天收盤價
        //4.運用函數
        //透過absvalue這個函數取close-close[1]的絕對值
        value2=absvalue(value1); 
        //指定變數值的計算公式，計算漲跌幅
        yi=value2/close; 
        //透過average這個函數計算數列的平均值
        value3=average(yi,longlength);//計算長期平均漲跌幅
        value4=average(yi,shortlength);//計算短期平均漲跌幅
        //5.條件判斷：例如使用cross over這樣的關係因子
        //6.設定警示條件：if.. then ret=1;
        //最後設定警示條件，當短期平均漲跌幅與長期平均漲跌幅黃金交叉時，觸發警示
        if value4 crosses over value3
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_2_getfield(df: pd.DataFrame, periods: int = 3, last: int = 10000) -> tuple[bool, str]:
        """
        Original Strategy: 2.getfield
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\2.getfield.xs
        XS Logic Reference:
        {@type:sensor}
        //除了一般K線的開高低收量之外，還可以透過getfield這樣的指令取得其他商品相關資訊
        //例如可以讓使用者把台股特有的外資買賣超的資料拿來語法中運算
        //只要在編輯器上打getfield就會列出可以使用的資料供user點選
        //一樣可以透過[n]的方式來回傳前第n根的數值
        //===========範例：外資連續多日買超超過1億元的語法==============================
        //1.宣告參數：利用input宣告輸入的參數。
        //2.宣告變數，利用variable
        //4.運用函數
        //利用getfield取得外資買賣超資料
        value1=Getfield("外資買賣超");//取得今日外資買賣超的值，單位是張數
        value1=Getfield("外資買賣超")[1];//取得昨日外資買賣超的值，單位是張數
        value2=close*value1/10;//收盤價*張數為買超金額，再將單位調整成萬元
        //今日盤中時,交易所並不會即時公告融資融券外資買賣超等籌碼資料
        //須等到交易所公告資後後才能正確取得今日籌碼詳細資訊
        //逐日計算是否滿足最低單日買超金額
        for xi=1 to periods
        begin
        	if value2[xi]>last//單日外資買超超過最低要求數值
        	then count=count+1;
        end;
        //6.設定警示條件：if.. then ret=1;
        if count=periods and close/close[1]<1.01//count=periods代表連續n日無一日不符合條件
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_3_getquote(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 3.getquote
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\3.getquote.xs
        XS Logic Reference:
        {@type:sensor}
        //第三個範例，我們示範如何利用盤中即時數據﹙委買、委賣、內盤量、外盤量等等﹚來製作警示
        //使用者可以透過"getquote"來取得這些數據
        //只要在編輯器上打getquote就可以直接挑選所提供的欄位
        //=====================範例：外盤漲停=======================================
        //4.運用函數
        //利用getfield取得買進價、賣出價及漲停價
        value1=GetQuote("Ask");//賣出價
        value2=GetQuote("DailyUplimit");//漲停價
        value3=GetQuote("Bid");//買進價
        //可以用q_來取代GetQuote完成快速引用
        //6.設定警示條件：if.. then ret=1;
        //賣出價=漲停價  且買進價跟賣出價相差不超過0.5%
        if value1=value2 and value1/value2<=1.005
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_4_if__then__else(df: pd.DataFrame, percent: int = 2) -> tuple[bool, str]:
        """
        Original Strategy: 4.if..then..else
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\4.if..then..else.xs
        XS Logic Reference:
        {@type:sensor}
        //if 條件1成立 then 動作1;
        //這是常用的語法，代表滿足條件1時，執行動作1
        //if 條件1成立 then 動作1 else 動作2;
        //這是完整的語法，除了定義滿足條件1時，執行動作1外，還定義了不滿足條件1時，需執行動作2
        //=====================範例：跳空上漲超過2%=======================================
        //例如我們在股價跳空上漲超過2%時希望電腦可以通知我們，我們可以編寫腳本如下：
        //1.宣告參數：利用input宣告輸入的參數。
        //if 條件1成立 then 動作1;
        //當出現2%跳空時，變數count等於1
        if open >= high[1]*(1+percent/100)
        then count=1; //只到這裡，這敘述最後必須加";"
        //if 條件1成立 then 動作1 else 動作2;
        //當count等於1時，觸發警示；count不等於1時，不觸發警示
        if count=1
        then ret=1 //有else時，這邊的敘述結束時就不必加上";"
        else
        ret=0;
        //6.設定警示條件：if.. then ret=1;
        //上面的句子可以簡化如下
        if open >= high[1]* (1+percent/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_5_if__begin__end__then(df: pd.DataFrame, N: int = 3, X: int = 10, _Y: int = 4) -> tuple[bool, str]:
        """
        Original Strategy: 5.if..begin..end..then
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\5.if..begin..end..then.xs
        XS Logic Reference:
        {@type:sensor}
        //當我們的條件需要多行敘述才能完成時，
        //可以用begin..end來標示。
        //=====================範例：累積漲幅達X%並且今日跳空開高超過Y%=======================================
        //例如若要找出前N日漲幅超過X%且今天跳空開高超過Y%的股票
        //1.宣告參數：利用input宣告輸入的參數。
        if open>high[1] then //跳空開高
        //用begin來呈現if 之後要執行的不只一件的事情
        begin
        value1=(1-close[1]/close[N])*100;//計算前N天的漲幅 
        value2=(open-high[1])/close*100;//計算跳空缺口的大小
        end;
        //最後用end來宣告if之後要執行程式的結束
        //6.設定警示條件：if.. then ret=1;
        if value1>=X and value2>=_Y
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_6_condition條件的交集(df: pd.DataFrame, range1: int = 2000, percent: float = 0.2) -> tuple[bool, str]:
        """
        Original Strategy: 6.condition條件的交集
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\6.condition條件的交集.xs
        XS Logic Reference:
        {@type:sensor}
        //就像value1~value99是系統內建變數，其回傳值是一個數值
        //condition1~condition99是系統內建回傳true或false邏輯值的變數名稱
        //於是我們在口語上的如果~而且~就通知我，這樣的語法很容易用這個方式來撰寫
        //========範例：融資餘額前十天大減超過2000張且減幅超過兩成===================
        //1.宣告參數：利用input宣告輸入的參數。
        condition1=false;//將condition1設成false狀態，一旦符合條件才轉成true
        //4.運用函數
        //利用getfield取得外資買賣超資料
        value1=getfield("融資餘額張數")[1];
        value2=getfield("融資餘額張數")[10];
        if value2-value1>range1 and (value2-value1)/value2>percent//計算融資增減張數
        then condition1=true;//融資餘額前十天大減超過2000張且減幅超過兩成
        //6.設定警示條件：if.. then ret=1;
        //多重條件交易才觸發警示
        if condition1 and average(close,20)/close[1]>1.05 and q_ask>open//近20天跌幅超過5%且現在外盤超過開盤價
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_7_0date_日期_的用法(df: pd.DataFrame, atVolume: int = 100, LaTime: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: 7.0date(日期)的用法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\7.0date(日期)的用法.xs
        XS Logic Reference:
        {@type:sensor}
        //系統用date來表示每根bar的日期，其回傳值為yyyymmdd，例如2013年3月20日為20130320
        //=========================範例：大單買進========================
        //1.宣告參數：利用input宣告輸入的參數。
        //2.宣告變數，利用variable
        value1=GetField("內外盤","Tick");//內外盤標記  內盤為-1 外盤為1
        //3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
        //日期函數應用
        if Date > XDate then Xtime =0; //開盤那根要歸0次數
        XDate = Date;
        if q_tickvolume > atVolume and value1>0 then  Xtime=Xtime+1; //外盤且單量夠大就加1次
        //6.設定警示條件：if.. then ret=1;
        if Xtime > LaTime  then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_7_1time_時間_的用法(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 7.1time(時間)的用法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\7.1time(時間)的用法.xs
        XS Logic Reference:
        {@type:sensor}
        //系統用time來代表時間，顯示格式為hhmmss
        //===========範例：開盤前三根K線都是陽線======================
        //3.引用時間序列的回傳值﹙包括開高低收成交量等﹚
        //時間函數應用
        if time=091500 //時間是九點十五分
        and close>close[1]     and close>open      
        and close[1]>close[2]  and close[1]>open[1]
        and close[2]>close[3]  and close[2]>open[2]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_8_0常用函數(df: pd.DataFrame, shortLen: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: 8.0常用函數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\8.0常用函數.xs
        XS Logic Reference:
        {@type:sensor}
        //函數是用來協助語法快速運算的功能
        //===========範例：均線糾結======================
        //1.宣告參數：利用input宣告輸入的參數。
        //4.運用函數
        //透過average這個函數計算數列的平均值
        value1=average(close,shortLen);//短期移動平均
        value2=average(close,midLen);//中期移動平均
        value3=average(close,longLen);//長期移動平均
        value4=value1-value2;
        value5=value2-value3;
        value6=value1-value3;
        //6.設定警示條件：if.. then ret=1;
        if absvalue(value4)/close<percent 
        and absvalue(value5)/close<percent 
        and absvalue(value6)/close<percent
        and close crosses above maxlist(value1,value2,value3)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_9_0for_迴圈_的用法(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 9.0for(迴圈)的用法
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\9.0for(迴圈)的用法.xs
        XS Logic Reference:
        {@type:sensor}
        //迴圈是用來重複執行多次相同的敘述句
        //==============================範例：開盤五分鐘創三次新高======================
        if  Barinterval=1 and barfreq ="Min" then Begin  //適用於1分鐘線
        //執行迴圈，檢查過去五分鐘高點過前高的次數
        if time = 90500 then begin
        	for n=1 to 5 begin//以下的陳述(到end;為止)，n=1執行一次，n=2執行一次，一直到n=5
        		if high[n]>high[n-1]
        		then count=count+1;
        	end;
        end;
        //設定警示條件：if.. then ret=1;
        if count>=3
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_9_1switch___case(df: pd.DataFrame, day: int = 10, ratio: float = 0.7) -> tuple[bool, str]:
        """
        Original Strategy: 9.1switch...case
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\9.1switch...case.xs
        XS Logic Reference:
        {@type:sensor}
        //透過switch..case的語法，可以在一個變數的數值不一樣時，往不同的流程進行
        //例如要計算外資過去十天買超超過七天時，可以運用以下的語法來寫腳本 
        //==============================範例：外資近日買超天數比例======================
        //1.宣告參數：利用input宣告輸入的參數。
        //2.宣告變數，利用variable
        value1=GetField("Fdifference");//外資買賣超
        for xi= 1 to day
        begin
        	//============================================
        	switch(value1[xi])
        	begin
        		case >0:
        			count=count+1;
        		case <0:
        			count=count;
        		case 0:
        			count=count;
        	end;//所有case都表達完之後，最後必須加end;來表示各種數值選項已結束
        	//============================================
        end;
        //6.設定警示條件：if.. then ret=1;
        if day<>0 and count/day>=ratio
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def strategy_9_2while_一直算到條件不符合_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 9.2while(一直算到條件不符合)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\9.2while(一直算到條件不符合).xs
        XS Logic Reference:
        {@type:sensor}
        //還有另一種迴圈是while，會一直執行到條件不符合
        //請小心不要造成無法跳出的無窮迴圈
        //==============================範例：開盤五分鐘創三次新高﹙改用while迴圈﹚======================
        if  Barinterval=1 and barfreq ="Min" then Begin  //適用於1分鐘線
        //執行迴圈，檢查過去五分鐘高點過前高的次數
        if time = 90500 then begin
        	n = 1;
        	while n <= 5 begin//以下的陳述(到end;為止)，n=1執行一次，n=2執行一次，一直到n=5
        		if high[n]>high[n-1]
        		then count=count+1;
        		n = n + 1;
        	end;
        end;
        //設定警示條件：if.. then ret=1;
        if count>=3
        then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 陣列例子(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 陣列例子
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\!語法範例\陣列例子.xs
        XS Logic Reference:
        {@type:sensor}
        //陣列可以用來存放多個相同屬性的變數值，而不需重複宣告
        //2.宣告變數，利用variable
        //宣告陣列，名稱ValueArray，內含100個元素，索引值從0到99，初始值為0
        array:ValueArray[99](0);
        //利用迴圈將陣列的每個元素填入對應的值，
        //例如：把過去1~99的High指到ValueArray裡
        //使得 ValueArray[1] =High[1] ,ValueArray[2] =High[2],
        //     ValueArray[3] =High[3] ... ValueArray[99] =High[99]
        for  i = 1 to 99
        begin
        	ValueArray[i] = High[i] ;
        end;
        //陣列可以透過內建函數做運算
        //如果要全部加總
        value1 = Array_Sum(ValueArray,1,99);
        //或是從第 7個加到第20個
        value1 = Array_Sum(ValueArray,7,20);
        //6.設定警示條件：if.. then ret=1;
        if value1 >= close * 14
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
