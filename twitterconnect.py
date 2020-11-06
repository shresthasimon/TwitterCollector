import os
import sys
from tweepy import API
from tweepy import OAuthHandler
def getTwitterAuthentication():
	try:
		consumerKey = os.environ['TWITTER_CONSUMER_KEY']
		consumerSecret = os.environ['TWITTER_CONSUMER_SECRET']
		accessToken = os.environ['TWITTER_ACCESS_TOKEN']
		accessSecret= os.environ['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("TWITTER_* environment variables not set\n")
		sys.exit(1)
	auth = OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessSecret)
	return auth

def getTwitterClient():
	auth = getTwitterAuthentication()
	client = API(auth)
	return client