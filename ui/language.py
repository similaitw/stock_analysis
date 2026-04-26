# Language Configuration for Stock Analysis System
# 語言配置模組

class Language:
    """語言配置類別 (Language Configuration Class)"""
    
    # UI Labels
    UI = {
        'zh': {
            # Main Title
            'app_title': '台股自動分析系統',
            'settings': '設定',
            'language': '語言',
            
            # Modes
            'mode': '模式',
            'single_stock': '個股分析',
            'strategy_backtest': '策略回測',
            'strategy_scanner': '策略選股',
            'realtime_monitor': '即時監控',
            
            # Data Source
            'data_source': '資料來源',
            'finmind_connected': 'FinMind 已連線',
            'api_limit': 'API 限制: 600 次/小時',
            'using_yfinance': '使用 yfinance + twstock',
            'chip_data_limited': '籌碼資料受限',
            'update_stock_list': '更新股票清單',
            'downloading': '下載全台股清單中...',
            'updated_stocks': '已更新 {count} 檔股票',
            
            # Stock Analysis
            'stock_id': '股票代碼',
            'search_stock': '搜尋股票',
            'period': '期間',
            'analyze': '開始分析',
            'analysis_target': '分析標的',
            
            # Chart Settings
            'chart_settings': '圖表與指標',
            'overlays': '主圖指標',
            'indicators': '副圖指標',
            
            # Tabs
            'technical': '技術分析',
            'chips_fundamentals': '籌碼與基本面',
            
            # Metrics
            'price': '即時/收盤價',
            'data_count': '資料筆數',
            'inst_buy_5d': '籌碼 (外資+投信 近5日買賣超)',
            'revenue_yoy': '營收年增',
            'margin': '毛利率',
            'yield': '殖利率',
            'div_ttm': 'Div (TTM)',
            
            # Charts
            'technical_chart': '技術分析圖表',
            'fundamentals': '基本面概況',
            'fetching_fundamentals': '抓取基本面資料...',
            'chip_analysis': '籌碼分析',
            'institutional_investors': '三大法人買賣超',
            'margin_trading': '融資融券',
            'major_shareholders': '大戶持股',
            'margin_balance': '融資餘額',
            'short_balance': '融券餘額',
            'margin_balance_chart': '融資融券餘額',
            'big_holder_percent': '千張大戶持股比率',
            
            # Messages
            'no_price_data': '無股價資料',
            'no_inst_data': '無三大法人資料 (免費來源僅提供簡易數據)',
            'no_margin_data': '無融資融券資料 (免費來源不支援)',
            'no_holder_data': '無大戶持股資料 (免費來源不支援)',
            'error_occurred': '發生錯誤',
            'fetching_data': '抓取資料中...',
            
            # Backtest
            'backtest_period': '回測期間',
            'strategy_params': '策略參數',
            'strategy': '策略',
            'initial_cash': '初始資金',
            'commission': '手續費',
            'stop_loss': '停損 %',
            'take_profit': '停利 %',
            'fast_ma': '快線',
            'slow_ma': '慢線',
            'period_param': '週期',
            'upper': '超買',
            'lower': '超賣',
            'std_dev': '標準差',
            'run_backtest': '執行回測',
            'backtest_report': '回測報告',
            'running_backtest': '執行回測中...',
            'initial': '初始資金',
            'final': '期末資金',
            'roi': '報酬率',
            'check_terminal': '詳細交易記錄請查看終端機輸出',
            'backtest_completed': '回測完成!',
            'backtest_error': '回測錯誤',
            
            # Scanner
            'scan_market': '掃描範圍',
            'scan_strategy': '選股策略',
            'start_scan': '開始掃描',
            'scan_complete': '掃描完成',
            'found_matches': '找到 {count} 檔符合條件標的',
            'no_matches': '未找到符合條件標的',
            
            # Monitor
            'watchlist': '監控清單 (格式: 2330, 2317)',
            'monitor_strategy': '監控策略',
            'auto_refresh': '自動刷新',
            'auto_refresh_note': '自動刷新已開啟 (每 10 秒刷新一次)',
            'monitoring': '監控中',
            'updating': '更新報價與訊號...',
            'no_data': '無資料',
            'monitor_error': '監控錯誤',
        },
        'en': {
            # Main Title
            'app_title': 'Taiwan Stock Analysis System',
            'settings': 'Settings',
            'language': 'Language',
            
            # Modes
            'mode': 'Mode',
            'single_stock': 'Single Stock',
            'strategy_backtest': 'Strategy Backtest',
            'strategy_scanner': 'Strategy Scanner',
            'realtime_monitor': 'Real-time Monitor',
            
            # Data Source
            'data_source': 'Data Source',
            'finmind_connected': 'FinMind Connected',
            'api_limit': 'API Limit: 600 calls/hour',
            'using_yfinance': 'Using yfinance + twstock',
            'chip_data_limited': 'Limited Chip Data',
            'update_stock_list': 'Update Stock List',
            'downloading': 'Downloading stock list...',
            'updated_stocks': 'Updated {count} stocks',
            
            # Stock Analysis
            'stock_id': 'Stock ID',
            'search_stock': 'Search Stock',
            'period': 'Period',
            'analyze': 'Analyze',
            'analysis_target': 'Analysis Target',
            
            # Chart Settings
            'chart_settings': 'Chart Settings',
            'overlays': 'Overlays',
            'indicators': 'Indicators',
            
            # Tabs
            'technical': 'Technical',
            'chips_fundamentals': 'Chips & Fundamentals',
            
            # Metrics
            'price': 'Price',
            'data_count': 'Data Count',
            'inst_buy_5d': 'Inst Buy (5d)',
            'revenue_yoy': 'Revenue YoY',
            'margin': 'Margin',
            'yield': 'Yield',
            'div_ttm': 'Div (TTM)',
            
            # Charts
            'technical_chart': 'Technical Chart',
            'fundamentals': 'Fundamentals',
            'fetching_fundamentals': 'Fetching fundamentals...',
            'chip_analysis': 'Chip Analysis',
            'institutional_investors': 'Institutional Investors',
            'margin_trading': 'Margin Trading',
            'major_shareholders': 'Major Shareholders',
            'margin_balance': 'Margin Balance',
            'short_balance': 'Short Balance',
            'margin_balance_chart': 'Margin Balance',
            'big_holder_percent': 'Big Holder Percentage (Level {level})',
            
            # Messages
            'no_price_data': 'No price data',
            'no_inst_data': 'No institutional data (limited in free sources)',
            'no_margin_data': 'No margin data (not supported in free sources)',
            'no_holder_data': 'No holder data (not supported in free sources)',
            'error_occurred': 'Error occurred',
            'fetching_data': 'Fetching data...',
            
            # Backtest
            'backtest_period': 'Backtest Period',
            'strategy_params': 'Strategy Params',
            'strategy': 'Strategy',
            'initial_cash': 'Initial Cash',
            'commission': 'Commission',
            'stop_loss': 'Stop Loss %',
            'take_profit': 'Take Profit %',
            'fast_ma': 'Fast MA',
            'slow_ma': 'Slow MA',
            'period_param': 'Period',
            'upper': 'Upper',
            'lower': 'Lower',
            'std_dev': 'Std Dev',
            'run_backtest': 'Run Backtest',
            'backtest_report': 'Backtest Report',
            'running_backtest': 'Running backtest...',
            'initial': 'Initial',
            'final': 'Final',
            'roi': 'ROI',
            'check_terminal': 'Check Terminal for Trade Log',
            'backtest_completed': 'Backtest Completed!',
            'backtest_error': 'Backtest Error',
            
            # Scanner
            'scan_market': 'Market',
            'scan_strategy': 'Strategy',
            'start_scan': 'Start Scan',
            'scan_complete': 'Scan Complete',
            'found_matches': 'Found {count} matches',
            'no_matches': 'No matches found',
            
            # Monitor
            'watchlist': 'Watchlist (Format: 2330, 2317)',
            'monitor_strategy': 'Strategy',
            'auto_refresh': 'Auto Refresh',
            'auto_refresh_note': 'Auto refresh enabled (every 10 seconds)',
            'monitoring': 'Monitoring',
            'updating': 'Updating...',
            'no_data': 'No Data',
            'monitor_error': 'Monitor Error',
        }
    }
    
    @staticmethod
    def get(key: str, lang: str = 'zh', **kwargs) -> str:
        """
        取得翻譯文字 (Get translated text)
        
        Args:
            key: 文字鍵值 (Text key)
            lang: 語言代碼 'zh' 或 'en' (Language code)
            **kwargs: 格式化參數 (Format parameters)
        
        Returns:
            翻譯後的文字 (Translated text)
        """
        text = Language.UI.get(lang, Language.UI['zh']).get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text
