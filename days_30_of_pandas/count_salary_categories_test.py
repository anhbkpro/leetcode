from .count_salary_categories import count_salary_categories
import pandas as pd


def test_count_salary_categories():
    # Input:
    # Accounts table:
    # +------------+--------+
    # | account_id | income |
    # +------------+--------+
    # | 3          | 108939 |
    # | 2          | 12747  |
    # | 8          | 87709  |
    # | 6          | 91796  |
    # +------------+--------+
    # Output:
    # +----------------+----------------+
    # | category       | accounts_count |
    # +----------------+----------------+
    # | Low Salary     | 1              |
    # | Average Salary | 0              |
    # | High Salary    | 3              |
    # +----------------+----------------+
    # Explanation:
    # Low Salary: Account 2.
    # Average Salary: No accounts.
    # High Salary: Accounts 3, 6, and 8.
    accounts = {
        "account_id": [3, 2, 8, 6],
        "income": [108939, 12747, 87709, 91796],
    }
    accounts = pd.DataFrame(accounts)
    expected = {
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": [1, 0, 3],
    }
    expected = pd.DataFrame(expected)
    assert count_salary_categories(accounts).equals(expected)
