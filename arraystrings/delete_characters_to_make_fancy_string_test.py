from .delete_characters_to_make_fancy_string import Solution


def test_delete_characters_to_make_fancy_string():
    assert Solution().makeFancyString("leeetcode") == "leetcode"
    assert Solution().makeFancyString("aaabaaaa") == "aabaa"
