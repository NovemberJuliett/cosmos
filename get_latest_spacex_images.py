import requests
import os
from save_image_helper import save_image


def get_latest_spacex_images():
    latest_spacex_response = requests.get("https://api.spacexdata.com/v5/launches/latest/")
    latest_flight = latest_spacex_response.json()
    latest_flight_links = latest_flight["links"]["flickr"]["original"]
    for index, link in enumerate(latest_flight_links):
        link_name, link_extension = os.path.splitext(link)
        save_image(link, f'images/spacex_{index}{link_extension}')
