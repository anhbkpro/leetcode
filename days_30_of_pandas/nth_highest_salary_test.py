from .nth_highest_salary import nth_highest_salary
import pandas as pd


def test_nth_highest_salary():
    # Input:
    # Employee table:
    # +----+--------+
    # | id | salary |
    # +----+--------+
    # | 1  | 100    |
    # | 2  | 200    |
    # | 3  | 300    |
    # +----+--------+
    # n = 2
    # Output:
    # +------------------------+
    # | getNthHighestSalary(2) |
    # +------------------------+
    # | 200                    |
    # +------------------------+
    df = {
        "id": [1, 2, 3],
        "salary": [100, 200, 300],
    }
    df = pd.DataFrame(df)
    expected = {
        "getNthHighestSalary(2)": [200],
    }
    expected = pd.DataFrame(expected)
    assert (
        nth_highest_salary(df, 2)["getNthHighestSalary(2)"].to_list()
        == expected["getNthHighestSalary(2)"].to_list()
    )
