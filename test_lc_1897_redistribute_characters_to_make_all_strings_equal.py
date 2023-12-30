from lc_1897_redistribute_characters_to_make_all_strings_equal import Solution


def test_make_equal():
    assert Solution().makeEqual(words=["abc", "aabc", "bc"]) is True
    assert Solution().makeEqual(words=["ab", "a"]) is False
