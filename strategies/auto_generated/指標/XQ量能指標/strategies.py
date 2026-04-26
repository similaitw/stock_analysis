# Auto-generated strategies for: 指標/XQ量能指標
import pandas as pd
import numpy as np

class Xq量能指標Strategies:

    @staticmethod
    def CV_積量指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: CV(積量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\CV(積量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: CV指標
        //
        If CurrentBar = 1 then
        	_cv = Close * Volume
        else	
        	_cv = _cv[1] + (Close - Close[1]) * Volume;
        Plot1(_cv, "CV");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def CVI_累計成交量指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: CVI(累計成交量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\CVI(累計成交量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: CVI指標
        //
        If CurrentBar > 1 then
        	_cvi = _cvi[1] + GetField("UpVolume") - GetField("DownVolume");
        Plot1(_cvi, "CVI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def EMV_簡易波動指標_(df: pd.DataFrame, Length: int = 14) -> tuple[bool, str]:
        """
        Original Strategy: EMV(簡易波動指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\EMV(簡易波動指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: EMV指標
        //
        if Volume = 0 then
        	_emv = 0
        else
        	_emv = factor * (((High + Low) / 2 - (High[1] + Low[1]) / 2) * (High - Low)) / Volume;
        Plot1(_emv, "EMV");
        If CurrentBar >= Length Then
        	avg = Average(_emv, Length)
        else
        	avg = _emv;	
        Plot2(avg, "EMVA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def MFI_資金流向指標_(df: pd.DataFrame, Length: int = 6) -> tuple[bool, str]:
        """
        Original Strategy: MFI(資金流向指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\MFI(資金流向指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: MFI指標
        //
        tp = TypicalPrice;
        tv = tp * Volume;
        if tp > tp[1] then
          begin
        	utv = tv;
        	dtv = 0;
          end
        else
          begin
        	utv = 0;
        	dtv = tv;
          end;
        pmf = Average(utv, MinList(CurrentBar, length));
        nmf = Average(dtv, MinList(CurrentBar, length));
        if CurrentBar < Length or (pmf + nmf) = 0 then
        	mfivalue = 50
        else 
        	mfivalue = 100 * pmf /(pmf + nmf);
        Plot1(mfivalue, "MFI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def NVI_負量指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: NVI(負量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\NVI(負量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: NVI指標
        //
        if CurrentBar = 1 then
        	_nvi = 1
        else
          begin	
        	if Volume < Volume[1] then
        		_nvi = _nvi[1] + (Close - Close[1]) / Close[1]
        	else
        		_nvi = _nvi[1];
          end;
        Plot1(_nvi, "NVI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def OBV_能量潮指標_(df: pd.DataFrame, SMAlength: int = 5) -> tuple[bool, str]:
        """
        Original Strategy: OBV(能量潮指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\OBV(能量潮指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: OBV指標
        //
        if CurrentBar = 1 then
        	obvolume = 0
        else
          begin	
        	if close > close[1] then
        		obvolume = obvolume[1] + volume
        	else
        	  begin
        		if close < close[1] then
        			obvolume = obvolume[1] - volume
        		else
        			obvolume = obvolume[1];
        	  end;		
          end;
        obvSMA = average(obvolume,SMAlength);
        obvMMA = average(obvolume,MMAlength);
        obvSMA_Str = text(numToStr(SMAlength,0),"MA");
        obvMMA_Str = text(numToStr(MMAlength,0),"MA");
        Plot1(obvolume,"OBV");
        plot2(obvSMA,"SMA",checkbox:=1);
        plot3(obvMMA,"MMA",checkbox:=1);
        setplotLabel(2,obvSMA_Str);
        setplotLabel(3,obvMMA_Str);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PVC_成交量變動百分比指標_(df: pd.DataFrame, Length: int = 10) -> tuple[bool, str]:
        """
        Original Strategy: PVC(成交量變動百分比指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\PVC(成交量變動百分比指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: PVC指標
        //
        value1 = Average(Volume, Length);
        if value1 <> 0 then
        	_pvc = 100 * (Volume - value1) / value1
        else
        	_pvc = 0;
        Plot1(_pvc, "PVC");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PVI_正量指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: PVI(正量指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\PVI(正量指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: PVI指標
        //
        If CurrentBar = 1 then
        	_pvi = 1
        else
          begin	
        	if Volume > Volume[1] then
        		_pvi = _pvi[1] + (Close - Close[1]) / Close[1]
        	else
        		_pvi = _pvi[1];
          end;
        Plot1(_pvi, "PVI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def PVT_價量趨勢指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: PVT(價量趨勢指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\PVT(價量趨勢指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: PVT指標
        //
        If CurrentBar = 1 then
        	_pvt = 0
        else	
        	_pvt = _pvt[1] + (close - close[1])/close[1] * Volume;
        Plot1(_pvt, "PVT");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def TAPI_每點成交值指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: TAPI(每點成交值指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\TAPI(每點成交值指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: TAPI指標
        //
        Plot1(Volume / Close, "TAPI");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VA_成交量累積散佈指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: VA(成交量累積散佈指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\VA(成交量累積散佈指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VA指標
        //
        if High <> Low then
        	Value1 = ((Close - Low) - (High - Close))/(High - Low) * Volume
        else
        	Value1 = 0;
        If CurrentBar = 1 then
        	_va = Value1
        else	
        	_va = Value1 + _va[1];
        Plot1(_va, "VA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VAOsc_成交量累積散佈擺盪指標_(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: VAOsc(成交量累積散佈擺盪指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\VAOsc(成交量累積散佈擺盪指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VA-Osc指標
        //
        support = (Close - Low);
        resist = (High - Close);
        hlDiff = (High - Low);
        if hlDiff = 0 then
        	netSupportResist = 0
        else
        	netSupportResist = (support - resist) / hlDiff;
        Plot1(netSupportResist * Volume, "VA-Osc");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VR_成交量比率指標_(df: pd.DataFrame, Length: int = 26) -> tuple[bool, str]:
        """
        Original Strategy: VR(成交量比率指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\VR(成交量比率指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VR指標
        //
        qf = 0;
        qu = 0;
        qd = 0;
        for _index = 1 to length
          begin
        	if close[(_index - 1)] > close[_index] then
        		qu = qu + Volume[(_index - 1)]
        	else
        	  begin
        		if close[(_index - 1)] < close[_index] then
        			qd = qd + Volume[(_index - 1)]
        		else { close[(_index - 1)] = close[_index] }
        			qf = qf + Volume[(_index - 1)];
        	  end;
          end;
        if (qd + qf/2) <> 0 then
          _vr = 100 * (qu + qf/2) /(qd + qf/2)
        else
          _vr = 1000;
        Plot1(_vr, "VR");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VRC_成交量變動指標_(df: pd.DataFrame, Length: int = 12) -> tuple[bool, str]:
        """
        Original Strategy: VRC(成交量變動指標)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\VRC(成交量變動指標).xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VRC指標
        //
        if volume[Length] <> 0 then
        	_vrc = 100 * (volume - volume[Length])/volume[Length]
        else
        	_vrc = 50;
        Plot1(_vrc, "VRC");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def VVA指標(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: VVA指標
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\VVA指標.xs
        XS Logic Reference:
        {@type:indicator}
        // XQ: VVA指標
        //
        if High <> Low then
        	Value1 = (Close - Open)/(High - Low) * Volume
        else
        	Value1 = 0;
        If CurrentBar = 1 then
        	_vva = Value1
        else	
        	_vva = Value1 + _vva[1];
        Plot1(_vva, "VVA");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投資建議目標價潛在獲利率(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投資建議目標價潛在獲利率
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\投資建議目標價潛在獲利率.xs
        XS Logic Reference:
        {@type:indicator}
        //支援頻率：不定期
        //支援商品 ：美(股票)
        exchange = GetSymbolInfo("交易所");
        if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");
        if getField("投資建議目標價") <> 0 then
        value1 = (getField("投資建議目標價")-close)/getField("投資建議目標價")
        else value1 = 0;
        plot1(value1,"潛在獲利率");
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 投資建議評級___(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 投資建議評級(%)
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\投資建議評級(%).xs
        XS Logic Reference:
        {@type:indicator}
        //支援頻率：不定期
        //支援商品 ：美(股票)
        { 說明：
        value1 = getField("投資建議評級");
        1<= value1 < 1.5 (SB_積極買進)
        1.5 <= value1 < 2.5 (B_買進)
        2.5 <= value1 < 3.5 (H_中立)
        3.5 <= value1 < 4.5 (S_賣出)
        4.5 <= value1 <= 5(SS_積極賣出) 
        }
        exchange = GetSymbolInfo("交易所");
        if exchange <> "NYSE" and exchange <> "NASDAQ" and exchange <> "AMEX" then raiseruntimeerror("僅支援美股");
        value1 = getField("投資建議評級");
        if value1 = 0 then raiseruntimeerror("無投資建議評級的歷史紀錄");
        _rank = (5-value1)/4; //將投資建議評級，轉成0~100的分布形式
        plot1(_rank);
        if 1>=_rank and _rank>0.875 then begin
        	plot20(_rank);
        	setplotLabel(1,"積極買進");
        end else if 0.875>=_rank and _rank>0.625 then begin 
        	plot21(_rank);
        	setplotLabel(1,"買進");
        end else if 0.625>=_rank and _rank>0.375 then begin
        	plot22(_rank);
        	setplotLabel(1,"中立");
        end else if 0.375>=_rank and _rank>0.125 then begin
        	plot23(_rank);
        	setplotLabel(1,"賣出");
        end else if 0.125>=_rank and _rank>=0 then begin
        	plot24(_rank);
        	setplotLabel(1,"積極賣出");
        end;
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""

    @staticmethod
    def 新聞分數(df: pd.DataFrame) -> tuple[bool, str]:
        """
        Original Strategy: 新聞分數
        Source: e:\anti-gravity\stock\stock_analysis\temp_xscript_preset\指標\XQ量能指標\新聞分數.xs
        XS Logic Reference:
        {@type:indicator}
        {
        	XQ量能指標。
        	支援日頻率。支援上市櫃普通股商品。
        }
        value1 = GetField("新聞正向分數") - GetField("新聞負向分數"); 
        //新聞總分=正向分數－負向分數。來判斷目前的新聞聲量為正向或者負向。
        plot1(value1,"新聞總分");//正向分數-負向分數
        plot2(GetField("新聞聲量分數"),"新聞總量",checkbox:=1);//正向分數+負向分數
        plot3(GetField("新聞正向分數"),"新聞正總量",checkbox:=0);
        plot4(GetField("新聞負向分數"),"新聞負總量",checkbox:=0);
        """
        if df.empty: return False, ""
        # TODO: Implement indicators
        return False, ""
