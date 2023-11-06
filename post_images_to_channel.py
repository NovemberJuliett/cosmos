import argparse
import time
import os
from telegram_bot import send_image


parser = argparse.ArgumentParser()
parser.add_argument("-delay_time", type=int, default=14400, help="Интервал отправки изображений")
args = parser.parse_args()
while True:
    send_image(args.delay_time)

