from sklearn.feature_extraction.text import CountVectorizer
from io_functions import list_download_directory, read_text_from_download_file


class ContentReader:
    def __init__(self, download_dir):
        self.download_dir = download_dir

    def read_all_content_from_download(self):
        files_in_download = list_download_directory()
        files_content = dict()

        for file_name in files_in_download:
            files_content[file_name] = read_text_from_download_file(file_name, self.download_dir)

        return files_content


class NGramsFinder:
    def __init__(self, min_n_gram, max_n_gram):
        self.min_n = min_n_gram
        self.max_n = max_n_gram

    def find_n_grams_in_text(self, text):
        vectorizer = CountVectorizer(ngram_range=(self.min_n, self.max_n))
        analyzer = vectorizer.build_analyzer()
        return analyzer(text)
