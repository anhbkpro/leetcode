import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return (views.groupby(['viewer_id', 'view_date'])  # 1 grouping by user and date
            .nunique()  # 2 counting unique articles
            .query("article_id > 1")  # 3 if any user had more than 1 article per day: count > 1
            .reset_index()['viewer_id']  # 4 resetting index and selecting viewers
            .drop_duplicates()  # 5 dropping duplicates because one reader could have more than 1 article in multiple
            # days
            .to_frame('id'))  # 6 returning renamed frame
