# This is where I try stuff

from sqlite3 import DatabaseError
import pandas as pd
import numpy as np




# Get ticker data 
df = pd.read_json('./ticker_data/A.json')

# Extract needed data from dataframe
opens = df["candles"].apply(lambda x: x["open"])
closes = df["candles"].apply(lambda x: x["close"])
time = df["candles"].apply(lambda x: x["datetime"])

# make a % series to comb for training data
percent_moved = (closes/opens * 100) - 100

# Make training data for 90 days before all 4% moves
desired_win_percent = 4
targets = percent_moved.loc[lambda x : x >= desired_win_percent]
index_list_4 = targets.index.to_list()

training_data = []
for x in index_list_4:
    c = closes.iloc[x-90 : x]
    d = pd.Series(True)
    e = pd.concat([c, d], ignore_index=True) # A boolean True instead of the winning candle
    training_data.append(e)

# Make training data for 90 days before all 3% moves (excluding 4% moves) to hone the machine
targets = percent_moved.loc[lambda x : x > 3]
targets.drop(index_list_4)
index_list_3_raw = targets.index.to_list()
index_list_3 = [x for x in index_list_3_raw if 610 < x]

for x in index_list_3:
    c = closes.iloc[x-90 : x]
    d = pd.Series(False)
    e = pd.concat([c, d], ignore_index=True)
    training_data.append(e)

# add 6x as many random 90 day periods
rng = np.random.default_rng()
index_list_rand = rng.integers(low=0, high=600, size=len(training_data) * 6)

for x in index_list_rand:
    c = closes.iloc[x-90 : x]
    d = pd.Series(False)
    e = pd.concat([c, d], ignore_index=True)
    training_data.append(e)

print (training_data)