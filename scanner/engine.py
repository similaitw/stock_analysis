import pandas as pd
# Force reload
import twstock
from data.fetcher import DataFetcher
from strategies.xscript_strategies import XScriptStrategies
import time
import concurrent.futures

class ScannerEngine:
    TSE_CODES = [] # Cache for stock codes

    @staticmethod
    def calculate_rsi(series, period=14):
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).fillna(0)
        loss = (-delta.where(delta < 0, 0)).fillna(0)
        
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    @staticmethod
    def get_stock_list(market_type='Tw50'):
        """
        Get list of stock codes.
        market_type: 'Tw50', 'TSE' (All Listed), 'OTC' (All OTC), 'All'
        """
        if market_type == 'Tw50':
             return ['2330', '2317', '2454', '2308', '2303', '2881', '2882']
        elif market_type == 'TEST':
             return ['2330', '2303', '2603']
        elif market_type == 'All':
            # Load from Storage
            from data.storage import Storage
            df = Storage.load_stock_list()
            if not df.empty:
                return df['code'].tolist()
            return ['2330'] # Fallback
        else:
            return ['2330', '2317', '2454', '2603', '2609', '2615', '2881', '2882', '2891', '2886']

    @staticmethod
    def _check_strategy(strategy_name, df, code, params=None):
        """
        Check if a single strategy signal exists.
        Returns: (bool, str) -> (is_signal, reason)
        params: dict of parameters for the strategy
        """
        if params is None:
            params = {}
            
        try:
            close = df['Close']
            
            if strategy_name == 'MA Crossover':
                # MA5 > MA20
                ma_fast = close.rolling(window=5).mean()
                ma_slow = close.rolling(window=20).mean()
                
                if ma_fast.iloc[-1] > ma_slow.iloc[-1] and ma_fast.iloc[-2] <= ma_slow.iloc[-2]:
                    return True, "Golden Cross (MA5 > MA20)"

            elif strategy_name == 'RSI Oversold':
                # RSI < 30
                rsi = ScannerEngine.calculate_rsi(close, 14)
                if rsi.iloc[-1] < 30:
                    return True, f"RSI Oversold ({rsi.iloc[-1]:.2f})"

            elif strategy_name == 'Bollinger Buy':
                # Close < Lower Band
                ma20 = close.rolling(window=20).mean()
                std20 = close.rolling(window=20).std()
                lower_band = ma20 - (2.0 * std20)
                
                if close.iloc[-1] < lower_band.iloc[-1]:
                    return True, "Touched Lower Band"
            
            elif strategy_name == 'Best Combo':
                # 1. Define Strategies to test
                strategies = {
                    'MA Cross': lambda c: (c.rolling(5).mean() > c.rolling(20).mean()) & (c.rolling(5).mean().shift(1) <= c.rolling(20).mean().shift(1)),
                    'RSI Oversold': lambda c: ScannerEngine.calculate_rsi(c, 14) < 30,
                    'Boll Buy': lambda c: c < (c.rolling(20).mean() - 2*c.rolling(20).std()),
                    'MACD Buy': lambda c: (c.ewm(span=12).mean() - c.ewm(span=26).mean()) > (c.ewm(span=12).mean() - c.ewm(span=26).mean()).ewm(span=9).mean()
                }
                
                best_strat = None
                best_win_rate = -1.0
                current_signal = False
                
                # 2. Backtest each strategy on historical data (simple vector backtest)
                # Use last 6 months data for testing
                future_returns = df['Close'].shift(-5) / df['Close'] - 1 # 5-day return
                
                for name, logic_func in strategies.items():
                    try:
                        signals = logic_func(close)
                        valid_signals = signals & future_returns.notna()
                        if valid_signals.sum() == 0:
                            continue
                            
                        wins = (valid_signals & (future_returns > 0)).sum()
                        total_trades = valid_signals.sum()
                        win_rate = wins / total_trades if total_trades > 0 else 0
                        
                        if win_rate > best_win_rate:
                            best_win_rate = win_rate
                            best_strat = name
                            current_signal = signals.iloc[-1]
                    except:
                        continue
                        
                if current_signal and best_win_rate >= 0.5: # Filter: Win rate must be >= 50%
                    return True, f"Best Strategy: {best_strat} (Win Rate: {best_win_rate*100:.0f}%)"

            elif strategy_name == 'Advanced Funnel':
                # Funnel Strategy Logic
                fund_data = DataFetcher.fetch_fundamentals(code)
                
                # Classic: Inst Buy > 0 + MA Long (MA5 > MA20 > MA60)
                is_classic = False
                if fund_data.get('Inst Buy', 0) > 0:
                    ma5 = close.rolling(5).mean().iloc[-1]
                    ma20 = close.rolling(20).mean().iloc[-1]
                    ma60 = close.rolling(60).mean().iloc[-1]
                    if ma5 > ma20 > ma60:
                        is_classic = True

                # Growth: Revenue YoY > 0 + Margin > 0 + Price Breakout (Close > MA60)
                is_growth = False
                if fund_data.get('Revenue YoY', 0) > 0 and fund_data.get('Margin', 0) > 0:
                        ma60 = close.rolling(60).mean().iloc[-1]
                        if close.iloc[-1] > ma60:
                            is_growth = True

                # Defensive: Yield > 4% + Inst Buy (optional) + Price Support (Close > MA60)
                is_defensive = False
                if fund_data.get('Yield', 0) > 4.0:
                        ma60 = close.rolling(60).mean().iloc[-1]
                        if close.iloc[-1] > ma60:
                            is_defensive = True
                
                matched_funnels = []
                if is_classic: matched_funnels.append("Classic")
                if is_growth: matched_funnels.append("Growth")
                if is_defensive: matched_funnels.append("Defensive")
                
                if matched_funnels:
                    return True, f"Funnel: {', '.join(matched_funnels)} (Rev:{fund_data.get('Revenue YoY',0):.1f}%, Inst:{fund_data.get('Inst Buy',0)//1000}k)"

            # --- Dynamic Strategies from Registry (Fallback) ---
            # This covers 04, 05, 06 and any XScript/Legacy strategies loaded in registry
            # Note: Hardcoded XScript checks removed to allow fallback to registry (which supports params)
            
            from strategies.registry import StrategyRegistry
            # Try to run from registry
            is_match, reason = StrategyRegistry.run_strategy(strategy_name, df, **params)
            if is_match:
                return True, reason
                    
        except Exception as e:
            # print(f"Strategy check error for {code}: {e}")
            pass
            
        return False, ""

    @staticmethod
    def scan(strategy_name, market_type='Tw50', progress_callback=None):
        """Legacy single strategy scan keeping for backward compatibility"""
        return ScannerEngine.scan_strategies([strategy_name], market_type, progress_callback, match_mode='OR')

    @staticmethod
    def _process_stock(code, strategy_names, match_mode, strategy_params):
        """
        Process a single stock for scanning.
        Returns: dict result or None
        """
        try:
            # Fetch recent history
            df = DataFetcher.fetch_history(code, period="6mo")
            if df.empty or len(df) < 30: 
                return None
            
            # Pre-fetch chip data if any chip-related strategies are present
            chip_data_cache = {}
            chip_keywords = ['籌碼', '投信', '外資', '法人', '融資', '融券', '借券', '主力', '大戶']
            has_chip_strategy = any(
                any(keyword in strat for keyword in chip_keywords) 
                for strat in strategy_names
            )
            
            if has_chip_strategy:
                try:
                    # Batch fetch all chip data once
                    chip_data_cache = {
                        'institutional': DataFetcher.fetch_institutional_investors(code, 90),
                        'margin': DataFetcher.fetch_margin_trading(code, 90),
                        'sbl': DataFetcher.fetch_borrowing_sell(code, 90)
                    }
                except Exception as e:
                    # If chip data fetch fails, continue with empty cache
                    chip_data_cache = {
                        'institutional': pd.DataFrame(),
                        'margin': pd.DataFrame(),
                        'sbl': pd.DataFrame()
                    }
            
            matched_reasons = []
            
            for strat in strategy_names:
                # Get params for this strategy
                params = strategy_params.get(strat, {}).copy()
                
                # Inject chip data cache if available
                if chip_data_cache:
                    params['_chip_cache'] = chip_data_cache
                
                is_signal, reason = ScannerEngine._check_strategy(strat, df, code, params=params)
                if is_signal:
                    matched_reasons.append(f"[{strat}] {reason}")
            
            is_hit = False
            if match_mode == 'AND':
                # Must match ALL strategies
                if len(matched_reasons) == len(strategy_names):
                    is_hit = True
            else: # OR
                # Match ANY strategy
                if len(matched_reasons) > 0:
                    is_hit = True
            
            if is_hit:
                last_price = df['Close'].iloc[-1]
                name, _ = DataFetcher.get_stock_info(code)
                vol = df['Volume'].iloc[-1] if 'Volume' in df.columns else 0
                return {
                    'Stock ID': code,
                    'Name': name,
                    'Price': f"{last_price:.2f}",
                    'Signal': " | ".join(matched_reasons),
                    'Volume': vol,
                    'Date': df.index[-1].strftime('%Y-%m-%d')
                }
        except Exception as e:
            # print(f"Error scanning {code}: {e}")
            pass
            
        return None


    @staticmethod
    def scan_strategies(strategy_names, market_type='Tw50', progress_callback=None, match_mode='AND', stock_list=None, strategy_params=None):
        """
        Scan multiple strategies using ThreadPoolExecutor for concurrency.
        strategy_params: dict of { strategy_name: { param: value } }
        """
        if stock_list:
            codes = stock_list
        else:
            codes = ScannerEngine.get_stock_list(market_type)
        
        results = []
        total = len(codes)
        if strategy_params is None:
            strategy_params = {}
        
        # Dynamic thread pool sizing based on stock count
        if total < 50:
            max_workers = 4
        elif total < 200:
            max_workers = 8
        else:
            max_workers = 12
            
        print(f"[Scanner] Starting scan for {total} stocks with {max_workers} threads...")
        print(f"[Scanner] Strategies: {', '.join(strategy_names)}")
        print(f"[Scanner] Match mode: {match_mode}")
        
        # Use ThreadPoolExecutor for concurrent scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Map futures to stock codes
            future_to_code = {
                executor.submit(
                    ScannerEngine._process_stock, 
                    code, 
                    strategy_names, 
                    match_mode, 
                    strategy_params
                ): code for code in codes
            }
            
            completed_count = 0
            success_count = 0
            error_count = 0
            
            for future in concurrent.futures.as_completed(future_to_code):
                code = future_to_code[future]
                completed_count += 1
                
                # Update progress
                if progress_callback:
                    progress_callback(completed_count / total, f"Scanning {code} ({completed_count}/{total})...")
                
                try:
                    res = future.result()
                    if res:
                        results.append(res)
                        success_count += 1
                except Exception as e:
                    error_count += 1
                    print(f"[Scanner] Error processing {code}: {e}")
        
        print(f"[Scanner] Scan complete: {success_count} signals found, {error_count} errors")
        return pd.DataFrame(results)

if __name__ == "__main__":
    print("Testing Scanner...")
    # res = ScannerEngine.scan('MA Crossover', market_type='Tw50')
    res = ScannerEngine.scan('XScript - Momentum Breakout', market_type='TEST')
    print(res)
