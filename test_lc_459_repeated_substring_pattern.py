from lc_459_repeated_substring_pattern import Solution


def test_repeated_substring_pattern():
    assert Solution.repeated_substring_pattern("abab") is True
    assert Solution.repeated_substring_pattern("aba") is False
    assert Solution.repeated_substring_pattern("abcabcabcabc") is True
