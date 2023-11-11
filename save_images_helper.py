from pathlib import Path
import requests
from urllib.parse import unquote
import os
from urllib.parse import urlsplit


def save_image(url, path):
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

