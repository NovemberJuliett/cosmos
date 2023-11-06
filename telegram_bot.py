import telegram
from dotenv import load_dotenv
import os
import time

load_dotenv()

telegram_api_key = os.environ["TOKEN"]
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_api_key)
updates = bot.get_updates()
text = 'Hello World!'


def send_message():
    bot.send_message(text=text, chat_id=chat_id)


def send_image(delay):
    for file in os.walk("images"):
        for element in file[2]:
            file_path = os.path.join("images", element)
            bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
            time.sleep(delay)
