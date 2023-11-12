import telegram


def send_file(file_path, token, chat_id):
    bot = telegram.Bot(token=token)
    with open(file_path, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)
