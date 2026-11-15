
import os

import requests
from dotenv import load_dotenv


class WeatherData:
    """Store and display weather information."""

    def __init__(self, city, temperature, humidity, description):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.description = description

    @classmethod
    def from_json(cls, data):
        """Create a WeatherData object from API JSON."""
        return cls(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            description=data["weather"][0]["description"]
        )

    def display_summary(self):
        """Print a formatted weather summary."""
        print("\n" + "=" * 35)
        print("       WEATHER SUMMARY")
        print("=" * 35)
        print(f"City        : {self.city}")
        print(f"Temperature : {self.temperature} °C")
        print(f"Humidity    : {self.humidity}%")
        print(f"Conditions  : {self.description.title()}")
        print("=" * 35)


def fetch_weather(city_name, api_key):
    """Retrieve and parse weather information from OpenWeatherMap."""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return WeatherData.from_json(data)


def main():
    load_dotenv()

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Error: Configure OPENWEATHER_API_KEY in .env")
        return

    try:
        weather = fetch_weather("Cairo,EG", api_key)
        weather.display_summary()

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {type(error).__name__}")
        print("Check your connection, API key and API access.")

    except (KeyError, IndexError, TypeError, ValueError) as error:
        print(f"Invalid weather data: {error}")


if __name__ == "__main__":
    main()
