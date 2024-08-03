from .create_a_dataframe_from_list import createDataframe
import pandas as pd


def test_create_dataframe():
    result_df = createDataframe([[1, 20], [2, 21], [3, 22]])
    expected_df = pd.DataFrame(
        [[1, 20], [2, 21], [3, 22]], columns=["student_id", "age"]
    )
    assert result_df.equals(expected_df)
