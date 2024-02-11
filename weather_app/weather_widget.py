import datetime
import tkinter

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

from .weather import WeatherForecast
from .classes import City


class WeatherPlot(tkinter.Frame):
    def __init__(
            self, parent: tkinter.Misc, weather_data: list[WeatherForecast]
    ) -> None:
        super().__init__(parent)
        figure = Figure(figsize=(5, 4), dpi=100)
        axes = figure.add_subplot(1, 1, 1)
        axes.errorbar(
            [forecast[0].hour for forecast in weather_data],
            [forecast[1] for forecast in weather_data],
            (
                [forecast[3] for forecast in weather_data],
                [forecast[4] for forecast in weather_data]
            ))
        canvas = FigureCanvasTkAgg(figure, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)


# class DailyWeather(tkinter.Frame):
#     weather_columns = ("Time", "Temperature", "Feels Like", "Min Temp", "Max Temp")
#
#     def __init__(
#             self,
#             master: tkinter.Misc,
#             weather_data: list[WeatherForecast]
#     ) -> None:
#         """Displays the weather data for a single day.
#
#         :param master: The parent widget.
#         :param weather_data: The weather data for the day.
#         """
#         super().__init__(master)
#
#         for column, title in enumerate(self.weather_columns):
#             tkinter.Label(self, text=title).grid(row=0, column=column)
#
#         for row, weather in enumerate(weather_data, start=1):
#             for column, value in enumerate(weather):
#                 tkinter.Label(self, text=value).grid(row=row, column=column)


class WeatherTable(tkinter.Frame):

    def __init__(
            self,
            master: tkinter.Misc,
            city: City,
            forecasts: dict[datetime.date, list[WeatherForecast]],
    ) -> None:
        """Displays the weather forecasts for a city.

        :param master: The parent widget.
        :param city: The city.
        :param forecasts: The weather forecasts.
        """
        super().__init__(master)
        tkinter.Label(self, text=city.name + " Weather").pack()
        for date, weather_data in forecasts.items():
            tkinter.Label(self, text=str(date)).pack()
            WeatherPlot(self, weather_data).pack()
