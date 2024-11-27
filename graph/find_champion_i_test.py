from .find_champion_i import Solution


def test_find_champion_i():
    assert Solution().findChampion(grid=[[0, 1], [0, 0]]) == 0
    assert Solution().findChampion(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]]) == 1
