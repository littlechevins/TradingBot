import requests, json
import time
import calendar

class Historical():




    def fetchHistory(self):


        # intervals_list = ["1h", "15m", "5m", "1m"]
        intervals_list = ["1m"]

        symbols = ["BTCUSDT"]


        for interval in intervals_list:

            filename = "binance_{}_{}.json".format(symbols[0], interval)

            qty = 10
            start_time = 1483243199000
            current_time = calendar.timegm(time.gmtime()) * 1000
            print("currenttime: {}".format(current_time))

            # create file
            f = open("../data/" + filename, "a")

            while start_time < current_time and qty > 0:

                request_print = "https://api.binance.com/api/v1/klines?symbol={}&interval={}&startTime={}".format(symbols[0], interval, start_time)

                print(request_print)

                server_request = requests.get("https://api.binance.com/api/v1/klines?symbol={}&interval={}&startTime={}".format(symbols[0], interval, start_time))
                response = server_request.json()

                # print(response)

                if "code" in response:
                    if response['code'] == 429:
                        print("LIMITER REACHED")
                        break

                string = json.dumps(response)

                if start_time != 1483243199000:
                    string = string[1:]

                start_time = response[-1][6]
                start_time += 1

                qty = len(response)

                if qty == 500:
                    string = string[:-1]
                    string += ","

                f.write(string)

                # time.sleep(0.5)
            f.close()




if __name__ == '__main__':
    h = Historical()
    h.fetchHistory()