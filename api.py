import os
import twitter

TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']

TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = ['TWITTER_TOKEN_SECRET']

TWITTER_APP_NAME = os.environ.get('TWITTER_APP_NAME')
# Getting an error that this is an invalid token. When I change which constants are strings,
# the API throws a "characters cannot be escaped" error.
api = twitter.Api(consumer_key='TWITTER_CONSUMER_KEY',
                      consumer_secret='TWITTER_CONSUMER_SECRET',
                      access_token_key='TWITTER_ACCESS_TOKEN',
                      access_token_secret='TWITTER_ACCESS_TOKEN_SECRET')
                      
def send_to_twitter(text):
    api.PostUpdate(text)
    return "Tweet posted!"
    # except:
#         print "Something went wrong sending that. :( "
#         return "Something went wrong sending that. :( "