from weather_app.request_forecast import request_forecast
from weather_app.get_location import get_location


def main():

    location_name = input("Enter location name: ")
    coordinates = get_location(location_name)
    weather_data = request_forecast(*coordinates)
    print(weather_data.city.name + " Weather")
    for forecast in weather_data.weather_list:
        print(forecast.date_time_text, forecast.main.temp, forecast.main.feels_like)
