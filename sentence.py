class Sentence:
	e1 = None
	e2 = None
	sentence = []
	nominal_distance = None
	pos_nominals = ()
	pos_words = ()
	stem_words = ()
	label= None
	"""
	Constructor for the sentence datatype

	Args:
	    nominals: Tuple (e1, e2)
	    sentence: Array of strings representing the entire sentence
	    nominal_distance: Number of words between the nominals 
        pos_nominals: POS tags of nominals
        pos_words: POS tags of words between nominals
        stem_words: Stems of words between nominals
        label: Target label for the sentence

	Returns:
	    Returns a Sentence obj
	"""
	def __init__(self,nominals, sentence, nominal_distance,pos_nominals,pos_words,stem_words,label):
		self.e1=nominals[0]
		self.e2=nominals[1]
		self.sentence = sentence
		self.nominal_distance = nominal_distance
		self.pos_nominals = pos_nominals
		self.pos_words = pos_words
		self.stem_words = stem_words
		self.label
	
	def get_nominals(self):
		return (self.e1,self.e2)

	def create_feature_dict(self):
			feature_dict = {'e1':self.e1, 'e2':self.e2}
			feature_dict.update({'words:'+sentence_word:True for sentence_word in self.sentence})
			feature_dict.update({'nom_dist':nominal_distance})
			feature_dict.update({'nom_pos:'+pos_nominal for pos_nominal in pos_nominals})
			feature_dict.update({'words_pos:'+pos_word for pos_word in pos_words})
			feature_dict.update({'words_stem:'+stem_word for stem_word in stem_words})
			print feature_set
