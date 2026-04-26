import pandas as pd
from data.fetcher import DataFetcher
from scanner.engine import ScannerEngine

class MonitorEngine:
    def __init__(self, watchlist=None):
        self.watchlist = watchlist if watchlist else ['2330', '2317', '2454']

    def check_signals(self, strategy_name="MA Crossover"):
        """
        Check signals for the watchlist using the Scanner's logic.
        Returns a DataFrame with current status.
        """
        results = []
        for code in self.watchlist:
            try:
                # Fetch data (Short period for speed)
                df = DataFetcher.fetch_history(code, period="3mo")
                current_price = DataFetcher.fetch_current_price(code)
                
                if df.empty or len(df) < 25:
                    results.append({
                        "Stock ID": code,
                        "Price": current_price,
                        "Change": 0.0,
                        "Signal": "No Data",
                        "Action": "None"
                    })
                    continue

                # Calculate Change
                last_close = df['Close'].iloc[-2] if len(df) >= 2 else current_price
                change_pct = ((current_price - last_close) / last_close) * 100 if last_close > 0 else 0.0

                # Check Indicators
                # Re-using logic similar to Scanner, but focused on single stock
                close = df['Close']
                # Append current price to simulate "real-time" if the history doesn't define today yet
                # Note: fetch_history might have 'today' if market is open/closed. 
                # For simplicity, we assume df contains up-to-date candles.
                
                signal_msg = ""
                action = "Hold"

                if strategy_name == 'MA Crossover':
                    ma_fast = close.rolling(window=5).mean()
                    ma_slow = close.rolling(window=20).mean()
                    
                    if ma_fast.iloc[-1] > ma_slow.iloc[-1] and ma_fast.iloc[-2] <= ma_slow.iloc[-2]:
                        signal_msg = "Golden Cross"
                        action = "BUY"
                    elif ma_fast.iloc[-1] < ma_slow.iloc[-1] and ma_fast.iloc[-2] >= ma_slow.iloc[-2]:
                         signal_msg = "Death Cross"
                         action = "SELL"

                elif strategy_name == 'RSI':
                    rsi = ScannerEngine.calculate_rsi(close, 14)
                    val = rsi.iloc[-1]
                    if val < 30:
                        signal_msg = f"RSI Oversold ({val:.1f})"
                        action = "BUY"
                    elif val > 70:
                        signal_msg = f"RSI Overbought ({val:.1f})"
                        action = "SELL"

                elif strategy_name == 'Bollinger Bands':
                    ma20 = close.rolling(window=20).mean()
                    std20 = close.rolling(window=20).std()
                    lower = ma20 - (2 * std20)
                    upper = ma20 + (2 * std20)
                    
                    if current_price < lower.iloc[-1]:
                        signal_msg = "Touched Lower Band"
                        action = "BUY"
                    elif current_price > upper.iloc[-1]:
                        signal_msg = "Touched Upper Band"
                        action = "SELL"

                # Get Info
                name, _ = DataFetcher.get_stock_info(code)

                results.append({
                    "Stock ID": code,
                    "Name": name,
                    "Price": f"{current_price:.2f}",
                    "Change": f"{change_pct:+.2f}%",
                    "Signal": signal_msg if signal_msg else "-",
                    "Action": action
                })

            except Exception as e:
                print(f"Error monitoring {code}: {e}")
                results.append({"Stock ID": code, "Error": str(e)})

        return pd.DataFrame(results)

if __name__ == "__main__":
    monitor = MonitorEngine(['2330', '2603'])
    print(monitor.check_signals(strategy_name="RSI"))
