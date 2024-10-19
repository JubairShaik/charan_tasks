from flask import Flask, jsonify
from config import CITIES
from weather_fetcher import fetch_weather_data
 
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
 

@app.route("/fetch-weather", methods=["GET"])
def get_weather_data():
    weather_data = []
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data.append(data)
    
    # Aggregating example (you can extend it)
    avg_temp = sum([d['temp'] for d in weather_data]) / len(weather_data)
    max_temp = max([d['temp'] for d in weather_data])
    min_temp = min([d['temp'] for d in weather_data])
    dominant_condition = max(set([d['condition'] for d in weather_data]), key=[d['condition'] for d in weather_data].count)

    response = {
        "avg_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_condition": dominant_condition
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
