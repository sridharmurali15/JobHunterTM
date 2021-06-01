# consumer_key = 'iO931nW13fne1QKYueKFGbqnU'
# consumer_secret = 'fH0wBJyc8z4CZ38Nf2XoGwrgkjIoOpefDpmPoIr3fy37TdFx4W'
# access_token = 'c'
# access_token_secret = 'vtiF6hzAYQdWd0RA31NZeSyo9c0f6xOjnDgC1sd6hrFYL'

import tweepy
import logging
import os

# logger = logging.getLogger()

def CreateAPI():
    auth = tweepy.OAuthHandler('iO931nW13fne1QKYueKFGbqnU', 'fH0wBJyc8z4CZ38Nf2XoGwrgkjIoOpefDpmPoIr3fy37TdFx4W')
    auth.set_access_token('1328406620892581888-uYsX3aB7JRDLzhRqyeDnBmkmB3R4HN', 'vtiF6hzAYQdWd0RA31NZeSyo9c0f6xOjnDgC1sd6hrFYL')
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        # print(type(api))
        # print('API Verified')
    except Exception as e:
        # logger.error("Error creating API", exc_info=True)
        raise e
    # logger.info("API created")
    return api