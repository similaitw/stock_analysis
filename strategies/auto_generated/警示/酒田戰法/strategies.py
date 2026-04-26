# Auto-generated strategies for: 警示/酒田戰法
import pandas as pd
import numpy as np

class 酒田戰法Strategies:

    @staticmethod
    def 三長下影線(df: pd.DataFrame, Percent: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 三長下影線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\三長下影線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(5);
        condition1 = (minlist(open,close)-Low) > absvalue(open-close)*3; 
        condition2 =  minlist(open, close)  > low* (100 + Percent)/100;
        if trueall( condition1 and condition2, 3) then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 三黑鴨(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 三黑鴨
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\三黑鴨.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	三黑鴨			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	連三黑K棒																																								
        }		
        settotalbar(5);																											
        {判斷狀況}								
        	condition1=	( open - close ) > (high -low) * 0.75					;//狀況1:	當期黑K棒
        	condition2=	( open[1] - close[1] ) > (high[1] -low[1]) * 0.75					;//狀況2:	前期黑K棒
        	condition3=	( open[2] - close[2] ) > (high[2] -low[2]) * 0.75					;//狀況3:	前前期黑K棒
        	condition4=	close < close[1] and close[1] < close[2]					;//狀況4:	連續下跌	
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 倒狀鎚子(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 倒狀鎚子
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\倒狀鎚子.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	倒狀鎚子			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	前期收長黑K棒 今期開低試圖上攻後收上影線短紅棒												
        }								
        settotalbar(5);
        {判斷狀況}								
        	condition1=	( open[1] - close[1] ) >(high[1] -low[1]) * 0.75					;//狀況1:	前期出長黑K棒
        	condition2=	 close[1] < close[2] - (high[2]-low[2])					;//狀況2:	前期呈波動放大下跌
        	condition3=	close > open and (high -close)> (close-open) *2					;//狀況3:	收紅上影線
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內困三日翻紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內困三日翻紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\內困三日翻紅.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	內困三日翻紅			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	黑K棒後內包前期短紅棒 當期再以紅棒突破黑棒開盤價												
        }								
        settotalbar(5);					
        {判斷狀況}								
        	condition1=	( open[2] - close[2] ) >(high[2] -low[2]) * 0.75					;//狀況1:	實體下跌K棒
        	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	實體上漲K棒
        	condition3=	 high[1] < high[2] and low[1] > low[2]					;//狀況3:	前期內包於前前期
        	condition4=	( close - open )  > 0.75 *(high -low)					;//狀況4:	當期實體上漲K棒
        	condition5=	close > open[2]					;//狀況5:	現價突破前前期開盤價
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 內困三日翻黑(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 內困三日翻黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\內困三日翻黑.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	內困三日翻黑			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	前兩期為長紅棒後包黑K棒 當期往下跌破紅棒開盤價																																								
        }	
        settotalbar(5);																											
        {判斷狀況}								
        	condition1=	close[2] > open[2] + high[3]-low[3]					;//狀況1:	前前期長紅棒
        	condition2=	high[2] < high[3] and low[2] > low[3]					;//狀況2:	前期內包黑K棒
        	condition3=	open >= close[1] and close < open[2]					;//狀況3:	開平高跌破三日低點
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 十字線(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 十字線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\十字線.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	十字線			[資料夾:]	酒田戰法	[適用方向]	不指定															
        [說明:]	K棒收十字線																																								
        }																						
        settotalbar(5);					
        {判斷狀況}								
        	condition1=	close =open					;//狀況1:	開盤價等於收盤價
        	condition2=	high>open					;//狀況2:	有漲
        	condition3=	low<open					;//狀況3:	有跌
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 吊人(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 吊人
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\吊人.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	吊人			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	短黑棒留長下影線																																								
        }																						
        settotalbar(5);						
        {判斷狀況}								
        	condition1=	open = High and close < open					;//狀況1:	開高收低留黑棒
        	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動倍增
        	condition3=	(close-low)> (open-close)  *2					;//狀況3:	下影線為實體兩倍以上
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭三星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭三星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\多頭三星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	多頭三星			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	近三期開高低收皆呈Ｖ形排列																																								
        }																						
        settotalbar(5);							
        {判斷狀況}								
        	condition1=	open> open[1] and open[2]>open[1]					;//狀況1:	開盤價排列
        	condition2=	high> high[1] and high[2]>high[1]					;//狀況2:	最高價排列
        	condition3=	low> low[1] and low[2]>low[1]					;//狀況3:	最低價排列
        	condition4=	close> close[1] and close[2]>close[1]					;//狀況4:	收盤價排列
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭吞噬(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭吞噬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\多頭吞噬.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	多頭吞噬			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	前期收短黑K棒 當期開低走高拉出長紅棒 波動率放大 穿過昨高																																									
        }																												
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出黑K棒
        	condition2=	( close - open ) >(high -low) * 0.75					;//狀況2:	當期紅棒
        	condition3=	high > high[1]					;//狀況3:	高過昨高
        	condition4=	open<low[1]					;//狀況4:	開低破昨低	
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭執帶(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭執帶
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\多頭執帶.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	多頭執帶			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	開在最低點一路走高收在最高點附近的K棒												
        }
        settotalbar(5);																
        {判斷狀況}								
        	condition1=	close>open					;//狀況1:	
        	condition2=	(Close-Open)>(high-low)*0.9					;//狀況2:	
        	condition3=	Close>Close[1]+high[1]-low[1]					;//狀況3:	
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭母子(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭母子
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\多頭母子.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	多頭母子			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	前期收長黑K棒 今期開高小幅收紅不過昨高																					
        }																						
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出長黑K棒
        	condition2=	close[1] < close[2] - high[2]-low[2]					;//狀況2:	前期呈波動放大下跌
        	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期紅棒
        	condition4=	high < high[1]					;//狀況4:	高不過昨高
        	condition5=	low>low[1]					;//狀況5:	低不破昨低
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多頭遭遇(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 多頭遭遇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\多頭遭遇.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	多頭遭遇			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	前期收黑K棒 當期開低走高紅棒嘗試反攻昨收 																																								
        }
        settotalbar(5);																														
        {判斷狀況}								
        	condition1=	 (open[1] - close[1] ) >(high[1] -low[1]) * 0.75					;//狀況1:	前期出黑K棒
        	condition2=	close[1] < close[2]					;//狀況2:	前期收跌
        	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期收紅K棒
        	condition4=	open  < close[1] and close < close[1]					;//狀況4:	開低且收跌
        	condition5=	low <  low[1]					;//狀況5:	破前期低點
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 夜星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 夜星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\夜星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	夜星			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	紅棒後 開高走低守平盤																																									
        }
        settotalbar(5);																														
        {判斷狀況}								
        	condition1=	 ( close[2] - open[2] ) > (high[2] -low[2]) * 0.75					;//狀況1:	前前期實體紅棒
        	condition2=	close[2] > close[3] + (high[3]-low[3])					;//狀況2:	前前期波動放大
        	condition3=	low[1] > high[2] and close[1]>open[1]					;//狀況3:	前期高開收紅
        	condition4=	open < close[1] and close < open - (high[1]-low[1])					;//狀況4:	當期開低收黑K棒
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量倒狀鎚子(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量倒狀鎚子
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量倒狀鎚子.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	倒狀鎚子			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	前期收長黑K棒 今期開低試圖上攻後收上影線短紅棒												
        }														
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( open[1] - close[1] ) >(high[1] -low[1]) * 0.75		;//狀況1:	前期出長黑K棒
        	condition2=	 close[1] < close[2] - (high[2]-low[2])					;//狀況2:	前期呈波動放大下跌
        	condition3=	close > open and (high -close)> (close-open) *2			;//狀況3:	收紅上影線	
        	condition4 = Volume > Volume[1];									;//狀況4:	帶量
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量吊人(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量吊人
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量吊人.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	帶量吊人			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	短黑棒留長下影線 量倍增																					
        }																						
        settotalbar(5);							
        {判斷狀況}								
        	condition1=	open = High and close < open					;//狀況1:	開高收低留黑棒
        	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動倍增
        	condition3=	(close-low)> (open-close)  *2					;//狀況3:	下影線為實體兩倍以上
        	condition4=	Volume > Volume[1]					;//狀況4:		
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量多頭吞噬(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量多頭吞噬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量多頭吞噬.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	多頭吞噬			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	前期收短黑K棒 當期開低走高拉出長紅棒 波動率放大 穿過昨高																																									
        }																						
        settotalbar(5);							
        {判斷狀況}								
        	condition1=	( open[1] - close[1] ) >(high[1] -low[1])*0.75					;//狀況1:	前期出黑K棒
        	condition2=	( close - open ) >(high -low) * 0.75					;//狀況2:	當期紅棒
        	condition3=	high > high[1]					;//狀況3:	高過昨高
        	condition4=	open<low[1]					;//狀況4:	開低破昨低
        	condition5=	Volume > Volume[1]*2					;//狀況5:	
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量多頭執帶(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量多頭執帶
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量多頭執帶.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	帶量多頭執帶			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	開在最低點一路走高收在最高點附近的K棒	衝出倍增量												
        }								
        settotalbar(5);								
        {判斷狀況}								
        	condition1=	close>open					;//狀況1:	
        	condition2=	(Close-Open)>(high-low)*0.9					;//狀況2:	
        	condition3=	Close>Close[1]+high[1]-low[1]					;//狀況3:	
        	condition4=	Volume > Volume[1]*2					;//狀況4:		
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量空頭執帶(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量空頭執帶
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量空頭執帶.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	帶量空頭執帶			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	量倍增長黑棒																																									
        }
        settotalbar(5);																														
        {判斷狀況}								
        	condition1=	( open - close ) > (high -low) * 0.8					;//狀況1:	實體黑K棒
        	condition2=	close < close[1] - (high[1]-low[1])					;//狀況2:	波動向下放大
        	condition3=	Volume > Volume[1]*2					;//狀況3:		
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 帶量鎚頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 帶量鎚頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\帶量鎚頭.xs
        XS Logic Reference:
        {@type:sensor}
        {									
        [檔名:]	帶量鎚頭			[資料夾:]	酒田戰法	[適用方向]	多		
        [說明:]	開盤後下跌試底,盤中拉升上攻後,收在高點留下下影線 衝出倍增量														
        }													
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	close >=high	and 	close > open			;//狀況1:	收高
        	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動放大
        	condition3=	(open-low) > (close - open)  *2 					;//狀況3:	長下影線
        	condition4=	Volume > Volume[1]*2					;//狀況4:	當期量倍增	
        {結果判斷}									
        IF									
        		condition1							
        	and	condition2							
        	and	condition3							
        	and	condition4														
        THEN	RET=1;								
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 晨星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 晨星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\晨星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	晨星			[資料夾:]	酒田戰法	[適用方向]	多															
        [說明:]	前前期收長黑K棒 前期再開低震盪收短紅棒後  當期開高紅棒反攻起跌點 																																									
        }																														
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( open[2] - close[2] ) >(high[2] -low[2]) * 0.75					;//狀況1:	前前期出黑K棒
        	condition2=	close[2] < close[3]-(high[3]-low[3])					;//狀況2:	跌勢擴大
        	condition3=	( close - open ) >(high -low) * 0.75					;//狀況3:	當期收紅K棒
        	condition4=	close> close[2]					;//狀況4:	收復黑棒收盤價
        	condition5=	close[1] <= close[2] and close[1] < open					;//狀況5:	前低收盤為三期低點
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭三星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭三星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭三星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭三星			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	開高低收A型排列																																										
        }																												
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	open[1] > open[2] and open[1] > open					;//狀況1:	開盤價A型
        	condition2=	high[1] > high[2] and high[1] > high					;//狀況2:	最高價A型
        	condition3=	low[1] > low[2] and low[1] > low					;//狀況3:	最低價A型
        	condition4=	close[1] > close[2] and close[1] > close					;//狀況4:	收盤價A型
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭吞噬(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭吞噬
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭吞噬.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭吞噬			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	紅棒後 開高下跌破昨低收長黑K棒																																									
        }																						
        settotalbar(5);								
        {判斷狀況}								
        	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.5					;//狀況1:	前期實體紅棒
        	condition2=	 high-low >( high[1]-low[1])*2					;//狀況2:	當期波動倍曾
        	condition3=	( open - close )>(high -low) * 0.75					;//狀況3:	當期黑K棒
        	condition4=	open > close[1] and close < low[1]					;//狀況4:	開高下跌破昨低
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭執帶(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭執帶
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭執帶.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭執帶			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	長黑棒																																									
        }																						
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( open - close ) > (high -low) * 0.8					;//狀況1:	實體黑K棒
        	condition2=	close < close[1] - (high[1]-low[1])					;//狀況2:	波動向下放大
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭母子(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭母子
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭母子.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭母子			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	長紅棒後 內包短黑K																																									
        }																													
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.8					;//狀況1:	前期實體紅棒
        	condition2=	close[1]> close[2] + high[2]-low[2]					;//狀況2:	前期波動向上放大
        	condition3=	( open - close )>(high -low) * 0.5					;//狀況3:	當期黑K棒
        	condition4=	high[1] > high and low[1] < Low 					;//狀況4:	高不過高 低不過低 內包K棒
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭流星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭流星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭流星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭流星			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	紅棒後 跳空開高收黑棒上影線																																								
        }																						
        settotalbar(5);						
        {判斷狀況}								
        	condition1=	open > close[1] and  close < open					;//狀況1:	開高且收黑
        	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	前期收實體紅K棒
        	condition3=	close[1]> close[2]					;//狀況3:	當期收漲
        	condition4=	(high - open ) > (open-close) * 2					;//狀況4:	留長上影線
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 空頭遭遇(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 空頭遭遇
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\空頭遭遇.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	空頭遭遇			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	紅棒後 開高走低守平盤																					
        }																													
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( close[1] - open[1] ) > (high[1] -low[1]) * 0.5					;//狀況1:	前期實體紅棒
        	condition2=	( open - close ) > (high -low) * 0.5					;//狀況2:	當期實體黑棒
        	condition3=	open > high[1] and close > close[1]					;//狀況3:	開過昨高收守平盤	
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 紅三兵(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 紅三兵
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\紅三兵.xs
        XS Logic Reference:
        {@type:sensor}
        {								
        [檔名:]	紅三兵			[資料夾:]	酒田戰法	[適用方向]	多	
        [說明:]	連續三根上漲實體K棒							
        }															
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	( close - open ) >(high -low) * 0.75					;//狀況1:	實體上漲K棒
        	condition2=	( close[1] - open[1] ) >(high[1] -low[1]) * 0.75					;//狀況2:	實體上漲K棒
        	condition3=	( close[2] - open[2] ) >(high[2] -low[2]) * 0.75					;//狀況3:	實體上漲K棒
        	condition4=	close > close[1]					;//狀況4:	上漲
        	condition5=	close[1] > close[2]					;//狀況5:	上漲
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        	and	condition3
        	and	condition4
        	and	condition5
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 蜻蜓十字(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 蜻蜓十字
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\蜻蜓十字.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	蜻蜓十字			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	T形線																					
        }																						
        settotalbar(5);							
        {判斷狀況}								
        	condition1=	close>=open and open>=high					;//狀況1:	開收高同價
        	condition2=	(high-low)> close *0.01					;//狀況2:	波動大於1%
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 鎚頭(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 鎚頭
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\鎚頭.xs
        XS Logic Reference:
        {@type:sensor}
        {									
        [檔名:]	鎚頭			[資料夾:]	酒田戰法	[適用方向]	多		
        [說明:]	開盤後下跌試底,盤中拉升上攻後,收在高點留下下影線								
        }																
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	close >=high	and 	close > open			;//狀況1:	收高
        	condition2=	(high -low) > 2 *(high[1]-low[1])					;//狀況2:	波動放大
        	condition3=	(open-low) > (close - open)  *2 					;//狀況3:	長下影線
        {結果判斷}									
        IF									
        		condition1							
        	and	condition2							
        	and	condition3													
        THEN	RET=1;								
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 長腳十字星(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 長腳十字星
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\酒田戰法\長腳十字星.xs
        XS Logic Reference:
        {@type:sensor}
        {																						
        [檔名:]	長腳十字星			[資料夾:]	酒田戰法	[適用方向]	空															
        [說明:]	大波動十字線																					
        }																												
        settotalbar(5);	
        {判斷狀況}								
        	condition1=	close>=open and open>=close					;//狀況1:	開收同價
        	condition2=	(high-low)> close *0.015					;//狀況2:	波動大於1.5%
        {結果判斷}		
        IF		
        		condition1
        	and	condition2
        THEN	RET=1;	
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
