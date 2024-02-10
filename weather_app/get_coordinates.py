import sys

from opencage.geocoder import OpenCageGeocode


def get_coordinates(location_name: str) -> tuple[float, float]:
    """Get the latitude and longitude of a location.

    :param location_name: The name of the location.
    :return: The latitude and longitude of the location.
    """
    try:
        with open("MAP_TOKEN", "r") as file:
            key = file.read()
    except FileNotFoundError:
        sys.exit("MAP_TOKEN file not found")

    geocoder = OpenCageGeocode(key)
    results = geocoder.geocode(location_name)

    return results[0]["geometry"]["lat"], results[0]["geometry"]["lng"]
