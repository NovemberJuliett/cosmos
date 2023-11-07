import argparse
import time
import os
import telegram
from dotenv import load_dotenv
import random

load_dotenv()


nasa_images = []
for file in os.walk("images"):
    for element in file[2]:
        nasa_images.append(element)


def send_image(delay):
    for image in nasa_images:
        file_path = os.path.join("images", image)
        bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
        time.sleep(delay)


def random_image():
    random.shuffle(nasa_images)


def main():
    telegram_api_key = os.environ["TOKEN"]
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telegram_api_key)

    parser = argparse.ArgumentParser()
    parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
    args = parser.parse_args()

    while True:
        send_image(args.delay_time)
        random_image()


if __name__ == '__main__':
    main()

