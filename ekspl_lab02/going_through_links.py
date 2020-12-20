import requests
from bs4 import BeautifulSoup
import logging
from io_functions import write_text_to_file_in_download
from link_finder import find_links_in_text

links_discovered = set()

class DownloadPages:
    def __init__(self, download_dir):
        self.download_dir = download_dir

    def go_to_links(self, links):
        new_links = set()
        for html_link in links:
            logging.info("HTML link: " + html_link)
            if html_link not in links_discovered:
                html_text = ""
                try:
                    html_text = requests.get(html_link).text
                except Exception:
                    logging.info("Cannot get to: " + str(html_link))

                links_discovered.add(html_link)
                soup = BeautifulSoup(html_text, 'html.parser')
                links = find_links_in_text(html_text, html_link)
                new_links.update(links)
                write_text_to_file_in_download(soup.get_text(), str(len(links_discovered)) + ".txt", self.download_dir)
            else:
                logging.info("HTML link was discovered!")

        return new_links

    def go_to_links_with_depth(self, html_link, depth=0):
        links_to_discover = set()
        links_to_discover.add(html_link)
        for i in range(0, depth + 1):
            logging.warning("depth: " + str(i))
            links_to_discover = self.go_to_links(links_to_discover)
