import pandas as pd


# My solution
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].size().reset_index()
    return df[df['timestamp'] >= 3].drop('timestamp', axis=1)


# LC solution
def actors_and_directors_lc(actor_director: pd.DataFrame) -> pd.DataFrame:
    cnts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
    return cnts[cnts['counts'] >= 3][['actor_id', 'director_id']]
