import requests
from pathlib import Path
from pprint import pprint
from urllib.parse import urlparse
from urllib.parse import unquote
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
Path("images").mkdir(parents=True, exist_ok=True)


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    spacex_id = '5eb87ce4ffd86e000604b338'
    spacex_response = requests.get(f"https://api.spacexdata.com/v5/launches/{spacex_id}")
    spacex_response.raise_for_status()
    flight_info = spacex_response.json()
    photo_links = flight_info["links"]["flickr"]["original"]
    for index, link in enumerate(photo_links):
        urlparse(link)
        link_name, link_extension = os.path.splitext(link)
        save_images(link, f'images/spacex_{index}{link_extension}')


def get_extension(url):
    encoded_url = urlsplit(url)
    url_path = encoded_url[2]
    decoded_url = unquote(url_path)
    file_name_split = os.path.split(decoded_url)
    file_name = file_name_split[1]
    url_name, url_extension = os.path.splitext(file_name)
    return url_extension


def get_apod_images():
    apod_api_key = os.environ["APOD_KEY"]
    apod_payload = {'api_key': apod_api_key, 'count': 30}
    apod_response = requests.get("https://api.nasa.gov/planetary/apod", params=apod_payload)
    apod_response.raise_for_status()
    apod_pics = apod_response.json()
    for index, picture in enumerate(apod_pics):
        apod_pic_link = picture['url']
        urlparse(apod_pic_link)
        link_name, link_extension = os.path.splitext(apod_pic_link)
        save_images(apod_pic_link, f'images/nasa_apod_{index}{link_extension}')


def get_epic_images():
    epic_api_key = os.environ["APOD_KEY"]
    epic_payload = {'api_key': epic_api_key}
    epic_response = requests.get("https://api.nasa.gov/EPIC/api/natural/images/", params=epic_payload)
    epic_info = epic_response.json()
    counter = 0
    for element in epic_info:
        date_value = element['date']
        image_name = element['image']
        formatted_date = datetime.strptime(date_value, '%Y-%m-%d %H:%M:%S')
        date_without_time = datetime.date(formatted_date)
        year = date_without_time.year
        month = f"{date_without_time:%m}"
        day = f"{date_without_time:%d}"
        new_epic_response = requests.get(
            "https://api.nasa.gov/EPIC/archive/natural/"f'{year}/{month}/{day}/png/'""f'{image_name}.png',
            params=epic_payload)
        epic_pic_link = new_epic_response.url
        save_images(epic_pic_link, f'images/nasa_epic_{counter}'".png")
        counter += 1

get_epic_images()
















