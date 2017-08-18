from nltk.tag import pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import re
from sentence import *
import _pickle as pickle


def readData():
    file = open("data/TRAIN_FILE.TXT", "r")
    data = file.readlines()
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
        nominal_words = re.search(r'</e1>(.*?)<e2>',sent).group(1)
        nominals.append((e1, e2))
        e1_toks = word_tokenize(e1)
        e2_toks = word_tokenize(e2)
        pos_nominals.append((pos_tag(e1_toks)[0][1],pos_tag(e2_toks)[0][1]))
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
                             words_between_nominals[i],pos_nominals[i],pos_words[i],stem_words[i]))
    pickle.dump(sent, open('data/cleaned.pkl', 'wb'), protocol=2)


readData()
