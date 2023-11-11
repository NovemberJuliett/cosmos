import requests
import os
from urllib.parse import urlparse
from save_image_helper import save_image


def fetch_apod_images(apod_key):
    number_of_images = 30
    apod_payload = {'apod_key': apod_key, 'count': number_of_images}
    apod_response = requests.get("https://api.nasa.gov/planetary/apod", params=apod_payload)
    apod_response.raise_for_status()
    apod_pics = apod_response.json()
    for index, picture in enumerate(apod_pics):
        apod_pic_link = picture['url']
        link_name, link_extension = os.path.splitext(apod_pic_link)
        save_image(apod_pic_link, f'images/nasa_apod_{index}{link_extension}')


def main():
    apod_api_key = os.environ["APOD_KEY"]
    fetch_apod_images(apod_api_key)


if __name__ == '__main__':
    main()
