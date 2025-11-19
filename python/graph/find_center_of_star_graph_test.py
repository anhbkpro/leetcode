from .find_center_of_star_graph import Solution


def test_find_center():
    assert Solution().findCenter([[1, 2], [2, 3], [4, 2]]) == 2
    assert Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
