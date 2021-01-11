import re
from io_functions import list_download_directory, read_text_from_download_file

# regex from: https://emailregex.com/
email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
p = re.compile(email_regex)


def read_emails_from_download():
    files_in_download = list_download_directory()
    emails = set()

    for file_name in files_in_download:
        content = read_text_from_download_file(file_name)
        emails.update(p.findall(content))

    return emails
