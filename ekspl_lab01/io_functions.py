import os
from pathlib import Path
import logging

FILE_PARENT_NAME = Path(os.path.dirname(__file__)).resolve()
DOWNLOAD_DIR = os.path.join(str(FILE_PARENT_NAME), "downloads")


def write_text_to_file(text, file_name):
    file = open(os.path.join(DOWNLOAD_DIR, file_name), "w", encoding="utf-8")
    file.write(text)
    file.close()


def read_text_from_file(file_name):
    file = open(os.path.join(DOWNLOAD_DIR, file_name), "r", encoding="utf-8")
    return file.read()


def remove_download_directory():
    for root, dirs, files in os.walk(DOWNLOAD_DIR, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def create_download_directory():
    try:
        os.mkdir(DOWNLOAD_DIR)
    except FileExistsError:
        logging.warning("Download directory exists...")
