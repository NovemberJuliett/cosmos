import requests
import os
from datetime import datetime
from save_images_helper import save_image


def fetch_epic_images(epic_api_key):
    epic_payload = {'api_key': epic_api_key}
    epic_response = requests.get("https://api.nasa.gov/EPIC/api/natural/images/", params=epic_payload)
    epic_info = epic_response.json()
    for index, element in enumerate(epic_info):
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
        save_image(epic_pic_link, f'images/nasa_epic_{index}'".png")


def main():
    epic_api_key = os.environ["APOD_KEY"]
    fetch_epic_images(epic_api_key)


if __name__ == '__main__':
    main()
