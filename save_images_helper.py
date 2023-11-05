from dotenv import load_dotenv
from pathlib import Path
import requests
from urllib.parse import unquote
import os
from urllib.parse import urlsplit


Path("images").mkdir(parents=True, exist_ok=True)


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    encoded_url = urlsplit(url)
    url_path = encoded_url[2]
    decoded_url = unquote(url_path)
    file_name_split = os.path.split(decoded_url)
    file_name = file_name_split[1]
    url_name, url_extension = os.path.splitext(file_name)
    return url_extension
