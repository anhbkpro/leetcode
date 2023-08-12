import pandas as pd


# My solution
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee, on=['id', 'managerId'], how='left')
    grouped = df.groupby('managerId').size().reset_index(name='count')
    grouped = grouped[grouped['count'] >= 5]
    employee = employee[employee['id'].isin(grouped['managerId'])]
    return employee[['name']]
