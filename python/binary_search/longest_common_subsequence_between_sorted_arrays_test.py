from binary_search.longest_common_subsequence_between_sorted_arrays import Solution


def test_longest_common_subsequence():
    assert Solution().longestCommonSubsequence(
        arrays=[[1, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 4, 5]]
    ) == [1, 3, 4, 5]
