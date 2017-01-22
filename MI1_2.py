from sets import Set
class WordList:
	"""Stores a list of words"""
	def __init__(self):
		"""Initializes a set to store the list of words"""
		self.trie = {}
	def addWord(self, word):
		"""Add a word to the word list"""
		temp_trie = self.trie
		for letter in word:
			temp_trie = temp_trie.setdefault(letter, {})
		temp_trie = temp_trie.setdefault('_end_', '_end_')
		self.temp_trie = temp_trie
	def addWords(self, words):
		for w in words:
			self.addWord(w)
	def printWordList(self):
		print self.trie
	def hasWord(self, word):
		"""Check if a word exists in a word list"""
		temp_trie = self.trie
		for letter in word:
			if letter not in temp_trie:
				return False
			temp_trie = temp_trie[letter]
		# word exits only if I have reached the end of the word
		return '_end_' in temp_trie.keys()
	def wordSuggestions(self, word):
		"""finds suggestions which are one letter different form the current word of the same length from the dictionary"""
		suggestions = []
		letters = ['h', 'e', 'a', 'v', 'r', 'd', 'n', 'l', 'o', 'p'] # consider only there letters in the alphabet
		# for each position of the letter, replace with another letter from the alphabet and check for it's existance
		for i in range(len(word)):
			for l in letters:
				if (l != word[i]):
					p_suggestion = word[0:i] + l + word[i+1:]
					if (self.hasWord(p_suggestion)):
						suggestions.append(p_suggestion)
		return suggestions
			

wl = WordList()
wl.addWords(['hello', 'heard', 'heaven', 'hear', 'heed', 'heap', 'help'])
wl.printWordList()
print 'hello exists: ', wl.hasWord('hello')
print 'hell exists: ', wl.hasWord('hell')
print 'suggestions for heep: ', wl.wordSuggestions("heep")