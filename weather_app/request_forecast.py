import sys

import requests

from weather_app.classes import ApiResponse


def request_forecast(latitude: float, longitude: float) -> ApiResponse:
    try:
        with open("API_TOKEN", "r") as file:
            key = file.read()
    except FileNotFoundError:
        sys.exit("API_TOKEN file not found")

    response = requests.get(
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={latitude}&lon={longitude}&appid={key}&units=metric"
    )
    return ApiResponse(response.json())
