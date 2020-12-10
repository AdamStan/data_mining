import logging
import sys
import requests

from email_finder import read_emails_from_download
from io_functions import remove_download_directory, create_download_directory, write_emails_to_csv
from going_through_links import go_to_links_with_depth

html_link = sys.argv[1]
depth = int(sys.argv[2])

html_text = requests.get(html_link).text

remove_download_directory()
create_download_directory()

go_to_links_with_depth(html_link, depth)

emails = read_emails_from_download()
print(emails)

write_emails_to_csv(emails, "emails")
