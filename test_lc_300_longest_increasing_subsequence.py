from lc_300_longest_increasing_subsequence import Solution


def test_length_of_lis():
    assert Solution.lengthOfLIS([1, 3, 5, 4, 7]) == 4
    assert Solution.lengthOfLIS([2, 2, 2, 2, 2]) == 1
