>>> import requests
>>> t = requests.get("https://codechalleng.es/bites/catalogue").text
>>> from bs4 import BeautifulSoup as Soup
>>> s = Soup(t, "html.parser")
>>> tr = s.select("tbody tr")
>>> tr[0].select("td")[0].getText().strip()[5:]
'1. Sum n numbers'
>>> tr[0].select("td")[1].select_one("img")["alt"].split()[0]
'Beginner'
>>> ", ".join(a.getText() for a in tr[0].select("td a.tag"))
'None, default args, range, sum'
