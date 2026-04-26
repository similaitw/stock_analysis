
import pandas as pd
from datetime import datetime, timedelta

class ChipScanner:
    """
    籌碼選股策略 (Chip Analysis Strategies)
    Inspired by XScript: 
    - 投信持股從無到有.xs
    - N日內三大法人曾同步買超.xs (簡化版)
    """

    @staticmethod
    def _get_daily_net(df: pd.DataFrame, keywords: list) -> pd.Series:
        """Helper to extract daily net buy/sell for specific investor type"""
        if df.empty or 'name' not in df.columns:
            return pd.Series(dtype='float64')
            
        mask = pd.Series([False] * len(df))
        for key in keywords:
            mask |= df['name'].str.contains(key, case=False, na=False)
            
        subset = df[mask].copy()
        if subset.empty:
            return pd.Series(dtype='float64')
            
        # Ensure 'net' column exists
        if 'net' not in subset.columns:
            if 'buy' in subset.columns and 'sell' in subset.columns:
                subset['net'] = subset['buy'] - subset['sell']
            else:
                return pd.Series(dtype='float64')
                
        # Group by date and sum
        daily_net = subset.groupby('date')['net'].sum().sort_index()
        return daily_net

    @staticmethod
    def check_trust_entry(df: pd.DataFrame, threshold: int = 100) -> tuple[bool, str]:
        """
        策略：投信首日介入 (Trust First Entry)
        邏輯：
        1. 今日投信買超 > threshold (預設 100 張)
        2. 前 5 日投信累積買超 < threshold (表示之前沒大動作)
        """
        trust_net = ChipScanner._get_daily_net(df, ["Trust", "投信", "Investment_Trust"])
        
        if trust_net.empty or len(trust_net) < 10:
            return False, ""
        
        today_buy = trust_net.iloc[-1]
        
        # Calculate past 5 days sum (excluding today)
        past_5_days_sum = trust_net.iloc[-6:-1].sum()
        
        if today_buy > threshold and past_5_days_sum < (threshold * 0.5): # 嚴格一點：之前幾乎沒買
            return True, f"投信首日大買 ({int(today_buy)}張) 🔥"
            
        return False, ""

    @staticmethod
    def check_inst_cooperation(df: pd.DataFrame) -> tuple[bool, str]:
        """
        策略：土洋合作 (Foreign & Trust Buying Together)
        邏輯：
        1. 今日外資買超 > 0
        2. 今日投信買超 > 0
        3. 兩者合計買超 > 500 張
        """
        trust_net = ChipScanner._get_daily_net(df, ["Trust", "投信", "Investment_Trust"])
        foreign_net = ChipScanner._get_daily_net(df, ["Foreign", "外資", "Foreign_Investor"])
        
        if trust_net.empty or foreign_net.empty:
            return False, ""
            
        try:
            # Join series on date
            combined = pd.concat([trust_net, foreign_net], axis=1, keys=['Trust', 'Foreign']).dropna()
            
            if combined.empty: return False, ""
            
            last_date = combined.index[-1]
            t_buy = combined.loc[last_date, 'Trust']
            f_buy = combined.loc[last_date, 'Foreign']
            
            if t_buy > 0 and f_buy > 0 and (t_buy + f_buy) > 500:
                return True, f"土洋合作 (外資+{int(f_buy)}, 投信+{int(t_buy)}) 🤝"
                
        except Exception as e:
            # print(f"Error checking cooperation: {e}")
            pass
            
        return False, ""

    @staticmethod
    def check_foreign_continuous_buy(df: pd.DataFrame, days: int = 3) -> tuple[bool, str]:
        """
        策略：外資連續買超 (Foreign Continuous Buying)
        邏輯：
        1. 連續 N 天買超 > 0
        2. 累積買超 > X 張
        """
        foreign_net = ChipScanner._get_daily_net(df, ["Foreign", "外資", "Foreign_Investor"])
        
        if foreign_net.empty or len(foreign_net) < days:
            return False, ""
            
        last_n = foreign_net.iloc[-days:]
        
        if (last_n > 0).all() and last_n.sum() > 1000:
            return True, f"外資連{days}買 (累計{int(last_n.sum())}張) 💰"
            
        return False, ""
