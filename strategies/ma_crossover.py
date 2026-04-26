import backtrader as bt
from .base import BaseStrategy

class MACrossoverStrategy(BaseStrategy):
    params = (
        ('pfast', 10),  # Fast MA period
        ('pslow', 30),  # Slow MA period
        ('stop_loss', 0.0), # Inherited
        ('take_profit', 0.0), # Inherited
    )

    def __init__(self):
        super().__init__() # Call Base __init__
        self.dataclose = self.datas[0].close
        
        # Calculate Moving Averages
        self.sma_fast = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.pfast)
        self.sma_slow = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=self.params.pslow)
            
        self.crossover = bt.indicators.CrossOver(self.sma_fast, self.sma_slow)

    def next(self):
        # Check SL/TP first
        if self.position:
            self.check_sl_tp()
            if not self.position: # Closed by SL/TP
                return

        if not self.position:  # Check if we are in the market
            if self.crossover > 0:  # Fast crosses above Slow
                self.buy()
        
        elif self.crossover < 0:  # Fast crosses below Slow
            self.sell()

