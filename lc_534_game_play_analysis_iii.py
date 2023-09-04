import pandas as pd


def gameplay_analysis(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(by=["player_id", "event_date"])[["player_id", "event_date", "games_played"]]
    df["games_played_so_far"] = df.groupby("player_id")["games_played"].transform(pd.Series.cumsum)
    return df.drop(columns=["games_played"])
