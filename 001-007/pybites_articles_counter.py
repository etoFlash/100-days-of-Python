import requests
import bs4

default_url = "https://pybit.es/pages/articles.html"


def count_articles(address=default_url, local=False):
    if local:
        with open(address) as f:
            data = f.read()
    else:
        r = requests.get(address)
        r.raise_for_status()
        data = r.text
    soup = bs4.BeautifulSoup(data, 'html.parser')

    return len(soup.select('#articleList li'))
