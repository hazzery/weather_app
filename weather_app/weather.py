import datetime

from .request_forecast import request_forecast
from .get_coordinates import get_coordinates
from .classes import WeatherData, City


WeatherForecast = tuple[datetime.time, float, float, float, float]


def transform_forecasts(
        weather_data: list[WeatherData]
) -> dict[datetime.date, list[WeatherForecast]]:
    """Map each day to all forecasts for that day.

    :param weather_data: A list of weather forecasts.
    :return: A dictionary mapping dates to a list of forecasts for that day.
    """
    forecasts = {}
    for forecast in weather_data:
        date = forecast.date_time.date()
        if date not in forecasts:
            forecasts[date] = []
        forecasts[date].append((
            forecast.date_time.time(),
            forecast.main.temp,
            forecast.main.feels_like,
            forecast.main.temp_max,
            forecast.main.temp_min
        ))

    return forecasts


def get_weather_data(
        location_name: str
) -> tuple[City, dict[datetime.date, list[WeatherForecast]]]:
    """Request the weather at ``location_name``.

    :param location_name: The name of the location to get the weather data for.
    :return: A list of weather data.
    """
    coordinates = get_coordinates(location_name)
    forecast = request_forecast(*coordinates)
    return forecast.city, transform_forecasts(forecast.weather_list)
