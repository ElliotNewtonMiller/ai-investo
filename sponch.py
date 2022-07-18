import pandas as pd
import numpy as np


def extract_training_data(ticker):
    # Get ticker data 
    df = pd.read_json("./ticker_data/" + ticker + ".json")

    # Extract needed data from dataframe
    opens = df["candles"].apply(lambda x: x["open"])
    closes = df["candles"].apply(lambda x: x["close"])
    time = df["candles"].apply(lambda x: x["datetime"])

    # make a % series to comb for training data
    percent_moved = (closes/opens * 100) - 100

    # Make training data for 90 days before all 4% moves
    desired_win_percent = 4
    targets = percent_moved.loc[lambda x : x >= desired_win_percent]
    index_list_4 = [x for x in targets.index.to_list() if 90 < x]

    training_data = []
    for x in index_list_4:
        c = closes.iloc[x-90 : x]
        d = pd.Series(True)
        e = pd.concat([c, d], ignore_index=True) # A boolean True instead of the winning candle
        training_data.append(e)

    # Make training data for 90 days before all 3% moves (excluding 4% moves) to hone the machine
    targets = percent_moved.loc[lambda x : x > 3]
    targets.drop(index_list_4, inplace=True)
    index_list_3 = [x for x in targets.index.to_list() if 90 < x]

    for x in index_list_3:
        c = closes.iloc[x-90 : x]
        d = pd.Series(False)
        e = pd.concat([c, d], ignore_index=True)
        training_data.append(e)

    # add 5x as many random 90 day periods ... note there are 252 trading days a year
    rng = np.random.default_rng()
    index_list_rand = rng.integers(low=len(training_data) - 414, high=len(training_data) - 0, size=len(training_data) * 5)

    for x in index_list_rand:
        c = closes.iloc[x-90 : x]
        d = pd.Series(False)
        e = pd.concat([c, d], ignore_index=True)
        training_data.append(e)

    return training_data