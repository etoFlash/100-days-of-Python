import shutil
import re
import traceback
from os import makedirs, remove
from os.path import join, exists
from collections import namedtuple

import requests
import img2pdf
from bs4 import BeautifulSoup as Soup

GENERATE_PDF = True
DELETE_IMG_AFTER_GENERATE_PDF = False
BASE_URL = "http://domain.com"
LOAD_LIST_FILE = "load_list.txt"
DESCRIPTION_FILE = "description.txt"
Row = namedtuple("Row", "url work_dir status")


def load_pic(pic_url, work_dir):
    # extract name like 00001.png
    r = re.search(r"/content/(\d{1,10}\.(png|jpg))", pic_url)
    assert r, "Picture name not found"
    pic_name = r.group(1)
    pic_response = requests.get(pic_url, stream=True)
    with open(join(work_dir, pic_name), "wb") as f_out:
        shutil.copyfileobj(pic_response.raw, f_out)
    return join(work_dir, pic_name)


def load_pics_from_page(url, work_dir):
    page_id = re.search(r"\d+", url).group()

    info_url = f"{BASE_URL}/site/catalogue/view?br={page_id}&locale=ru"
    load_url = f"{BASE_URL}/bookView/view/?brId={page_id}&simple=true&lang=ru"

    data = requests.get(info_url)
    soup = Soup(data.text, "html.parser")
    info = soup.select_one('p[itemprop="about"]').text.strip()
    with open(join(work_dir, DESCRIPTION_FILE), "w",
              encoding='utf-8') as f_out:
        f_out.write(info)

    data = requests.get(load_url)
    counter = 0
    print(f"Start loading from: {load_url}")

    images = []
    for pic_postfix in re.findall(r"pages.push\('(.*)'\);", data.text):
        images.append(load_pic(f"{BASE_URL}{pic_postfix}", work_dir))
        if counter % 15 == 0:
            print(f"Loaded: {counter}")
        counter += 1
    print(f"Loaded: {counter}")
    print(f"End loading from: {load_url}")
    if images and GENERATE_PDF:
        with open(join(work_dir, work_dir + ".pdf"), "wb") as f_out:
            f_out.write(img2pdf.convert(images))
            print(f"{work_dir}.pdf generated\n")
            if DELETE_IMG_AFTER_GENERATE_PDF:
                for img in images:
                    remove(img)


def do_load_all():
    # ex. of line in list: url;dir_name;status
    # status can be empty
    loads = []
    with open(LOAD_LIST_FILE, encoding="utf-8") as f_in:
        for load_line in f_in:
            if not load_line.strip():
                continue
            if load_line.count(";") < 2:
                load_line += ";"
            row = Row(*[s.strip() for s in load_line.split(";")])
            if not row.status:
                row = row._replace(status="no processed")
            loads.append(row)

    for index, row in enumerate(loads):
        if row.status == "OK":
            continue
        try:
            if not exists(row.work_dir):
                makedirs(row.work_dir)
            load_pics_from_page(row.url, row.work_dir)
            loads[index] = row._replace(status="OK")
        except Exception as e:
            loads[index] = row._replace(status="error")
            with open(join(row.work_dir, "log.txt"), "w") as f_out:
                f_out.write(traceback.format_exc())
                print(f"Loading failed. See 'log.txt' in dir '{row.work_dir}'.")

    with open(LOAD_LIST_FILE, "w", encoding="utf-8") as f_out:
        f_out.writelines(";".join(row) for row in loads)


if __name__ == '__main__':
    do_load_all()
