from lc_239_sliding_window_maximum import Solution


def test_max_sliding_window():
    assert Solution.max_sliding_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert Solution.max_sliding_window(nums=[1], k=1) == [1]
    assert Solution.max_sliding_window(nums=[1, -1], k=1) == [1, -1]
