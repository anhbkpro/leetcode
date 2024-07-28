from .second_minimum_time_to_reach_destination import Solution


def test_second_minimum():
    assert Solution().secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5) == 13
