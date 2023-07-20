import time
import os.path
from publish_to_telegram import publish_to_telegram 
import argparse
import random
from dotenv import load_dotenv


def automatically_post_telegram(bot_token, chat_id, folder_to_post, frequency):
    images=[]
    for address, dirs, files in os.walk(folder_to_post):
        for name in files:
            images.append(os.path.join(address, name))
    while True:
        for image in images:
            with open(image, 'rb', encoding='utf-8') as image_file:
                publish_to_telegram(bot_token, chat_id, image_file)
            time.sleep(int(frequency)*3600)
        random.shuffle(images)


def main():
    parser = argparse.ArgumentParser(description='Upload images to Telegram chat')
    parser.add_argument('-f', '--folder_to_post', type=str, default = 'images', help='Path to load images')    
    folder_to_post = parser.parse_args().folder_to_post
    load_dotenv()
    bot_token = os.environ['TELEGRAM_BOT_KEY']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    frequency = os.environ['TELEGRAM_PUBLICATION_FREQUENCY']
    automatically_post_telegram(bot_token, chat_id, folder_to_post, frequency)


if __name__ == '__main__':
    main()
