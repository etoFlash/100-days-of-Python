import re
import csv
from collections import namedtuple

import requests


BASE_URL = "http://fulltext.pl.spb.ru/"
DELIMITER = ";"
PARENT_DIR_LABEL = "Parent Directory"
LINK_PATTERN = r"<li><a href=\"(.*?)\">(.*?)</a></li>"
Info = namedtuple("Info", "dir_or_file size")
result = []


def check_files_from_dir(path):
    global result
    result.append(Info(path, ""))
    r = requests.get(path)
    links = re.findall(LINK_PATTERN, r.text)
    for link in links:
        if PARENT_DIR_LABEL in link[1]:
            continue
        elif link[0].endswith("/"):
            check_files_from_dir(path + link[0])
            continue
        elif not link[0].lower().endswith(".pdf"):
            continue

        url = path + link[0]
        h = requests.head(url, allow_redirects=True)
        size = round(int(h.headers.get('content-length', 0)) / 1024 / 1024)
        size = 2 if size < 2 else size
        result.append(Info(url, str(size)))


if __name__ == '__main__':
    print("In process...")
    check_files_from_dir(BASE_URL)
    with open("result.csv", "w", newline='') as fp:
        w = csv.writer(fp, delimiter=DELIMITER)
        w.writerow(Info._fields)
        w.writerows((r.dir_or_file, r.size) for r in result)
