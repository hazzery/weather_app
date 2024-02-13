# weather_app

weather_app is a simple application designed to show a
five-day three-hour weather-forcast for a location of your choice.

Internally, the OpenWeatherMap API is used to fetch weather data,
and the OpenCage geocoding API is used to fetch coordinates for a
given location name.

To use the application, you will need to sign up for an API key
from both OpenWeatherMap and OpenCage. Once you have your API keys,
you can add them as WEATHER_TOKEN and MAP_TOKEN files in the root
directory of the project.

## How to run

To run the weather_app, execute the following command in the root
directory of the project:

```bash
python3 -m weather_app
```