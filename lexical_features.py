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
    for sent in sentences:
        e1 = re.findall(r'<e1>(.*?)<\/e1>', sent)[0]
        e2 = re.findall(r'<e2>(.*?)<\/e2>', sent)[0]
        words = re.findall(r'<e1>(.*?)<\/e2>', sent)[0].split()
        nominals.append((e1, e2))
        words_between_nominals.append((len(words) - 2))
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
                             words_between_nominals))
    pickle.dump(sent, open('data/cleaned.pkl', 'wb'), protocol=2)


readData()
