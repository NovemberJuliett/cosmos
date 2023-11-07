import random
import telegram
from dotenv import load_dotenv
import os
import time

load_dotenv()

telegram_api_key = os.environ["TOKEN"]
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_api_key)
updates = bot.get_updates()

nasa_images = []
for file in os.walk("images"):
    for element in file[2]:
        nasa_images.append(element)
print(nasa_images)


def send_image(delay):
    print(nasa_images)
    for image in nasa_images:
        file_path = os.path.join("images", image)
        bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
        time.sleep(delay)


def random_image():
    random.shuffle(nasa_images)

if __name__ == '__main__':
    send_image(1)
    random_image()


