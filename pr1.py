import re
import io
from nltk import word_tokenize, pos_tag, ne_chunk

class character(object):
	def __init__(self, index):
		self.number = 1
		self.locations = [index]

	def getNumber(self):
		return self.number

	def addNumber(self):
		self.number += 1

	def addLocation(self, index):
		self.locations.append(index)

	def getLocations(self):
		return map(str, self.locations)

source = io.open("book1.txt", mode="r", encoding="utf-8")
text = source.read()

delimiters = '|'.join(['\n', ' ', ',', '\.', '!', '\?', ':', ';'])
tokens = [s for s in list(re.split(delimiters, text)) if s.isalpha()]
tagged_words = pos_tag(tokens)

chunked_tree = ne_chunk(tagged_words)
person_chunks = [chunk for chunk in chunked_tree.subtrees() if chunk.label() == 'PERSON']
person_entities = [' '.join(c[0].lower() for c in entity) for entity in person_chunks]

names = {}
for index, t in enumerate(person_entities):
	if t in names:
		curr_charcter = names[t]
		curr_charcter.addNumber()
		curr_charcter.addLocation(index)
	else:
		names[t] = character(index)

output = io.open("results.txt", mode="w+", encoding="utf-8")
for k in sorted(list(names), key=lambda x: names[x].getNumber(), reverse=True)[:10]:
	output.write("Entity: %s\n" % k)
	output.write("Appeared: %s\n" % unicode(names[k].getNumber()))
	output.write("Locations: %s\n" % unicode(', '.join(names[k].getLocations())))
	output.write(unicode('='*20+'\n'))