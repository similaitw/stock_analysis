import backtrader as bt
from .base import BaseStrategy

class BollingerStrategy(BaseStrategy):
    params = (
        ('period', 20),
        ('devfactor', 2.0),
        ('stop_loss', 0.0),
        ('take_profit', 0.0),
    )

    def __init__(self):
        super().__init__()
        self.boll = bt.indicators.BollingerBands(
            self.datas[0], 
            period=self.params.period, 
            devfactor=self.params.devfactor
        )

    def next(self):
        # Check SL/TP
        if self.position:
            self.check_sl_tp()
            if not self.position:
                return

        if not self.position:
            if self.datas[0].close < self.boll.lines.bot:
                self.buy()
        else:
            if self.datas[0].close > self.boll.lines.top:
                self.sell()
