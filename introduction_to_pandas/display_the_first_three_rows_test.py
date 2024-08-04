from .display_the_first_three_rows import selectFirstRows
import pandas as pd


def test_select_first_rows():
    # DataFrame employees
    # +-------------+-----------+-----------------------+--------+
    # | employee_id | name      | department            | salary |
    # +-------------+-----------+-----------------------+--------+
    # | 3           | Bob       | Operations            | 48675  |
    # | 90          | Alice     | Sales                 | 11096  |
    # | 9           | Tatiana   | Engineering           | 33805  |
    # | 60          | Annabelle | InformationTechnology | 37678  |
    # | 49          | Jonathan  | HumanResources        | 23793  |
    # | 43          | Khaled    | Administration        | 40454  |
    # +-------------+-----------+-----------------------+--------+
    employees = pd.DataFrame(
        [
            [3, "Bob", "Operations", 48675],
            [90, "Alice", "Sales", 11096],
            [9, "Tatiana", "Engineering", 33805],
            [60, "Annabelle", "InformationTechnology", 37678],
            [49, "Jonathan", "HumanResources", 23793],
            [43, "Khaled", "Administration", 40454],
        ],
        columns=["employee_id", "name", "department", "salary"],
    )
    result = selectFirstRows(employees)
    expected = pd.DataFrame(
        [
            [3, "Bob", "Operations", 48675],
            [90, "Alice", "Sales", 11096],
            [9, "Tatiana", "Engineering", 33805],
        ],
        columns=["employee_id", "name", "department", "salary"],
    )
    assert result.equals(expected)
