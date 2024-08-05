from .drop_missing_data import dropMissingData
import pandas as pd


def test_drop_missing_data():
    # Input:
    # +------------+---------+-----+
    # | student_id | name    | age |
    # +------------+---------+-----+
    # | 32         | Piper   | 5   |
    # | 217        | None    | 19  |
    # | 779        | Georgia | 20  |
    # | 849        | Willow  | 14  |
    # +------------+---------+-----+
    # Output:
    # +------------+---------+-----+
    # | student_id | name    | age |
    # +------------+---------+-----+
    # | 32         | Piper   | 5   |
    # | 779        | Georgia | 20  |
    # | 849        | Willow  | 14  |
    # +------------+---------+-----+
    students = pd.DataFrame(
        [
            [32, "Piper", 5],
            [217, None, 19],
            [779, "Georgia", 20],
            [849, "Willow", 14],
        ],
        columns=["student_id", "name", "age"],
    )
    students = dropMissingData(students)
    assert students["name"].to_list() == ["Piper", "Georgia", "Willow"]
