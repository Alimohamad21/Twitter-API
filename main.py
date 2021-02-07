import json
import sys

import tweepy

data = json.load(open('D:\passwords.json'))
auth = tweepy.OAuthHandler(data['API_key'], data['API_secret_key'])
auth.set_access_token(data['access_token'], data['access_token_secret'])
api = tweepy.API(auth)


class Stats:
    def __init__(self, username):
        self.username = username
        self.total_likes = 0
        self.total_rts = 0
        self.average_likes = 0
        self.average_retweets = 0
        self.user_timeline = api.user_timeline(self.username, include_rts=False, count=200, exclude_replies=True)
        self.total_tweets = len(self.user_timeline)
        self.followers = api.followers(user, count=200)
        self.counted_stats = False

    def count_average_retweets_and_likes(self):
        if self.total_tweets == 0 or self.counted_stats:
            return
        for tweet in self.user_timeline:
            self.total_rts += tweet.retweet_count
            self.total_likes += tweet.favorite_count
        self.counted_stats = True
        self.average_likes = round(self.total_likes / self.total_tweets)
        self.average_retweets = round(self.total_rts / self.total_tweets)

    def print_stats(self):
        if not self.counted_stats:
            self.count_average_retweets_and_likes()
        print(f'{self.username} average likes per tweet:{self.average_likes}')
        print(f'{self.username} average retweets per tweet:{self.average_retweets}')


user = input('Please enter the twitter account username:')
s = Stats(user)
users = []
s.print_stats()
users.append(s)
followers = s.followers
for follower in followers:
    try:
        f = Stats(follower.screen_name)
        f.count_average_retweets_and_likes()
        users.append(f)
    except:
        continue
users.sort(key=lambda x: x.average_likes, reverse=True)
print(f"\n\nTop 3 average likes in {user}'s followers: ")
for i in range(3):
    print(f'{i+1}-')
    users[i].print_stats()
print(f'\n\n{user} average likes rank among their followers:{users.index(s)+1}')
users.sort(key=lambda x: x.average_retweets, reverse=True)
print(f"\n\nTop 3 average rts in {user}'s followers: ")
for i in range(3):
    print(f'{i+1}-')
    users[i].print_stats()
print(f'\n\n{user} average rts rank among their followers:{users.index(s)+1}')
