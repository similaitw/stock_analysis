# Auto-generated strategies for: 警示/2.市場常用語
import pandas as pd
import numpy as np

class Cat2市場常用語Strategies:

    @staticmethod
    def N期內創新高次數(df: pd.DataFrame, Length: int = 10, mNewHighTimes: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: N期內創新高次數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\N期內創新高次數.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        for i = 1 to la begin  
             if ( high[la-i]  > QHigh ) then
              begin
                _outputdays+=1;　　
              　QHigh = high[la-i];
             end; 
        end;
        if high = QHigh and _outputdays >= mNewHighTimes then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def N期內破底次數(df: pd.DataFrame, Length: int = 10, mNewLowTimes: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: N期內破底次數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\N期內破底次數.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        for i = 1 to la begin  
             if ( Low[la-i]  < QLow ) then
              begin
                _outputdays+=1;　　
              　QLow = Low[la-i];
             end; 
        end;
        if Low = QLow and _outputdays >= mNewLowTimes then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 今日多方表態(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 今日多方表態
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\今日多方表態.xs
        XS Logic Reference:
        {@type:sensor}
        {三次到頂而破}
        Array:peakDate[50](0),peakPrice[50](0),LongTrendPercent[50](0);
        CaliPrice = (High[0]+Low[0]+Close[0])/3;
        if CaliPrice[2] = MaxList(CaliPrice ,CaliPrice[1],CaliPrice[2],CaliPrice[3],CaliPrice[4]) and High[2] > CaliPrice[4]*1.02 and High[2] > CaliPrice[0]*1.02  then begin
        	peakDate[peakIndex] = Date[2];peakPrice[peakIndex] = High[2];
        	if peakIndex = 0 then LongTrendPercent[peakIndex]  = ( High[2]/ Close[2+20]-1)*100;
        	if peakIndex > 0 and DateDiff(date,peakDate[peakIndex-1]) >5 then LongTrendPercent[peakIndex]  = ( High[2]/ Close[2+20]-1)*100;
        	peakIndex+=1;
        end;
        if Date=CurrentDate  and Close > Open then begin
          if peakIndex >2 and Absvalue(peakPrice[peakIndex-1]/ peakPrice[peakIndex-2]-1 )< 0.01 and DateDiff(Date, peakDate[peakIndex-1])>20 then condition1 =true ;
          if  condition1  and  Close*1.065   >  highest(high[1],100) and
            minlist(low[100],low[99],low[98],low[97],low[96]) = Lowest(Low,100) and
            peakIndex >3 and LongTrendPercent[peakIndex-2] >20 and 
            Absvalue( peakPrice[peakIndex-1]/ peakPrice[peakIndex-2]-1 )< 0.01 and 
            DateDiff( peakDate[peakIndex-2] ,peakDate[peakIndex-3]) > 20 and 
            DateDiff( peakDate[peakIndex-1] ,peakDate[peakIndex-2]) > 5 and 
            Date < DateAdd(peakDate[peakIndex-1],"D",20)  
            then begin
            MaxPeak =MaxList(peakPrice[peakIndex-1],peakPrice[peakIndex-2]);
            if  Close > MaxPeak*1.005  and C>O then ret=1; 
            end;
        end;
        {激烈波動}
        if Date =currentdate then  begin
        	if C>O and Volume*GetField("均價") > 30000{仟元} and  Close > High*0.99 and high = highest(high,20) and highest(high[1],19)/lowest(Low[1],19) - 1 <0.065 and 
        	   TrueAll(ABSValue(high[1]/low[1]-1)<0.04,15) and  Volume > average(Volume[1],19)+STDEV then ret=1;   
        end;
        {波段初漲}
        if DateDiff(currentdate,date) < 93 then begin 	
            eLow = minlist(low,elow);
        	if DateDiff(currentdate,date) >=90 then begin iHigh =high; iDate= Date; value1=open; end;
        	hHigh = maxlist(high,hHigh); 
        	if eLow = Low then hHigh = low;
        	if hHigh > iHigh  then begin
        	if C>O and iHigh<> iLow and close> eLow*1.08 and DateDiff(Date,iDate)> 30 and v>500 then  ret=1;
        	iHigh =hHigh;iLOw = hHigh;iDate =Date;
        	end else iLow =minlist(Low,iLow);
        end;
        {突破均線極度糾結}
         AVG1 = average(close,5);AVG2 = average(close,10);AVG3 = average(close,20);AVG4 = average(close,60);
         if Date = currentdate then   begin
           VSTDEV=standarddev(volume[1],19,1)*3;
           PSTDEV=standarddev(H[1]-L[1],19,1)*3;
           if volume < average(Volume[1],19)+VSTDEV  or (C-O)/(H-L) < 0.7 then return;
           if C>O and Close  > maxlist(AVG1,AVG2,AVG3,AVG4)  and C > L +PSTDEV and  TrueAll( H[1]/L[1]-1 < 0.07,20) and 
               TrueAll(maxlist(AVG1,AVG2,AVG3,AVG4)/Maxlist( Minlist(AVG1,AVG2,AVG3,AVG4),0.01)-1 < 0.035,20) then ret=1;
         end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 今日資券籌碼分析(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 今日資券籌碼分析
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\今日資券籌碼分析.xs
        XS Logic Reference:
        {@type:sensor}
        if Currenttime > 220000  or Currenttime < 083000 then i=0; 
        settotalbar(3);
        if GetField("成交金額")[i]>10000000 and GetField("融資使用率")[i+1] > 0 and
           (GetField("融資使用率")[i]/GetField("融資使用率")[i+1]-1)*100 * (C[i]/C[i+1]-1)*100 >40
        then ret=1;
        if  C[i] > C[i+2]*1.1 and (GetField("融券增減張數")[i]*C[i])> 10000 then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 分鐘暴量n_(df: pd.DataFrame, percent: int = 100, Length: int = 200, XLimit: str = "True", atVolume: int = 500, TXT: str = "建議使用分鐘線") -> tuple[bool, str]:
        """
        Original Strategy: 分鐘暴量n%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\分鐘暴量n%.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        AvgVolume=Average(volume,Length);
        if XLimit then 
        begin
          if Volume > atVolume  and  volume > AvgVolume *(1+ percent/100)  then ret=1;
        end
        else
        begin
          if Volume > Volume[1]  and  volume > AvgVolume *(1+ percent/100)  then ret=1;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 外盤漲停(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 外盤漲停
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\外盤漲停.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if GetField("漲停價", "D") = q_Ask and close <> GetField("漲停價", "D") then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 多次觸底而破_(df: pd.DataFrame, HitTimes: int = 3, RangeRatio: int = 1, Length: int = 20) -> tuple[bool, str]:
        """
        Original Strategy: 多次觸底而破 
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\多次觸底而破 .xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        for ix = length-1  downto 1 
        begin
              if Low[ix] < LowUpperBound  then TouchRangeTimes +=1;  //回算在此區間中 進去瓶頸區的次數
        end;
        if  TouchRangeTimes >= HitTimes   and  (q_bid <theLow  or  close < theLow)  then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 大單敲進(df: pd.DataFrame, atVolume: int = 100, LaTime: int = 10, TXT: str = "須逐筆洗價") -> tuple[bool, str]:
        """
        Original Strategy: 大單敲進
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\大單敲進.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        Volumestamp =GetField("Volume", "D");
        if Date > XDate or Volumestamp = Volumestamp[1]  then Xtime =0; //開盤那根要歸0次數
        XDate = Date;
        if GetField("Volume", "Tick") > atVolume and GetField("內外盤","Tick")=1 then  Xtime+=1; //量夠大就加1次
        if Xtime > LaTime  then 
        begin
        	ret=1; 
        	Xtime=0;
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 急拉(df: pd.DataFrame, P1: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 急拉
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\急拉.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        IF close > close[1]*(1+P1/100)  and close=high and volume>volume[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 急殺(df: pd.DataFrame, P1: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 急殺
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\急殺.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        IF close < close[1]*(1-P1/100)  and close=Low and volume>volume[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 拉尾盤(df: pd.DataFrame, Ratio: int = 1, tTime: int = 130000, TXT: str = "限用5分鐘以下") -> tuple[bool, str]:
        """
        Original Strategy: 拉尾盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\拉尾盤.xs
        XS Logic Reference:
        {@type:sensor}
        if barfreq <> "Min" or barinterval > 5 then return;
        settotalbar(3);
        if time < tTime then fPrice = Close else
        if Close > fPrice*(1+Ratio/100) and time >= tTime and fPrice>0 
        then RET=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 殺尾盤(df: pd.DataFrame, TXT: str = "限用10分鐘以下") -> tuple[bool, str]:
        """
        Original Strategy: 殺尾盤
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\殺尾盤.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if Date> date[1] then KeyPrice = 0;		// 換日的話則重新定義KeyPrice
        if time>132000 and KeyPrice = 0 then KeyPrice =close;
        if KeyPrice > 0 and close <= KeyPrice *0.99//時間超過13:20分且十分鐘跌幅超過1%
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 當日上漲n_(df: pd.DataFrame, percent: float = 1.5) -> tuple[bool, str]:
        """
        Original Strategy: 當日上漲n%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\當日上漲n%.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if  WorkTrue and  currenttime <= TimeAdd(time,"M",1) and 
            Close > GetField("RefPrice", "D") * (1+ Percent/100) then 
        begin
        Ret=1;
        WorkTrue =false;
        end;
        if WorkTrue =false and Close < GetField("RefPrice", "D") * (1+ Percent/100) then WorkTrue =true;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 盤中多方警示(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 盤中多方警示
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\盤中多方警示.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(20);
        array:intrabarpersist Trigger[20](True);
        Array: intrabarpersist MK[330,6](0),intrabarpersist MD[7](1); {Time,Open,High,Low,Close,Volume}
        if CurrentTime < TimeAdd(OT,"M",BI*MF) then 
        begin  
        MD[2]=MaxList(MD[2],C); MD[3]=MinList(MD[3],C);MD[4]=C; MD[7]+=q_TickVolume;
        if BI =1 then  begin MD[1]=GetField("Open", "D");MD[2]=GetField("High", "D");MD[3]=GetField("Low", "D") ;end;
        end else begin
        MK[BI,0]=TimeAdd(OT,"M",BI-1);MK[BI,1]=MD[1];MK[BI,2]=MD[2];MK[BI,3]= MD[3];MK[BI,4]= MD[4];MK[BI,5]=GetField("Volume", "D")-q_TickVolume-MD[5];            
        BI+=1; MD[1]=C;MD[2]=C;MD[3]=C;MD[4]=C; MD[5]=GetField("Volume", "D")-q_TickVolume; MD[7]=q_TickVolume;
        end;
        array:intrabarpersist Q1[100,3](90000),intrabarpersist Q2[10,3](90000),intrabarpersist QI[5,5](0); QI[1,4] = 99; QI[2,4] = 9; 
        for QD = 1 to 2
        begin
        if QI[QD,1] < QI[QD,4] then QI[QD,1]+=1 else QI[QD,1]=0; 
        if QI[QD,1] =0 then QI[QD,2]=QI[QD,4] else QI[QD,2]=QI[QD,2]-1; 
        if QI[QD,1] =QI[QD,4] then QI[QD,3]=0 else QI[QD,3]=QI[QD,1]+1;
        end;
        Q1[QI[1,1],0] = currenttime;Q1[QI[1,1],1] = Close;Q1[QI[1,1],2] = q_TickVolume;     
        Q2[QI[2,1],0] = currenttime;Q2[QI[2,1],1] = Close;Q2[QI[2,1],2] = q_TickVolume;     
        {=============}
        if Date = currentdate then begin
        if TA1 = -1  then TA1 = Countif( GetField("融資增減張數")[1]<0,10);
        if V[1] > 0 then forceratio = GetField("主力買賣超張數")[1]/V[1] else forceratio = forceratio[1];
        if TA2 = -1 then TA2 = Summation(forceratio,10);
        if AVGX =10000 then AVGX = Average(Close,5);{五日}
        end;
        {=============}
        {開盤處理融資追繳後的反彈}
        if Trigger[19] then  if currenttime < 093000 and Close > Low *1.02 and Close > Open and  V > V[1]*0.6 and  TA1=10{融資增減張數之減少天數}
        and Low = Lowest(Low,20) and Low < Highest(high,20)*0.7 then  begin ret=1; trigger[19]=false; end;
        if h > highest(h[1],8) and v < highest(v[1],18)*BI/135 then return; 
        {過濾} 
        if Close = GetField("漲停價", "D") or Close < highest(high,10)*0.95 or GetField("均價")*GetField("Volume", "D") < 10000{仟元}   
           or Close < GetField("Volume", "D")*0.985 or Date <currentdate 
           or Close > AVGX*1.25 or Close > C[5]*1.25   then return;
        {1.1分鐘線爆量上漲}
        if Trigger[1] then  if MD[7] > (V[1]+V)/(270+BI)*3 and Close > MD[1]*1.01  then begin ret=1; trigger[1]=false; end;
        {2.5分鐘線3連陽}
        if Trigger[2] then  if BI >= 15 and MK[BI,4]> MK[BI-4,1] and MK[BI-5,4]> MK[BI-9,1] and MK[BI-10,4] > MK[BI-14,1] then begin ret=1; trigger[2]=false; end;
        {3.連日盤整後急拉}
        if Trigger[3] then  if Close > Q2[QI[2,3],1]*1.015 and TimeDiff(currenttime, Q2[QI[2,3],0],"M") <5 and TrueAll(absvalue(high[1]/low[1]-1) < 0.03,10) then begin ret=1; trigger[3]=false; end;
        {4.主動性買盤大增} variable: AvgOutSideVol(averageIF( close > close[1] ,volume,15));
        if Trigger[4] then if GetField("外盤量", "D") > AvgOutSideVol*1.5 then begin ret=1; trigger[4]=false; end;
        {5.多頭波動表態}   variable:STDEV(standarddev(High[1]-Low[1],15,1)*3);
        if Trigger[5] then if q_PriceChangeRatio >3{%} and Volume*GetField("均價") > 30000{仟元} and  High > Low + average(High[1]-Low[1],15)+STDEV then begin ret=1; trigger[5]=false; end;
        {6.多方放量待起漲} variable:VSTDEV(standarddev(volume,15,1)*3);
        if Trigger[6] then if q_PriceChangeRatio>2{%} and  volume > average(volume[1],15)+3*VSTDEV and close > highest(high[1],15)*0.965 then begin ret=1; trigger[6]=false; end;
        {7.連日強攻再滾量攻高}
        if Trigger[7] then  if BI>3 and  Close > High[1] and (MK[BI,5]+MK[BI-1,5]+MK[BI-2,5])*GetField("均價") > 10000{仟元} and CountIF(high>high[1],10) > 7 then begin ret=1; trigger[7]=false; end;
        {8.10個1分鐘階梯連漲} variable:Steps(true); 
        if Trigger[8] then if BI>10 then begin for QD=0 to 9   begin    Steps  = Steps and (MK[BI-QD,4]>MK[BI-1-QD,4]); end;  if Steps then begin ret=1; trigger[8]=false; end; ;end;  
        {9.多方人氣急增}
        if Trigger[9] then if BI>4  and q_PriceChangeRatio > 2{%} and MK[BI,4]> MK[BI-1,1]  and MK[BI-1,4]> MK[BI-3,1]  and (TimeDiff( currenttime, Q1[QI[1,3],0],"S")- TimeDiff(currenttime, Q2[QI[2,3],0],"S"))/90 > TimeDiff(currenttime, Q2[QI[2,3],0],"S")*3/10 then begin ret=1; trigger[9]=false; end;
        {10.主力決心作價}
        if Trigger[10] then if  V*GetField("均價")> 30000{仟元} and TA2{"主力買賣超張數"} > 0.33 and high= Highest(High,10) then  begin ret=1; trigger[10]=false; end;
        {11.開盤快速急攻}
        if Trigger[11] then if CurrentTime < 091500  and q_PriceChangeRatio >2{%} and Volume*GetField("均價") > 30000{仟元}  and high =Highest(High,15)  and  High > Low[1] + average(High[1]-Low[1],15)+STDEV then begin ret=1; trigger[11]=false; end;
        {12.2%門前急拉} 
        if Trigger[12] then if Q2[QI[2,1],1] < GetField("RefPrice", "D") *1.02 and close >= GetField("RefPrice", "D") *1.02 and  Close * q_TickVolume >500{仟元} and  Close > Q2[QI[2,3],1]*1.01  and   timediff(Currenttime,Q2[QI[2,3],0],"M")< 3{分鐘}  then begin ret=1; trigger[12]=false; end;    {3分鐘內快速拉升}
        {13.下殺後反彈過今高}
        if Trigger[13] then if Close > GetField("RefPrice", "D") and Close > GetField("Open", "D") and  Close = GetField("Volume", "D") and  Close >= GetField("Low", "D")*1.02 then begin ret=1; trigger[13]=false; end;
        {14.帶量衝新高}
        if Trigger[14] then if Close = GetField("Volume", "D") and Close > highest(H[1],20)  and Close*q_TickVolume > 3000  then begin ret=1; trigger[14]=false; end;
        {15.開盤15分鐘一路向上不回頭} variable:Counter(0);
        if Trigger[15] then  If BI =15 then  for QD =0 to 13  if MK[BI-QD,4] > MK[BI-1-QD,4] then Counter+=1;  if Counter > 12 then begin ret=1; trigger[15]=false; end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 突破上切線(df: pd.DataFrame, Length: int = 20, Rate: int = 50) -> tuple[bool, str]:
        """
        Original Strategy: 突破上切線
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\突破上切線.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        Factor = 100/Close[Length];
        if close > open and close > highest(high[1],Length) and 
           (linearregslope(high*Factor,3) -linearregslope(high*Factor,Length))>Rate*0.01 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 翻紅(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 翻紅
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\翻紅.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(7);
        if close crosses over close[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 翻黑(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 翻黑
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\翻黑.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(7);
        if close crosses under close[1]
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 資減券增(df: pd.DataFrame, x1: int = 300, x2: int = 200, x3: int = 10, Type: int = 1, TXT1: str = "僅適用日線", TXT2: str = "盤中無當日資券資料") -> tuple[bool, str]:
        """
        Original Strategy: 資減券增
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\資減券增.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        value1=GetField("融資增減張數")[Type];//融資增減張數
        value2=GetField("融券增減張數")[Type];//融券增減張數
         if value1 <-x1 and 
            value2 > x2 and 
            (value2-value1)/volume[Type]>x3/100
         then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 近日多方火力集中(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 近日多方火力集中
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\近日多方火力集中.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(10);
        if Currenttime > 170000  or Currenttime < 083000 then i=0; 
        Trigger=False;
        XAmount =Summation(GetField("成交金額")[i],CDay);XV = Summation(V[i],CDay);XPrice = XAmount/XV/1000;
        XDataAmount = Summation(GetField("主力買賣超張數")[i],CDay)/XV; if XDataAmount>0.2 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
        XDataAmount = Summation(GetField("實戶買賣超張數")[i],CDay)/XV; if XDataAmount>0.25 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
        XDataAmount = Summation(GetField("控盤者買賣超張數")[i],CDay)/XV; if XDataAmount>0.25 and trueall( XDataAmount[1]<0.1,5) then Trigger=true;
        if C[i]> XPrice and  V>300 and Trigger then ret=1;
        if high > iHigh then begin iHigh= high;iDate= Date; end;
        if DateDiff(Date,iDate) >30  and C > iHigh *0.935 and C<iHigh and
           (Summation(GetField("外資買賣超")[i]*XPrice,CDay) > 30000 or
            Summation(GetField("投信買賣超")[i]*XPrice,CDay) > 30000 or
        	Summation(GetField("自營商買賣超")[i]*XPrice,CDay) > 30000)
        then ret=1; 
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 連日量縮下跌(df: pd.DataFrame, percent: int = 4, ratio: int = 20, Length: int = 3) -> tuple[bool, str]:
        """
        Original Strategy: 連日量縮下跌
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\連日量縮下跌.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if close[Length-1]  > Close * (1+percent/100) and 
           volume[Length-1] > Volume* (1+ratio/100) and 
           TrueAll(Close < Close[1] ,Length-1) 
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開低走高(df: pd.DataFrame, OpenGap: int = 1, uppercent: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 開低走高
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\開低走高.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if  GetField("Low", "D") = GetField("Open", "D") and
            GetField("Open", "D") < GetField("RefPrice", "D") * (1- OpenGap/100) and
            q_Last	> GetField("Low", "D") * (1+uppercent/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 開高走低(df: pd.DataFrame, OpenGap: int = 1, Downpercent: int = 1) -> tuple[bool, str]:
        """
        Original Strategy: 開高走低
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\開高走低.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(3);
        if  GetField("High", "D") = GetField("Open", "D") and
            GetField("Open", "D") > GetField("RefPrice", "D") * (1+ OpenGap/100) and
            Close < GetField("High", "D") * (1 - Downpercent/100)
        then ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 高點回檔n_(df: pd.DataFrame, Length: int = 20, percent: int = 7) -> tuple[bool, str]:
        """
        Original Strategy: 高點回檔n%
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\警示\2.市場常用語\高點回檔n%.xs
        XS Logic Reference:
        {@type:sensor}
        settotalbar(Length + 3);
        if close < highest(high,Length)*(1- percent/100) then Ret=1;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
