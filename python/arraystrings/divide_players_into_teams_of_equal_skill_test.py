from .divide_players_into_teams_of_equal_skill import Solution


def test_divide_players():
    assert Solution().dividePlayers(skill=[3, 2, 5, 1, 3, 4]) == 22
    assert Solution().dividePlayers(skill=[3, 4]) == 12
