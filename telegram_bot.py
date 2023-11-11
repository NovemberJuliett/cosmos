import telegram
import os
from dotenv import load_dotenv


def send_file(file_path, api_key, token):
    load_dotenv()
    telegram_api_key = os.environ["TOKEN"]
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telegram_api_key)
    bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))



