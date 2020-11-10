import sys
from collections import Counter
import json

def get_lang(tweet):
    lang = tweet.get('lang', [])
    return lang

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        lang = Counter()
        for line in f:
            tweet = json.loads(line)
            lang_in_tweet = get_lang(tweet)
            lang.update([lang_in_tweet])
        for lang, count in lang.most_common(4):
            print("{}: {}".format(lang, count))