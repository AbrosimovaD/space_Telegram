import requests
import os
from dotenv import load_dotenv
import argparse
import random
from files_from_url_info_and_load import image_load, file_info
from publish_to_telegram import publish_to_telegram


def fetch_nasa_apod(bot_api, chat_id, api_key, number_of_images, path_to_load ):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    headers = {'Accept': 'application/json'}
    params = {'count': number_of_images, 'api_key': api_key}
    response = requests.get(apod_url, headers = headers, params = params)
    response.raise_for_status()
    numb_to_post = random.randint(0, number_of_images)
    for i, launch in enumerate(response.json()):
        link = launch['url']
        image_load(link, path_to_load, file_info(link)['file_name'])
        if i==numb_to_post:
            publish_to_telegram(bot_api, chat_id, link)


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    bot_api = os.environ['TELEGRAM_BOT_KEY']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(description='Load images from NASA APOD')
    parser.add_argument('-n', '--numb', type=int, default = 1,  help='Number of photos to load')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')    
    arguments = parser.parse_args()
    numb = arguments.numb
    path_to_load = arguments.path_to_load
    fetch_nasa_apod(bot_api, chat_id, api_key, numb, path_to_load)


if __name__ == '__main__':
    main()
