import requests
from pathlib import Path
from os import path
from urllib import parse


def download_image(url, path, filename):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)


def get_file_name_and_type(url):
    file_path = parse.urlsplit(url).path
    file_name = parse.unquote(path.split(file_path)[1])
    file_type = path.splitext(file_name)[1]
    return {'file_name':file_name,'file_type':file_type}
