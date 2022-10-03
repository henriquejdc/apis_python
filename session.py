import requests
import datetime
from bs4 import BeautifulSoup


def gettitle(num):
    url = f'https://scrapethissite.com/pages/forms/?page_num={num}'
    response = requests.get(url)
    sp = BeautifulSoup(response.text, 'html.parser')
    print(sp.title.text)
    return


if __name__ == '__main__':
    session = requests.Session()
    start = datetime.datetime.now()

    for x in range(1, 21):
        gettitle(x)
    finish = datetime.datetime.now() - start
    print(finish)
