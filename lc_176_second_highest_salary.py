import pandas as pd


# My solution:
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    df.rename(columns={'salary': 'SecondHighestSalary'}, inplace=True)
    return df.sort_values('SecondHighestSalary', ascending=False).head(2).tail(1)
