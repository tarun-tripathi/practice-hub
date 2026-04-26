# Q2: Live Weather App
# Task: Fetch live weather data using OpenWeatherMap API for any city
# API Docs: https://openweathermap.org/api
# Sign up at openweathermap.org to get a free API key

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"
City: {data['name']}, {data['sys']['country']}")
        print(f"Temperature: {data['main']['temp']} C")
        print(f"Feels Like: {data['main']['feels_like']} C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {response.status_code} - City not found")

city = input("Enter city name: ")
get_weather(city)