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


# LC solution: Using Regular Expressions
def valid_emails_lc(users: pd.DataFrame) -> pd.DataFrame:
    # Note how we use a raw string (putting an `r` in front) to avoid having to escape the backslash
    # Also note that we escaped the `@` character, as it has a special meaning in some regex flavors
    # 1. ^: This represents the start of a string or line.
    # 2. [a-z]: This represents a character range, matching any character from a to z.
    #   2.1 [0-9]: This represents a character range, matching any character from 0 to 9.
    #   2.2 [a-zA-Z]: This variant matches any character from a to z or A to Z. Note that there is no limit to
    #       the number of character ranges you can specify inside the square brackets -- you can add additional
    #       characters or ranges you want to match.
    #   2.3 [^a-z]: This variant matches any character that is not from a to z. Note that the ^ character
    #       is used to negate the character range, which means it has a different meaning inside the square brackets
    #       than outside where it means the start.
    # 3. [a-z]*: This represents a character range, matching any character from a to z zero or more times.
    # 4. [a-z]+: This represents a character range, matching any character from a to z one or more times.
    # 5. .: This matches exactly one of any character.
    # 6. \.: This represents a period character. Note that the backslash is used to escape the period character,
    #       as the period character has a special meaning in regular expressions.
    #       Also note that in many languages, you need to escape the backslash itself, so you need to use \\..
    # 7. $: This represents the end of a string or line.

    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]
