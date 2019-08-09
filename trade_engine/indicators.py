import pandas as pd
import matplotlib.pyplot as plt


class TradeEngine():

    def __init__(self):
        # Dataframes for storing data
        self.transaction_dataframe = pd.DataFrame(data={'Binance_id': [], 'ticker': [], 'datetime': [], 'price': [],
                                                        'quantity': [], 'status': [], 'fiat_balance': []})

        # self.ema_dataframe = pd.DataFrame(data={'datetime':[], 'price':[], 'EMA5':[], 'EMA20':[], 'RSI':[], 'SIGNAL':[]})
        self.ema_dataframe = pd.DataFrame(data={'datetime':[], 'price':[], 'EMA5':[], 'EMA20':[], 'SIGNAL':[]})




    def EMA(self, ticker, exchange):


        price = exchange.getPrice(ticker)
        datetime = exchange.getTime()
        # print(price)
        # print(datetime)
        self.ema_dataframe = self.ema_dataframe.append(pd.DataFrame({'datetime':datetime, 'price':price}, index=[0]), ignore_index=True)
        length = self.ema_dataframe.shape[0]
        # print("ll {}".format(length))

        # Prevents from calculating EMA before 5 / 20 / x candles are read in
        if length > 50:
            # print("5")
            self.ema_dataframe['EMA5'] = self.ema_dataframe['price'].ewm(com=50).mean()
        if length > 200:
            # print("20")
            self.ema_dataframe['EMA20'] = self.ema_dataframe['price'].ewm(com=200).mean()

        # Cleaning out the df when it gets too large
        if length > 500:
            self.resizeDf()

    def resizeDf(self):
        self.ema_dataframe = self.ema_dataframe.tail(210)
        # print(self.ema_dataframe)

    def calculateCrossover(self):
        length = self.ema_dataframe.shape[0]
        # print(length)
        if length > 5:
            # print("length > 5")
            EMA5 = self.ema_dataframe['EMA5'].tail(2).reset_index(drop=True)
            EMA20 = self.ema_dataframe['EMA20'].tail(2).reset_index(drop=True)
            if (EMA5[1] <= EMA20[1]) & (EMA5[0] >= EMA20[0]):
                # signal = {'signal': True, 'value': 'sell', 'price': self.ema_dataframe['price']}
                signal = {'value': 'sell', 'price': self.ema_dataframe['price']}
            elif (EMA5[1] >= EMA20[1]) & (EMA5[0] <= EMA20[0]):
                # signal = {'signal': True, 'value': 'buy', 'price': self.ema_dataframe['price']}
                signal = {'value': 'buy', 'price': self.ema_dataframe['price']}
            else:
                signal = {'signal': False, 'value': None}
            self.ema_dataframe.loc[self.ema_dataframe.index[length - 1], 'signal'] = signal['value']
            # self.logPrice(True)
            return signal
        # else:
        #     print("None")
            # self.logPrice(True)

    def plotGraph(self):
        #Plot X/Y graph for both EMAs
        self.ema_dataframe['price'] = self.ema_dataframe['price'].astype(float)
        self.ema_dataframe['EMA5'] = self.ema_dataframe['EMA5'].astype(float)
        self.ema_dataframe['EMA20'] = self.ema_dataframe['EMA20'].astype(float)
        pl = self.ema_dataframe[['datetime', 'price']].plot(label='Price')
        self.ema_dataframe[['datetime', 'EMA5']].plot(label='EMA5', ax=pl)
        self.ema_dataframe[['datetime', 'EMA20']].plot(label='EMA20', ax=pl)
        plt.xlabel('Datetime')
        plt.ylabel('Price')
        plt.legend()
        plt.show()


    def pnl(self, buy, sell):

        return ((buy - sell) / ((buy + sell) / 2)) * 100
