from lc_1624_largest_substring_between_two_equal_characters import Solution


def test_max_length_between_equal_characters():
    assert Solution().maxLengthBetweenEqualCharacters(s="aa") == 0
    assert Solution().maxLengthBetweenEqualCharacters(s="abca") == 2
    assert Solution().maxLengthBetweenEqualCharacters(s="cbzxy") == -1
