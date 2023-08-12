import pandas as pd


def sort_table(olympic: pd.DataFrame) -> pd.DataFrame:
    olympic.sort_values(['country'], inplace=True)
    olympic.sort_values(['gold_medals', 'silver_medals', 'bronze_medals'], ascending=False, inplace=True)
    return olympic
