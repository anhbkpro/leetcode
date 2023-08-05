import pandas as pd


# Table Users:
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains information of the users signed up in a website. Some e-mails are invalid.

# My solution:
def validate_email(email):
    if email is None:
        return False
    if not email[0].isalpha():
        return False
    if not email.endswith('@leetcode.com'):
        return False
    sub = email[:-len('@leetcode.com')]
    for c in sub:
        if not c.isalpha() and not c.isdigit() and c not in ['_', '.', '-']:
            return False

    return True


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users = users[users['mail'].apply(validate_email)]
    return users
