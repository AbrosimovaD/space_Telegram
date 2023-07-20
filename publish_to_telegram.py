import telegram

def publish_to_telegram(bot_api, chat_id,photo_url):
    bot = telegram.Bot(token=bot_api)
    bot.send_photo(chat_id=chat_id, photo=photo_url)
