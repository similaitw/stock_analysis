import pandas as pd
import numpy as np

try:
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    RandomForestClassifier = None

import os
from data.fetcher import DataFetcher

class StockPredictor:
    def __init__(self):
        self.model = None

        self.features = ['RSI', 'MACD', 'MACD_Signal', 'KD_K', 'KD_D', 'BB_Upper', 'BB_Lower', 'MA5_Diff', 'MA20_Diff', 'Volume_Change']

    def _calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate technical indicators for AI features using pandas only.
        """
        df = df.copy()
        
        # RSI (14)
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD (12, 26, 9)
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = exp1 - exp2
        df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
        
        # KD (9) - Stochastic Oscillator
        low_min = df['Low'].rolling(window=9).min()
        high_max = df['High'].rolling(window=9).max()
        df['RSV'] = 100 * ((df['Close'] - low_min) / (high_max - low_min))
        df['KD_K'] = df['RSV'].ewm(com=2, adjust=False).mean() # 1/3 K + 2/3 Prev_K -> alpha=1/3 -> com=2
        df['KD_D'] = df['KD_K'].ewm(com=2, adjust=False).mean()
        
        # Bollinger Bands (20, 2)
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['std'] = df['Close'].rolling(window=20).std()
        df['BB_Upper'] = df['MA20'] + (df['std'] * 2)
        df['BB_Lower'] = df['MA20'] - (df['std'] * 2)
        
        # MA Differences (Price vs MA)
        df['MA5'] = df['Close'].rolling(window=5).mean()
        df['MA5_Diff'] = (df['Close'] - df['MA5']) / df['MA5']
        df['MA20_Diff'] = (df['Close'] - df['MA20']) / df['MA20']
        
        # Volume Change
        df['Volume_Change'] = df['Volume'].pct_change()
        
        return df

    def prepare_data(self, df: pd.DataFrame):
        """
        Prepare features and target for training.
        """
        df = self._calculate_indicators(df)
        df = df.dropna()
        
        # Create Target: 1 if next day close > current close, else 0
        df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
        
        # Shift features? No, we use today's indicators to predict tomorrow's return.
        # But we need to be careful. The 'Target' is derived from Future(t+1) and Current(t).
        # We use Features(t) to predict Target(t).
        # Correct.
        
        # Drop the last row because it has no target (NaN after shift)
        # Actually shift(-1) creates NaN at the end.
        df = df.dropna()
        
        return df

    def train_model(self, stock_id: str, days: int = 2000):
        """
        Train a Random Forest model for the stock.
        """
        if not globals().get('SKLEARN_AVAILABLE', False):
             print(f"Skipping training for {stock_id}: Scikit-learn not available.")
             return None, 0.0, {}

        print(f"Training model for {stock_id}...")
        df = DataFetcher.fetch_history(stock_id, period='5y') # Fetch enough data
        
        if df.empty or len(df) < 200:
            return None, 0.0, {}

        data = self.prepare_data(df)
        
        X = data[self.features]
        y = data['Target']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        # Initialize and train model
        self.model = RandomForestClassifier(n_estimators=100, min_samples_split=10, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        
        # Feature Importance
        importances = dict(zip(self.features, self.model.feature_importances_))
        
        return self.model, accuracy, importances

    def predict_next_day(self, stock_id: str):
        """
        Predict the probability of up/down for the next trading day.
        """
        # Fetch data
        df = DataFetcher.fetch_history(stock_id, period='1y')
        if df.empty:
            return None
        
        # If model not trained, train it
        if self.model is None:
            self.train_model(stock_id)
            
        if self.model is None:
            return None
            
        # Calculate indicators for the latest data
        df_latest = self._calculate_indicators(df)
        
        # strict dropna might remove the last row if indicators invoke NaN (like rolling)
        # But we need the LAST row to predict Tomorrow.
        # So we only drop NaNs that are results of calculation at the beginning.
        # We check if the last row has valid features.
        
        latest_data = df_latest.iloc[[-1]][self.features]
        
        if latest_data.isnull().values.any():
            return {'error': 'Not enough data for indicators'}
            
        # Predict
        prediction = self.model.predict(latest_data)[0]
        probability = self.model.predict_proba(latest_data)[0] # [prob_down, prob_up]
        
        return {
            'prediction': 'Up' if prediction == 1 else 'Down',
            'probability_up': probability[1],
            'probability_down': probability[0],
            'last_date': df_latest.index[-1]
        }
