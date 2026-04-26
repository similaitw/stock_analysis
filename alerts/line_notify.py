
import requests
import os

class LineNotifier:
    def __init__(self, token: str = None):
        # 優先使用傳入的 token，否則嘗試從環境變數讀取
        self.token = token or os.environ.get("LINE_NOTIFY_TOKEN")
        self.api_url = "https://notify-api.line.me/api/notify"

    def send_message(self, message: str, token: str = None) -> bool:
        """
        發送訊息到 Line Notify
        
        Args:
            message: 要發送的訊息內容
            token: 可選，若指定則使用此 token，否則使用初始化的 token
        
        Returns:
            bool: 是否發送成功
        """
        target_token = token or self.token
        
        if not target_token:
            print("Line Notify Token not set.")
            return False

        headers = {
            "Authorization": f"Bearer {target_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        payload = {"message": message}

        try:
            response = requests.post(self.api_url, headers=headers, data=payload)
            response.raise_for_status()
            return True
        except Exception as e:
            print(f"Error sending Line Notify message: {e}")
            return False
