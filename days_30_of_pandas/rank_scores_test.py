from .rank_scores import order_scores
import pandas as pd


def test_order_scores():
    # Input:
    # Scores table:
    # +----+-------+
    # | id | score |
    # +----+-------+
    # | 1  | 3.50  |
    # | 2  | 3.65  |
    # | 3  | 4.00  |
    # | 4  | 3.85  |
    # | 5  | 4.00  |
    # | 6  | 3.65  |
    # +----+-------+
    # Output:
    # +-------+------+
    # | score | rank |
    # +-------+------+
    # | 4.00  | 1    |
    # | 4.00  | 1    |
    # | 3.85  | 2    |
    # | 3.65  | 3    |
    # | 3.65  | 3    |
    # | 3.50  | 4    |
    # +-------+------+
    scores = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6], "score": [3.5, 3.65, 4.0, 3.85, 4.0, 3.65]}
    )
    expected = pd.DataFrame(
        {"score": [4.0, 4.0, 3.85, 3.65, 3.65, 3.5], "rank": [1, 1, 2, 3, 3, 4]}
    )
    assert order_scores(scores)["score"].tolist() == expected["score"].tolist()
    assert order_scores(scores)["rank"].tolist() == expected["rank"].tolist()
