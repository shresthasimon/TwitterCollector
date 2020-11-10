import sys 
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

def process_text(text, tokenizer=TweetTokenizer(), stopwords=[]):
	text = text.lower()
	tokens = tokenizer.tokenize(text)
	return [token for token in tokens if token not in stopwords and not token.isdigit()]

if __name__ == '__main__':
	fname = sys.argv[1]
	tweet_tokenizer = TweetTokenizer()
	punctuation = list(string.punctuation)
	stopword_list = stopwords.words('english') + punctuation + ['rt', 'via', '...']

	words = Counter()
	with open(fname, 'r') as file:
		for line in file:
			tweet = json.loads(line)
			tokens = process_text(text=tweet['text'], tokenizer=tweet_tokenizer, stopwords=stopword_list)
			words.update(tokens)
		for tag, count in words.most_common(20):
			print("{}: {}".format(tag, count))