from .drop_duplicate_rows import dropDuplicateEmails
import pandas as pd


def test_dropDuplicateEmails():
    # Input:
    # +-------------+---------+---------------------+
    # | customer_id | name    | email               |
    # +-------------+---------+---------------------+
    # | 1           | Ella    | emily@example.com   |
    # | 2           | David   | michael@example.com |
    # | 3           | Zachary | sarah@example.com   |
    # | 4           | Alice   | john@example.com    |
    # | 5           | Finn    | john@example.com    |
    # | 6           | Violet  | alice@example.com   |
    # +-------------+---------+---------------------+
    # Output:
    # +-------------+---------+---------------------+
    # | customer_id | name    | email               |
    # +-------------+---------+---------------------+
    # | 1           | Ella    | emily@example.com   |
    # | 2           | David   | michael@example.com |
    # | 3           | Zachary | sarah@example.com   |
    # | 4           | Alice   | john@example.com    |
    # | 6           | Violet  | alice@example.com   |
    # +-------------+---------+---------------------+
    customers = pd.DataFrame(
        [
            [1, "Ella", "emily@example.com"],
            [2, "David", "michael@example.com"],
            [3, "Zachary", "sarah@example.com"],
            [4, "Alice", "john@example.com"],
            [5, "Finn", "john@example.com"],
            [6, "Violet", "alice@example.com"],
        ],
        columns=["customer_id", "name", "email"],
    )
    customers = dropDuplicateEmails(customers)

    assert customers["email"].tolist() == [
        "emily@example.com",
        "michael@example.com",
        "sarah@example.com",
        "john@example.com",
        "alice@example.com",
    ]
