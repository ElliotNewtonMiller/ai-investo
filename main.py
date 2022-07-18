from ameritrade_api_functions import UpdateAuthentication, GetPriceHistories
import create_sponch

UpdateAuthentication()
GetPriceHistories()

list_of_series = create_sponch.extract_training_data("AAPL")

print(list_of_series)
#  create data