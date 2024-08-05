from .fill_missing_data import fillMissingValues
import pandas as pd


def test_fill_missing_values():
    # Example 1:
    # Input:+-----------------+----------+-------+
    # | name            | quantity | price |
    # +-----------------+----------+-------+
    # | Wristwatch      | None     | 135   |
    # | WirelessEarbuds | None     | 821   |
    # | GolfClubs       | 779      | 9319  |
    # | Printer         | 849      | 3051  |
    # +-----------------+----------+-------+
    # Output:
    # +-----------------+----------+-------+
    # | name            | quantity | price |
    # +-----------------+----------+-------+
    # | Wristwatch      | 0        | 135   |
    # | WirelessEarbuds | 0        | 821   |
    # | GolfClubs       | 779      | 9319  |
    # | Printer         | 849      | 3051  |
    # +-----------------+----------+-------+
    products = pd.DataFrame(
        {
            "name": ["Wristwatch", "WirelessEarbuds", "GolfClubs", "Printer"],
            "quantity": [None, None, 779, 849],
            "price": [135, 821, 9319, 3051],
        }
    )
    assert fillMissingValues(products)["quantity"].tolist() == [0, 0, 779, 849]
