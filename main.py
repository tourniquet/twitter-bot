import tweepy
from keys import api_key, api_secret, access_token, access_token_secret

def api():
  auth = tweepy.OAuthHandler(api_key, api_secret)
  auth.set_access_token(access_token, access_token_secret)

  return tweepy.API(auth)


def tweet(api: tweepy.API, message: str):
  api.update_status(message)


if __name__ == '__main__':
  api = api()
  tweet(api, 'This was tweeted from Python')
