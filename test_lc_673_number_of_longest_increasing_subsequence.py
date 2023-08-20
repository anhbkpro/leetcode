from lc_673_number_of_longest_increasing_subsequence import Solution


def test_find_number_of_lis():
    assert Solution.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert Solution.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
