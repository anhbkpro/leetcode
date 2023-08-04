import pandas as pd


# Pandas schema:
# Views = pd.DataFrame([], columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({
# 'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})
# My solution:
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["author_id"] == views["viewer_id"]]
    df = df[["author_id"]].drop_duplicates().rename(columns={"author_id": "id"}).sort_values("id")
    return df


# LC solution:
def article_views_lc(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]

    df.drop_duplicates(subset=['author_id'], inplace=True)
    df.sort_values(by=['author_id'], inplace=True)
    df.rename(columns={'author_id': 'id'}, inplace=True)

    df = df[['id']]

    return df
