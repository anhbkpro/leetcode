from .make_string_a_subsequence_using_cyclic_increments import Solution


def test_can_make_subsequence():
    assert Solution().canMakeSubsequence(str1="abc", str2="ad") is True
    assert Solution().canMakeSubsequence(str1="zc", str2="ad") is True
