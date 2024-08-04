from .create_a_new_column import createBonusColumn
import pandas as pd


def test_create_bonus_column():
    # Input:
    # DataFrame employees
    # +---------+--------+
    # | name    | salary |
    # +---------+--------+
    # | Piper   | 4548   |
    # | Grace   | 28150  |
    # | Georgia | 1103   |
    # | Willow  | 6593   |
    # | Finn    | 74576  |
    # | Thomas  | 24433  |
    # +---------+--------+
    # Output:
    # +---------+--------+--------+
    # | name    | salary | bonus  |
    # +---------+--------+--------+
    # | Piper   | 4548   | 9096   |
    # | Grace   | 28150  | 56300  |
    # | Georgia | 1103   | 2206   |
    # | Willow  | 6593   | 13186  |
    # | Finn    | 74576  | 149152 |
    # | Thomas  | 24433  | 48866  |
    # +---------+--------+--------+
    employees = pd.DataFrame(
        [
            ["Piper", 4548],
            ["Grace", 28150],
            ["Georgia", 1103],
            ["Willow", 6593],
            ["Finn", 74576],
            ["Thomas", 24433],
        ],
        columns=["name", "salary"],
    )
    employees = createBonusColumn(employees)
    assert employees["bonus"].tolist() == [9096, 56300, 2206, 13186, 149152, 48866]
