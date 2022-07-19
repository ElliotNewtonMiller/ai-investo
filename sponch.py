import pandas as pd
import numpy as np

def get_df(ticker):
    # Get ticker data 
    df = pd.read_json("./ticker_data/" + ticker + ".json")
    return df

def convert_list_to_sponch(df, indexes, scope_days=90, win_percent=0.04):
    # Extract needed data from dataframe
    opens = df["candles"].apply(lambda x: x["open"])
    closes = df["candles"].apply(lambda x: x["close"])
    time = df["candles"].apply(lambda x: x["datetime"])

    training_data = pd.DataFrame()

    min_index = next(i for i,v in enumerate(closes))

    for x in indexes:
        if (x - scope_days >= min_index):
            c = closes.iloc[x-scope_days : x] # 2x89
            d = pd.concat([c, pd.Series(int(closes[x]/opens[x] - 1.0 >= win_percent))], ignore_index=True) #2x1
            training_data = training_data.append(d.T, ignore_index=True)
     
    return training_data

