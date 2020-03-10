#!/usr/bin/python3

from collections import defaultdict, Counter

# Counter is a dictionary where all keys are defined
# and have default value 0
langs = Counter()
print('langs["example"]=',langs["example"])

hashtags = Counter()
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#covid19'] += 1
print('hashtags=',hashtags)

# defaultdict lets us specify what we want the
# default value to be for keyss that don't exist

hashtags = defaultdict(lambda: 0)
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#coronavirus'] += 1
hashtags['#covid19'] += 1
print('hashtags=',hashtags)


for tweet in tweets:
    if '#coronavirus' in tweet:
        hashtags['#coronavirus'] += 1
    for each hashtag in tweet:
        hashtags[hashtag] += 1
