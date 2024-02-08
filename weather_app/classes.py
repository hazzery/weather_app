from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    ground_level: int
    humidity: int
    temp_kf: float


@dataclass(slots=True)
class Weather:
    id: int
    main: str
    description: str
    icon: str


@dataclass(slots=True)
class WeatherData:
    dt: int
    main: Main
    weather: list[Weather]
    clouds: dict[str, Any]
    wind: dict[str, Any]
    visibility: int
    pop: float
    sys: dict[str, Any]
    date_time: str

    def __init__(self, weather_data: dict[str, Any]):
        self.dt = weather_data["dt"]
        self.main = Main(*weather_data["main"])
        self.weather = [Weather(*weather) for weather in weather_data["weather"]]
        self.clouds = weather_data["clouds"]
        self.wind = weather_data["wind"]
        self.visibility = weather_data["visibility"]
        self.pop = weather_data["pop"]
        self.sys = weather_data["sys"]
        self.date_time = weather_data["dt_txt"]


@dataclass(slots=True)
class City:
    id: int
    name: str
    coord: dict[str, float]
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


@dataclass(slots=True)
class ApiResponse:
    code: int
    message: str
    count: int
    weather_list: list[WeatherData]
    city: City

    def __init__(self, api_response: dict[str, Any]):
        self.code = api_response["cod"]
        self.message = api_response["message"]
        self.count = api_response["cnt"]
        self.weather_list = [WeatherData(weather) for weather in api_response["list"]]
        self.city = City(*api_response["city"])
