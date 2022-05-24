from datetime import date

class Stock(object):
    def __init__(self, symbol, open, close, high, low, price, change, percent_change):
        self.symbol = symbol
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.price = price
        self.change = change
        self.percent_change = percent_change

    def print_data(self):
        today = date.today()
        print(self.name + "'s data for " + today)


class Crypto(Stock):
    def __init__(self,name, price):
        super().__init__(name)
        self.price = price