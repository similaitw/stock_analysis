"""
警示管理模組
Alert Manager for Price and Strategy Alerts
"""
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional

class AlertManager:
    """警示管理器"""
    
    def __init__(self, data_dir: str = "data/alerts"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def create_alert(
        self,
        name: str,
        ticker: str,
        alert_type: str,  # 'price' or 'strategy'
        condition: Dict,
        notification: List[str] = None,
        enabled: bool = True
    ) -> Dict:
        """
        建立新警示
        
        Args:
            name: 警示名稱
            ticker: 股票代碼
            alert_type: 警示類型 ('price' 或 'strategy')
            condition: 條件設定
            notification: 通知方式列表
            enabled: 是否啟用
        
        Returns:
            警示資料字典
        """
        alert_id = f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        alert = {
            "id": alert_id,
            "name": name,
            "ticker": ticker,
            "type": alert_type,
            "condition": condition,
            "notification": notification or ["web"],
            "enabled": enabled,
            "created_at": datetime.now().isoformat(),
            "triggered_at": None,
            "trigger_count": 0
        }
        
        self._save_alert(alert)
        return alert
    
    def load_alert(self, alert_id: str) -> Optional[Dict]:
        """載入警示"""
        filepath = self.data_dir / f"{alert_id}.json"
        
        if not filepath.exists():
            return None
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading alert {alert_id}: {e}")
            return None
    
    def list_alerts(self, enabled_only: bool = False) -> List[Dict]:
        """列出所有警示"""
        alerts = []
        
        for filepath in self.data_dir.glob("alert_*.json"):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    alert = json.load(f)
                    if not enabled_only or alert.get('enabled', False):
                        alerts.append(alert)
            except Exception as e:
                print(f"Error loading {filepath}: {e}")
                continue
        
        alerts.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return alerts
    
    def update_alert(
        self,
        alert_id: str,
        name: Optional[str] = None,
        condition: Optional[Dict] = None,
        notification: Optional[List[str]] = None,
        enabled: Optional[bool] = None
    ) -> bool:
        """更新警示"""
        alert = self.load_alert(alert_id)
        if not alert:
            return False
        
        if name is not None:
            alert["name"] = name
        if condition is not None:
            alert["condition"] = condition
        if notification is not None:
            alert["notification"] = notification
        if enabled is not None:
            alert["enabled"] = enabled
        
        self._save_alert(alert)
        return True
    
    def delete_alert(self, alert_id: str) -> bool:
        """刪除警示"""
        filepath = self.data_dir / f"{alert_id}.json"
        
        if not filepath.exists():
            return False
        
        try:
            filepath.unlink()
            return True
        except Exception as e:
            print(f"Error deleting alert {alert_id}: {e}")
            return False
    
    def check_price_alert(self, alert: Dict, current_price: float) -> bool:
        """檢查價格警示是否觸發"""
        condition = alert.get('condition', {})
        operator = condition.get('operator', '>=')
        target_price = condition.get('value', 0)
        
        if operator == '>=':
            return current_price >= target_price
        elif operator == '<=':
            return current_price <= target_price
        elif operator == '==':
            return abs(current_price - target_price) < 0.01
        
        return False
    
    def trigger_alert(self, alert_id: str) -> bool:
        """觸發警示"""
        alert = self.load_alert(alert_id)
        if not alert:
            return False
        
        alert["triggered_at"] = datetime.now().isoformat()
        alert["trigger_count"] = alert.get("trigger_count", 0) + 1
        
        self._save_alert(alert)
        return True
    
    def _save_alert(self, alert: Dict) -> None:
        """儲存警示到檔案"""
        filepath = self.data_dir / f"{alert['id']}.json"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(alert, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving alert: {e}")
            raise
