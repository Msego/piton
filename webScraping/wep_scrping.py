# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib

def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeaitifulSoup(response.content, 'html.parser')
        image_tag = soup.find(id='comic')

        image_url = image_tag.find('img')['src']
        image_name = image_url.spit('/')[-1]
        print('Descargando la imagen: {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(image_url), image_name)

if __name__ == '__main__':
    run()