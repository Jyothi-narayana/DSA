from sets import Set
class WordList:
	"""Stores a list of words"""
	def __init__(self):
		"""Initializes a set to store the list of words"""
		self.words = Set()
	def addWord(self, word):
		"""Add a word to the word list"""
		self.words.add(word)
	def addWords(self, words):
		for w in words:
			self.addWord(w)
	def hasWord(self, word):
		"""Check if a word exists in a word list"""
		if (word in self.words):
			return True
		else:
			return False

wl = WordList()
wl.addWords(['hello', 'heard', 'heaven', 'hear', 'heed', 'heap', 'help', 'hipster'])
print 'hello exists: ', wl.hasWord('hello')
print 'hell exists: ', wl.hasWord('hell')
