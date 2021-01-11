import requests
from bs4 import BeautifulSoup
import logging
from io_functions import write_text_to_file_in_download
from link_finder import find_links_in_text


class DownloadPages:
    def __init__(self, download_dir, driver):
        self.download_dir = download_dir
        self.driver = driver
        self.links_discovered = list()
        self.links_to_html_pages = dict()

    def go_to_links(self, links):
        new_links = set()
        for html_link in links:
            logging.info("HTML link: " + html_link)
            if html_link not in self.links_discovered:
                html_text = ""
                try:
                    self.driver.get(html_link)
                    html_text = self.driver.page_source
                except Exception:
                    logging.info("Cannot get to: " + str(html_link))

                self.links_discovered.append(html_link)
                soup = BeautifulSoup(html_text, 'html.parser')
                links = find_links_in_text(html_text, html_link)
                new_links.update(links)
                file_name = str(len(self.links_discovered)) + ".txt"
                write_text_to_file_in_download(soup.get_text(), file_name, self.download_dir)
                self.links_to_html_pages[file_name] = html_link
            else:
                logging.info("HTML link was discovered!")

        return new_links

    def go_to_links_with_depth(self, html_link, depth=0):
        links_to_discover = set()
        links_to_discover.add(html_link)
        for i in range(0, depth + 1):
            logging.warning("depth: " + str(i))
            links_to_discover = self.go_to_links(links_to_discover)

        return self.links_to_html_pages
