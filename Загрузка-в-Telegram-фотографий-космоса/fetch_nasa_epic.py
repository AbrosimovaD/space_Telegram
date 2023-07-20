import requests
import random
from datetime import datetime as dt
from files_from_url_info_and_load import image_load, file_info
from publish_to_telegram import publish_to_telegram
from dotenv import load_dotenv
import argparse
import os


def fetch_nasa_epic(bot_api, chat_id, api_key, n, path_to_load):
    epic_url = 'https://api.nasa.gov/EPIC/{}/natural{}'
    image_type = 'png'
    headers = {'Accept': 'application/json'}
    params = {'api_key': api_key}
    response = requests.get(epic_url.format('api',''), headers = headers, params = params)
    response.raise_for_status()
    numb_to_post = random.randint(0, n)    
    for i, info in enumerate(response.json()):
        image = info['image']
        image_date = dt.strftime(dt.strptime(info['date'], "%Y-%m-%d %H:%M:%S"), "%Y/%m/%d")
        image_url = epic_url.format('archive',f'/{image_date}/{image_type}/{image}.{image_type}?api_key={api_key}')
        image_load(image_url, path_to_load, f'{image}.{image_type}')
        if i==numb_to_post:
        	publish_to_telegram(bot_api, chat_id, image_url)
        if i == n:
            break


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    bot_api = os.environ['TELEGRAM_BOT_KEY']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    parser = argparse.ArgumentParser(description='Load images from NASA EPIC')
    parser.add_argument('--numb', type=int, default = 1, help='Number of photos to load')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')    
    numb = parser.parse_args().numb
    path_to_load = parser.parse_args().path_to_load
    fetch_nasa_epic(bot_api, chat_id, api_key, numb, path_to_load )   


if __name__ == '__main__':
    main() 
