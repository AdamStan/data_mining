import sys
import requests

from download import DOWNLOAD_DIR

from io_functions import remove_download_directory, create_download_directory
from going_through_links import DownloadPages

html_link = sys.argv[1]

html_text = requests.get(html_link).text

remove_download_directory(download_dir=DOWNLOAD_DIR)
create_download_directory(download_dir=DOWNLOAD_DIR)

downloader = DownloadPages(DOWNLOAD_DIR)
downloader.go_to_links_with_depth(html_link, 1)
