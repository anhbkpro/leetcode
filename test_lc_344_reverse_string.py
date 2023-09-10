from lc_344_reverse_string import Solution


def test_reverse_string():
    s = ["h", "e", "l", "l", "o"]
    Solution.reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]
    s = ["H", "a", "n", "n", "a", "h"]
    Solution.reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]


def test_reverse_string_recursion():
    s = ["h", "e", "l", "l", "o"]
    Solution.reverse_string_recursion(s)
    assert s == ["o", "l", "l", "e", "h"]
    s = ["H", "a", "n", "n", "a", "h"]
    Solution.reverse_string_recursion(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
