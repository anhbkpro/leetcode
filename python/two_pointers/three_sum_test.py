from two_pointers.three_sum import Solution


def test_sort_3sum():
    assert Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum(nums=[]) == []
