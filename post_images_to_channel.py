import argparse
import time
import os
import random
from dotenv import load_dotenv
from telegram_bot import send_file


def send_images(delay, images_list, token, chat_id):
    for image in images_list:
        file_path = os.path.join("images", image)
        send_file(file_path, token, chat_id)
        time.sleep(delay)


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    nasa_images = []
    for file in os.walk("images"):
        for element in file[2]:
            nasa_images.append(element)

    parser = argparse.ArgumentParser(description="Отправляет изображения в телеграм-канал")
    parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--image_name", help="Название файла с расширением")
    group.add_argument("--infinite_loop", action='store_true', help="Запуск бесконечного цикла отправки изображений")
    args = parser.parse_args()

    if args.image_name is None and not args.infinite_loop:
        random_image = random.choice(nasa_images)
        file_path = os.path.join("images", random_image)
        send_file(file_path, token, chat_id)
        return

    if args.image_name:
        file_path = os.path.join("images", args.image_name)
        send_file(file_path, token, chat_id)
        return

    if args.infinite_loop:
        while True:
            send_images(args.delay_time, nasa_images, token, chat_id)
            random.shuffle(nasa_images)
            return


if __name__ == '__main__':
    main()





