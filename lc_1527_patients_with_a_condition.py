import pandas as pd


def filter_patient(conditions):
    for condition in conditions.split(' '):
        if condition.startswith('DIAB1'):
            return True
    return False


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients[patients['conditions'].apply(filter_patient)]
    return patients
