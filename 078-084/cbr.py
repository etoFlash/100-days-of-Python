import sqlite3
from datetime import datetime

from bs4 import BeautifulSoup as Soup
import requests

DB_FILE = "rates.db"
RATE_TABLE = "t_rate"
BASE_URL = "https://cbr.ru"


with sqlite3.connect(DB_FILE) as conn:
    for row in conn.execute("SELECT COUNT(1) FROM sqlite_master WHERE type='table' AND name=?", (RATE_TABLE,)):
        if not row[0]:
            with open(f"{RATE_TABLE}.sql") as f:
                conn.execute(f.read())

    r = requests.get(BASE_URL)
    r.raise_for_status()
    s = Soup(r.text, "html.parser")
    div = s.select_one("div#widget_exchange")
    tr = div.select("tr")

    for i, rate_type in ([0, "U"], [1, "E"]):
        date = div.select("tr")[0].select("th")[1].text
        date_stamp = int(datetime.strptime(date, "%d.%m.%Y").timestamp())
        # USD rate exists in 2nd row, EURO in 3rd
        rate = float(div.select("tr")[1 + i].select("td")[1].text.replace("руб.", "").lstrip().replace(",", "."))
        row = conn.execute(f"SELECT * FROM {RATE_TABLE}"
                           "  WHERE TYPE=? AND DATE=?", (rate_type, date_stamp)).fetchone()
        # insert rate for date only if it not exists in table
        if not row:
            conn.execute(f"INSERT INTO {RATE_TABLE} (TYPE, DATE, RATE)"
                         " VALUES (?, ?, ?)", (rate_type, date_stamp, rate))
            conn.commit()
