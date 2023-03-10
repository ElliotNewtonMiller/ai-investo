import numpy as np
import pandas as pd
from ameritrade_api_functions import UpdateAuthentication, GetPriceHistories
import sponch

UpdateAuthentication()
GetPriceHistories()

#make a random list of indexes and sponch them
rng = np.random.default_rng()
df = sponch.get_df("AAPL")
tr = sponch.convert_list_to_sponch(df, rng.integers(low=0, high=502 - 0, size=10), 90, 0.04)

print(tr)