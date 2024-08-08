from .fix_names_in_a_table import fix_names
import pandas as pd


def test_fix_names():
    # Input:
    # Users table:
    # +---------+-------+
    # | user_id | name  |
    # +---------+-------+
    # | 1       | aLice |
    # | 2       | bOB   |
    # +---------+-------+
    # Output:
    # +---------+-------+
    # | user_id | name  |
    # +---------+-------+
    # | 1       | Alice |
    # | 2       | Bob   |
    # +---------+-------+
    users = {
        "user_id": [1, 2],
        "name": ["aLice", "bOB"],
    }
    users = pd.DataFrame(users)
    expected = {
        "user_id": [1, 2],
        "name": ["Alice", "Bob"],
    }
    expected = pd.DataFrame(expected)
    assert fix_names(users)["user_id"].to_list() == expected["user_id"].to_list()
    assert fix_names(users)["name"].to_list() == expected["name"].to_list()
