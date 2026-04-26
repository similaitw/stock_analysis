import yfinance as yf
import pandas as pd
import datetime
import time
import twstock
from FinMind.data import DataLoader
from data.cache import DataCache
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False
try:
    from config import Config
except ImportError:
    # Fallback if config not available
    class Config:
        @staticmethod
        def has_finmind_token():
            return False
        @staticmethod
        def should_use_finmind():
            return False
        FINMIND_API_TOKEN = ""

class DataFetcher:
    _finmind_api = None
    
    @staticmethod
    def _get_finmind_api():
        """取得 FinMind API 實例"""
        if DataFetcher._finmind_api is None and Config.has_finmind_token():
            print("[DataFetcher] 初始化 FinMind API...")
            DataFetcher._finmind_api = DataLoader()
            DataFetcher._finmind_api.login_by_token(api_token=Config.FINMIND_API_TOKEN)
            print("[DataFetcher] [OK] FinMind API 已連線")
        return DataFetcher._finmind_api
    @staticmethod
    def get_ticker_symbol(stock_id: str) -> str:
        """
        Convert stock ID to Yahoo Finance ticker format.
        e.g., "2330" -> "2330.TW"
        """
        if stock_id.endswith(".TW") or stock_id.endswith(".TWO"):
            return stock_id
        # Simple heuristic: try .TW first. In real scenario, might need to distinguish TSE/OTC.
        return f"{stock_id}.TW"

    @staticmethod
    def _validate_dataframe(df: pd.DataFrame) -> bool:
        """Validate if dataframe has required columns and data"""
        if df.empty:
            return False
        required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
        return all(col in df.columns for col in required_cols) and len(df) > 0
    
    @staticmethod
    @st.cache_data(ttl=300) if HAS_STREAMLIT else lambda f: f
    def fetch_history(stock_id: str, period: str = "1y", interval: str = "1d", max_retries: int = 3) -> pd.DataFrame:
        """
        Fetch historical data with retry logic and caching.
        Try FinMind first, fallback to Yahoo Finance.
        """
        # Check cache first
        cache_key = f"history_{stock_id}_{period}_{interval}"
        cached_data = DataCache.get(cache_key)
        if cached_data is not None and DataFetcher._validate_dataframe(cached_data):
            return cached_data
        
        last_error = None
        
        for attempt in range(max_retries):
            try:
                # Try FinMind first if available
                if Config.should_use_finmind():
                    print(f"[DataFetcher] 使用 FinMind 抓取 {stock_id} 歷史資料... (嘗試 {attempt + 1}/{max_retries})")
                    df = DataFetcher._fetch_from_finmind(stock_id, period)
                    
                    if DataFetcher._validate_dataframe(df):
                        print(f"[DataFetcher] [OK] FinMind 成功取得 {len(df)} 筆歷史資料")
                        DataCache.set(cache_key, df, ttl=300)
                        return df
                    else:
                        print(f"[DataFetcher] FinMind 資料驗證失敗，切換至 yfinance")
                
                # Fallback to yfinance
                print(f"[DataFetcher] 使用 yfinance 抓取 {stock_id} 歷史資料...")
                df = DataFetcher._fetch_from_yfinance(stock_id, period, interval)
                
                if DataFetcher._validate_dataframe(df):
                    DataCache.set(cache_key, df, ttl=300)
                    return df
                else:
                    last_error = f"資料驗證失敗 (empty or missing columns)"
                    
            except Exception as e:
                last_error = str(e)
                print(f"[DataFetcher] 抓取失敗 (嘗試 {attempt + 1}/{max_retries}): {e}")
                
                # Wait before retry (exponential backoff)
                if attempt < max_retries - 1:
                    wait_time = 0.5 * (2 ** attempt)  # 0.5s, 1s, 2s
                    time.sleep(wait_time)
        
        # All retries failed
        print(f"[DataFetcher] [ERR] {stock_id} 資料抓取失敗 ({max_retries} 次嘗試): {last_error}")
        return pd.DataFrame()
    
    @staticmethod
    def _fetch_from_finmind(stock_id: str, period: str) -> pd.DataFrame:
        """Fetch data from FinMind API"""
        try:
            api = DataFetcher._get_finmind_api()
            if not api:
                return pd.DataFrame()
            
            # Convert period to days
            period_days = {
                "1mo": 30, "3mo": 90, "6mo": 180,
                "1y": 365, "2y": 730, "5y": 1825, "10y": 3650
            }
            days = period_days.get(period, 365)
            
            end_date = datetime.datetime.now().strftime("%Y-%m-%d")
            start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
            
            df = api.taiwan_stock_daily(
                stock_id=stock_id,
                start_date=start_date,
                end_date=end_date
            )
            
            if df.empty:
                return pd.DataFrame()
            
            # Check if 'data' key exists (API error response)
            if isinstance(df, dict) and 'data' not in df:
                print(f"[DataFetcher] FinMind API 回傳格式錯誤: {df}")
                return pd.DataFrame()
            
            # Rename columns to match yfinance format
            df = df.rename(columns={
                'date': 'Date',
                'open': 'Open',
                'max': 'High',
                'min': 'Low',
                'close': 'Close',
                'Trading_Volume': 'Volume'
            })
            
            df['Date'] = pd.to_datetime(df['Date'])
            df['StockID'] = stock_id
            df = df.set_index('Date')
            
            return df
            
        except Exception as e:
            print(f"[DataFetcher] FinMind 錯誤: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def _fetch_from_yfinance(stock_id: str, period: str, interval: str) -> pd.DataFrame:
        """Fetch data from Yahoo Finance"""
        ticker_symbol = DataFetcher.get_ticker_symbol(stock_id)
        ticker = yf.Ticker(ticker_symbol)
        df = ticker.history(period=period, interval=interval)
        
        if df.empty:
            # Try .TWO if .TW failed (for OTC stocks)
            if ticker_symbol.endswith(".TW"):
                ticker_symbol = ticker_symbol.replace(".TW", ".TWO")
                ticker = yf.Ticker(ticker_symbol)
                df = ticker.history(period=period, interval=interval)

        if df.empty:
            return df
            
        df['StockID'] = stock_id
        return df

    @staticmethod
    @st.cache_data(ttl=60) if HAS_STREAMLIT else lambda f: f
    def fetch_current_price(stock_id: str) -> float:
        """
        Get the latest closed price. Try FinMind first, fallback to yfinance.
        """
        # Try FinMind first
        if Config.should_use_finmind():
            try:
                api = DataFetcher._get_finmind_api()
                if api:
                    # Get latest 1 day data
                    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    start_date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%d")
                    
                    df = api.taiwan_stock_daily(
                        stock_id=stock_id,
                        start_date=start_date,
                        end_date=end_date
                    )
                    
                    if not df.empty:
                        latest_price = df.iloc[-1]['close']
                        print(f"[DataFetcher] [OK] FinMind 取得 {stock_id} 最新價格: {latest_price}")
                        return float(latest_price)
            except Exception as e:
                print(f"[DataFetcher] FinMind 價格錯誤: {e}，切換至 yfinance")
        
        # Fallback to yfinance
        price = 0.0
        try:
            # Try twstock for real-time (kept as secondary fallback)
            stock = twstock.Stock(stock_id)
            if stock.price and len(stock.price) > 0 and stock.price[-1] is not None:
                return float(stock.price[-1])
        except Exception as e:
            print(f"twstock error for {stock_id}: {e}")

        # Fallback to yfinance if twstock fails
        try:
            ticker_symbol = DataFetcher.get_ticker_symbol(stock_id)
            ticker = yf.Ticker(ticker_symbol)
            if hasattr(ticker, 'fast_info') and 'last_price' in ticker.fast_info:
                 price = ticker.fast_info['last_price']
            
            if not price or price == 0.0:
                 df = ticker.history(period="1d")
                 if not df.empty:
                     price = df["Close"].iloc[-1]
                     
            return float(price)
        except Exception as e:
            print(f"yfinance error for {stock_id}: {e}")
            return 0.0

    @staticmethod
    def fetch_fundamentals(stock_id):
        """
        Fetch fundamental data using yfinance (Ticker.info).
        Returns dict with: Revenue YoY, Profit Margin, EPS, Institutional Buy (Stub).
        """
        try:
            ticker_symbol = DataFetcher.get_ticker_symbol(stock_id)
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info
            
            # 1. Revenue YoY (quarterlyRevenueGrowth)
            revenue_yoy = info.get('revenueGrowth', 0) * 100 if info.get('revenueGrowth') else 0.0
            
            # 2. Institutional Investors (Not available in free yfinance for TW stocks usually)
            # We stub this or use 'heldPercentInstitutions' if available
            inst_buy = 0
            inst_text = "N/A"
            if info.get('heldPercentInstitutions'):
                inst_text = f"{info['heldPercentInstitutions']*100:.2f}% (Hold)"
            
            # 3. Financial Statements (EPS, Margin)
            eps = info.get('trailingEps', 0.0)
            margin = info.get('profitMargins', 0) * 100 if info.get('profitMargins') else 0.0
            
            # 4. Dividend (Yield)
            div_yield = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0.0
            cash_div = info.get('dividendRate', 0.0)

            return {
                "Revenue YoY": revenue_yoy,
                "Inst Buy": inst_buy,
                "Inst Text": inst_text,
                "EPS": eps,
                "Margin": margin,
                "Dividend": cash_div,
                "Yield": div_yield
            }
        except Exception as e:
            print(f"Error fetching fundamentals for {stock_id}: {e}")
            return {
                "Revenue YoY": 0.0,
                "Inst Buy": 0,
                "Inst Text": "Err",
                "EPS": 0.0,
                "Margin": 0.0,
                "Dividend": 0.0,
                "Yield": 0.0
            }

    @staticmethod
    def fetch_institutional_investors(stock_id: str, days: int = 90) -> pd.DataFrame:
        """
        Fetch Institutional Investors buy/sell data (Foreign, Trust, Dealer).
        Returns DataFrame with columns: date, name, buy, sell, net.
        """
        # Try FinMind if available
        if Config.should_use_finmind():
            print(f"[DataFetcher] 使用 FinMind 抓取 {stock_id} 三大法人資料...")
            try:
                api = DataFetcher._get_finmind_api()
                if api:
                    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
                    
                    df = api.taiwan_stock_institutional_investors(
                        stock_id=stock_id,
                        start_date=start_date,
                        end_date=end_date
                    )
                    
                    if not df.empty:
                        # Rename columns for consistency
                        # FinMind columns: date, stock_id, name, buy, sell, ...
                        df['net'] = df['buy'] - df['sell']
                        print(f"[DataFetcher] ✅ FinMind 成功取得 {len(df)} 筆資料")
                        return df[['date', 'name', 'buy', 'sell', 'net']]
            except Exception as e:
                print(f"FinMind institutional investors error for {stock_id}: {e}")
        else:
            print(f"[DataFetcher] ⚠️ FinMind 未啟用，跳過三大法人資料")
        
        # Return empty DataFrame if FinMind not available
        return pd.DataFrame()

    @staticmethod
    def fetch_margin_trading(stock_id: str, days: int = 90) -> pd.DataFrame:
        """
        Fetch Margin Trading data (Financing, Short Selling).
        Returns DataFrame with columns: date, MarginPurchaseTodayBalance, ShortSaleTodayBalance.
        """
        # Try FinMind if available
        if Config.should_use_finmind():
            try:
                api = DataFetcher._get_finmind_api()
                if api:
                    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
                    
                    df = api.taiwan_stock_margin_purchase_short_sale(
                        stock_id=stock_id,
                        start_date=start_date,
                        end_date=end_date
                    )
                    
                    if not df.empty:
                        return df
            except Exception as e:
                print(f"FinMind margin trading error for {stock_id}: {e}")
        
        return pd.DataFrame()

    @staticmethod
    def fetch_shareholding(stock_id: str, days: int = 180) -> pd.DataFrame:
        """
        Fetch large shareholder holding percentage.
        Returns DataFrame with columns: date, HoldingSharesLevel, percent.
        """
        # Try FinMind if available
        if Config.should_use_finmind():
            try:
                api = DataFetcher._get_finmind_api()
                if api:
                    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    start_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
                    
                    df = api.taiwan_stock_shareholding(
                        stock_id=stock_id,
                        start_date=start_date,
                        end_date=end_date
                    )
                    
                    if not df.empty:
                        return df
            except Exception as e:
                print(f"FinMind shareholding error for {stock_id}: {e}")
        
        return pd.DataFrame()

    @staticmethod
    def get_stock_info(stock_id):
        """
        取得股票基本資訊
        Returns: (name, industry, description)
        """
        try:
            # 先嘗試從本地股票清單取得
            from data.storage import Storage
            import os
            
            if os.path.exists(Storage.STOCK_LIST_PATH):
                df_stocks = Storage.load_stock_list()
                match = df_stocks[df_stocks['code'] == stock_id]
                
                if not match.empty:
                    name = match.iloc[0]['name']
                    industry = match.iloc[0].get('industry', match.iloc[0].get('market', '-'))
                    return name, industry, ""
            
            # 如果本地沒有，嘗試使用 twstock
            import twstock
            if stock_id in twstock.codes:
                info = twstock.codes[stock_id]
                return info.name, info.type, f"上市日期: {info.start}\nCUSIP: {info.CUSIP}"
            
            return stock_id, "-", ""
        except Exception as e:
            print(f"[DataFetcher] 取得股票資訊錯誤: {e}")
            return stock_id, "-", ""


    @staticmethod
    def fetch_market_index(market: str = 'TSE', period: str = '1y') -> pd.DataFrame:
        """
        Fetch market index data (TSE or OTC).
        TSE: ^TWII
        OTC: ^TWOII
        """
        symbol = "^TWII" if market == 'TSE' else "^TWOII"
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period)
            return df
        except Exception as e:
            print(f"Error fetching index {market}: {e}")
            return pd.DataFrame()

    @staticmethod
    def fetch_borrowing_sell(stock_id: str, days: int = 90) -> pd.DataFrame:
        """
        Fetch Securities Lending (SBL) data (借券賣出餘額).
        FinMind: taiwan_stock_securities_lending
        Returns: DataFrame with columns [date, balance, ...]
        """
        try:
            # Lazy import to avoid circular dependency
            from FinMind.data import DataLoader
            api = DataLoader()
            start_date = (pd.Timestamp.now() - pd.DateOffset(days=days)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_securities_lending(
                stock_id=stock_id,
                start_date=start_date
            )
            
            if df.empty:
                return pd.DataFrame()
                
            # Rename columns to standard format
            # Typical columns: transaction_date, stock_id, securities_lending_volume, ...
            # We want 'date' and 'balance' (outstanding_volume)
            
            rename_map = {
                'transaction_date': 'date',
                'Date': 'date',
                'outstanding_volume': 'balance',
                'balance_volume': 'balance' # Just in case
            }
            df = df.rename(columns=rename_map)
            
            # Ensure 'balance' exists
            if 'balance' not in df.columns:
                print(f"[DataFetcher] SBL columns: {df.columns.tolist()} (Missing 'balance')")
                # Fallback: maybe use 'volume' as balance? Or just return empty to avoid crash.
                # Returning empty DF causes App to show "No SBL Data"
                return pd.DataFrame()
            
            return df
        except Exception as e:
            print(f"Error fetching SBL: {e}")
            return pd.DataFrame()

    @staticmethod
    def fetch_macro_data(type: str = 'USD/TWD', period: str = '1y') -> pd.DataFrame:
        """
        Fetch Macro Economic Data.
        Types: 
        - 'USD/TWD': TWD=X (Exchange Rate)
        - 'US10Y': ^TNX (US Treasury Yield 10 Years)
        - 'TAIEX_FUT_OP': Future/Option Open Interest (Need to find source, or use yfinance ^TWII proxy?)
          For 'TAIEX_FUT_OP' (Foreign Open Interest), FinMind might have it: 'taiwan_futures_institutional_investors'
        """
        symbol_map = {
            'USD/TWD': 'TWD=X',
            'US10Y': '^TNX',
            'VIX': '^VIX'
        }
        
        symbol = symbol_map.get(type)
        if not symbol:
            return pd.DataFrame()
            
        try:
            ticker = yf.Ticker(symbol)
            df = ticker.history(period=period)
            return df
        except Exception as e:
            print(f"Error fetching macro {type}: {e}")
            return pd.DataFrame()

    @staticmethod
    def fetch_per_pbr(stock_id: str, days: int = 365*2) -> pd.DataFrame:
        """
        Fetch PER/PBR Ratio data.
        FinMind: taiwan_stock_per_pbr (PER, PBR, dividend_yield)
        """
        try:
            api = DataLoader()
            start_date = (pd.Timestamp.now() - pd.DateOffset(days=days)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_per_pbr(
                stock_id=stock_id,
                start_date=start_date
            )
            return df
        except Exception as e:
            print(f"Error fetching PER/PBR: {e}")
            return pd.DataFrame()

    @staticmethod
    @st.cache_data(ttl=86400) if HAS_STREAMLIT else lambda f: f
    def fetch_monthly_revenue(stock_id: str, months: int = 12) -> pd.DataFrame:
        """
        抓取月營收明細
        Returns DataFrame with columns: date, revenue, revenue_year_growth_rate
        """
        cache_key = f"revenue_{stock_id}_{months}"
        cached = DataCache.get(cache_key)
        if cached is not None and not cached.empty:
            return cached
            
        try:
            api = DataFetcher._get_finmind_api()
            if not api:
                from FinMind.data import DataLoader
                api = DataLoader()
                
            start_date = (pd.Timestamp.now() - pd.DateOffset(months=months + 3)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_month_revenue(
                stock_id=stock_id,
                start_date=start_date
            )
            
            if not df.empty:
                DataCache.set(cache_key, df, ttl=86400) # 1 day
            return df
        except Exception as e:
            print(f"Error fetching monthly revenue for {stock_id}: {e}")
            return pd.DataFrame()

    @staticmethod
    @st.cache_data(ttl=86400) if HAS_STREAMLIT else lambda f: f
    def fetch_financial_ratios(stock_id: str, quarters: int = 8) -> pd.DataFrame:
        """
        抓取完整財務比率 (含三率與償債能力)
        從 taiwan_stock_financial_statement 計算
        """
        try:
            api = DataFetcher._get_finmind_api()
            if not api:
                from FinMind.data import DataLoader
                api = DataLoader()
                
            start_date = (pd.Timestamp.now() - pd.DateOffset(months=quarters*3+12)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_financial_statement(
                stock_id=stock_id,
                start_date=start_date
            )
            
            if df.empty:
                return pd.DataFrame()
            
            # 定義需要的項目
            needed_types = [
                'Revenue', 'OperatingRevenue', 'GrossProfit', 'OperatingIncome', 
                'IncomeAfterTaxes', 'TotalAssets', 'TotalLiabilities',
                'CurrentAssets', 'CurrentLiabilities', 'Inventories'
            ]
            
            subset = df[df['type'].isin(needed_types)]
            if subset.empty:
                return pd.DataFrame()
            
            # 計算比率
            res = pd.DataFrame(index=pivot.index)
            
            # 營收判定 (支援多種營收科目)
            rev_cols = ['Revenue', 'OperatingRevenue', 'TotalOperatingIncome']
            rev = None
            for c in rev_cols:
                if c in pivot.columns:
                    rev = pivot[c]
                    break
            
            if rev is None or rev.sum() == 0:
                # 如果沒有營收科目，嘗試使用利息收入或其他 (金融業特有)
                if 'InterestIncome' in pivot.columns:
                    rev = pivot['InterestIncome']
                else:
                    return pd.DataFrame()
            
            # 1. 三率 (有些科目可能缺失)
            if 'GrossProfit' in pivot.columns:
                res['gross_margin'] = (pivot['GrossProfit'] / rev) * 100
            
            # 營益率: 營業利益 / 營收
            op_cols = ['OperatingIncome', 'OperatingProfit']
            op_inc = None
            for c in op_cols:
                if c in pivot.columns:
                    op_inc = pivot[c]
                    break
            if op_inc is not None:
                res['operating_margin'] = (op_inc / rev) * 100
                
            # 淨利率: 本期淨利 / 營收
            net_cols = ['IncomeAfterTaxes', 'NetIncome', 'ProfitLossAfterTaxes']
            net_inc = None
            for c in net_cols:
                if c in pivot.columns:
                    net_inc = pivot[c]
                    break
            if net_inc is not None:
                res['net_margin'] = (net_inc / rev) * 100
            
            # 2. 償債與資產品質
            if 'TotalLiabilities' in pivot.columns and 'TotalAssets' in pivot.columns:
                res['debt_ratio'] = (pivot['TotalLiabilities'] / pivot['TotalAssets']) * 100
                
            if 'CurrentAssets' in pivot.columns and 'CurrentLiabilities' in pivot.columns:
                res['current_ratio'] = (pivot['CurrentAssets'] / pivot['CurrentLiabilities']) * 100
                inv = pivot.get('Inventories', 0)
                res['quick_ratio'] = ((pivot['CurrentAssets'] - inv) / pivot['CurrentLiabilities']) * 100
            
            return res.reset_index().tail(quarters)
            
        except Exception as e:
            print(f"Error calculating financial ratios for {stock_id}: {e}")
            return pd.DataFrame()

    @staticmethod
    @st.cache_data(ttl=86400) if HAS_STREAMLIT else lambda f: f
    def fetch_eps_data(stock_id: str, quarters: int = 8) -> pd.DataFrame:
        """
        Fetch Quarterly EPS data.
        From taiwan_stock_financial_statement
        Returns DataFrame with: date, eps
        """
        try:
            api = DataFetcher._get_finmind_api()
            if not api:
                from FinMind.data import DataLoader
                api = DataLoader()
                
            start_date = (pd.Timestamp.now() - pd.DateOffset(months=quarters*3+12)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_financial_statement(
                stock_id=stock_id,
                start_date=start_date
            )
            
            if df.empty:
                return pd.DataFrame()
            
            # 支援多種 EPS 欄位定義
            eps_types = ['EarningsPerShare', 'EPS', 'BasicEarningsPerShare']
            subset = df[df['type'].isin(eps_types)]
            
            if subset.empty:
                return pd.DataFrame()
            
            subset = subset.sort_values('date')
            # 如果有多個符合，取最後一個出現的 type (通常是最新的定義)
            result = subset.drop_duplicates('date', keep='last')[['date', 'value']].rename(columns={'value': 'eps'})
            return result.tail(quarters).reset_index(drop=True)
            
        except Exception as e:
            print(f"Error fetching EPS for {stock_id}: {e}")
            return pd.DataFrame()

    @staticmethod
    @st.cache_data(ttl=86400) if HAS_STREAMLIT else lambda f: f
    def fetch_balance_sheet_ratios(stock_id: str, quarters: int = 8) -> pd.DataFrame:
        """
        抓取資產負債表關鍵指标
        """
        try:
            api = DataFetcher._get_finmind_api()
            if not api:
                from FinMind.data import DataLoader
                api = DataLoader()
                
            start_date = (pd.Timestamp.now() - pd.DateOffset(months=quarters*3+12)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_financial_statement(
                stock_id=stock_id,
                start_date=start_date
            )
            
            if df.empty:
                return pd.DataFrame()
                
            needed = ['TotalAssets', 'TotalLiabilities', 'Equity', 'CurrentAssets', 'CurrentLiabilities', 'Inventories']
            subset = df[df['type'].isin(needed)]
            if subset.empty:
                return pd.DataFrame()
                
            # 支援多種負債與資產科目
            liab = pivot.get('TotalLiabilities')
            assets = pivot.get('TotalAssets')
            equity = pivot.get('Equity')
            
            res = pd.DataFrame(index=pivot.index)
            if liab is not None and assets is not None:
                res['debt_to_asset'] = (liab / assets) * 100
            if liab is not None and equity is not None:
                res['debt_to_equity'] = (liab / equity) * 100
            
            if 'CurrentAssets' in pivot.columns and 'CurrentLiabilities' in pivot.columns:
                res['current_ratio'] = (pivot['CurrentAssets'] / pivot['CurrentLiabilities']) * 100
                inv = pivot.get('Inventories', 0)
                res['quick_ratio'] = ((pivot['CurrentAssets'] - inv) / pivot['CurrentLiabilities']) * 100
                    
            return res.reset_index().tail(quarters)
        except Exception as e:
            print(f"Error fetching balance sheet ratios for {stock_id}: {e}")
            return pd.DataFrame()


    @staticmethod
    def fetch_dividend_history(stock_id: str, years: int = 5) -> pd.DataFrame:
        """
        抓取股利發放歷史
        Returns DataFrame with: date, CashEarningsDistribution, StockEarningsDistribution
        """
        try:
            api = DataLoader()
            start_date = (pd.Timestamp.now() - pd.DateOffset(years=years)).strftime('%Y-%m-%d')
            df = api.taiwan_stock_dividend(
                stock_id=stock_id,
                start_date=start_date
            )
            return df
        except Exception as e:
            print(f"Error fetching dividend history: {e}")
            return pd.DataFrame()
    
    @staticmethod
    def fetch_fundamental_data(stock_id: str) -> dict:
        """抓取基本面資料 (ROE, PB, PE等)"""
        try:
            ticker_symbol = DataFetcher.get_ticker_symbol(stock_id)
            ticker = yf.Ticker(ticker_symbol)
            info = ticker.info
            
            return {
                'ROE': info.get('returnOnEquity', 0) * 100 if info.get('returnOnEquity') else 0,
                'PBR': info.get('priceToBook', 0),
                'PER': info.get('trailingPE', 0),
                'dividend_yield': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0
            }
        except Exception as e:
            print(f"Error fetching fundamental data: {e}")
            return {}


if __name__ == "__main__":
    # Test
    print("Testing DataFetcher...")
    print(DataFetcher.get_stock_info("2330"))

    df = DataFetcher.fetch_history("2330")
    print(f"2330 shape: {df.shape}")
    print(df.tail())
    price = DataFetcher.fetch_current_price("2330")
    print(f"2330 price: {price}")
