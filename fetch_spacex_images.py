import requests
import argparse
from urllib.parse import urlparse
import os
from save_image_helper import save_image


def fetch_spacex_images(flight_id):
    url = f"https://api.spacexdata.com/v5/launches/{flight_id}"
    if not flight_id:
        url = "https://api.spacexdata.com/v5/launches/latest/"

    spacex_response = requests.get(url)
    spacex_response.raise_for_status()
    flight = spacex_response.json()
    photo_links = flight["links"]["flickr"]["original"]
    for index, link in enumerate(photo_links):
        link_name, link_extension = os.path.splitext(link)
        save_image(link, f'images/spacex_{index}{link_extension}')


def main():
    parser = argparse.ArgumentParser(description="Скачивает изображения с запусков SpaceX")
    parser.add_argument("--spacex_id", help="ID запуска")
    args = parser.parse_args()
    fetch_spacex_images(args.spacex_id)


if __name__ == '__main__':
    main()
