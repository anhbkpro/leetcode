from .shortest_subarray_to_be_removed_to_make_array_sorted import Solution


def test_shortest_subarray_to_be_removed_to_make_array_sorted():
    assert Solution().findLengthOfShortestSubarray(arr=[1, 2, 3, 10, 4, 2, 3, 5]) == 3
