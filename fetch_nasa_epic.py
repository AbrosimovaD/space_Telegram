import requests
from datetime import datetime as dt
from files_from_url_info_and_load import download_image, get_file_name_and_type
from dotenv import load_dotenv
import argparse
import os


def fetch_nasa_epic(api_key, number_of_photo, path_to_load):
    epic_url = 'https://api.nasa.gov/EPIC/{}/natural{}'
    image_type = 'png'
    headers = {'Accept': 'application/json'}
    params = {'api_key': api_key}
    response = requests.get(epic_url.format('api',''), headers = headers, params = params)
    response.raise_for_status()  
    for photo_number, photo_info in enumerate(response.json()):
        image = photo_info['image']
        image_date = dt.strftime(dt.strptime(photo_info['date'], "%Y-%m-%d %H:%M:%S"), "%Y/%m/%d")
        image_url = epic_url.format('archive',f'/{image_date}/{image_type}/{image}.{image_type}')
        download_image(image_url, params, path_to_load, f'{image}.{image_type}')
        if photo_number == number_of_photo:
            break


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    parser = argparse.ArgumentParser(description='Load images from NASA EPIC')
    parser.add_argument('--numb', type=int, default = 1, help='Number of photos to load')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')    
    arguments = parser.parse_args()
    numb = arguments.numb
    path_to_load = arguments.path_to_load
    fetch_nasa_epic(api_key, numb, path_to_load)


if __name__ == '__main__':
    main() 
