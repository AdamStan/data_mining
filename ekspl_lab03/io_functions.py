import os
from pathlib import Path
import logging

FILE_PARENT_NAME = Path(os.path.dirname(__file__)).resolve()
DOWNLOAD_DIR = os.path.join(str(FILE_PARENT_NAME), "downloads")
DOWNLOAD_IMAGE_DIR = os.path.join(str(FILE_PARENT_NAME), "images")


def write_text_to_file_in_download(text, file_name, download_dir=DOWNLOAD_DIR):
    file = open(os.path.join(download_dir, file_name), "w", encoding="utf-8")
    file.write(text)
    file.close()


def read_text_from_download_file(file_name, download_dir=DOWNLOAD_DIR):
    file = open(os.path.join(download_dir, file_name), "r", encoding="utf-8")
    return file.read()


def remove_download_directory(download_dir=DOWNLOAD_DIR):
    for root, dirs, files in os.walk(download_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def create_download_directory(download_dir=DOWNLOAD_DIR):
    try:
        os.mkdir(download_dir)
    except FileExistsError:
        logging.warning("Download directory exists...")


def list_download_directory():
    return os.listdir(DOWNLOAD_DIR)


def write_emails_to_csv(emails, file_name):
    file = open(os.path.join(FILE_PARENT_NAME, file_name + ".csv"), "w", encoding="utf-8")
    for email in emails:
        file.write(email)
        file.write("\n")
    file.close()
