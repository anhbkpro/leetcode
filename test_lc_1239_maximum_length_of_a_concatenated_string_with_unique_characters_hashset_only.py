from lc_1239_maximum_length_of_a_concatenated_string_with_unique_characters_hashset_only import Solution


def test_max_length():
    assert Solution().maxLength(["un", "iq", "ue"]) == 4
    assert Solution().maxLength(["cha", "r", "act", "ers"]) == 6
