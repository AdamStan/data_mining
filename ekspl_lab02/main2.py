import sys
import requests

from download import FILE_PARENT_NAME, DOWNLOAD_DIR

from io_functions import remove_download_directory, create_download_directory
from going_through_links import DownloadPages

from ekspl_lab02.io_functions import write_dict_to_csv_file_in_download, write_text_to_file_in_download
from ekspl_lab02.jaccard_index import jaccard_similarity
from ekspl_lab02.ngrams import ContentReader, NGramsFinder

html_link = sys.argv[1]

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
ngrams_finder = NGramsFinder(1, 3)
ngrams_in_files = dict()
for file_name, text in files_content.items():
    ngrams_in_file = ngrams_finder.find_n_grams_in_text(text)
    print(ngrams_in_file)
    ngrams_in_files[file_name] = ngrams_in_file

# count them
file_name_and_ngrams_with_count = dict()
for key, ngrams_list in ngrams_in_files.items():
    number_of_ngrams = dict()
    for item in ngrams_list:
        if item not in number_of_ngrams.keys():
            number_of_ngrams[item] = 1
        else:
            number_of_ngrams[item] += 1
    file_name_and_ngrams_with_count[key] = number_of_ngrams

# save in downloads (as 1.txt.csv)
for key, d in file_name_and_ngrams_with_count.items():
    print(key)
    print(d)
    write_dict_to_csv_file_in_download(d, key)

# find 3 najbardziej podobne strony (adresy url) z bazy danych do strony podanej na wejsciu

ngrams_from_link = file_name_and_ngrams_with_count["1.txt"]
print("ngrams dict from first link")
print(ngrams_from_link)

del file_name_and_ngrams_with_count["1.txt"]
print(file_name_and_ngrams_with_count.keys())

### using Jaccard index
jaccard_index_similarity_with_first_page = dict()
for key, dict_with_ngrams in file_name_and_ngrams_with_count.items():
    just_ngrams = dict_with_ngrams.keys()
    jaccard_index_similarity_with_first_page[key] = jaccard_similarity(ngrams_from_link.keys(), just_ngrams)

print(jaccard_index_similarity_with_first_page)
# sorting by values

jaccard_index_similarity_with_first_page_sorted = {k: v for k, v in sorted(
    jaccard_index_similarity_with_first_page.items(), key=lambda item: item[1], reverse=True)}
print(jaccard_index_similarity_with_first_page_sorted)
# three the best pages - save result to file
three_the_best_results = list(jaccard_index_similarity_with_first_page_sorted.keys())[0:3]
print(three_the_best_results)

result_to_save = ""
for file_name in three_the_best_results:
    result_to_save += links_discovered[file_name]
    result_to_save += "\n"

write_text_to_file_in_download(str(result_to_save), "jaccard_index_result.txt", FILE_PARENT_NAME)

### TODO: using bag of words

### TODO: using consine distance