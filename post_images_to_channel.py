import argparse
import time
import os
import telegram
from dotenv import load_dotenv
import random

load_dotenv()

telegram_api_key = os.environ["TOKEN"]
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_api_key)

parser = argparse.ArgumentParser()
parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--image_name", help="Название файла с расширением")
group.add_argument("--infinity_loop", action='store_true', help="Запуск бесконечного цикла отправки изображений")
args = parser.parse_args()
print(args)

nasa_images = []
for file in os.walk("images"):
    for element in file[2]:
        nasa_images.append(element)


def send_images(delay):
    for image in nasa_images:
        file_path = os.path.join("images", image)
        bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
        time.sleep(delay)


def send_random_image():
    random.shuffle(nasa_images)
    for image in nasa_images:
        file_path = os.path.join("images", image)
    bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))


def send_one_image(image_name):
    file_path = os.path.join("images", image_name)
    bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))


if args.image_name is None and args.infinity_loop is None:
    send_random_image()

if args.image_name is not None:
    send_one_image(args.image_name)

if args.infinity_loop is not None:
    while True:
        send_images(args.delay_time)
        send_random_image()




