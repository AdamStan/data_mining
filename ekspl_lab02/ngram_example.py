from sklearn.feature_extraction.text import CountVectorizer

text = "this is a foo bar sentences and i want to ngramize it, this is a foo"
vectorizer = CountVectorizer(ngram_range=(1, 3))
analyzer = vectorizer.build_analyzer()
print(analyzer(text))
