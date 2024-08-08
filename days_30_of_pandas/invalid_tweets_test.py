from .invalid_tweets import invalid_tweets
import pandas as pd


def test_invalid_tweets():
    # Input:
    # Tweets table:
    # +----------+----------------------------------+
    # | tweet_id | content                          |
    # +----------+----------------------------------+
    # | 1        | Vote for Biden                   |
    # | 2        | Let us make America great again! |
    # +----------+----------------------------------+
    # Output:
    # +----------+
    # | tweet_id |
    # +----------+
    # | 2        |
    # +----------+
    # Explanation:
    # Tweet 1 has length = 14. It is a valid tweet.
    # Tweet 2 has length = 32. It is an invalid tweet.
    tweets = {
        "tweet_id": [1, 2],
        "content": ["Vote for Biden", "Let us make America great again!"],
    }
    tweets = pd.DataFrame(tweets)
    expected = {
        "tweet_id": [2],
    }
    expected = pd.DataFrame(expected)
    assert (
        invalid_tweets(tweets)["tweet_id"].to_list() == expected["tweet_id"].to_list()
    )
