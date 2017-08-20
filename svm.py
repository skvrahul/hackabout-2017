import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import _pickle as pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from nominal_features import *
from sklearn.feature_extraction import DictVectorizer
from sentence import *
from sklearn.feature_extraction.text import CountVectorizer


Sent = pickle.load(open("data/cleaned.pkl", "rb"))
# print(Sent[0].create_feature_dict())

# Target
Y = np.empty((0, 100))

# Features

# Order of features: (nominal_distance, pos_nominal, stem_word)

vectorizer = CountVectorizer()
corpus = []
pos_corpus = []
for s in Sent:
    np.append()
    corpus.append(s.sentence)
    pos_corpus.append(" ".join(str(x) for x in s.pos_words))

sentences = vectorizer.fit_transform(corpus)
vec_sentences = sentences.toarray()  # Vectors of all the sentences in the corpus

pos_words = vectorizer.fit_transform(pos_corpus)
vec_pos_words = pos_words.toarray()  # Vectors of all pos tags in corpus


'''
clf = SVC(kernel='linear', C=1.5)
cv = ShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
scores = cross_val_score(clf, X, Y, cv=cv)
print(scores)
'''

clf = SVC()
clf.fit(X, Y)


print(lowest_common_hypernym([(Sent[1].get_nominals()[1],
                               Sent[1].pos_nominals[1]),
                              (Sent[1].get_nominals()[1],
                               Sent[1].pos_nominals[1])]))
print(Sent[1].get_nominals()[1], Sent[1].pos_nominals[1])
