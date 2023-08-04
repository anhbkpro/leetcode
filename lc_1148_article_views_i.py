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


# LC solution 2:
def article_views_lc2(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id and viewer_id are the same (authors viewing their own articles)
    authors_viewed_own_articles = views[views['author_id'] == views['viewer_id']]

    # Get unique author_ids from the filtered data
    unique_authors = authors_viewed_own_articles['author_id'].unique()

    # Sort the unique author_ids in ascending order
    unique_authors = sorted(unique_authors)

    # Create a DataFrame with the sorted unique author_ids and rename the 'author_id' column to 'id'
    result_df = pd.DataFrame({'id': unique_authors})

    return result_df
