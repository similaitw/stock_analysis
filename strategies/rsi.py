import backtrader as bt
from .base import BaseStrategy

class RSIStrategy(BaseStrategy):
    params = (
        ('period', 14),
        ('upper', 70),
        ('lower', 30),
        ('stop_loss', 0.0),
        ('take_profit', 0.0),
    )

    def __init__(self):
        super().__init__()
        self.rsi = bt.indicators.RSI(self.datas[0], period=self.params.period)

    def next(self):
        # Check SL/TP
        if self.position:
            self.check_sl_tp()
            if not self.position:
                return

        if not self.position:
            if self.rsi < self.params.lower:
                self.buy()
        else:
            if self.rsi > self.params.upper:
                self.sell()
