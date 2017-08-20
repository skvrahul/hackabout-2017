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


Sent = pickle.load(open("data/cleaned.pkl", "rb"))
# print(Sent[0].create_feature_dict())

# Target
Y = np.empty([8000, 1])

# Features
X = np.empty([8000, 4])

# Order of features: (nominal_distance, pos_nominal, stem_word)


for s in Sent[]:
    np.append(Y, s.label)
    tmp_list = np.empty([4], dtype=object)
    tmp_list[0] = np.asarray(s.nominal_distance)
    # print(np.asarray(s.nominal_distance))
    tmp_list[1] = np.asarray(s.pos_nominals)
    # print(np.asarray(s.pos_nominals))
    tmp_list[2] = np.asarray(s.stem_words)
    # print(s.stem_words)
    tmp_list[3] = np.asarray(s.pos_words)
    # print(s.pos_words)
    np.append(X, tmp_list)
    # print(tmp_list)

print(X)

'''
clf = SVC(kernel='linear', C=1.5)
cv = ShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
scores = cross_val_score(clf, X, Y, cv=cv)
print(scores)
'''

#clf = SVC()
#clf.fit(X, Y)

'''
print(lowest_common_hypernym([(Sent[0].get_nominals()[0],
                               Sent[0].pos_nominals[0]),
                              (Sent[0].get_nominals()[1],
                               Sent[0].pos_nominals[1])]))
print(Sent[0].get_nominals()[0], Sent[0].pos_nominals[0])
'''
