from .minimum_number_of_removals_to_make_mountain_array import Solution


def test_minimum_number_of_removals_to_make_mountain_array():
    assert Solution().minimumMountainRemovals(nums=[2, 1, 1, 5, 6, 2, 3, 1]) == 3
    assert Solution().minimumMountainRemovals(nums=[4, 3, 2, 1, 1, 2, 3, 1]) == 4
