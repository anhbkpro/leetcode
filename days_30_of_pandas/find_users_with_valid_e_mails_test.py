from .find_users_with_valid_e_mails import valid_emails
import pandas as pd


def test_valid_emails():
    # Input:
    # Users table:
    # +---------+-----------+-------------------------+
    # | user_id | name      | mail                    |
    # +---------+-----------+-------------------------+
    # | 1       | Winston   | winston@leetcode.com    |
    # | 2       | Jonathan  | jonathanisgreat         |
    # | 3       | Annabelle | bella-@leetcode.com     |
    # | 4       | Sally     | sally.come@leetcode.com |
    # | 5       | Marwan    | quarz#2020@leetcode.com |
    # | 6       | David     | david69@gmail.com       |
    # | 7       | Shapiro   | .shapo@leetcode.com     |
    # +---------+-----------+-------------------------+
    # Output:
    # +---------+-----------+-------------------------+
    # | user_id | name      | mail                    |
    # +---------+-----------+-------------------------+
    # | 1       | Winston   | winston@leetcode.com    |
    # | 3       | Annabelle | bella-@leetcode.com     |
    # | 4       | Sally     | sally.come@leetcode.com |
    # +---------+-----------+-------------------------+
    users = {
        "user_id": [1, 2, 3, 4, 5, 6, 7],
        "name": [
            "Winston",
            "Jonathan",
            "Annabelle",
            "Sally",
            "Marwan",
            "David",
            "Shapiro",
        ],
        "mail": [
            "winston@leetcode.com",
            "jonathanisgreat",
            "bella-@leetcode.com",
            "sally.come@leetcode.com",
            "quarz#2020@leetcode.com",
            "david69@gmail.com",
            ".shapo@leetcode.com",
        ],
    }
    users = pd.DataFrame(users)
    expected = {
        "user_id": [1, 3, 4],
        "name": ["Winston", "Annabelle", "Sally"],
        "mail": [
            "winston@leetcode.com",
            "bella-@leetcode.com",
            "sally.come@leetcode.com",
        ],
    }
    expected = pd.DataFrame(expected)
    assert valid_emails(users)["user_id"].to_list() == expected["user_id"].to_list()
    assert valid_emails(users)["name"].to_list() == expected["name"].to_list()
    assert valid_emails(users)["mail"].to_list() == expected["mail"].to_list()
