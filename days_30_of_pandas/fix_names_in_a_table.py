import pandas as pd


def format_name(name) -> str:
    return name.capitalize()


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(format_name)
    return users.sort_values("user_id")
