from .department_highest_salary import department_highest_salary
import pandas as pd


def test_department_highest_salary():
    # Input:
    # Employee table:
    # +----+-------+--------+--------------+
    # | id | name  | salary | departmentId |
    # +----+-------+--------+--------------+
    # | 1  | Joe   | 70000  | 1            |
    # | 2  | Jim   | 90000  | 1            |
    # | 3  | Henry | 80000  | 2            |
    # | 4  | Sam   | 60000  | 2            |
    # | 5  | Max   | 90000  | 1            |
    # +----+-------+--------+--------------+
    # Department table:
    # +----+-------+
    # | id | name  |
    # +----+-------+
    # | 1  | IT    |
    # | 2  | Sales |
    # +----+-------+
    # Output:
    # +------------+----------+--------+
    # | Department | Employee | Salary |
    # +------------+----------+--------+
    # | IT         | Jim      | 90000  |
    # | Sales      | Henry    | 80000  |
    # | IT         | Max      | 90000  |
    # +------------+----------+--------+
    employee = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
            "salary": [70000, 90000, 80000, 60000, 90000],
            "departmentId": [1, 1, 2, 2, 1],
        }
    )
    department = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})
    expected_output = pd.DataFrame(
        {
            "Department": ["IT", "Sales", "IT"],
            "Employee": ["Jim", "Henry", "Max"],
            "Salary": [90000, 80000, 90000],
        }
    )
    output = department_highest_salary(employee, department)
    assert output["Department"].to_list() == expected_output["Department"].to_list()
    assert output["Employee"].to_list() == expected_output["Employee"].to_list()
    assert output["Salary"].to_list() == expected_output["Salary"].to_list()
