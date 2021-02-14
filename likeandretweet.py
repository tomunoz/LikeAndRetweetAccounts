
import pandas as pd
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


def create_api():
    # credentials to login to twitter api
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    
    # create the api
    auth = tp.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tp.API(auth, wait_on_rate_limit=True)
    return api


# retrieve list of twitter accounts
def get_accounts():
    twitter_accounts = ""
    twitter_accounts = pd.read_csv("TwitterAccounts.csv")
    accounts = twitter_accounts.values.tolist()
    return accounts


# retrieve the last xx tweets for the twitter account
def get_latest_tweet(account, api):
    tweets = api.user_timeline(screen_name=account, count=60, include_rts = False, tweet_mode = 'extended')
    return tweets


# like the tweets that haven't been liked
def like_the_tweets(tweets, api):
    for tweet in reversed(tweets):
        tweet_status = api.get_status(tweet.id)
        liked = tweet_status.favorited
        if liked == False:
            try:
                api.create_favorite(tweet.id)
                print("Liked a tweet.")
            except:
                pass
    return


def main():
    while True:
        accounts = get_accounts()
        api = create_api()
        for account_to_like in accounts:
            tweets = get_latest_tweet(account_to_like[0], api)
            like_the_tweets(tweets, api)
        print("Starting new hour")
        #time.sleep(3600)
        break
    exit()


if __name__ == '__main__':
    main()