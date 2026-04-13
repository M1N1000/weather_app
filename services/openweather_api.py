import requests
from datetime import datetime
from common.tools import convert_temp, convert_wind_speed
from config import Config

def get_weather():

    API_KEY = Config.API_KEY
    city = Config.API_CITY

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        record = {
            "city": data.get("name"),
            "temp": convert_temp(data.get("main").get("temp")),
            "feels_like": convert_temp(data.get("main").get("feels_like")),
            "wind": convert_wind_speed(data.get("wind").get("speed")),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description")
        }

        return record
    except Exception as e:
        print(e)
