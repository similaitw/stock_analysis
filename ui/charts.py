import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

def calculate_ma(df, window):
    return df['Close'].rolling(window=window).mean()

def calculate_bollinger(df, window=20, dev=2):
    ma = df['Close'].rolling(window=window).mean()
    std = df['Close'].rolling(window=window).std()
    upper = ma + (std * dev)
    lower = ma - (std * dev)
    return upper, lower

def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_kd(df, period=9):
    low_min = df['Low'].rolling(window=period).min()
    high_max = df['High'].rolling(window=period).max()
    rsv = 100 * ((df['Close'] - low_min) / (high_max - low_min))
    k = rsv.ewm(com=2, adjust=False).mean() # fast 3, slow 3 usually. Here simulating with ewm
    d = k.ewm(com=2, adjust=False).mean()
    return k, d

def calculate_macd(df, fast=12, slow=26, signal=9):
    exp1 = df['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = df['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calculate_williams_r(df, period=14):
    """
    威廉指標 (%R)
    Williams %R = -100 * (Highest High - Close) / (Highest High - Lowest Low)
    """
    high_max = df['High'].rolling(window=period).max()
    low_min = df['Low'].rolling(window=period).min()
    wr = -100 * ((high_max - df['Close']) / (high_max - low_min))
    return wr

def calculate_dmi(df, period=14):
    """
    DMI 趨向指標 (Directional Movement Index)
    Returns: +DI, -DI, ADX
    """
    # 計算價格變動
    high_diff = df['High'].diff()
    low_diff = -df['Low'].diff()
    
    # 計算 +DM 和 -DM
    plus_dm = high_diff.where((high_diff > low_diff) & (high_diff > 0), 0)
    minus_dm = low_diff.where((low_diff > high_diff) & (low_diff > 0), 0)
    
    # 計算 True Range
    tr = pd.concat([
        df['High'] - df['Low'],
        (df['High'] - df['Close'].shift()).abs(),
        (df['Low'] - df['Close'].shift()).abs()
    ], axis=1).max(axis=1)
    
    # 計算平滑後的值
    atr = tr.rolling(period).mean()
    plus_di = 100 * (plus_dm.rolling(period).mean() / atr)
    minus_di = 100 * (minus_dm.rolling(period).mean() / atr)
    
    # 計算 DX 和 ADX
    dx = 100 * ((plus_di - minus_di).abs() / (plus_di + minus_di))
    adx = dx.rolling(period).mean()
    
    return plus_di, minus_di, adx

def calculate_volume_ma(df, window):
    """
    成交量移動平均線
    """
    return df['Volume'].rolling(window=window).mean()

def render_interactive_chart(df: pd.DataFrame, ticker: str, overlays: list = [], indicators: list = [], signals: list = []):
    """
    Render an interactive candlestick chart with configurable Overlays and Indicators using Plotly.
    
    Args:
        df: DataFrame with OHLCV data.
        ticker: Stock symbol.
        overlays: List of strings (e.g., ['MA5', 'MA20', 'Bollinger']).
        indicators: List of strings (e.g., ['Volume', 'RSI', 'KD', 'MACD', 'Williams %R', 'DMI']).
        signals: List of signal dicts with keys: date, price, type ('buy'/'sell'), text.
    """
    
    # Determine subplot rows
    row_map = { 'Price': 1 }
    current_row = 2
    
    # Pre-calculate layout settings
    row_heights = [0.65] # Main chart gets more space (增加主圖表空間)
    titles = ['']  # 移除子圖標題，避免重複
    
    active_indicators = [i for i in indicators if i in ['Volume', 'RSI', 'KD', 'MACD', 'Williams %R', 'DMI']]
    
    for ind in active_indicators:
        row_map[ind] = current_row
        row_heights.append(0.15) # Giving equal small height to indicators
        titles.append(ind)
        current_row += 1
        
    # Normalize row heights to sum to 1
    total = sum(row_heights)
    row_heights = [h/total for h in row_heights]
    
    fig = make_subplots(
        rows=len(row_heights), cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.02,  # 減少間距
        subplot_titles=titles,
        row_heights=row_heights
    )

    # 1. Main Chart (Candlestick) - 台股配色：紅漲綠跌
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='OHLC',
            increasing_line_color='#FF3333',  # 紅色（漲）
            decreasing_line_color='#00CC00',  # 綠色（跌）
            increasing_fillcolor='#FF6666',
            decreasing_fillcolor='#33DD33'
        ), 
        row=1, col=1
    )

    # 2. Overlays (on Main Chart)
    # Moving Averages - 改進配色
    colors = {
        'MA5': '#FFA500',    # 橘色
        'MA10': '#00BFFF',   # 深天藍
        'MA20': '#FF1493',   # 深粉紅
        'MA60': '#32CD32',   # 萊姆綠
        'MA120': '#9370DB'   # 中紫色
    }
    
    for overlay in overlays:
        if overlay.startswith('MA'):
            try:
                window = int(overlay.replace('MA', ''))
                ma = calculate_ma(df, window)
                fig.add_trace(
                    go.Scatter(
                        x=df.index, 
                        y=ma, 
                        mode='lines', 
                        name=overlay, 
                        line=dict(width=1.5, color=colors.get(overlay, '#FFFFFF'))
                    ), 
                    row=1, col=1
                )
            except:
                pass
        
        elif overlay == 'Bollinger':
            upper, lower = calculate_bollinger(df)
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=upper, 
                    mode='lines', 
                    name='布林上軌', 
                    line=dict(width=1, color='rgba(128,128,128,0.5)', dash='dot')
                ), 
                row=1, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=lower, 
                    mode='lines', 
                    name='布林下軌', 
                    line=dict(width=1, color='rgba(128,128,128,0.5)', dash='dot'), 
                    fill='tonexty',
                    fillcolor='rgba(128,128,128,0.1)'
                ), 
                row=1, col=1
            )

    # 3. Indicators (Separate Panels)
    for ind in active_indicators:
        r_idx = row_map[ind]
        
        if ind == 'Volume':
            # Volume Colors - 台股配色
            vol_colors = ['#FF6666' if r['Close'] >= r['Open'] else '#33DD33' for i, r in df.iterrows()]
            fig.add_trace(
                go.Bar(
                    x=df.index, 
                    y=df['Volume'], 
                    name='成交量', 
                    marker_color=vol_colors,
                    opacity=0.7
                ), 
                row=r_idx, col=1
            )
            
        elif ind == 'RSI':
            rsi = calculate_rsi(df)
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=rsi, 
                    name='RSI', 
                    line=dict(color='#9370DB', width=2)
                ), 
                row=r_idx, col=1
            )
            # Add 70/30 lines
            fig.add_hline(
                y=70, 
                row=r_idx, col=1, 
                line_dash="dash", 
                line_color="rgba(255,0,0,0.5)", 
                annotation_text="超買",
                annotation_position="right"
            )
            fig.add_hline(
                y=30, 
                row=r_idx, col=1, 
                line_dash="dash", 
                line_color="rgba(0,255,0,0.5)", 
                annotation_text="超賣",
                annotation_position="right"
            )
            
        elif ind == 'KD':
            k, d = calculate_kd(df)
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=k, 
                    name='K值', 
                    line=dict(color='#FFA500', width=1.5)
                ), 
                row=r_idx, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=d, 
                    name='D值', 
                    line=dict(color='#00BFFF', width=1.5)
                ), 
                row=r_idx, col=1
            )
            
        elif ind == 'MACD':
            macd, signal, hist = calculate_macd(df)
            # Histogram colors
            hist_colors = ['#FF6666' if h > 0 else '#33DD33' for h in hist]
            fig.add_trace(
                go.Bar(
                    x=df.index, 
                    y=hist, 
                    name='MACD柱狀圖', 
                    marker_color=hist_colors,
                    opacity=0.6
                ), 
                row=r_idx, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=macd, 
                    name='MACD', 
                    line=dict(color='#FFA500', width=1.5)
                ), 
                row=r_idx, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=signal, 
                    name='訊號線', 
                    line=dict(color='#00BFFF', width=1.5)
                ), 
                row=r_idx, col=1
            )
        
        elif ind == 'Williams %R':
            wr = calculate_williams_r(df)
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=wr, 
                    name='Williams %R', 
                    line=dict(color='#FF6347', width=2)
                ), 
                row=r_idx, col=1
            )
            # Add -20/-80 lines
            fig.add_hline(
                y=-20, 
                row=r_idx, col=1, 
                line_dash="dash", 
                line_color="rgba(255,0,0,0.5)", 
                annotation_text="超買",
                annotation_position="right"
            )
            fig.add_hline(
                y=-80, 
                row=r_idx, col=1, 
                line_dash="dash", 
                line_color="rgba(0,255,0,0.5)", 
                annotation_text="超賣",
                annotation_position="right"
            )
        
        elif ind == 'DMI':
            plus_di, minus_di, adx = calculate_dmi(df)
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=plus_di, 
                    name='+DI', 
                    line=dict(color='#00FF00', width=1.5)
                ), 
                row=r_idx, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=minus_di, 
                    name='-DI', 
                    line=dict(color='#FF0000', width=1.5)
                ), 
                row=r_idx, col=1
            )
            fig.add_trace(
                go.Scatter(
                    x=df.index, 
                    y=adx, 
                    name='ADX', 
                    line=dict(color='#FFD700', width=2)
                ), 
                row=r_idx, col=1
            )
    
    # 4. 加入策略信號標記
    if signals:
        buy_signals = [s for s in signals if s.get('type') == 'buy']
        sell_signals = [s for s in signals if s.get('type') == 'sell']
        
        if buy_signals:
            fig.add_trace(
                go.Scatter(
                    x=[s['date'] for s in buy_signals],
                    y=[s['price'] for s in buy_signals],
                    mode='markers',
                    name='買入信號',
                    marker=dict(symbol='triangle-up', size=12, color='#FF3333', line=dict(width=1, color='white')),
                    hovertext=[s.get('text', '') for s in buy_signals],
                    hoverinfo='text'
                ),
                row=1, col=1
            )
        
        if sell_signals:
            fig.add_trace(
                go.Scatter(
                    x=[s['date'] for s in sell_signals],
                    y=[s['price'] for s in sell_signals],
                    mode='markers',
                    name='賣出信號',
                    marker=dict(symbol='triangle-down', size=12, color='#00CC00', line=dict(width=1, color='white')),
                    hovertext=[s.get('text', '') for s in sell_signals],
                    hoverinfo='text'
                ),
                row=1, col=1
            )

    # Layout Updates - 專業圖表設定
    fig.update_layout(
        title={
            'text': f'{ticker} 技術分析圖表',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#FFFFFF'}
        },
        xaxis_rangeslider_visible=False,
        height=600 + (len(active_indicators) * 200),  # 增加圖表高度
        template="plotly_dark",  # 深色主題
        margin=dict(l=60, r=60, t=80, b=50),
        legend=dict(
            orientation="h", 
            yanchor="bottom", 
            y=1.01, 
            xanchor="right", 
            x=1,
            bgcolor='rgba(0,0,0,0.5)',
            font=dict(size=10)
        ),
        hovermode='x unified',  # 統一顯示游標資訊
        plot_bgcolor='#0E1117',  # 圖表背景色
        paper_bgcolor='#0E1117',  # 整體背景色
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1M", step="month", stepmode="backward"),
                    dict(count=3, label="3M", step="month", stepmode="backward"),
                    dict(count=6, label="6M", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1Y", step="year", stepmode="backward"),
                    dict(step="all", label="All")
                ]),
                bgcolor='rgba(100, 100, 100, 0.3)',
                activecolor='rgba(150, 150, 150, 0.5)',
                font=dict(color='white', size=10),
                x=0,
                y=1.05,
                xanchor='left',
                yanchor='bottom'
            ),
            rangeslider=dict(visible=True, thickness=0.05)
        )
    )
    
    # 啟用時間滑軌（rangeslider）進行縮放
    fig.update_xaxes(
        rangeslider_visible=True,  # 啟用滑軌
        rangeslider_thickness=0.05, # 滑軌高度
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        row=1  # 只在主圖表顯示滑軌
    )
    
    # 其他 X 軸不顯示滑軌
    for i in range(2, len(row_heights) + 1):
        fig.update_xaxes(
            rangeslider_visible=False,
            showgrid=True,
            gridcolor='rgba(128,128,128,0.2)',
            row=i
        )
    
    # 改進 Y 軸設定
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    )
    
    return fig
