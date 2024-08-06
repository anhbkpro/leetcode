from .article_views_i import article_views
import pandas as pd


def test_article_views():
    # Input:
    # Views table:
    # +------------+-----------+-----------+------------+
    # | article_id | author_id | viewer_id | view_date  |
    # +------------+-----------+-----------+------------+
    # | 1          | 3         | 5         | 2019-08-01 |
    # | 1          | 3         | 6         | 2019-08-02 |
    # | 2          | 7         | 7         | 2019-08-01 |
    # | 2          | 7         | 6         | 2019-08-02 |
    # | 4          | 7         | 1         | 2019-07-22 |
    # | 3          | 4         | 4         | 2019-07-21 |
    # | 3          | 4         | 4         | 2019-07-21 |
    # +------------+-----------+-----------+------------+
    # Output:
    # +------+
    # | id   |
    # +------+
    # | 4    |
    # | 7    |
    # +------+
    views = {
        "article_id": [1, 1, 2, 2, 4, 3, 3],
        "author_id": [3, 3, 7, 7, 7, 4, 4],
        "viewer_id": [5, 6, 7, 6, 1, 4, 4],
        "view_date": ["2019-08-01", "2019-08-02", "2019-08-01", "2019-08-02", "2019-07-22", "2019-07-21", "2019-07-21"],
    }
    views = pd.DataFrame(views)
    expected = {
        "id": [4, 7],
    }
    expected = pd.DataFrame(expected)
    assert (
        article_views(views)["id"].to_list()
        == expected["id"].to_list()
    )
