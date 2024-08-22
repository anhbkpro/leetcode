from .second_highest_salary import second_highest_salary
import pandas as pd


def test_second_highest_salary():
    # Input:
    # Employee table:
    # +----+--------+
    # | id | salary |
    # +----+--------+
    # | 1  | 100    |
    # | 2  | 200    |
    # | 3  | 300    |
    # +----+--------+
    # Output:
    # +---------------------+
    # | SecondHighestSalary |
    # +---------------------+
    # | 200                 |
    # +---------------------+
    df = {
        "id": [1, 2, 3],
        "salary": [100, 200, 300],
    }
    df = pd.DataFrame(df)
    expected = {
        "SecondHighestSalary": [200],
    }
    expected = pd.DataFrame(expected)
    assert (
        second_highest_salary(df)["SecondHighestSalary"].to_list()
        == expected["SecondHighestSalary"].to_list()
    )
