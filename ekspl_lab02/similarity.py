

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))


def jaccard_the_bests_results(file_name_and_ngrams_with_count, ngrams_from_link, n_bests=3):
    """
    :param file_name_and_ngrams_with_count: a dictionary with file name as a key and other dictionary as a value -
                                            ngrams with number how many it is in the file
    :param ngrams_from_link: a dictionary with ngrams as a key and number of this ngrams
    :param n_bests: how many bests links we want to get
    :return:
    """
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
    n_the_best_results = list(jaccard_index_similarity_with_first_page_sorted.keys())[0:n_bests]
    print(n_the_best_results)
    return n_the_best_results
