import pandas as pd

# Table: Users
# +---------+-----------+
# | Column  | Type      |
# +---------+-----------+
# | user_id | int       |
# | name    | varchar   |
# +---------+-----------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
# Pandas Schema: Users = pd.DataFrame([], columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})


def format_name(name) -> str:
    return name.title()


# My solution:
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(format_name)
    return users.sort_values('user_id')


# LC Approach 1: Separating the first character from the rest
def fix_names_lc2(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str[0].str.upper() + users["name"].str[1:].str.lower()
    return users.sort_values("user_id")


# LC Approach 2: Using .title() str method
def fix_names_lc(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.title()
    return users.sort_values('user_id')
