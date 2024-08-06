from .reshape_data_melt import meltTable
import pandas as pd


def test_melt_table():
    # Input:
    # +-------------+-----------+-----------+-----------+-----------+
    # | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
    # +-------------+-----------+-----------+-----------+-----------+
    # | Umbrella    | 417       | 224       | 379       | 611       |
    # | SleepingBag | 800       | 936       | 93        | 875       |
    # +-------------+-----------+-----------+-----------+-----------+
    # Output:
    # +-------------+-----------+-------+
    # | product     | quarter   | sales |
    # +-------------+-----------+-------+
    # | Umbrella    | quarter_1 | 417   |
    # | SleepingBag | quarter_1 | 800   |
    # | Umbrella    | quarter_2 | 224   |
    # | SleepingBag | quarter_2 | 936   |
    # | Umbrella    | quarter_3 | 379   |
    # | SleepingBag | quarter_3 | 93    |
    # | Umbrella    | quarter_4 | 611   |
    # | SleepingBag | quarter_4 | 875   |
    # +-------------+-----------+-------+
    report = pd.DataFrame(
        {
            "product": ["Umbrella", "SleepingBag"],
            "quarter_1": [417, 800],
            "quarter_2": [224, 936],
            "quarter_3": [379, 93],
            "quarter_4": [611, 875],
        }
    )
    ans = meltTable(report)
    expected = pd.DataFrame(
        {
            "product": ["Umbrella", "SleepingBag", "Umbrella", "SleepingBag", "Umbrella", "SleepingBag", "Umbrella", "SleepingBag"],
            "quarter": ["quarter_1", "quarter_1", "quarter_2", "quarter_2", "quarter_3", "quarter_3", "quarter_4", "quarter_4"],
            "sales": [417, 800, 224, 936, 379, 93, 611, 875],
        }
    )
    assert ans.equals(expected)
