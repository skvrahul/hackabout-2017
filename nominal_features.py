from nltk.corpus import wordnet as wn

"""
    NOTE: synsets 'pos' argument accepts only four possible attributes. 
    They are as follows:
        VERB
        NOUN
        ADV
        ADJ
    POS tags of the words have to be classified into the above categories
    before the functions can be used.
"""

"""
    Dictionary that stores POS of POS tags
"""
pos = {
        'JJ':'ADJ',
        'NN':'NOUN',
        'RB':'ADV',
        'VB':'VERB'
        }

"""
    hypernym takes input of a list containg (word,pos_tag) tuple pairs
    and return a list of hypernyms.
"""
def hypernym(words):
    hypernyms = []
    for word in words:
        arg = wn.synsets(word[0],pos=getattr(wn,pos[word[1][:2]]))[0]
        hypernyms.append(arg.hypernyms()[0].name().split('.')[0])
    return hypernyms

"""
    lowest_common_hypernym takes input a list containing the 
    [(nominal1,pos_tag),(nominal2,pos_tag)] tuple pairs and 
    returns lowest common hypernym.
"""
def lowest_common_hypernym(words):
    lch = []
    for word in words:
        arg_1 = wn.synsets(word[0][0],pos=getattr(wn,pos[word[0][1][:2]]))[0]
        arg_2 = wn.synsets(word[1][0],pos=getattr(wn,pos[word[1][1][:2]]))[0]
        lch.append(arg_1.lowest_common_hypernyms(arg_2)[0].name().split('.')[0])
    return lch
