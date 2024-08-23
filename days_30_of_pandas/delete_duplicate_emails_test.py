from .delete_duplicate_emails import delete_duplicate_emails
import pandas as pd


def test_delete_duplicate_emails():
    # Input:
    # Person table:
    # +----+------------------+
    # | id | email            |
    # +----+------------------+
    # | 1  | john@example.com |
    # | 2  | bob@example.com  |
    # | 3  | john@example.com |
    # +----+------------------+
    # Output:
    # +----+------------------+
    # | id | email            |
    # +----+------------------+
    # | 1  | john@example.com |
    # | 2  | bob@example.com  |
    # +----+------------------+
    person = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "email": ["john@example.com", "bob@example.com", "john@example.com"],
        }
    )
    delete_duplicate_emails(person)
    expected = pd.DataFrame(
        {"id": [1, 2], "email": ["john@example.com", "bob@example.com"]}
    )
    assert person["id"].tolist() == expected["id"].tolist()
    assert person["email"].tolist() == expected["email"].tolist()
