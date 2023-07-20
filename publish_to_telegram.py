import telegram

def publish_to_telegram(bot_token, chat_id,photo_url):
    bot = telegram.Bot(token=bot_token)
    bot.send_photo(chat_id=chat_id, photo=photo_url)
