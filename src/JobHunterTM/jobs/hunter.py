import tweepy as tw
import json
import pandas as pd
from .config_api import CreateAPI
import sys
import re
import json


## Define the search term and the date_since date as variables
# search_words_1 = "hiring+jobs+machine+learning-filter:retweets"
# search_words_2 = "hiring+jobs+artificial+intelligence-filter:retweets"
# data+machine+learning+artificial+intelligence+ds+ml+computer+vision+nlp -filter:retweets"
# date_since = "2021-01-01"

# filters = {
#     "date": "2021-01-01",
#     "ml": "hiring+jobs+machine+learning-filter:retweets",
#     "ai": "hiring+jobs+artificial+intelligence-filter:retweets",
#     "ds": "hiring+jobs+data+science-filter:retweets",
#     "cv": "hiring+jobs+computer+vision-filter:retweets",
#     "nlp": "hiring+jobs+nlp-filter:retweets"
# }

class JobHunterTM:

    def __init__(self, date):
        self.api = CreateAPI()
        self.date = date
        print("hunter initiated")

    def GetTweets(self, search_words):
        # Search in Twitter
        print("hunter search begin")
        tweets = tw.Cursor(self.api.search,
                    q=search_words,
                    lang="en",
                    since=self.date).items(50)
        # Save data in df
        op = [[tweet.text, str(tweet.created_at.date()), tweet.user.location, tweet.user.screen_name, tweet.favorite_count, tweet.retweet_count] for tweet in tweets]
        df = pd.DataFrame(op, columns=['Tweet', 'Date', 'Location', 'User', 'Likes', 'Retweet'])
        # extract URLs from tweet
        urlRe = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = []
        tweet_text = []
        for tt in df["Tweet"]:
            url = re.findall(urlRe, tt)
            for u in url:
                tt = tt.replace(u,'')
            urls.append(url)
            tweet_text.append(tt)
        df['Tweet'] = tweet_text
        df['URLs'] = urls
        # remove posts with 0 likes and 0 retweets
        df = df[(df['Likes']>0) | (df['Retweet']>0)]
        return df

# def __main__():
#     with open('filter.json', 'r') as j:
#         filters= json.loads(j.read())
#     api = CreateAPI()
#     hunter = JobHunterTM(api, filters)
#     hunter.GetTweets(filters['cv'])
    
# if __name__ =="__main__":
#     __main__()