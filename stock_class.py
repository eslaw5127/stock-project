from datetime import date
from email.charset import BASE64
import requests

class Stock(object):
    @classmethod
    def __init__(self, symbol, open, close, high, low, price, change, percent_change):
        self.symbol = symbol
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.price = price
        self.change = change
        self.percent_change = percent_change

    @classmethod
    def print_data(self):
        today = date.today()
        print()
        print((self.symbol).upper() + "'s data for " + str(today))
        print("Open: $" + str(self.open))
        print("Close: $" + str(self.close))
        print("High: $" + str(self.high))
        print("Low: $" + str(self.low))
        print("Price: $" + str(self.price))
        print("Change: $" + str(self.change) + " (" + self.percent_change + ")")


    @staticmethod
    def time_series_daily(symbol):
        API_KEY = '8E1LCLI81IQHDHAY'
        BASE_URL = 'https://www.alphavantage.co/query'

        url = f'{BASE_URL}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(url)

        data = response.json()

        today_data = list(data["Time Series (Daily)"].values())[0]

        open = round(float(list(today_data.values())[0]),2)
        high = round(float(list(today_data.values())[1]),2)
        low = round(float(list(today_data.values())[2]),2)
        close = round(float(list(today_data.values())[3]),2)

        return (open,high,low,close)

    @staticmethod
    def global_quote(symbol):
        API_KEY = '8E1LCLI81IQHDHAY'
        BASE_URL = 'https://www.alphavantage.co/query'

        url = f'{BASE_URL}?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
        response = requests.get(url)

        data_new = response.json()
    
        data_new = data_new['Global Quote']
        price = data_new["05. price"]
        change = data_new["09. change"]
        change_percent = data_new["10. change percent"]

        return (price,change,change_percent)


class Crypto(object):
    @classmethod
    def __init__(self,symbol,price,name):
        self.symbol = symbol
        self.price = price
        self.name = name
    
    @staticmethod
    def crypto_rates(symbol):
        API_KEY = '8E1LCLI81IQHDHAY'
        BASE_URL = 'https://www.alphavantage.co/query'
        to_currency = "USD"
        function = "CURRENCY_EXCHANGE_RATE"

        request_url = f'{BASE_URL}?function={function}&from_currency={symbol}&to_currency={to_currency}&apikey={API_KEY}'
        response = requests.get(request_url)

        data = response.json()
        data = data["Realtime Currency Exchange Rate"]
        name = data["2. From_Currency Name"]
        price = data["8. Bid Price"]

        return (price,name)

    @classmethod
    def print_crypto(self):
        today = date.today()
        print()
        print((self.name).upper() + "'s data for " + str(today))
        print("Price:" , str(round(float(self.price),2)))
