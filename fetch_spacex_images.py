import os
from dotenv import load_dotenv
import requests
import argparse
import random
from files_from_url_info_and_load import image_load, file_info
from publish_to_telegram import publish_to_telegram


def fetch_spacex_last_launch(bot_api, chat_id, launch_id, path_to_load):
    url = 'https://api.spacexdata.com/v5/launches/'
    if launch_id=='':
        url += 'latest'
    else:
        url = f'{url}{launch_id}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers = headers)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    for link in photos:
        image_load(link, path_to_load, file_info(link)['file_name'])  
    publish_to_telegram(bot_api, chat_id, photos[random.randint(0, len(photos))])


def main():
    parser = argparse.ArgumentParser(description='Load images from SpaceX')
    parser.add_argument('--launch_id', type=str, default = '', help='provide an id')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')
    arguments = parser.parse_args()
    path_to_load = arguments.path_to_load
    launch_id = arguments.launch_id
    load_dotenv()
    bot_api = os.environ['TELEGRAM_BOT_KEY']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    fetch_spacex_last_launch(bot_api, chat_id, launch_id, path_to_load)


if __name__ == '__main__':
	main()
