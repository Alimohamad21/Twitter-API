import json
import sys

import tweepy

user = input('Please enter the twitter account username:')
data = json.load(open('D:\passwords.json'))
auth = tweepy.OAuthHandler(data['API_key'], data['API_secret_key'])
auth.set_access_token(data['access_token'], data['access_token_secret'])
api = tweepy.API(auth)
try:
    user_timeline = api.user_timeline(user, include_rts=False, count=2000, exclude_replies=True)
except:
    print('Invalid username')
    sys.exit(1)
total_likes = 0
total_rts = 0
tweets_count = len(user_timeline)
for tweet in user_timeline:
    total_likes += tweet.favorite_count
    total_rts += tweet.retweet_count

print(f'average likes per tweet:{round(total_likes / tweets_count)}')
print(f'average retweets per tweet:{round(total_rts / tweets_count)}')
