from lc_1657_determine_if_two_strings_are_close import Solution


def test_close_strings():
    assert Solution().closeStrings("abc", "bca") is True
    assert Solution().closeStrings("a", "aa") is False
