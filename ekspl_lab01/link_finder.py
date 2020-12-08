from bs4 import BeautifulSoup
import logging

protocol_start = ("http:", "https:")


def find_links_in_text(text, url):
    soup = BeautifulSoup(text, 'html.parser')
    index_of_last_slash = url.rfind("/")
    links = set()

    for link in soup.find_all('a'):
        link_base = link.get('href')

        if link_base is None or len(link_base) == 0:
            continue

        index_of_hash_section = link_base.rfind("#")

        if index_of_hash_section != -1:
            # link_base = url + link_base
            continue
        elif not link_base.startswith(protocol_start):
            link_base = url[0:index_of_last_slash + 1] + link_base

        logging.warning("Base link: " + link_base)
        links.add(str(link_base))

    return links
