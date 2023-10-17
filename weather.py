import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    temp_min: float
    temp_max: float
    humidity: int
    feels_like: float

def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'),data.get('lon')
    return lat, lon


def get_current_weather(lat,lon, API_key,measurement):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={measurement}').json()
    data = WeatherData(
        main = resp.get('weather')[0].get('main'),
        description= resp.get('weather')[0].get('description'),
        icon= resp.get('weather')[0].get('icon'),
        temperature= resp.get('main').get('temp'),
        temp_max= resp.get('main').get('temp_max'),
        temp_min= resp.get('main').get('temp_min'),
        humidity= resp.get('main').get('humidity'),
        feels_like= resp.get('main').get('feels_like')
    )
    return data

def main(city_name, state_name, country_name, measurement):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key, measurement)
    return weather_data

if __name__ == "__main__":
    lat, lon = get_lat_lon('Tampa', 'FL', 'United States', api_key)
    print(get_current_weather(lat,lon,api_key, 'imperial'))