import re


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
    for sentence in sentences:
        e1 = re.findall(r'<e1>(.*?)<\/e1>', sentence)[0]
        e2 = re.findall(r'<e2>(.*?)<\/e2>', sentence)[0]
        words = re.findall(r'<e1>(.*?)<\/e2>', sentence)[0].split()
        nominals.append((e1, e2))
        words_between_nominals.append((len(words) - 2))
        prefixes = []
        for i in range(1, len(words) - 1):
            prefixes.append(words[i][:5])
        word_prefixes.append(prefixes)
    print(len(sentences), len(nominals), word_prefixes[:5])


readData()
