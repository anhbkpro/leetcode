from .change_data_type import changeDatatype
import pandas as pd


def test_change_datatype():
    # Example 1:
    # Input:
    # DataFrame students:
    # +------------+------+-----+-------+
    # | student_id | name | age | grade |
    # +------------+------+-----+-------+
    # | 1          | Ava  | 6   | 73.0  |
    # | 2          | Kate | 15  | 87.0  |
    # +------------+------+-----+-------+
    # Output:
    # +------------+------+-----+-------+
    # | student_id | name | age | grade |
    # +------------+------+-----+-------+
    # | 1          | Ava  | 6   | 73    |
    # | 2          | Kate | 15  | 87    |
    # +------------+------+-----+-------+
    df = pd.DataFrame(
        {
            "student_id": [1, 2],
            "name": ["Ava", "Kate"],
            "age": [6, 15],
            "grade": [73.0, 87.0],
        }
    )
    assert changeDatatype(df).dtypes["grade"] == int
