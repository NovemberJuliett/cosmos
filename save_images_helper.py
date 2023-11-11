from pathlib import Path
import requests
from dotenv import load_dotenv


def save_image(url, path):
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

