from .modify_columns import modifySalaryColumn


def test_modify_salary_column():
    import pandas as pd

    df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "salary": [100, 200, 300]})
    modified_df = modifySalaryColumn(df)
    assert modified_df["salary"].tolist() == [200, 400, 600]
