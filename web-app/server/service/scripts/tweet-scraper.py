from twitter_scraper import get_tweets
import sys
import re

def get_username(url):
  return url.split('twitter.com/')[1].split('/')[0]

def get_tweetId(url):
  return url.split(get_username(url))[1].split('/')[2]

def clean_tweet(tw):
  return [' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tw).split())]

def get_tweet(url):
  username = get_username(url)
  tweetId = get_tweetId(url)

  tweets = get_tweets(username)
  for t in tweets:
    if (t['tweetId'] == tweetId):
      print(clean_tweet(t['text']))
      sys.stdout.flush()
      break

if __name__ == '__main__':
  get_tweet(sys.argv[1])
