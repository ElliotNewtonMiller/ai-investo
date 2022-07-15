import json
import requests
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
        response = requests.post("https://api.tdameritrade.com/v1/oauth2/token", data = data)
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

        response = requests.post("https://api.tdameritrade.com/v1/oauth2/token", data = data)
        response_json = json.load(StringIO(response.text))
        config["access_token"]["token"] = response_json["access_token"]
        config["access_token"]["datetime"] = str(datetime.now())

        with open("config.json", "w") as file:
            json.dump(config, file)