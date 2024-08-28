from .the_number_of_rich_customers import count_rich_customers
import pandas as pd


def test_count_rich_customers():
    # Input:
    # Store table:
    # +---------+-------------+--------+
    # | bill_id | customer_id | amount |
    # +---------+-------------+--------+
    # | 6       | 1           | 549    |
    # | 8       | 1           | 834    |
    # | 4       | 2           | 394    |
    # | 11      | 3           | 657    |
    # | 13      | 3           | 257    |
    # +---------+-------------+--------+
    # Output:
    # +------------+
    # | rich_count |
    # +------------+
    # | 2          |
    # +------------+
    store = pd.DataFrame(
        {
            "bill_id": [6, 8, 4, 11, 13],
            "customer_id": [1, 1, 2, 3, 3],
            "amount": [549, 834, 394, 657, 257],
        }
    )
    output = count_rich_customers(store)
    assert output.equals(pd.DataFrame({"rich_count": [2]}))
