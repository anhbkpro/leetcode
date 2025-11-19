from .two_best_non_overlapping_events import Solution


def test_max_two_events():
    assert Solution().maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [2, 4, 3]]) == 4
    assert Solution().maxTwoEvents(events=[[1, 3, 2], [4, 5, 2], [1, 5, 5]]) == 5
    assert Solution().maxTwoEvents(events=[[1, 5, 3], [1, 5, 1], [6, 6, 5]]) == 8
