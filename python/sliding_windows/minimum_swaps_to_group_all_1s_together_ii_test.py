from .minimum_swaps_to_group_all_1s_together_ii import Solution


def test_min_swaps():
    assert Solution().minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]) == 1
    assert Solution().minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2
    assert Solution().minSwaps(nums=[1, 1, 0, 0, 1]) == 0
