from .customers_who_never_order import customers_who_never_order
import pandas as pd


def test_customers_who_never_order():
    # Input:
    # Customers table:
    # +----+-------+
    # | id | name  |
    # +----+-------+
    # | 1  | Joe   |
    # | 2  | Henry |
    # | 3  | Sam   |
    # | 4  | Max   |
    # +----+-------+
    # Orders table:
    # +----+------------+
    # | id | customerId |
    # +----+------------+
    # | 1  | 3          |
    # | 2  | 1          |
    # +----+------------+
    # Output:
    # +-----------+
    # | Customers |
    # +-----------+
    # | Henry     |
    # | Max       |
    # +-----------+
    customers = {
        "id": [1, 2, 3, 4],
        "name": ["Joe", "Henry", "Sam", "Max"],
    }
    customers = pd.DataFrame(customers)
    orders = {
        "id": [1, 2],
        "customerId": [3, 1],
    }
    orders = pd.DataFrame(orders)
    expected = {
        "Customers": ["Henry", "Max"],
    }
    expected = pd.DataFrame(expected)
    assert (
        customers_who_never_order(customers, orders)["Customers"].to_list()
        == expected["Customers"].to_list()
    )
