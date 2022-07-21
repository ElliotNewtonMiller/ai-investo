import numpy as np
import datetime
from json import loads


class Peep:

    def __init__(self, ticker):
        with open("./ticker_data/" + ticker + ".json", "r") as file:
            candles = loads(file.read())["candles"]

        self.opens = np.array([x["open"] for x in candles])
        self.highs = np.array([x["high"] for x in candles])
        self.lows = np.array([x["low"] for x in candles])
        self.closes = np.array([x["close"] for x in candles])
        self.volumes = np.array([x["volume"] for x in candles])
        self.times = np.array([datetime.datetime.fromtimestamp(x["datetime"]/1000) for x in candles])

        # Simple Moving Average - 10 day
        self.sma10 = np.array(SMA_calc(10, self.closes))


def SMA_calc(sma_range, list_data):
    sma = []
    
    for x in np.arange(len(list_data)):
        value = 0
        
        a = (sum(list_data[x+1 - sma_range : x+1]) / sma_range) * int(x >= sma_range)
        b = (sum(list_data[0 : x+1]) / (x+1)) * int(x < sma_range)
        value = np.round(a + b, 2)

        sma.append(value)
    
    return sma