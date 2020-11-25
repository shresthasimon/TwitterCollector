import sys
from collections import Counter
import json
import matplotlib.pyplot as plt

def get_links(tweet):
    entities = tweet.get('entities', {})
    links = entities.get('urls', [])
    return [tag['expanded_url'] for tag in links]

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        links = Counter()
        for line in f:
            tweet = json.loads(line)
            links_in_tweet = get_links(tweet)
            print(links_in_tweet)
            links.update(links_in_tweet)
        for tag, count in links.most_common(10):
            print("{}: {}".format(tag, count))