from pathlib import Path
import requests


def save_image(url, path, query_params=None):
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=query_params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

