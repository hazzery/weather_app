from tkinter import ttk
import tkinter

from .classes import ApiResponse
from .weather import daily_forecasts
from .weather_widget import WeatherTable


def launch_app(weather_data: ApiResponse) -> None:
    root = tkinter.Tk()
    root.geometry('600x900')
    root.title('Weather App')

    header = ttk.Label(
        root, text=weather_data.city.name + " Weather", font=("Arial", 20)
    )
    header.pack()

    forecasts = daily_forecasts(weather_data.weather_list)

    weather_table = WeatherTable(root, forecasts)
    weather_table.pack()

    root.mainloop()
