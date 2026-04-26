"""
Technical Dashboard Module
技術面儀表板 - 價格趨勢與技術指標分析
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from data.fetcher import DataFetcher
from ui.language import Language

def calculate_deviation(df: pd.DataFrame, ma_period: int = 20) -> pd.Series:
    """計算乖離率 (Deviation from MA)"""
    ma = df['Close'].rolling(window=ma_period).mean()
    deviation = ((df['Close'] - ma) / ma) * 100
    return deviation

def create_per_pbr_river_chart(df_per_pbr: pd.DataFrame, metric: str = 'PER', ticker: str = '') -> go.Figure:
    """
    創建 PER/PBR 河流圖
    
    Args:
        df_per_pbr: DataFrame with columns ['date', 'PER', 'PBR']
        metric: 'PER' or 'PBR'
        ticker: Stock ID for title
    """
    if df_per_pbr.empty or metric not in df_per_pbr.columns:
        return go.Figure()
    
    df = df_per_pbr.copy()
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # 計算統計值
    median = df[metric].median()
    std = df[metric].std()
    
    # 創建河流圖
    fig = go.Figure()
    
    # +2σ
    fig.add_trace(go.Scatter(
        x=df['date'], y=[median + 2*std] * len(df),
        mode='lines', name='+2σ',
        line=dict(color='rgba(255,0,0,0.3)', width=1, dash='dot'),
        fill=None
    ))
    
    # +1σ
    fig.add_trace(go.Scatter(
        x=df['date'], y=[median + std] * len(df),
        mode='lines', name='+1σ',
        line=dict(color='rgba(255,100,0,0.5)', width=1, dash='dot'),
        fill='tonexty', fillcolor='rgba(255,0,0,0.1)'
    ))
    
    # 中位數
    fig.add_trace(go.Scatter(
        x=df['date'], y=[median] * len(df),
        mode='lines', name='中位數',
        line=dict(color='white', width=2),
        fill='tonexty', fillcolor='rgba(255,150,0,0.1)'
    ))
    
    # -1σ
    fig.add_trace(go.Scatter(
        x=df['date'], y=[median - std] * len(df),
        mode='lines', name='-1σ',
        line=dict(color='rgba(0,255,0,0.5)', width=1, dash='dot'),
        fill='tonexty', fillcolor='rgba(0,255,0,0.1)'
    ))
    
    # -2σ
    fig.add_trace(go.Scatter(
        x=df['date'], y=[median - 2*std] * len(df),
        mode='lines', name='-2σ',
        line=dict(color='rgba(0,255,0,0.3)', width=1, dash='dot'),
        fill='tonexty', fillcolor='rgba(0,255,0,0.1)'
    ))
    
    # 實際值
    fig.add_trace(go.Scatter(
        x=df['date'], y=df[metric],
        mode='lines', name=f'{metric} 實際值',
        line=dict(color='cyan', width=2)
    ))
    
    # 標示當前位置
    current_value = df[metric].iloc[-1]
    fig.add_annotation(
        x=df['date'].iloc[-1],
        y=current_value,
        text=f'{current_value:.2f}',
        showarrow=True,
        arrowhead=2,
        arrowcolor='yellow',
        bgcolor='rgba(0,0,0,0.7)',
        font=dict(color='yellow', size=12)
    )
    
    fig.update_layout(
        title=f'{ticker} {metric} 河流圖 (River Chart)',
        xaxis_title='日期',
        yaxis_title=metric,
        template='plotly_dark',
        height=400,
        hovermode='x unified',
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def render_technical_dashboard(stock_id: str, period: str = '1y', lang: str = 'zh'):
    """
    渲染技術面儀表板
    
    Args:
        stock_id: 股票代碼
        period: 資料期間
        lang: 語言 ('zh' or 'en')
    """
    
    st.subheader(Language.get('technical_analysis', lang))
    
    with st.spinner(Language.get('loading', lang)):
        try:
            # 1. 抓取股價資料
            df = DataFetcher.fetch_history(stock_id, period=period)
            
            if df.empty:
                st.error(Language.get('no_data', lang))
                return
            
            # 2. 主圖表 (K線 + 均線 + 成交量)
            st.markdown("### 📈 價格走勢與技術指標")
            
            from ui.charts import render_interactive_chart
            
            # 使用者可選擇的疊加指標
            col1, col2 = st.columns(2)
            with col1:
                selected_overlays = st.multiselect(
                    '疊加指標',
                    ['MA5', 'MA10', 'MA20', 'MA60', 'MA120', 'Bollinger'],
                    default=['MA5', 'MA20', 'MA60']
                )
            with col2:
                selected_indicators = st.multiselect(
                    '副圖指標',
                    ['Volume', 'RSI', 'MACD', 'KD'],
                    default=['Volume', 'RSI']
                )
            
            fig = render_interactive_chart(
                df, 
                stock_id, 
                overlays=selected_overlays,
                indicators=selected_indicators
            )
            st.plotly_chart(fig, width='stretch')
            
            # 3. 乖離率分析
            st.markdown("### 📊 乖離率分析")
            
            col1, col2, col3 = st.columns(3)
            
            for i, ma_period in enumerate([5, 20, 60]):
                deviation = calculate_deviation(df, ma_period)
                current_dev = deviation.iloc[-1]
                
                # 計算歷史分位數
                percentile = (deviation <= current_dev).sum() / len(deviation) * 100
                
                with [col1, col2, col3][i]:
                    st.metric(
                        f"MA{ma_period} 乖離率",
                        f"{current_dev:.2f}%",
                        help=f"歷史分位數: {percentile:.1f}%"
                    )
                    
                    # 簡易視覺化
                    if current_dev > 10:
                        st.warning("⚠️ 嚴重正乖離")
                    elif current_dev > 5:
                        st.info("📈 正乖離")
                    elif current_dev < -10:
                        st.warning("⚠️ 嚴重負乖離")
                    elif current_dev < -5:
                        st.info("📉 負乖離")
                    else:
                        st.success("✅ 正常範圍")
            
            # 4. PER/PBR 河流圖
            st.markdown("### 🌊 估值河流圖 (Valuation River)")
            
            with st.spinner("載入 PER/PBR 資料..."):
                df_per_pbr = DataFetcher.fetch_per_pbr(stock_id, days=730)
                
                if not df_per_pbr.empty:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        fig_per = create_per_pbr_river_chart(df_per_pbr, 'PER', stock_id)
                        st.plotly_chart(fig_per, width='stretch')
                    
                    with col2:
                        fig_pbr = create_per_pbr_river_chart(df_per_pbr, 'PBR', stock_id)
                        st.plotly_chart(fig_pbr, width='stretch')
                    
                    # 顯示當前估值
                    current_per = df_per_pbr['PER'].iloc[-1]
                    current_pbr = df_per_pbr['PBR'].iloc[-1]
                    median_per = df_per_pbr['PER'].median()
                    median_pbr = df_per_pbr['PBR'].median()
                    
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("當前 PER", f"{current_per:.2f}")
                    col2.metric("歷史中位數 PER", f"{median_per:.2f}")
                    col3.metric("當前 PBR", f"{current_pbr:.2f}")
                    col4.metric("歷史中位數 PBR", f"{median_pbr:.2f}")
                else:
                    st.info("無 PER/PBR 資料")
            
            # 5. 大盤比較
            st.markdown("### 📊 大盤比較")
            
            with st.spinner("載入大盤資料..."):
                df_tse = DataFetcher.fetch_market_index('TSE', period=period)
                
                if not df_tse.empty:
                    # 計算相對強弱
                    stock_return = (df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100
                    tse_return = (df_tse['Close'].iloc[-1] / df_tse['Close'].iloc[0] - 1) * 100
                    relative_strength = stock_return - tse_return
                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("個股報酬率", f"{stock_return:.2f}%")
                    col2.metric("大盤報酬率", f"{tse_return:.2f}%")
                    col3.metric(
                        "相對強弱", 
                        f"{relative_strength:.2f}%",
                        delta=f"{'強於' if relative_strength > 0 else '弱於'}大盤"
                    )
        
        except Exception as e:
            st.error(f"發生錯誤: {e}")
            st.exception(e)
