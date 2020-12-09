import sys
import requests

from io_functions import remove_download_directory, create_download_directory
from going_through_links import go_to_links_with_depth


html_link = sys.argv[1]
depth = int(sys.argv[2])
html_text = requests.get(html_link).text

remove_download_directory()
create_download_directory()

go_to_links_with_depth(html_link, depth)
