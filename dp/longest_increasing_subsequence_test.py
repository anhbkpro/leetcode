from .longest_increasing_subsequence import Solution


def test_longest_increasing_subsequence():
    assert Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
