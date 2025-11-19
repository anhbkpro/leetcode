from .minimum_difference_between_largest_and_smallest_value_in_three_moves import (
    Solution,
)


def test_min_difference():
    assert Solution().minDifference(nums=[5, 3, 2, 4]) == 0
    assert Solution().minDifference(nums=[1, 5, 0, 10, 14]) == 1
