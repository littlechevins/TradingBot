import json, datetime

class MockExchange():
    def __init__(self):
        self.index = 0
        self.mockdata = self.getMockData()

    def getMockData(self):
        f = open("data/5m.json", "r")
        if f.mode == "r":
            contents = f.read()
        print("Mockdata length")
        return json.loads(contents)



    def getTime(self):
        epoch_time = self.mockdata[self.index][0] / 1000 # position of epoch time for candle open
        dt = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
        return dt


    def getPrice(self, ticker):
        # optional ticker symbol
        if ticker != None:
            pass # we dont care about symbol

        price = self.mockdata[self.index][4] # position of close price
        return price

    def getSize(self):
        return len(self.mockdata)

    # def getHistorical(self, ticker, interval, start, end):

        # Limits are hardcoded into method

