class Sentence:
	e1 = None
	e2 = None
	sentence = []
	nominal_distance = None
	def __init__(self,nominals, sentence, nominal_distance):
		self.e1=nominals[0]
		self.e2=nominals[1]
		self.sentence = sentence
		self.nominal_distance = nominal_distance
	
	def get_nominals(self):
		return (self.e1,self.e2)
