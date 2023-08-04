import pandas as pd


# Pandas schema:
# Tweets = pd.DataFrame([], columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
# My solution:
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    df = df[['tweet_id']]
    return df


# LC solution:
def invalid_tweets_lc(tweets: pd.DataFrame) -> pd.DataFrame:
    is_valid = tweets['content'].str.len() > 15
    df = tweets[is_valid]
    return df[['tweet_id']]
