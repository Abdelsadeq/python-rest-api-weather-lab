
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
        print("\n" + "=" * 40)
        print("           WEATHER SUMMARY")
        print("=" * 40)
        print(f"City        : {self.city}")
        print(f"Temperature : {self.temperature} °C")
        print(f"Humidity    : {self.humidity}%")
        print(f"Conditions  : {self.description.title()}")
        print("=" * 40)


def fetch_weather(city_name, api_key):
    """Retrieve weather information from OpenWeatherMap."""

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


def display_menu(countries):
    """Display the available countries."""

    print("\n" + "=" * 40)
    print("           WEATHER API CLIENT")
    print("=" * 40)
    print("Select a country to check the weather:\n")

    for number, (country, city) in enumerate(countries, start=1):
        print(f"  {number}. {country:<18} ({city.split(',')[0]})")

    print("\n  Type any letter to exit.")
    print("=" * 40)


def main():
    load_dotenv()

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Error: Configure OPENWEATHER_API_KEY in .env")
        return

    countries = {
        "Egypt": "Cairo,EG",
        "Saudi Arabia": "Riyadh,SA",
        "United Kingdom": "London,GB",
        "France": "Paris,FR",
        "Japan": "Tokyo,JP",
        "United States": "New York,US"
    }

    country_list = list(countries.items())

    while True:
        display_menu(country_list)

        choice = input("\nEnter your choice (1-6): ").strip()

        # Any letter exits the program
        if choice.isalpha():
            print("\nThank you for using Weather API Client!")
            print("Goodbye!\n")
            break

        # Validate the numeric input
        if not choice.isdigit():
            print("\nInvalid input! Enter 1-6 or a letter to exit.")
            continue

        choice_number = int(choice)

        if choice_number < 1 or choice_number > len(country_list):
            print("\nInvalid number! Please select 1 to 6.")
            continue

        # Get the selected country and city
        country, city = country_list[choice_number - 1]

        print(f"\nFetching weather for {country}...")

        try:
            weather = fetch_weather(city, api_key)
            weather.display_summary()

        except requests.exceptions.RequestException as error:
            print(f"\nAPI request failed: {type(error).__name__}")

        except (KeyError, IndexError, TypeError, ValueError) as error:
            print(f"\nInvalid weather data: {error}")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
