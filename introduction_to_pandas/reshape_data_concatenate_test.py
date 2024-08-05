from .reshape_data_concatenate import concatenateTables
import pandas as pd


def test_concatenate_tables():
    # Input:
    # df1
    # +------------+---------+-----+
    # | student_id | name    | age |
    # +------------+---------+-----+
    # | 1          | Mason   | 8   |
    # | 2          | Ava     | 6   |
    # | 3          | Taylor  | 15  |
    # | 4          | Georgia | 17  |
    # +------------+---------+-----+
    # df2
    # +------------+------+-----+
    # | student_id | name | age |
    # +------------+------+-----+
    # | 5          | Leo  | 7   |
    # | 6          | Alex | 7   |
    # +------------+------+-----+
    # Output:
    # +------------+---------+-----+
    # | student_id | name    | age |
    # +------------+---------+-----+
    # | 1          | Mason   | 8   |
    # | 2          | Ava     | 6   |
    # | 3          | Taylor  | 15  |
    # | 4          | Georgia | 17  |
    # | 5          | Leo     | 7   |
    # | 6          | Alex    | 7   |
    # +------------+---------+-----+
    df1 = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4],
            "name": ["Mason", "Ava", "Taylor", "Georgia"],
            "age": [8, 6, 15, 17],
        }
    )
    df2 = pd.DataFrame(
        {
            "student_id": [5, 6],
            "name": ["Leo", "Alex"],
            "age": [7, 7],
        }
    )
    result_df = concatenateTables(df1, df2)
    expected_df = pd.DataFrame(
        {
            "student_id": [1, 2, 3, 4, 5, 6],
            "name": ["Mason", "Ava", "Taylor", "Georgia", "Leo", "Alex"],
            "age": [8, 6, 15, 17, 7, 7],
        }
    )
    assert result_df["student_id"].tolist() == expected_df["student_id"].tolist()
    assert result_df["name"].tolist() == expected_df["name"].tolist()
    assert result_df["age"].tolist() == expected_df["age"].tolist()
