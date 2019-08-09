from exchange.mockexchange import MockExchange
from trade_engine.indicators import TradeEngine
import time


class Threads():

    def __init__(self):
        self.gains = 0
        self.losses = 0
        self.starting_sum = 100.0

    def run(self):

        engine = TradeEngine()
        be = MockExchange()
        print(len(be.mockdata))
        engine.buyprice = 0.0
        engine.sellprice = 0.0
        engine.intrade = False
        engine.pnltotal = 0.0
        # print(trade_engine.pnl(10.0, 11.0))
        print("Starting...")
        index = 0
        print("size: ", be.getSize())
        while (index < be.getSize()):
            self.test(engine, be, index)
            index += 1

        print(engine.ema_dataframe)

        print("Gains: {}".format(self.gains))

        print("Losses: {}".format(self.losses))

    def test(self, engine, be, index):

        be.index = index

        ticker = 'BTCUSDT'

        engine.EMA(ticker, be)

        signal = engine.calculateCrossover()
        # print(engine.ema_dataframe)

        if signal is not None:
            if signal['value'] == 'buy':
                # order_thread = Thread(target=self.order, args=('buy',))
                # order_thread.daemon = True
                # order_thread.start()
                print("BUY")

                if engine.intrade == False:
                    engine.intrade = True
                    # print(signal['price'].tail(1))
                    engine.buyprice = float(signal['price'].tail(1))
                    # pnl = trade_engine.pnl(trade_engine.buyprice, trade_engine.sellprice)
                    # trade_engine.pnltotal = trade_engine.pnltotal + pnl
                print("Date: {}").format(engine.ema_dataframe['datetime'].head(1))
                print("PNL: {}".format(engine.pnltotal))
                print("*" * 64)


            elif signal['value'] == 'sell':
                # order_thread = Thread(target=self.order, args=('sell',))
                # order_thread.daemon = True
                # order_thread.start()
                print("SELL")
                if engine.intrade == True:
                    engine.intrade = False
                    engine.sellprice = float(signal['price'].tail(1))
                    pnl = engine.pnl(engine.buyprice, engine.sellprice)
                    if pnl < 0.0:
                        print("LOSS {}".format(pnl))
                        self.losses += 1
                    else:
                        print("GAIN {}".format(pnl))
                        self.gains += 1
                    engine.pnltotal = engine.pnltotal + pnl
                    self.starting_sum = self.starting_sum + (self.starting_sum * (pnl/100))

                print("PNL: {}".format(engine.pnltotal))
                print("Current sum: {}").format(self.starting_sum)
                print("*" * 64)

            # elif signal['value'] == None:
            #     print("WAIT")
        # print('Df size: {}').format(len(engine.ema_dataframe.index))


if __name__ == '__main__':
    t = Threads()
    t.run()