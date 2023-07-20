import os
from dotenv import load_dotenv
import requests
import argparse
from files_from_url_info_and_load import download_image, get_file_name_and_type


def fetch_spacex_last_launch(launch_id, path_to_load):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers = headers)
    response.raise_for_status()
    photos = response.json()['links']['flickr']['original']
    for link in photos:
        download_image(link, path_to_load, get_file_name_and_type(link)['file_name'])  


def main():
    parser = argparse.ArgumentParser(description='Load images from SpaceX')
    parser.add_argument('--launch_id', type=str, default = 'latest', help='provide an id')
    parser.add_argument('-p', '--path_to_load', type=str, default = 'images', help='Path to load images')
    arguments = parser.parse_args()
    path_to_load = arguments.path_to_load
    launch_id = arguments.launch_id
    load_dotenv()
    fetch_spacex_last_launch(launch_id, path_to_load)


if __name__ == '__main__':
	main()
