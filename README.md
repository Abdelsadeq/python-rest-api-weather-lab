
# Weather API Client

## Lab Assignment 1: Working with a Public REST API Using Python

### Project Description

This project is a Python application that retrieves
current weather information from OpenWeatherMap using
a public REST API.

The application parses the JSON response, stores
weather information in a custom Python class, and
displays a formatted summary in the terminal.

### Features

- Retrieves live weather data using HTTP GET.
- Parses JSON responses.
- Uses a custom WeatherData class.
- Displays temperature, humidity, and conditions.
- Handles API and data processing errors.
- Loads the API key from environment variables.
- Uses a Python virtual environment.

### Technologies

- Python 3
- requests
- python-dotenv
- OpenWeatherMap API

### Project Files

- main.py: Main application and WeatherData class
- test_weather.py: Tests for JSON parsing
- requirements.txt: Project dependencies
- .env.example: Example environment configuration
- .gitignore: Excludes local secrets and environments

### Installation

1. Clone or download the project.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   python -m venv .venv

4. Activate it on Windows PowerShell:

   .\.venv\Scripts\Activate.ps1

5. Install the dependencies:

   python -m pip install -r requirements.txt

### Configuration

1. Register at https://openweathermap.org/
2. Obtain an API key with Current Weather Data access.
3. Copy .env.example to .env.
4. Set OPENWEATHER_API_KEY to your actual key.

Never publish or share the real .env file.

### Running the Application

Run the following command:

   python main.py

### Example Output

===================================
       WEATHER SUMMARY
===================================
City        : Cairo
Temperature : 25.5 °C
Humidity    : 60%
Conditions  : Clear Sky
===================================

Note: The values above are illustrative.

### Testing

Run the JSON parsing and class tests:

   python test_weather.py

### How It Works

1. Load the API key from the environment.
2. Send a GET request to OpenWeatherMap.
3. Validate the HTTP response.
4. Parse the JSON response.
5. Create a WeatherData object.
6. Display the formatted weather summary.

### Security

- The API key is stored in a local .env file.
- The .env file is excluded by .gitignore.
- An .env.example file documents the configuration.
- The virtual environment is not included in the
  source-code submission.

### Author

Student: Abdelsadeq Khamis Abdelsadeq

