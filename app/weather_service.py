import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')

def get_coordinates(city: str):
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GEOCODING_API_KEY}"
    try:
        response = requests.get(geocoding_url)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'],location['lng']
        
        else:
            print(f"Error fetching geolocation: {data['status']}")
            raise Exception(f"Geocoding API error: {data['status']}")
    except requests.RequestException as e:
        print(f"Error fetching geolocation data: {e}")
        raise

def get_weather(city: str):
    try:
        lat, lon = get_coordinates(city)
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(weather_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json() 
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        raise