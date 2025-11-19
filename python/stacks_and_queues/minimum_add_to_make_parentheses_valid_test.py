from .minimum_add_to_make_parentheses_valid import Solution


def test_minimum_add_to_make_parentheses_valid():
    assert Solution().minAddToMakeValid("())") == 1
    assert Solution().minAddToMakeValid("(((") == 3
    assert Solution().minAddToMakeValid("()") == 0
