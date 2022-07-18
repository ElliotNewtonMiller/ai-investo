import json
import requests as rq
from datetime import datetime, timedelta
from io import StringIO


def UpdateAuthentication():
    # Open config data
    with open("config.json", "r") as file:
        config = json.load(file)


    # get api key from config
    api_key = config["api_key"]

    # get refresh token data from config
    refresh_token = config["refresh_token"]["token"]
    rt_date = config["refresh_token"]["datetime"]
    current_rt_date = (datetime.strptime(rt_date, "%Y-%m-%d %H:%M:%S.%f"))


    # update refresh token if it expires within 10 days (access token gets updated, too)
    if current_rt_date + timedelta(days = 83) < datetime.now():
        print("updating refresh token")

        data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "access_type": "offline",
        "client_id": api_key,
        "redirect_uri": "http://localhost:8080/"
        }
        response = rq.post("https://api.tdameritrade.com/v1/oauth2/token", data = data)
        response_json = json.load(StringIO(response.text))
        config["refresh_token"]["token"] = response_json["refresh_token"]
        config["refresh_token"]["datetime"] = str(datetime.now())
        config["access_token"]["token"] = response_json["access_token"]
        config["access_token"]["datetime"] = str(datetime.now())

        with open("config.json", "w") as file:
            json.dump(config, file)



    # refresh config data
    with open("config.json", "r") as file:
        config = json.load(file)

    # get access token data from config
    at_time = config["access_token"]["datetime"]
    current_at_time = datetime.strptime(at_time,"%Y-%m-%d %H:%M:%S.%f")

    # update access token if it is expired
    if current_at_time + timedelta(minutes = 29) < datetime.now():
        print("updating access token")

        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": config["api_key"],
            "redirect_uri": "http://localhost:8080/"
        }

        response = rq.post("https://api.tdameritrade.com/v1/oauth2/token", data = data)
        response_json = json.load(StringIO(response.text))
        config["access_token"]["token"] = response_json["access_token"]
        config["access_token"]["datetime"] = str(datetime.now())

        with open("config.json", "w") as file:
            json.dump(config, file)




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