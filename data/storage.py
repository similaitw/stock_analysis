import pandas as pd
import twstock
import os

class Storage:
    DATA_DIR = os.path.dirname(os.path.abspath(__file__))
    STOCK_LIST_PATH = os.path.join(DATA_DIR, 'stock_list.csv')

    @staticmethod
    def update_stock_list():
        """
        Download latest stock codes from twstock and save to CSV.
        """
        print("Updating stock list from twstock...")
        # twstock might need update
        try:
            twstock.__update_codes()
        except:
            pass # Ignore if update fails, use bundled
        
        # Filter for stocks only (TSE & OTC)
        data = []
        for code, info in twstock.codes.items():
            if info.type == '股票':
                market = "TSE" if info.market == '上市' else "OTC"
                data.append({
                    'code': code,
                    'name': info.name,
                    'market': market,
                    'industry': info.group
                })
        
        df = pd.DataFrame(data)
        df.to_csv(Storage.STOCK_LIST_PATH, index=False, encoding='utf-8-sig')
        print(f"Saved {len(df)} stocks to {Storage.STOCK_LIST_PATH}")
        return df

    @staticmethod
    def load_stock_list():
        """
        Load stock list from CSV. If not exists, update first.
        """
        if not os.path.exists(Storage.STOCK_LIST_PATH):
            return Storage.update_stock_list()
        
        try:
            return pd.read_csv(Storage.STOCK_LIST_PATH, dtype={'code': str})
        except Exception as e:
            print(f"Error loading stock list: {e}")
            return Storage.update_stock_list()

if __name__ == "__main__":
    df = Storage.update_stock_list()
    print(df.head())
