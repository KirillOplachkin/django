import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://rezka.ag"
URL = "https://rezka.ag/films"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []

    for item in items:
        films.append(
            {
                'title': item.find('div', class_="b-content__inline_item-link").get_text(),
                'image': item.find('a', href_="").find('img').get('src')
            }
        )

        return films

@csrf_exempt
def parser_func():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            films.extend(get_data(html.text))
            return films
            # print(films)
    else:
        raise ValueError('Error maybe permission denied')
    
