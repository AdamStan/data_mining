import sys
import requests
from bs4 import BeautifulSoup

from io_functions import write_text_to_file
from link_finder import find_links_in_text
from going_through_links import go_to_links_with_depth

# from: https://emailregex.com/
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
links = {}
links_discovered = set()

html_link = sys.argv[1]
depth = int(sys.argv[2])
html_text = requests.get(html_link).text

go_to_links_with_depth(html_link, depth)
