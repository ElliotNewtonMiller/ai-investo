from authentication import UpdateAuthentication
import json
import requests as rq
from io import StringIO


def GetPriceHistories():
    # get chosen tickers and authentication data
    with open("tickers.txt", "r") as csv_file:
        csv = str.split(csv_file.read(), ", ")
        print("Tickers loaded")

    with open("config.json", "r") as file:
        config = json.load(file)
        api_key = config["api_key"]
        print("API key loaded")

    params = {
        "apikey": api_key,
        "periodType": "year",
        "period": "2",
        "frequencyType": "daily",
        "frequency": "1",
        "needExtendedHoursData": "false"
    }

    # make a json file for each ticker
    for x in csv:
        with open("ticker_data\\" + x + ".json", "w") as new_file:

            response = rq.get("https://api.tdameritrade.com/v1/marketdata/" + x + "/pricehistory", params = params)
            response_json = json.load(StringIO(response.text))

            # print(response.url)

            print("Writing to " + x)
            json.dump(response_json, new_file)