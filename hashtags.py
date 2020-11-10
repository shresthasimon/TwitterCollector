import sys
from collections import Counter
import json
import matplotlib.pyplot as plt

def get_hashtags(tweet):
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])
    return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        hashtags = Counter()
        for line in f:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hashtags.update(hashtags_in_tweet)
        for tag, count in hashtags.most_common(10):
            print("{}: {}".format(tag, count))

y = [count for tag, count in hashtags.most_common(10)]
x = range(1, len(y)+1)

plt.bar(x,y)
plt.title("Hashtag Frequencies")
plt.ylabel("Frequency")
plt.savefig('test.png')