import pandas as pd


# My solution
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
    return df.rename(columns={'subject_id': 'cnt'})


# LC solution
def count_unique_subjects_lc(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby(["teacher_id"])["subject_id"].nunique().reset_index()
    df = df.rename({'subject_id': "cnt"}, axis=1)
    return df
