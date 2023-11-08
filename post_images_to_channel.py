import argparse
import time
import os
from dotenv import load_dotenv
import random
from telegram_bot import send_file

load_dotenv()


nasa_images = []
for file in os.walk("images"):
    for element in file[2]:
        nasa_images.append(element)


def send_images(delay):
    for image in nasa_images:
        file_path = os.path.join("images", image)
        send_file(file_path)
        time.sleep(delay)


def send_random_image():
    random_image = random.choice(nasa_images)
    file_path = os.path.join("images", random_image)
    send_file(file_path)


def send_one_image(image_name):
    file_path = os.path.join("images", image_name)
    send_file(file_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--image_name", help="Название файла с расширением")
    group.add_argument("--infinite_loop", action='store_true', help="Запуск бесконечного цикла отправки изображений")
    args = parser.parse_args()

    if args.image_name is None and args.infinity_loop is False:
        send_random_image()
        return

    if args.image_name is not None:
        send_one_image(args.image_name)
        return

    if args.infinite_loop is not None:
        while True:
            send_images(args.delay_time)
            random.shuffle(nasa_images)
            return


if __name__ == '__main__':
    main()





