import requests
from bs4 import BeautifulSoup
import csv

HOST = "https://wiktenauer.com/"
URL = "https://wiktenauer.com/wiki/Manuscripts"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('td', class_='Article smwtype_wpg')
    cards = []

    for item in items:
        cards.append(
                HOST + 'wiki/'+ 'Index:'+ item.find('a').get('href').strip('wiki/')
        )
    return cards

def parser():
    PAGENATION = input('Кол-во страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
    else:
        print("error")

def tonowhere():
    html = get_html(URL)
    listof = get_content(html.text)
    print(listof)
tonowhere()


