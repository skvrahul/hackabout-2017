class Sentence:
	e1 = None
	e2 = None
	sentence = []
	nominal_distance = None
	pos_nominals = ()
	pos_words = ()
	stem_words = ()
	"""
	Constructor for the sentence datatype

	Args:
	    nominals: Tuple (e1, e2)
	    sentence: Array of strings representing the entire sentence
	    nominal_distance: Number of words between the nominals 
        pos_nominals: POS tags of nominals
        pos_words: POS tags of words between nominals
        stem_words: Stems of words between nominals

	Returns:
	    Returns a Sentence obj
	"""
	def __init__(self,nominals, sentence, nominal_distance,pos_nominals,pos_words,stem_words):
		self.e1=nominals[0]
		self.e2=nominals[1]
		self.sentence = sentence
		self.nominal_distance = nominal_distance
		self.pos_nominals = pos_nominals
		self.pos_words = pos_words
		self.stem_words = stem_words
	
	def get_nominals(self):
		return (self.e1,self.e2)
