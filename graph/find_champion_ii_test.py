from .find_champion_ii import Solution


def test_find_champion_ii():
    assert Solution().findChampion(n=3, edges=[[0, 1], [1, 2]]) == 0
    assert Solution().findChampion(n=4, edges=[[0, 2], [1, 3], [1, 2]]) == -1
