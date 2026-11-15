
from main import WeatherData

sample_data = {
    "name": "Alexandria",
    "main": {
        "temp": 22.0,
        "humidity": 70
    },
    "weather": [
        {
            "description": "scattered clouds"
        }
    ]
}

weather = WeatherData.from_json(sample_data)

assert weather.city == "Alexandria"
assert weather.temperature == 22.0
assert weather.humidity == 70
assert weather.description == "scattered clouds"

weather.display_summary()

print("\nAll tests passed!")
