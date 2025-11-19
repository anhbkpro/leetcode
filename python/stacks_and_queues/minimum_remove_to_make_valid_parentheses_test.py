from .minimum_remove_to_make_valid_parentheses import Solution


def test_min_remove_to_make_valid():
    assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid("))((") == ""
