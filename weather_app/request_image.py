from PIL import ImageTk
import requests


def request_image(icon_id: str) -> ImageTk.PhotoImage:
    """Request the image for the weather icon.

    :param icon_id: The OpenWeatherMap icon id.
    :return: The image.
    """
    response = requests.get(f"https://openweathermap.org/img/wn/{icon_id}.png")
    return ImageTk.PhotoImage(data=response.content)
