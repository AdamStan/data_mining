# Twoim zadaniem jest utworzenie Scrapera, który będzie pobierać dane (np. adresy e-mail) korzystając z
# narzędzia Selenium. Wybierz taką stronę, która pobiera dane za pomocą skryptów javascript. Porównaj
# wyniki z poprzednio zaimplementowanym rozwiązaniem.
import sys

from io_functions import DOWNLOAD_DIR, write_emails_to_csv
from going_through_links import DownloadPages
from email_finder import read_emails_from_download

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

html_site = sys.argv[1]
print(html_site)

driver = webdriver.Firefox()
# driver.get(html_site)
# print(driver.page_source)

downloader = DownloadPages(download_dir=DOWNLOAD_DIR, driver=driver)
downloader.go_to_links_with_depth(html_site, 1)

emails = read_emails_from_download()
print(emails)

write_emails_to_csv(emails, "emails")
