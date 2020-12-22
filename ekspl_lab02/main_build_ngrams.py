import os
from pathlib import Path

from ekspl_lab02.io_functions import write_dict_to_csv_file_in_download, write_text_to_file_in_download
from ekspl_lab02.similarity import jaccard_the_bests_results

from ekspl_lab02.ngrams import ContentReader, NGramsFinder, find_n_grams, count_n_grams

FILE_PARENT_NAME = Path(os.path.dirname(__file__)).resolve()
DOWNLOAD_DIR = os.path.join(str(FILE_PARENT_NAME), "downloads")

# dictionary with file_name and files_content
reader = ContentReader(DOWNLOAD_DIR)
files_content = reader.read_all_content_from_download()
print(files_content.keys())
ngrams_finder = NGramsFinder(1, 3)
# create function
ngrams_in_files = find_n_grams(files_content, ngrams_finder)

# count them
file_name_and_ngrams_with_count = count_n_grams(ngrams_in_files)

# save in downloads (as 1.txt.csv)
# for key, d in file_name_and_ngrams_with_count.items():
#     print(key)
#     print(d)
#     write_dict_to_csv_file_in_download(d, key)

# find 3 najbardziej podobne strony (adresy url) z bazy danych do strony podanej na wejsciu

ngrams_from_link = file_name_and_ngrams_with_count["1.txt"]
print("ngrams dict from first link")
print(ngrams_from_link)

del file_name_and_ngrams_with_count["1.txt"]
print(file_name_and_ngrams_with_count.keys())

### using Jaccard index
three_the_best_results = jaccard_the_bests_results(file_name_and_ngrams_with_count, ngrams_from_link, 3)
print(three_the_best_results)

# write_text_to_file_in_download(str(three_the_best_results), "jaccard_index_result.txt", FILE_PARENT_NAME)

### TODO: using bag of words

### TODO: using consine distance
