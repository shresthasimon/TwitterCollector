from tweepy.streaming import StreamListener
from tweepy import Stream
from twitterconnect import getTwitterAuthentication
import sys
import string
import time

def format_filename(fname):
	return ''.join(convert_valid(char) for char in fname)

class Listener(StreamListener):

	def __init__(self,fname):
		safe_fname = format_filename(fname)
		self.outfile = "stream_%s.json1" % safe_fname

	def on_data(self,data):
		try:
			with open(self.outfile, 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			sys.stderr.write("error on_data: {}\n".format(e))
			time.sleep(5)
		return True

	def on_error(self,status):
		if status == 420:
			sys.stderr.write("Rate Limit was reached\n")
			return False
		else:
			sys.stderr.write("error {}\n".format(status))
			return True

def convert_valid(char):
	valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
	if char in valid_chars:
		return char
	else:
		return '_'

if __name__ == '__main__':
	query = sys.argv[1:]
	query_fname = ' '.join(query)
	auth = getTwitterAuthentication()
	twitter_stream = Stream(auth, Listener(query_fname))
	twitter_stream.filter(track=query, is_async=True)
