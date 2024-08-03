from .get_the_size_of_a_dataframe import getDataframeSize
import pandas as pd


def test_get_dataframe_size():
    players = pd.DataFrame(
        [[1, "John", 20], [2, "Doe", 21], [3, "Jane", 22]],
        columns=["player_id", "player_name", "player_age"],
    )
    result = getDataframeSize(players)
    assert result == [3, 3]
