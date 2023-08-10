import pandas as pd


# My solution
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    return df[df['student'] >= 5].drop(['student'], axis=1)
