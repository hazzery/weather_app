import statistics
from tkinter import ttk
import datetime
import tkinter

from .request_image import request_image
from .weather import WeatherForecast
from .classes import City


class WeatherIcon(tkinter.Label):
    def __init__(self, master: tkinter.Misc, icon: str) -> None:
        """Displays a weather icon.

        :param master: The parent widget.
        :param icon: The icon to display.
        """
        super().__init__(master)
        self.icon = request_image(icon)
        self.configure(image=self.icon)
        self.image = self.icon


# Class from https://stackoverflow.com/a/16198198
class VerticalScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """

    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(fill='y', side='right', expand=False)
        canvas = tkinter.Canvas(
            self, bd=0, highlightthickness=0, yscrollcommand=scrollbar.set
        )
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(
            0, 0, window=interior, anchor='nw'
        )

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(_):
            # Update the scrollbars to match the size of the inner frame.
            width = interior.winfo_reqwidth()
            height = interior.winfo_reqheight()
            canvas.config(scrollregion=(0, 0, width, height))
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())

            if interior.winfo_reqheight() != canvas.winfo_height():
                # Update the canvas's height to fit the inner frame.
                canvas.config(height=interior.winfo_reqheight())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(_):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)


class DailyWeather(tkinter.Frame):
    weather_columns = ("Time", "Temperature", "Feels Like", "Min Temp", "Max Temp")

    def __init__(
            self,
            master: tkinter.Misc,
            weather_data: list[WeatherForecast]
    ) -> None:
        """Displays the weather data for a single day.

        :param master: The parent widget.
        :param weather_data: The weather data for the day.
        """
        super().__init__(master)
        self.configure(borderwidth=1, relief="solid")

        for column, title in enumerate(self.weather_columns):
            tkinter.Label(self, text=title).grid(
                row=0, column=column, padx=5, pady=2
            )

        for row, weather in enumerate(weather_data, start=1):
            for column, value in enumerate(weather[1:]):
                tkinter.Label(self, text=value).grid(
                    row=row, column=column, padx=5, pady=2
                )


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

        self.frame = VerticalScrolledFrame(self)
        canvas = self.frame.interior

        tkinter.Label(canvas, text=city.name + " Weather").pack()
        for date, weather_data in forecasts.items():
            WeatherIcon(
                canvas, statistics.mode(forecast[0] for forecast in weather_data)
            ).pack()
            tkinter.Label(canvas, text=date.strftime("%A %d %B %Y")).pack()
            DailyWeather(canvas, weather_data).pack()
        self.frame.pack(fill='both', expand=True)
