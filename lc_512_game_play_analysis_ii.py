import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    idx_first_event_date = activity.groupby('player_id')['event_date'].idxmin()
    return activity.loc[idx_first_event_date][['player_id', 'device_id']]
