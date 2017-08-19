from nltk.tag import pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import re
from sentence import *
import _pickle as pickle

""" Returns an integer from 0-9 for the various classes
               Other : 0
        Cause-Effect : 1
     Component-Whole : 2
  Entity-Destination : 3
    Product-Producer : 4
       Entity-Origin : 5
   Member-Collection : 6
       Message-Topic : 7
   Content-Container : 8
   Instrument-Agency : 9
"""


def getClass(label):
    if label == 'Other':
        return 0
    elif label == 'Cause-Effect':
        return 1
    elif label == 'Component-Whole':
        return 2
    elif label == 'Entity-Destination':
        return 3
    elif label == 'Product-Producer':
        return 4
    elif label == 'Entity-Origin':
        return 5
    elif label == 'Member-Collection':
        return 6
    elif label == 'Message-Topic':
        return 7
    elif label == 'Contnen-Container':
        return 8
    elif label == 'Instrument-Agency':
        return 9


def readData():
    file = open("data/TRAIN_FILE.TXT", "r")
    data = file.readlines()
    labels = []  # labels will hold all the relations per sentence
    for i in range(1, len(data), 4):
        if 'Other' in data[i]:
            labels.append('Other')
        else:
            labels.append(re.findall(r'(.*?)\(', data[i])[0])
    class_labels = []  # Holds the labels after conversion to integers

    for label in labels:
        class_labels.append(getClass(label))

    sentences = []
    for line in data:
        if line[0].isdigit():
            sentences.append(line)
    nominals = []
    words_between_nominals = []
    word_prefixes = []
    pos_nominals = []
    pos_words = []
    stem_words = []
    stemmer = SnowballStemmer("english")
    for sent in sentences:
        e1 = re.findall(r'<e1>(.*?)<\/e1>', sent)[0]
        e2 = re.findall(r'<e2>(.*?)<\/e2>', sent)[0]
        words = re.search(r'</e1>(.*?)<e2>', sent).group(1).split()
        nominal_words = re.search(r'</e1>(.*?)<e2>', sent).group(1)
        nominals.append((e1, e2))
        e1_toks = word_tokenize(e1)
        e2_toks = word_tokenize(e2)
        pos_nominals.append((pos_tag(e1_toks)[0][1], pos_tag(e2_toks)[0][1]))
        nominal_words_toks = word_tokenize(nominal_words)
        pos_words.append(([i[1] for i in pos_tag(nominal_words_toks)]))
        stem_words.append([stemmer.stem(i) for i in nominal_words_toks])
        words_between_nominals.append((len(words)))
        prefixes = []
        for i in range(1, len(words) - 1):
            prefixes.append(words[i][:5])
        word_prefixes.append(prefixes)
    print(len(sentences), len(nominals))
    sent2 = []  # Sent2 holds all the clean sentences in double quotes
    for sent in sentences:
        sent2.append(re.findall(r'(\".*\")', sent)[0])
    sent = []
    for i in range(len(nominals)):
        sent.append(Sentence(nominals[i], sent2[i].split(),
                             words_between_nominals[i],
                             pos_nominals[i], pos_words[i], stem_words[i],class_labels[i]))
    pickle.dump(sent, open('data/cleaned.pkl', 'wb'), protocol=2)


readData()
