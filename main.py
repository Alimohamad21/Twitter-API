import json

import tweepy

data = json.load(open('D:\passwords.json'))
auth = tweepy.OAuthHandler(data['API_key'], data['API_secret_key'])
auth.set_access_token(data['access_token'], data['access_token_secret'])
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))
