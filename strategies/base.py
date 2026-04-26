import backtrader as bt

class BaseStrategy(bt.Strategy):
    """
    Base strategy class that implements common logic like Stop Loss and Take Profit.
    """
    params = (
        ('stop_loss', 0.0),   # 0.0 means disabled. 0.05 means 5%
        ('take_profit', 0.0), # 0.0 means disabled. 0.1 means 10%
    )

    def __init__(self):
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                # self.log(
                #     'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                #     (order.executed.price,
                #      order.executed.value,
                #      order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:  # Sell
                # self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                #          (order.executed.price,
                #           order.executed.value,
                #           order.executed.comm))
                pass

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            # self.log('Order Canceled/Margin/Rejected')
            pass

        # Write down: no pending order
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        # self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
        #          (trade.pnl, trade.pnlcomm))

    def check_sl_tp(self):
        """
        Check Stop Loss and Take Profit conditions.
        Should be called in next() implementation of subclasses.
        """
        if not self.position:
            return

        if self.params.stop_loss > 0 or self.params.take_profit > 0:
            price = self.datas[0].close[0]
            buy_price = self.buyprice
            
            if not buy_price:
                return # Should not happen if position > 0

            # Calculate change %
            change_pct = (price - buy_price) / buy_price

            # Stop Loss
            if self.params.stop_loss > 0 and change_pct < -self.params.stop_loss:
                # self.log(f'STOP LOSS TRIGGERED: {change_pct:.2%}')
                self.close()
            
            # Take Profit
            elif self.params.take_profit > 0 and change_pct > self.params.take_profit:
                # self.log(f'TAKE PROFIT TRIGGERED: {change_pct:.2%}')
                self.close()

    def log(self, txt, dt=None):
        """ Logging function for this strategy"""
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))
