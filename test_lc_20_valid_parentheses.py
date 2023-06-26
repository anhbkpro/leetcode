from lc_20_valid_parentheses import isValid


def test_is_valid():
    assert isValid("()") is True
    assert isValid("()[]{}") is True
    assert isValid("(]") is False
