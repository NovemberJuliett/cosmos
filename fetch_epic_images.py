import requests
import os
from datetime import datetime
from save_image_helper import save_image
from dotenv import load_dotenv
from urllib.parse import urlparse, urlunparse, urlencode


def fetch_epic_images(epic_api_key):
    epic_payload = {'api_key': epic_api_key}
    epic_response = requests.get("https://api.nasa.gov/EPIC/api/natural/images/", params=epic_payload)
    image_features = epic_response.json()
    for index, image in enumerate(image_features):
        date_value = image['date']
        image_name = image['image']
        formatted_date = datetime.strptime(date_value, '%Y-%m-%d %H:%M:%S')
        date_without_time = datetime.date(formatted_date)
        year = date_without_time.year
        month = f"{date_without_time:%m}"
        day = f"{date_without_time:%d}"
        new_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
        save_image(new_url, f'images/nasa_epic_{index}.png', query_params=epic_payload)


def main():
    load_dotenv()
    epic_api_key = os.environ["APOD_KEY"]
    fetch_epic_images(epic_api_key)


if __name__ == '__main__':
    main()
