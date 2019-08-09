from exchange.binance import BinanceExchange
from trade_engine.indicators import TradeEngine
import time

class Threads():
    

    def run(self):


        engine = TradeEngine()
        engine.buyprice = 0.0
        engine.sellprice = 0.0
        engine.intrade = False
        engine.pnltotal = 0.0
        # print(trade_engine.pnl(10.0, 11.0))
        print("Starting...")

        while(True):
            self.test(engine)
            time.sleep(300) # 5 Min candles

    def test(self, engine):

        ticker = 'BTCUSDT'

        be = BinanceExchange()

        engine.EMA(ticker, be)

        signal = engine.calculateCrossover()
        print(engine.ema_dataframe)


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
                    else:
                        print("GAIN {}".format(pnl))
                    engine.pnltotal = engine.pnltotal + pnl

                print("PNL: {}".format(engine.pnltotal))
                print("*" * 64)

            # elif signal['value'] == None:
            #     print("WAIT")


if __name__ == '__main__':
    t = Threads()
    t.run()