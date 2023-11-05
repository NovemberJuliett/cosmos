import telegram
from dotenv import load_dotenv
import os

load_dotenv()

telegram_api_key = os.environ["TOKEN"]
bot = telegram.Bot(token=telegram_api_key)

print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

bot.send_message(text='Hello World!', chat_id="@nasaspacephotos")
