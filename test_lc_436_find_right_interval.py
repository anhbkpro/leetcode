from lc_436_find_right_interval import Solution


def test_find_right_interval():
    assert Solution.findRightInterval(intervals=[[1, 2]]) == [-1]
    assert Solution.findRightInterval(intervals=[[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]
    assert Solution.findRightInterval(intervals=[[1, 4], [2, 3], [3, 4]]) == [-1, 2, -1]
