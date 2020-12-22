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


def find_n_grams(files_content, ngrams_finder):
    """
    :param files_content: dictionary with key - file_name and value - text in the file
    :param ngrams_finder: an object with strategy (should have a method called find_n_grams_in_text(self, text)
    :return: dictionary
    """
    ngrams_in_files = dict()
    for file_name, text in files_content.items():
        ngrams_in_file = ngrams_finder.find_n_grams_in_text(text)
        print(ngrams_in_file)
        ngrams_in_files[file_name] = ngrams_in_file
    return ngrams_in_files


def count_n_grams(ngrams_in_files):
    """
    :param ngrams_in_files: a dictionary with file name as a key and with list of ngrams as a value
    :return: dictionary with key - file name and value as dictionary with key - word and value - number - how many
             ngram was in this file
    """
    file_name_and_ngrams_with_count = dict()
    for key, ngrams_list in ngrams_in_files.items():
        number_of_ngrams = dict()
        for item in ngrams_list:
            if item not in number_of_ngrams.keys():
                number_of_ngrams[item] = 1
            else:
                number_of_ngrams[item] += 1
        file_name_and_ngrams_with_count[key] = number_of_ngrams
    return file_name_and_ngrams_with_count
