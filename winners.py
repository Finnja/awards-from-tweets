# 5 Feb 2017
# EECS 337 - NLP
# Assignment 2: Part 1 (golden globe winners) 
# Group 9 - Alex Kaldjian, Jiahui Li, John Garbuzinksi, Madhab Ghei

import csv
from nltk.corpus import stopwords
import string

def award_info(n):
	"""returns lists of award titles, keywords, and nominees for each award"""

	if n == 1:
		title = 'Best Motion Picture - Drama'
		nominees = ['moonlight', 'hell or high water', 'lion', 'manchester by the sea', 'hacksaw ridge']

	elif n == 2:
		title = 'Best Motion Picture - Musical or Comedy'
		nominees = ['la la land', '20th century women', 'deadpool', 'florence foster jenkins', 'sing street']	

	elif n == 3:
		title = 'Best Performance by an Actress in a Motion Picture - Drama'
		nominees = ['isabelle huppert', 'amy adams', 'jessica chastain', 'ruth negga', 'natalie portman']

	elif n == 4:
		title = 'Best Performance by an Actor in a Motion Picture - Drama'
		nominees = ['casey affleck', 'joel edgerton', 'andrew garfield', 'viggo mortensen', 'denzel washington']

	elif n == 5:
		title = 'Best Performance by an Actress in a Motion Picture - Musical or Comedy'
		nominees = ['emma stone', 'annette bening', 'lily collins', 'hailee steinfeld', 'meryl streep']

	elif n == 6:
		title = 'Best Performance by an Actor in a Motion Picture - Musical or Comedy'
		nominees = ['ryan gosling', 'colin farrell', 'hugh grant', 'jonah hill', 'ryan reynolds']

	elif n == 7:
		title = 'Best Performance by an Actress in a Supporting Role in any Motion Picture'
		nominees = ['viola davis', 'naomie harris', 'nicole kidman', 'octavia spencer', 'michelle williams']

	elif n == 8:
		title = 'Best Performance by an Actor in a Supporting Role in any Motion Picture'
		nominees = ['aaron taylorjohnson', 'mahershala ali', 'jeff bridges', 'simon helberg', 'dev patel']

	elif n == 9:
		title = 'Best Director - Motion Picture'
		nominees = ['damien chazelle', 'tom ford', 'mel gibson', 'barry jenkins', 'kenneth lonergan']

	elif n == 10:
		title = 'Best Screenplay - Motion Picture'
		nominees = ['damien chazelle', 'tom ford', 'taylor sheridan', 'barry jenkins', 'kenneth lonergan']

	elif n == 11:
		title = 'Best Motion Picture - Animated'
		nominees = ['zootopia', 'moana', 'my life as a zucchini', 'sing', 'kubo and the two strings']

	elif n == 12:
		title = 'Best Motion Picture - Foreign Language'
		nominees = ['elle', 'divines', 'neruda', 'the salesman', 'toni erdmann']

	elif n == 13:
		title = 'Best Original Score - Motion Picture'
		nominees = ['justin hurwitz', 'nicholas britell', 'johann johannsson', 'dustin ohalloran', 'hans zimmer']

	elif n == 14:
		title = 'Best Original Song - Motion Picture'
		nominees = ['city of stars', 'cant stop the feeling', 'faith', 'gold ', 'how far ill go']

	elif n == 15:
		title = 'Best Television Series - Drama'
		nominees = ['the crown', 'game of thrones', 'stranger things', 'this is us', 'westworld']

	elif n == 16:
		title = 'Best Television Series - Musical or Comedy'
		nominees = ['atlanta', 'black-ish', 'mozart in the jungle', 'transparent', 'veep']

	elif n == 17:
		title = 'Best Television Limited Series or Motion Picture Made for Television'
		nominees = ['oj simpson', 'american crime', 'the dresser', 'the night manager', 'the night of']

	elif n == 18:
		title = 'Best Performance by an Actress in a Limited Series or a Motion Picture Made for Television'
		nominees = ['sarah paulson', 'riley keough', 'charlotte rampling', 'kerry washington', 'felicity huffman']

	elif n == 19:
		title = 'Best Performance by an Actor in a Limited Series or a Motion Picture Made for Television'
		nominees = ['tom hiddleston', 'riz ahmed', 'bryan cranston', 'john turturro', 'courtney vance']

	elif n == 20:
		title = 'Best Performance by an Actress In A Television Series - Drama'
		nominees = ['claire foy', 'caitriona balfe', 'keri russell', 'winona ryder', 'evan rachel wood']

	elif n == 21:
		title = 'Best Performance by an Actor In A Television Series - Drama'
		nominees = ['billy bob thornton', 'rami malek', 'bob odenkirk', 'matthew rhys', 'liev schreiber']

	elif n == 22:
		title = 'Best Performance by an Actress in a Television Series - Musical or Comedy'
		nominees = ['tracee ellis ross', 'rachel bloom', 'julia louisdreyfus', 'sarah jessica parker', 'issa rae']
	
	elif n == 23:
		title = 'Best Performance by an Actor in a Television Series - Musical or Comedy'
		nominees = ['donald glover', 'anthony anderson', 'gael garcia bernal', 'nick nolte', 'jeffrey tambor']

	elif n == 24:
		title = 'Best Performance by an Actress in a Supporting Role in a Motion Picture Made for TV'
		nominees = ['olivia colman', 'lena headey', 'chrissy metz', 'mandy moore', 'thandie newton']
	
	elif n == 25:
		title = 'Best Performance by an Actor in a Supporting Role in a Motion Picture Made for TV'
		nominees = ['hugh laurie', 'sterling brown', 'john lithgow', 'christian slater', 'john travolta']

	
	stop = set(stopwords.words('english'))
	title_parse = title.lower().translate(None, string.punctuation).split()
	kw = [i for i in title_parse if i not in stop]

	return title, kw, nominees


def keyword_search(kwList, tweet):
	"""checks to see if all item in a list present in a string""" 
	for kw in kwList:
		if kw not in tweet:
			return False

	return True 


def run():
	L = []
	with open("goldenglobes.tab") as tsv:
			for line in csv.reader(tsv, delimiter='\t'):
				if len(line):
					L.append(line[0].lower().translate(None, string.punctuation))

	for i in range(25):
		award = i + 1

		title, keywords, noms = award_info(award)

		# list of tweets that contain all keywords
		matches = [x for x in L if keyword_search(keywords, x)]

		# makes dict w keys = nominees, vals = 0
		d = dict((key, value) for (key, value) in zip(noms, [0]*5))

		# increment corresponding value every time nominee is mentioned
		for match in matches:
			for key in d.keys():
				if key in match:
					d[key] += 1

		# sort by mentions
		winner = max(d.iterkeys(), key=(lambda k: d[k]))

		
		print('Award: ' + title)
		print('Winner: ' + winner + '\n')

if __name__ == '__main__':
	run()
	

