import requests
import argparse
from urllib.parse import urlparse
import os
from save_images_helper import save_images


def fetch_spacex_images(flight_id):
    spacex_response = requests.get(f"https://api.spacexdata.com/v5/launches/{flight_id}")
    spacex_response.raise_for_status()
    flight_info = spacex_response.json()
    photo_links = flight_info["links"]["flickr"]["original"]
    for index, link in enumerate(photo_links):
        urlparse(link)
        link_name, link_extension = os.path.splitext(link)
        save_images(link, f'images/spacex_{index}{link_extension}')


def get_latest_spacex_images():
    latest_spacex_response = requests.get("https://api.spacexdata.com/v5/launches/latest/")
    latest_flight_info = latest_spacex_response.json()
    latest_flight_links = latest_flight_info["links"]["flickr"]["original"]
    for index, link in enumerate(latest_flight_links):
        urlparse(link)
        link_name, link_extension = os.path.splitext(link)
        save_images(link, f'images/spacex_{index}{link_extension}')
        if latest_flight_links is None:
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spacex_id", help="ID запуска")
    args = parser.parse_args()
    if args.spacex_id is None:
        get_latest_spacex_images()
    else:
        fetch_spacex_images(args.spacex_id)


if __name__ == '__main__':
    main()
