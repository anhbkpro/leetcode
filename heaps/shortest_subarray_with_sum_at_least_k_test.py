from .shortest_subarray_with_sum_at_least_k import Solution


def test_shortest_subarray():
    assert Solution().shortestSubarray([1], 1) == 1
    assert Solution().shortestSubarray([1, 2], 4) == -1
    assert Solution().shortestSubarray([2, -1, 2], 3) == 3
