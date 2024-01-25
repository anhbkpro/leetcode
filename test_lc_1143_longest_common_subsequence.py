from lc_1143_longest_common_subsequence import Solution


def test_longest_common_subsequence():
    assert Solution.longestCommonSubsequence(text1="abcde", text2="ace") == 3
    assert Solution.longestCommonSubsequence(text1="abc", text2="abc") == 3
    assert Solution.longestCommonSubsequence(text1="abc", text2="def") == 0
