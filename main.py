from ameritrade_api_functions import UpdateAuthentication, GetPriceHistories
import sponch

UpdateAuthentication()
GetPriceHistories()

list_of_series = sponch.extract_training_data("AAPL")

print(list_of_series)
#  create data