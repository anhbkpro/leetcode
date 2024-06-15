from .merge_intervals import Solution


def test_merge():
    assert Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert Solution().merge(intervals = [[1,4],[4,5]]) == [[1,5]]
