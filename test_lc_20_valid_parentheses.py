from lc_20_valid_parentheses import isValid, isValid_LC_solution


def test_is_valid():
    assert isValid("()") is True
    assert isValid("()[]{}") is True
    assert isValid("(]") is False
    assert isValid_LC_solution("()") is True
    assert isValid_LC_solution("()[]{}") is True
    assert isValid_LC_solution("(]") is False
