import argparse
import time
import os
import random
from telegram_bot import send_file


def send_images(delay, images_list):
    for image in images_list:
        file_path = os.path.join("images", image)
        send_file(file_path)
        time.sleep(delay)


def send_random_image(images_list):
    random_image = random.choice(images_list)
    file_path = os.path.join("images", random_image)
    send_file(file_path)


def send_one_image(image_name):
    file_path = os.path.join("images", image_name)
    send_file(file_path)


def main():
    nasa_images = []
    for file in os.walk("images"):
        for element in file[2]:
            nasa_images.append(element)

    parser = argparse.ArgumentParser(description="Введите выбранные аргументы:")
    parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--image_name", help="Название файла с расширением")
    group.add_argument("--infinite_loop", action='store_true', help="Запуск бесконечного цикла отправки изображений")
    args = parser.parse_args()

    if args.image_name is None and not args.infinite_loop:
        send_random_image(nasa_images)
        return

    if args.image_name:
        send_one_image(args.image_name)
        return

    if args.infinite_loop:
        while True:
            send_images(args.delay_time, nasa_images)
            random.shuffle(nasa_images)
            return


if __name__ == '__main__':
    main()





