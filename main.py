import os
from urllib import response
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params=params, timeout=10)
    except requests.RequestException:
        print("An error occurred while making the request.")
        return None

    if response.status_code == 200:
        data = response.json()

        city = data["name"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        return {
            "city": city,
            "temperature": temperature,
            "weather": weather,
            "humidity": humidity
        }
    
    elif response.status_code == 404:
        print(f"City '{city}' not found. Please check the spelling and try again.")
    elif response.status_code == 401:
        print("Authentication failed. Please check your API key and try again.")
    else:
        print(f"An error occurred: {response.status_code}")
    return None

def main():
    print("=====================")
    print("WEATHER APP")
    print("=====================")

    city = input("Enter city name: ")
    if not city:
        print("City name cannot be empty. Please enter a valid city name.")
        return

    weather = get_weather(city)
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Weather: {weather['weather']}")
        print(f"Humidity: {weather['humidity']}%")

if __name__ == "__main__":
    main()