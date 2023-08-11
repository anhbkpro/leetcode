import pandas as pd


# My solution
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    groups = employees.merge(employee_uni, how='left', on='id')
    return groups[['unique_id', 'name']]
