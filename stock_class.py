class Stock(object):
    def __init__(self, name, open, close, high, low):
        self.name = name
        self.open = open
        self.close = close
        self.high = high
        self.low = low

    def give_name(self):
        print(self.name)


class Crypto(Stock):
    def __init__(self,name, price):
        super().__init__(name)
        self.price = price