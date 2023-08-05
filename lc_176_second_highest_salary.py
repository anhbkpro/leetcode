import numpy as np
import pandas as pd


# My solution:
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    df.rename(columns={'salary': 'SecondHighestSalary'}, inplace=True)
    return df.sort_values('SecondHighestSalary', ascending=False).head(2).tail(1)


# LC solution:
def second_highest_salary_lc(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. drop any duplicate salaries.
    employee = employee.drop_duplicates(["salary"])

    # 2. If there are less than two unique salaries, return `np.NaN`.
    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})

    # 3. Sort the table by `salary` in descending order.
    employee = employee.sort_values("salary", ascending=False)

    # 4. Drop the `id` column.
    employee.drop("id", axis=1, inplace=True)

    # 5. Rename the `salary` column.
    employee.rename({"salary": "SecondHighestSalary"}, axis=1, inplace=True)

    # 6, 7. Return the second-highest salary.
    return employee.head(2).tail(1)
