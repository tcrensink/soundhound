#!/usr/bin/env python3
"""
utility functions that may be of use for word frequency task.
"""

from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='all', shuffle=True, random_state=17)

def generate_text_files():
    """
    generates text files of the 20newsgroups contained in sklearn.
    """
    for j, text in enumerate(twenty_train.data):
        with open('../text_samples/article_' + str(j), 'w') as f:
            f.write(text)


def generate_frequency_dict():
    """
    creates frequency table based on total available newsgroup data.  It would be preferable to use one constructed from a general English corpus, but no such options was freely available.
    """
    for j, text in enumerate(twenty_train.data)
            cv = CountVectorizer(ngram_range=(1, 1), min_df=1)
            cv_fit = cv.fit_transform(text)
            terms = cv.get_feature_names()
            counts = cv_fit.toarray().reshape(-1).T
            self.count_dict = dict(zip(terms, counts))
