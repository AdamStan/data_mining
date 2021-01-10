import math


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))


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


def cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def cosine_the_best_results(file_name_and_ngrams_with_count, ngrams_from_link, n_bests=3):
    """
    :param file_name_and_ngrams_with_count: dictionary with file_name and nggrams dictionary
    :param ngrams_from_link: will be compared with dictionary of ngrams
    :param n_bests: from first parameter
    :return:
    """
    results_dict = dict()
    for file_name, dict_with_ngrams in file_name_and_ngrams_with_count.items():
        result = cosine_similarity(ngrams_from_link, dict_with_ngrams)
        results_dict[file_name] = result

    results_dict_sorted = {k: v for k, v in sorted(
        results_dict.items(), key=lambda item: item[1], reverse=True)}

    return list(results_dict_sorted.keys())[0:n_bests]

