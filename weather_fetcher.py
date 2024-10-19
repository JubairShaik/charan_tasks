import requests
from datetime import datetime

API_KEY = "0e22252796e2bbc4c4efc0c6f0581843"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        feels_like = data['main']['feels_like'] - 273.15
        condition = data['weather'][0]['main']
        timestamp = data['dt']
        return {
            "city": city,
            "temp": temp_celsius,
            "feels_like": feels_like,
            "condition": condition,
            "timestamp": datetime.fromtimestamp(timestamp)
        }
    else:
        return None
