from .rename_columns import renameColumns
import pandas as pd


def test_rename_columns():
    assert renameColumns(
        pd.DataFrame(
            {
                "id": [1, 2, 3],
                "first": ["Alice", "Bob", "Charlie"],
                "last": ["Smith", "Jones", "Brown"],
                "age": [25, 30, 35],
            }
        )
    ).columns.tolist() == ["student_id", "first_name", "last_name", "age_in_years"]
