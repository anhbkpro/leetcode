from lc_1425_constrained_subsequence_sum import Solution


def test_constrained_subset_sum():
    assert Solution().constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2) == 37
    assert Solution().constrainedSubsetSum(nums=[-1, -2, -3], k=1) == -1
    assert Solution().constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2) == 23
