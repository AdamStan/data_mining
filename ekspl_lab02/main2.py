import sys
import requests

from ekspl_lab02.download import FILE_PARENT_NAME, DOWNLOAD_DIR
from ekspl_lab02.going_through_links import DownloadPages

from ekspl_lab02.io_functions import write_dict_to_csv_file_in_download, write_text_to_file_in_download, \
                                     remove_download_directory, create_download_directory
from ekspl_lab02.similarity import jaccard_the_bests_results
from ekspl_lab02.ngrams import ContentReader, NGramsFinder, find_n_grams, count_n_grams

# checking arguments
if len(sys.argv) < 2:
    print("There is no html link!")
    exit(1)
elif len(sys.argv) < 3:
    print("We need max_n_gram number, suggest 3 or 2")
    exit(1)


html_link = sys.argv[1]
max_n_gram = int(sys.argv[2])

html_text = requests.get(html_link).text

remove_download_directory(download_dir=DOWNLOAD_DIR)
create_download_directory(download_dir=DOWNLOAD_DIR)

downloader = DownloadPages(DOWNLOAD_DIR)
links_discovered = downloader.go_to_links_with_depth(html_link, 1)

# links_discovered - dict with file_name and html_link
print(links_discovered)

# find all ngrams with duplicates
reader = ContentReader(DOWNLOAD_DIR)
files_content = reader.read_all_content_from_download()
print(files_content.keys())
ngrams_finder = NGramsFinder(1, max_n_gram)
# find ngrams in downloaded files
ngrams_in_files = find_n_grams(files_content, ngrams_finder)
# count them
file_name_and_ngrams_with_count = count_n_grams(ngrams_in_files)
# save in downloads (as 1.txt.csv)
for key, d in file_name_and_ngrams_with_count.items():
    print(key)
    print(d)
    write_dict_to_csv_file_in_download(d, key)

##### find 3 najbardziej podobne strony (adresy url) z bazy danych do strony podanej na wejsciu

# prepare dictionary from first link
ngrams_from_link = file_name_and_ngrams_with_count["1.txt"]
del file_name_and_ngrams_with_count["1.txt"]

### using Jaccard index
three_the_best_results = jaccard_the_bests_results(file_name_and_ngrams_with_count, ngrams_from_link, 3)
print(three_the_best_results)
result_to_save = ""
for file_name in three_the_best_results:
    result_to_save += links_discovered[file_name]
    result_to_save += "\n"

write_text_to_file_in_download(str(result_to_save), "jaccard_index_result.txt", FILE_PARENT_NAME)

### TODO: using bag of words

### TODO: using consine distance