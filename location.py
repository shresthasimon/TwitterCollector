import sys
from collections import Counter
import json

def get_location(tweet):
    user = tweet.get('user', {})
    location = user.get('location', [])
    return location

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        location = Counter()
        for line in f:
            tweet = json.loads(line)
            location_in_tweet = get_location(tweet)
            location.update([location_in_tweet])
        for location, count in location.most_common(10):
            print("{}: {}".format(location, count))