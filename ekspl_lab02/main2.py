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
links_discovered = downloader.go_to_links_with_depth(html_link, 1)

print(links_discovered)
# find all ngrams with duplicates

# count them

# save in downloads as for example ngrams1.txt

# find 3 najbardziej podobne strony (adresy url) z bazy danych do strony podanej na wejsciu
