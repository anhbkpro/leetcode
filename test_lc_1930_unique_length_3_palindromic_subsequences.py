from lc_1930_unique_length_3_palindromic_subsequences import Solution


def test_count_palindromic_subsequence():
    assert Solution.countPalindromicSubsequence(s="aabca") == 3
    assert Solution.countPalindromicSubsequence(s="adc") == 0
    assert Solution.countPalindromicSubsequence(s="bbcbaba") == 4
