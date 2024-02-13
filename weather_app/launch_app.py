from tkinter import ttk
import tkinter

from .weather_widget import WeatherTable
from .weather import get_weather_data


def launch_app() -> None:
    root = tkinter.Tk()
    root.title('Weather App')

    starting_frame = ttk.Frame(root)
    starting_frame.pack(pady=10, padx=10)

    ttk.Label(
        starting_frame,
        text='Weather App',
        font=('Arial', 20)
    ).pack(pady=10, padx=10)

    ttk.Label(
        starting_frame,
        text='Enter a place name:',
        font=('Arial', 12)
    ).pack(pady=10, padx=10)

    location_input = ttk.Entry(starting_frame, width=30)
    location_input.pack(pady=10, padx=10)

    def go(location_name: str) -> None:
        starting_frame.destroy()
        city, weather_data = get_weather_data(location_name)
        WeatherTable(root, city, weather_data).pack(fill='both', expand=False)

    ttk.Button(
        starting_frame,
        text='Go',
        command=lambda: go(location_input.get())
    ).pack(pady=10, padx=10)

    root.mainloop()
