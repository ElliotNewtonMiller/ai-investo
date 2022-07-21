import numpy as np
import datetime
from json import loads


class Peep:

    def __init__(self, ticker):
        with open("./ticker_data/" + ticker + ".json", "r") as file:
            _file_text= loads(file.read())
            self.candles = _file_text["candles"]
            self.ticker = _file_text["symbol"]


    def opens(self):
        return np.array([x["open"] for x in self.candles])
    def highs(self):
        return np.array([x["high"] for x in self.candles])
    def lows(self):
        return np.array([x["low"] for x in self.candles])
    def closes(self):
        return np.array([x["close"] for x in self.candles])
    def volumes(self):
        return np.array([x["volume"] for x in self.candles])
    def times(self):
        return np.array([datetime.datetime.fromtimestamp(x["datetime"]/1000) for x in self.candles])
    
    def sma10(self):
        return np.array(sma_calc(10, self.closes))


def sma_calc(sma_range, list_data):
    sma = []
    
    for x in np.arange(len(list_data)):
        value = 0
        
        a = (sum(list_data[x+1 - sma_range : x+1]) / sma_range) * int(x >= sma_range)
        b = (sum(list_data[0 : x+1]) / (x+1)) * int(x < sma_range)
        value = np.round(a + b, 2)

        sma.append(value)
    
    return sma