from .calculate_special_bonus import calculate_special_bonus
import pandas as pd


def test_calculate_special_bonus():
    # Input:
    # Employees table:
    # +-------------+---------+--------+
    # | employee_id | name    | salary |
    # +-------------+---------+--------+
    # | 2           | Meir    | 3000   |
    # | 3           | Michael | 3800   |
    # | 7           | Addilyn | 7400   |
    # | 8           | Juan    | 6100   |
    # | 9           | Kannon  | 7700   |
    # +-------------+---------+--------+
    # Output:
    # +-------------+-------+
    # | employee_id | bonus |
    # +-------------+-------+
    # | 2           | 0     |
    # | 3           | 0     |
    # | 7           | 7400  |
    # | 8           | 0     |
    # | 9           | 7700  |
    # +-------------+-------+
    df = {
        "employee_id": [2, 3, 7, 8, 9],
        "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
        "salary": [3000, 3800, 7400, 6100, 7700],
    }
    df = pd.DataFrame(df)
    expected = {
        "employee_id": [2, 3, 7, 8, 9],
        "bonus": [0, 0, 7400, 0, 7700],
    }
    expected = pd.DataFrame(expected)
    assert (
        calculate_special_bonus(df)["employee_id"].to_list()
        == expected["employee_id"].to_list()
    )
    assert calculate_special_bonus(df)["bonus"].to_list() == expected["bonus"].to_list()
