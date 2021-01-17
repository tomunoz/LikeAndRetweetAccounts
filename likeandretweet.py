import tweepy as tp
from datetime import date
import time
import os
from os import environ

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from collections import Counter
import sys

# credentials to login to twitter api
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']

ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tp.API(auth, wait_on_rate_limit=True)

#def get_target(account):
    #user_account = api.get_user(account)
    #print("name: " + user_account.name)
    #print("screen_name: " + user_account.screen_name)
    #print("description: " + user_account.description)
    #print("statuses_count: " + str(user_account.statuses_count))
    #print("friends_count: " + str(user_account.friends_count))
    #print("followers_count: " + str(user_account.followers_count))
    #print("\n")

def get_latest_tweet(account):
    tweets = api.user_timeline(screen_name=account,
                           # 200 is the maximum allowed count
                           count=60,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    #for item in tweets:
    #    print("ID: {}".format(item.id))
    #    print(item.created_at)
    #    print(item.full_text)
    #    print("\n")
    return tweets

def like_the_tweets(tweets):
    for tweet in tweets:
        tweet_status = api.get_status(tweet.id)
        liked = tweet_status.favorited
        if liked == False:
            try:
                api.create_favorite(tweet.id)
                #print("ID: {}".format(tweet.id))
                #print(tweet.full_text)
                #print("\n")
            except:
                pass
                #print("couldn't like the tweet ", tweet.id)
        #else:
            #print("Tweet already like ", tweet.id)
    return


def main():
    account_to_like = "TriangleUlty"
    #get_target(account_to_like)
    while True:
        tweets = get_latest_tweet(account_to_like)
        like_the_tweets(tweets)
        print("Starting new minujte")
        time.sleep(3600)


if __name__ == '__main__':
    main()