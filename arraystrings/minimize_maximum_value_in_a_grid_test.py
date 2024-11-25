from .minimize_maximum_value_in_a_grid import Solution


def test_min_score():
    assert Solution().minScore(grid=[[3, 1], [2, 5]]) == [[2, 1], [1, 2]]
