import sys
import requests
from bs4 import BeautifulSoup

from io_functions import write_text_to_file
from link_finder import find_links_in_text

# from: https://emailregex.com/
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
links = {}
links_discovered = set()

html_link = sys.argv[1]

html_text = requests.get(html_link).text

links_discovered.add(html_link)
soup = BeautifulSoup(html_text, 'html.parser')
links = find_links_in_text(html_text, html_link)

write_text_to_file(soup.get_text(), "1.txt")


print(links)

print(soup.get_text())
