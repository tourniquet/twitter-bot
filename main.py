import tweepy
from datetime import datetime
import time

from keys import api_key, api_secret, access_token, access_token_secret

auth = tweepy.OAuth1UserHandler(
  api_key, api_secret, access_token, access_token_secret
)


def tweet(api: tweepy.API, message: str):
  api.update_status(message)


while True:
  api = tweepy.API(auth)

  print(datetime.now().strftime('%I:%M %p, %A, %B %d, %Y'))

  if datetime.now().strftime('%I:%M') == '9:31':
    tweet(api, datetime.now().strftime('%I:%M, %A, %B %d, %Y'))

  time.sleep(60)
