import nltk
import re, string
from nltk.corpus import stopwords
from nltk.util import ngrams




sentenceTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
with open('goldenglobes.tab', 'r') as f:
	tweet_text = f.readlines()
tweet_text = [x.strip() for x in tweet_text]

new_tweets = []

from nltk.tokenize import TreebankWordTokenizer
wordTokenizer = TreebankWordTokenizer()


num_best_dressed = 3
bigram_regex = "([A-Z][a-z]+\s[A-Z][-'a-zA-Z]+)"


word = ["dress","dressed", "party", "parties"]
count = 0
file = open("newfile.txt", "w")
for t in tweet_text:
	letters = t.lower()
	for w in word:
		if (w in letters):
			new_tweets.append(t)
			token = re.sub(r'[^a-zA-Z0-9 ]',r'',t)
			file.write(token)
			file.write("\n")
			count += 1
file.close()

def bestDressed():
    # This function will find the best dressed celebrities of the show.
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        keywords = ["dressed", "dress", "gorgeous", "stunning", "beautiful", "gorgeous"]
        for w in keywords:
            if w in tt:
                possible_winners = possible_winners + re.findall(bigram_regex, tweet)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    results.pop("Best Dressed")
    results.pop("Worst Dressed")

    i = 0
    best_dressed = list()
    while results and (i < num_best_dressed):
        each = max(results, key = results.get);
        best_dressed.append(each);
        results.pop(each);
        i += 1
    return best_dressed

def worstDressed():
    # This function will find the best dressed celebrities of the show.
    results = dict()
    for tweet in new_tweets:
        possible_winners = list()
        tt = tweet.lower()
        keywords = ["dressed", "dress", "horrible", "ugly", "disaster", "hideous", "trainwreck"]
        for w in keywords:
            if w in tt:
                possible_winners = possible_winners + re.findall(bigram_regex, tweet)
        for r in possible_winners:
            if r in results:
                results[r] += 1
            else:
                results[r] = 1
    results.pop("Golden Globes")
    results.pop("Worst Dressed")
    results.pop("Best Dressed")    
    i = 0
    best_dressed = list()
    while results and (i < num_best_dressed):
        each = max(results, key = results.get);
        best_dressed.append(each);
        results.pop(each);
        i += 1
    return best_dressed

def main():
    bDressed = bestDressed()
    wDressed = worstDressed()
    print "Best Dressed: "
    for each in bDressed:
        print(str(each))
    print "Worst Dressed: "
    for each in wDressed:
    	print(str(each))


if __name__ == '__main__':
	main()
