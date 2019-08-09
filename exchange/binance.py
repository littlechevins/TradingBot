import json, requests, datetime

class BinanceExchange():
    def __init__(self):
        # , api_key, secret_key, passphrase, api_url
        # self.api_url = api_url
        self.base_url = "https://api.binance.com"
        # self.url_api_endpoint = "/api/v1/"
        # self.auth = BinanceAuth(api_key, secret_key, passphrase)



    def getTime(self):
        server_request = requests.get(self.base_url + '/api/v1/time')
        epoch_time = server_request.json()['serverTime'] / 1000 # convert to seconds
        dt = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
        return dt


    def getPrice(self, ticker):
        # optional ticker symbol
        if ticker != None:
            ticker = "?symbol=" + ticker
        server_request = requests.get(self.base_url + "/api/v3/ticker/price" + ticker)
        price = server_request.json()['price']
        return price

    def getHistorical(self, ticker, interval, start, end):

        # Limits are hardcoded into method

