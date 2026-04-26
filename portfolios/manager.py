"""
選股組合管理模組
Portfolio Manager for Custom Screening
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

class PortfolioManager:
    """選股組合管理器"""
    
    def __init__(self, data_dir: str = "data/portfolios"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def create_portfolio(
        self,
        name: str,
        description: str,
        strategy: str,
        market: str,
        stocks: List[str] = None
    ) -> Dict:
        """
        建立新的選股組合
        
        Args:
            name: 組合名稱
            description: 組合描述
            strategy: 策略名稱
            market: 市場範圍
            stocks: 初始股票清單
        
        Returns:
            組合資料字典
        """
        portfolio_id = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        portfolio = {
            "id": portfolio_id,
            "name": name,
            "description": description,
            "strategy": strategy,
            "market": market,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "results": []
        }
        
        # 如果有初始股票清單，加入第一筆結果
        if stocks:
            portfolio["results"].append({
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "stocks": stocks,
                "count": len(stocks)
            })
        
        # 儲存組合
        self._save_portfolio(portfolio)
        
        return portfolio
    
    def add_result(self, portfolio_id: str, stocks: List[str]) -> bool:
        """
        新增選股結果到組合
        
        Args:
            portfolio_id: 組合 ID
            stocks: 股票清單
        
        Returns:
            是否成功
        """
        portfolio = self.load_portfolio(portfolio_id)
        if not portfolio:
            return False
        
        # 新增結果
        portfolio["results"].append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "stocks": stocks,
            "count": len(stocks)
        })
        
        portfolio["updated_at"] = datetime.now().isoformat()
        
        # 儲存更新
        self._save_portfolio(portfolio)
        
        return True
    
    def load_portfolio(self, portfolio_id: str) -> Optional[Dict]:
        """
        載入組合
        
        Args:
            portfolio_id: 組合 ID
        
        Returns:
            組合資料或 None
        """
        filepath = self.data_dir / f"{portfolio_id}.json"
        
        if not filepath.exists():
            return None
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading portfolio {portfolio_id}: {e}")
            return None
    
    def list_portfolios(self) -> List[Dict]:
        """
        列出所有組合
        
        Returns:
            組合清單
        """
        portfolios = []
        
        for filepath in self.data_dir.glob("portfolio_*.json"):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    portfolio = json.load(f)
                    portfolios.append(portfolio)
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
                continue
        
        # 按更新時間排序（最新的在前）
        portfolios.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
        
        return portfolios
    
    def update_portfolio(
        self,
        portfolio_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        strategy: Optional[str] = None,
        market: Optional[str] = None
    ) -> bool:
        """
        更新組合資訊
        
        Args:
            portfolio_id: 組合 ID
            name: 新名稱（可選）
            description: 新描述（可選）
            strategy: 新策略（可選）
            market: 新市場範圍（可選）
        
        Returns:
            是否成功
        """
        portfolio = self.load_portfolio(portfolio_id)
        if not portfolio:
            return False
        
        # 更新欄位
        if name is not None:
            portfolio["name"] = name
        if description is not None:
            portfolio["description"] = description
        if strategy is not None:
            portfolio["strategy"] = strategy
        if market is not None:
            portfolio["market"] = market
        
        portfolio["updated_at"] = datetime.now().isoformat()
        
        # 儲存更新
        self._save_portfolio(portfolio)
        
        return True
    
    def add_stock(self, portfolio_id: str, stock_id: str) -> bool:
        """手動新增股票到組合"""
        try:
            pf = self.load_portfolio(portfolio_id)
            if not pf: return False
            
            # Check if results exist
            if not pf.get('results'):
                pf['results'] = [{
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'count': 0,
                    'stocks': []
                }]
            
            latest = pf['results'][-1]
            if stock_id not in latest['stocks']:
                latest['stocks'].append(stock_id)
                latest['count'] = len(latest['stocks'])
                pf['updated_at'] = datetime.now().isoformat()
                self._save_portfolio(pf)
                return True
            return False
        except Exception as e:
            print(f"Error adding stock: {e}")
            return False

    def remove_stock(self, portfolio_id: str, stock_id: str) -> bool:
        """手動從組合移除股票"""
        try:
            pf = self.load_portfolio(portfolio_id)
            if not pf: return False
            
            if pf.get('results'):
                latest = pf['results'][-1]
                if stock_id in latest['stocks']:
                    latest['stocks'].remove(stock_id)
                    latest['count'] = len(latest['stocks'])
                    pf['updated_at'] = datetime.now().isoformat()
                    self._save_portfolio(pf)
                    return True
            return False
        except Exception as e:
            print(f"Error removing stock: {e}")
            return False

    def delete_portfolio(self, portfolio_id: str) -> bool:
        """
        刪除組合
        
        Args:
            portfolio_id: 組合 ID
        
        Returns:
            是否成功
        """
        filepath = self.data_dir / f"{portfolio_id}.json"
        
        if not filepath.exists():
            return False
        
        try:
            filepath.unlink()
            return True
        except Exception as e:
            print(f"Error deleting portfolio {portfolio_id}: {e}")
            return False
    
    def get_latest_result(self, portfolio_id: str) -> Optional[Dict]:
        """
        取得組合的最新選股結果
        
        Args:
            portfolio_id: 組合 ID
        
        Returns:
            最新結果或 None
        """
        portfolio = self.load_portfolio(portfolio_id)
        if not portfolio or not portfolio.get("results"):
            return None
        
        return portfolio["results"][-1]
    
    def compare_results(self, portfolio_id: str, limit: int = 5) -> List[Dict]:
        """
        比較組合的歷史結果
        
        Args:
            portfolio_id: 組合 ID
            limit: 最多比較幾筆結果
        
        Returns:
            結果清單
        """
        portfolio = self.load_portfolio(portfolio_id)
        if not portfolio or not portfolio.get("results"):
            return []
        
        # 取最近的 N 筆結果
        results = portfolio["results"][-limit:]
        
        return results
    
    def _save_portfolio(self, portfolio: Dict) -> None:
        """
        儲存組合到檔案
        
        Args:
            portfolio: 組合資料
        """
        filepath = self.data_dir / f"{portfolio['id']}.json"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(portfolio, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving portfolio: {e}")
            raise
