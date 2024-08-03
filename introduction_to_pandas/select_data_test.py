from .select_data import selectData
import pandas as pd

def test_select_data():
    # Example 1:
    # Input:
    # +------------+---------+-----+
    # | student_id | name    | age |
    # +------------+---------+-----+
    # | 101        | Ulysses | 13  |
    # | 53         | William | 10  |
    # | 128        | Henry   | 6   |
    # | 3          | Henry   | 11  |
    # +------------+---------+-----+
    # Output:
    # +---------+-----+
    # | name    | age |
    # +---------+-----+
    # | Ulysses | 13  |
    # +---------+-----+
    students = pd.DataFrame(
        [[101, "Ulysses", 13], [53, "William", 10], [128, "Henry", 6], [3, "Henry", 11]],
        columns=["student_id", "name", "age"],
    )
    students = selectData(students)
    assert students["name"].tolist() == ["Ulysses"]
    assert students["age"].tolist() == [13]
