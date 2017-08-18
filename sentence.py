class Sentence:
	e1 = None
	e2 = None
	sentence = []
	nominal_distance = None
	def __init__(self):
		pass
	
	def __init__(self,(e1,e2), sentence):
		self.e1=e1
		self.e2=e2
		self.sentence = sentence

	def __init__(self,(e1,e2), sentence, nominal_distance):
		self.e1=e1
		self.e2=e2
		self.sentence = sentence
		self.nominal_distance = nominal_distance
	
	def get_nominals(self):
		return (e1,e2)
			