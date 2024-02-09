import datetime

from weather_app.classes import WeatherData


def daily_forecasts(weather_data: list[WeatherData]) -> dict[datetime.date, list[WeatherData]]:
    """This function will take the weather data and return a dictionary of daily forecasts.

    :return:
    """
    forecasts: dict[datetime.date, list[WeatherData]] = {}
    for forcast in weather_data:
        date = forcast.date_time.date()
        if date not in forecasts:
            forecasts[date] = []
        forecasts[date].append(forcast)

    return forecasts
