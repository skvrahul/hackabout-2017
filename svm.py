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
FEATURE_LEN = 1800

Sent = pickle.load(open("data/cleaned.pkl", "rb"))
# print(Sent[0].create_feature_dict())

# Target


# Features

# Order of features: (nominal_distance, pos_nominal, stem_word)

vectorizer = CountVectorizer()
corpus = []
pos_corpus = []
for s in Sent:
    corpus.append(s.sentence)
    pos_corpus.append(" ".join(str(x) for x in s.pos_words))

sentences = vectorizer.fit_transform(corpus)
vec_sentences = sentences.toarray()  # Vectors of all the sentences in the corpus

pos_words = vectorizer.fit_transform(pos_corpus)
vec_pos_words = pos_words.toarray()  # Vectors of all pos tags in corpus

X = None
Y = np.empty(8000)
i = 0
print(np.shape(vec_sentences))
print(np.shape(vec_pos_words))
X = np.append(vec_sentences, vec_pos_words, axis=1)
for i, s in enumerate(Sent):
    Y[i] = s.label
print(X.shape)
print(Y.shape)

X = X[:FEATURE_LEN]
Y = Y[:FEATURE_LEN]

clf = SVC(kernel='linear', C=1.5, verbose=True)
cv = ShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
scores = cross_val_score(clf, X, Y, cv=cv)
print(scores)
print('IsFinite:', np.isfinite(Y).all())
print('isnull:', np.isnan(Y).any().any())
# clf = SVC(verbose=True)
# clf.fit(X, Y)

hypernyms = []
'''
for s in Sent[:3]:
    hypernyms.append(lowest_common_hypernym([(s.get_nominals()[1],
                                              s.pos_nominals[1]),
                                             (s.get_nominals()[1],
                                              s.pos_nominals[1])]))
print(Sent[1].get_nominals()[1], Sent[1].pos_nominals[1])
print(hypernyms[:10])
'''
