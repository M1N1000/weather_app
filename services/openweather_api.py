import requests
from datetime import datetime
from common.tools import convert_temp
from common.tools import convert_wind_speed

def get_weather(city):
    API_KEY = "92284de54c3a67afe9350676f0c2a178"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},&appid={API_KEY}"


    try:
        response = requests.get(url)
        data = (response.json())


        record = {
            "city": data.get('name'),
            "temp": round(convert_temp(data.get('main').get('temp')),2),
            "feels_like":round(convert_temp( data.get('main').get('feels_like')),2),
            "wind" : convert_wind_speed(data.get('wind').get('speed')),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get('main').get('humidity'),
            "pressure": data.get('main').get('pressure'),
            "description": data.get('weather')[0].get('description'),
        }

        return record
    except:
        print("Error")


