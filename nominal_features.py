from nltk.corpus import wordnet as wn

"""
    NOTE: synsets 'pos' argument accepts only four possible attributes. They are as follows:
        VERB
        NOUN
        ADV
        ADJ
    POS tags of the words ave to be classified into the above categories before the function can be used.
"""


"""
    hypernym takes input of a list containg (word,pos_tag) tuple pairs and return list of hypernyms.
"""
def hypernym(words):
    hypernyms = []
    for word in words:
        arg = wn.synsets(word[0],pos=getattr(wn,word[1]))[0]
        hypernyms.append(arg.hypernyms()[0])
    return hypernyms

"""
    lowest_common_hypernym takes input a list containing the (nominal,pos_tag) tuple pairs and returns lowest common hypernym.
"""
def lowest_common_hypernym(words):
    lch = []
    arg_1 = wn.synsets(words[0][0],pos=getattr(wn,words[0][1]))[0]
    arg_2 = wn.synsets(words[1][0],pos=getattr(wn,words[1][1]))[0]
    lch.append(arg_1.lowest_common_hypernyms(arg_2)[0])
    return lch



