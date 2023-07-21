import requests
import os
from dotenv import load_dotenv
import argparse
from files_from_url_info_and_load import download_image, get_file_name_and_type
from publish_to_telegram import publish_to_telegram


def fetch_nasa_apod(api_key, number_of_images, path_to_load):
    apod_url = 'https://api.nasa.gov/planetary/apod'
    headers = {'Accept': 'application/json'}
    params = {'count': number_of_images, 'api_key': api_key}
    response = requests.get(apod_url, headers = headers, params = params)
    response.raise_for_status()
    for launch in response.json():
        link = launch['url']
        download_image(link, path_to_load, get_file_name_and_type(link)['file_name'])


def main():
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    parser = argparse.ArgumentParser(description='Load images from NASA APOD')
    parser.add_argument('-n', '--numb', type=int, default = 1,  help='Number of photos to load')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')    
    arguments = parser.parse_args()
    numb = arguments.numb
    path_to_load = arguments.path_to_load
    fetch_nasa_apod(api_key, numb, path_to_load)


if __name__ == '__main__':
    main()
