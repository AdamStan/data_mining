import requests
from bs4 import BeautifulSoup
import logging
from io_functions import write_text_to_file
from link_finder import find_links_in_text

links_discovered = set()


def go_to_links(links):
    new_links = set()
    for html_link in links:
        logging.warning("HTML link: " + html_link)
        if html_link not in links_discovered:
            html_text = requests.get(html_link).text

            links_discovered.add(html_link)
            soup = BeautifulSoup(html_text, 'html.parser')
            links = find_links_in_text(html_text, html_link)
            new_links.update(links)
            write_text_to_file(soup.get_text(), str(len(links_discovered)) + ".txt")
        else:
            logging.warning("HTML link was discovered!")

    return new_links


def go_to_links_with_depth(html_link, depth=0):
    links_to_discover = set()
    links_to_discover.add(html_link)
    for i in range(0, depth + 1):
        links_to_discover = go_to_links(links_to_discover)
