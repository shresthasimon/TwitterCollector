import sys
from collections import Counter
import json
import matplotlib.pyplot as plt

def get_mentions(tweet):
    entities = tweet.get('entities', {})
    mentions = entities.get('user_mentions', [])
    return [tag['screen_name'].lower() for tag in mentions]

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        mentions = Counter()
        for line in f:
            tweet = json.loads(line)
            mentions_in_tweet = get_mentions(tweet)
            mentions.update(mentions_in_tweet)
        for tag, count in mentions.most_common(10):
            print("{}: {}".format(tag, count))
