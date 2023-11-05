import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlparse
from save_images_helper import save_images

load_dotenv()


def fetch_apod_images(api_key):
    apod_payload = {'api_key': api_key, 'count': 30}
    apod_response = requests.get("https://api.nasa.gov/planetary/apod", params=apod_payload)
    apod_response.raise_for_status()
    apod_pics = apod_response.json()
    for index, picture in enumerate(apod_pics):
        apod_pic_link = picture['url']
        urlparse(apod_pic_link)
        link_name, link_extension = os.path.splitext(apod_pic_link)
        save_images(apod_pic_link, f'images/nasa_apod_{index}{link_extension}')


def main():
    apod_api_key = os.environ["APOD_KEY"]
    fetch_apod_images(apod_api_key)


if __name__ == '__main__':
    main()
