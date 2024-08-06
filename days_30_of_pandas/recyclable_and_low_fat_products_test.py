from .recyclable_and_low_fat_products import find_products
import pandas as pd


def test_find_products():
    # Input:
    # Products table:
    # +-------------+----------+------------+
    # | product_id  | low_fats | recyclable |
    # +-------------+----------+------------+
    # | 0           | Y        | N          |
    # | 1           | Y        | Y          |
    # | 2           | N        | Y          |
    # | 3           | Y        | Y          |
    # | 4           | N        | N          |
    # +-------------+----------+------------+
    # Output:
    # +-------------+
    # | product_id  |
    # +-------------+
    # | 1           |
    # | 3           |
    # +-------------+
    products = {
        "product_id": [0, 1, 2, 3, 4],
        "low_fats": ["Y", "Y", "N", "Y", "N"],
        "recyclable": ["N", "Y", "Y", "Y", "N"],
    }
    products = pd.DataFrame(products)
    expected = {
        "product_id": [1, 3],
    }
    expected = pd.DataFrame(expected)
    assert (
        find_products(products)["product_id"].to_list()
        == expected["product_id"].to_list()
    )
