# Zadanie 3: Pobieranie zdjęć ze stron internetowych. Zaimplementuj narzędzie, które będzie pobierać zdjęcia z
# wybranej przez Ciebie strony internetowej (może być kilka stron). Wykorzystaj to narzędzie do pobrania po
# kilkudziesiąt zdjęć z 5 różnych kategorii (np. piłkarzy, psów, budynków, przyrody, narzędzi).
import sys
import os
import urllib.request as url_req

from io_functions import DOWNLOAD_IMAGE_DIR, remove_download_directory
from selenium import webdriver

html_links = list()
if len(sys.argv) < 2:
    print("Please give me one link or more")

for index in range(1, len(sys.argv)):
    html_links.append(sys.argv[index])
    print(html_links[index - 1])

print(html_links)
remove_download_directory(DOWNLOAD_IMAGE_DIR)
driver = webdriver.Firefox()
page_index = 1

for link in html_links:
    driver.get(link)
    os.mkdir("images\\" + str(page_index))
    images = driver.find_elements_by_tag_name('img')
    name = 1
    for image in images:
        print(image.get_attribute('src'))
        try:
            url_req.urlretrieve(image.get_attribute('src'), "images\\" + str(page_index) + "\\" + str(name) + ".png")
        except Exception:
            print("Something is not yes")
        name += 1
    page_index += 1
