from heaps.minimum_cost_to_connect_sticks import Solution


def test_minimum_cost_to_connect_sticks():
    assert Solution().connectSticks([2, 4, 3]) == 14
    assert Solution().connectSticks([1, 8, 3, 5]) == 30
    assert Solution().connectSticks([5]) == 0
