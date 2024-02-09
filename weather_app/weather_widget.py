import dataclasses
import datetime
import tkinter

from classes import WeatherData, Main


class DailyWeather(tkinter.Frame):
    weather_columns = dataclasses.fields(Main)

    def __init__(
            self,
            master: tkinter.Misc,
            date: datetime.date,
            weather_data: list[WeatherData],
            **kwargs
    ) -> None:
        super().__init__(master, kwargs)

        tkinter.Label(self, text="Time").grid(row=0, column=0)
        for column, title in enumerate(self.weather_columns, start=1):
            tkinter.Label(self, text=title.name).grid(row=0, column=column)

        for row, weather in enumerate(weather_data, start=1):
            tkinter.Label(self, text=date.strftime("%A %d %B")).grid(row=row, column=0)
            for column, value in enumerate(dataclasses.asdict(weather.main).values(), start=1):
                tkinter.Label(self, text=value).grid(row=row, column=column)


class WeatherTable(tkinter.Frame):

    def __init__(
            self,
            master: tkinter.Misc,
            forecasts: dict[datetime.date, list[WeatherData]],
            **kwargs
    ) -> None:
        super().__init__(master, kwargs)
        for date, weather_data in forecasts.items():
            DailyWeather(self, date, weather_data).pack()
            tkinter.Label(self, text="").pack()
