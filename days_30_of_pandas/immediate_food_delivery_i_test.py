from .immediate_food_delivery_i import food_delivery
import pandas as pd


def test_food_delivery():
    # Input:
    # Delivery table:
    # +-------------+-------------+------------+-----------------------------+
    # | delivery_id | customer_id | order_date | customer_pref_delivery_date |
    # +-------------+-------------+------------+-----------------------------+
    # | 1           | 1           | 2019-08-01 | 2019-08-02                  |
    # | 2           | 5           | 2019-08-02 | 2019-08-02                  |
    # | 3           | 1           | 2019-08-11 | 2019-08-11                  |
    # | 4           | 3           | 2019-08-24 | 2019-08-26                  |
    # | 5           | 4           | 2019-08-21 | 2019-08-22                  |
    # | 6           | 2           | 2019-08-11 | 2019-08-13                  |
    # +-------------+-------------+------------+-----------------------------+
    # Output:
    # +----------------------+
    # | immediate_percentage |
    # +----------------------+
    # | 33.33                |
    # +----------------------+
    delivery = {
        "delivery_id": [1, 2, 3, 4, 5, 6],
        "customer_id": [1, 5, 1, 3, 4, 2],
        "order_date": [
            "2019-08-01",
            "2019-08-02",
            "2019-08-11",
            "2019-08-24",
            "2019-08-21",
            "2019-08-11",
        ],
        "customer_pref_delivery_date": [
            "2019-08-02",
            "2019-08-02",
            "2019-08-11",
            "2019-08-26",
            "2019-08-22",
            "2019-08-13",
        ],
    }
    delivery = pd.DataFrame(delivery)
    expected = {"immediate_percentage": [33.33]}
    expected = pd.DataFrame(expected)
    assert food_delivery(delivery).equals(expected)
