import random
import telegram
from dotenv import load_dotenv
import os
import time

load_dotenv()

telegram_api_key = os.environ["TOKEN"]
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_api_key)

user_images = []
for file in os.walk("images"):
    for element in file[2]:
        user_images.append(element)

file_path = os.path.join("images", "nasa_apod_0.jpg")
bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
if image_name is None:




