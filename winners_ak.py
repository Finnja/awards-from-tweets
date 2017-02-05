import csv
import nltk
import string

def keywords_and_nominees(n):
	"""returns lists of award keywords and nominees for each award"""
	if n == 1:
		kw = ['best', 'television', 'series', 'drama']
		nominees = ['the crown', 'game of thrones', 'stranger things', 'this is us', 'westworld']

	elif n == 2:
		kw = ['actor', 'best', 'performance', 'television', 'drama']
		nominees = ['billy bob thornton', 'rami malek', 'bob odenkirk', 'matthew rhys', 'liev schreiber']

	elif n == 3:
		kw = ['actress', 'best', 'performance', 'television', 'drama']
		nominees = ['claire foy', 'caitriona balfe', 'keri russell', 'winona ryder', 'evan rachel wood']

	elif n == 4:
		kw = ['best', 'television', 'series', 'musical', 'comedy']
		nominees = ['atlanta', 'black-ish', 'mozart in the jungle', 'transparent', 'veep']

	elif n == 5:
		kw = ['television', 'motion', 'picture', 'limited', 'series']
		nominees = ['oj simpson', 'american crime', 'the dresser', 'the night manager', 'the night of']

	elif n == 6:
		kw = ['actress', 'television', 'motion', 'picture', 'limited', 'series']
		nominees = ['sarah paulson', 'riley keough', 'charlotte rampling', 'kerry washington', 'felicity huffman']
	
	return kw, nominees

def keyword_search(kwList, tweet):
	"""checks to see if all keywords in a list present in a string""" 
	for kw in kwList:
		if kw not in tweet:
			return False

	return True 

if __name__ == '__main__':

	# empty list
	L = []

	award = 1

	keywords, noms = keywords_and_nominees(award)

	
	with open("goldenglobes.tab") as tsv:
		for line in csv.reader(tsv, delimiter='\t'):
			if len(line):
				L.append(line[0].lower().translate(None, string.punctuation))

		# list of tweets that contain all keywords
		matches = [x for x in L if keyword_search(keywords, x)]

	# makes dict w keys = nominees, vals = 0
	d = dict((key, value) for (key, value) in zip(noms, [0]*5))

	# increment nominee value every time they are mentioned
	for match in matches:
		for key in d.keys():
			if key in match:
				d[key] += 1

	print(d)

	# sort
	print(max(d.iterkeys(), key=(lambda k: d[k])))
