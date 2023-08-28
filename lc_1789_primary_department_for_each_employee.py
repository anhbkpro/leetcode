import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # create additional column counting number of departments employee is in
    employee['d_cnt'] = employee.groupby(['employee_id']).department_id.transform('count')
    # filter rows which are with primary flag, or those who have only one department.
    employee = employee.query("(primary_flag == 'Y') | (d_cnt == 1)").iloc[:, [0, 1]]
    return employee
