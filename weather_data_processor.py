# weather_data_processor.py
import requests
from config import API_KEY, API_URL, CITIES
from datetime import datetime

def fetch_weather_data(city):
    url = f"{API_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    condition = data['weather'][0]['main']
    timestamp = datetime.utcfromtimestamp(data['dt'])
    return {
        'city': city,
        'temp': temp_celsius,
        'condition': condition,
        'timestamp': timestamp
    }

def process_weather_rollup(weather_data_list):
    """Calculate daily aggregates (average, max, min temperature, dominant weather condition)."""
    total_temp = sum([data['temp'] for data in weather_data_list])
    avg_temp = total_temp / len(weather_data_list)
    max_temp = max([data['temp'] for data in weather_data_list])
    min_temp = min([data['temp'] for data in weather_data_list])
    dominant_condition = max([data['condition'] for data in weather_data_list], key=weather_data_list.count)
    return {
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
