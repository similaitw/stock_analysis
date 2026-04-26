import pandas as pd
import plotly.graph_objects as go
from data.fetcher import DataFetcher

def render_comparison_chart(stock_list: list, period: str = "1y"):
    """
    多股票比較圖表
    
    Args:
        stock_list: 股票代碼列表，如 ['2330', '2317', '2454']
        period: 時間週期
    
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    for ticker in stock_list:
        try:
            df = DataFetcher.fetch_history(ticker, period=period)
            if not df.empty:
                # 正規化價格（以第一天為 100）
                normalized = (df['Close'] / df['Close'].iloc[0]) * 100
                
                # 取得股票名稱
                name, _, _ = DataFetcher.get_stock_info(ticker)
                
                fig.add_trace(go.Scatter(
                    x=df.index,
                    y=normalized,
                    mode='lines',
                    name=f"{ticker} {name}",
                    line=dict(width=2),
                    hovertemplate='%{y:.2f}<extra></extra>'
                ))
        except Exception as e:
            print(f"Error loading {ticker}: {e}")
            continue
    
    fig.update_layout(
        title="多股票相對強弱比較 (Multi-Stock Comparison)",
        xaxis_title="日期 (Date)",
        yaxis_title="相對價格 (Relative Price, 起始點=100)",
        hovermode='x unified',
        template='plotly_dark',
        height=600,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0,0,0,0.5)'
        ),
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    # 加入 100 基準線
    fig.add_hline(
        y=100, 
        line_dash="dash", 
        line_color="rgba(255,255,255,0.3)",
        annotation_text="起始點",
        annotation_position="right"
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)',
        rangeslider_visible=True,
        rangeslider_thickness=0.05
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridcolor='rgba(128,128,128,0.2)'
    )
    
    return fig


def render_volume_distribution(df: pd.DataFrame, ticker: str):
    """
    成交量分布圖
    
    Args:
        df: 股票資料
        ticker: 股票代碼
    
    Returns:
        Plotly figure object
    """
    import plotly.express as px
    
    fig = px.histogram(
        df, 
        x='Volume', 
        nbins=50,
        title=f"{ticker} 成交量分布 (Volume Distribution)",
        labels={'Volume': '成交量 (Volume)', 'count': '次數 (Count)'}
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=400,
        showlegend=False
    )
    
    return fig


def render_return_distribution(df: pd.DataFrame, ticker: str):
    """
    日報酬率分布圖
    
    Args:
        df: 股票資料
        ticker: 股票代碼
    
    Returns:
        Plotly figure object
    """
    import plotly.express as px
    
    # 計算日報酬率
    returns = df['Close'].pct_change() * 100
    returns = returns.dropna()
    
    fig = px.histogram(
        returns, 
        nbins=50,
        title=f"{ticker} 日報酬率分布 (Daily Return Distribution)",
        labels={'value': '報酬率 % (Return %)', 'count': '次數 (Count)'}
    )
    
    fig.update_layout(
        template='plotly_dark',
        height=400,
        showlegend=False
    )
    
    # 加入 0% 基準線
    fig.add_vline(
        x=0, 
        line_dash="dash", 
        line_color="rgba(255,255,255,0.5)",
        annotation_text="0%",
        annotation_position="top"
    )
    
    return fig
