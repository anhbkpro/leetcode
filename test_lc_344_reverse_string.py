from lc_344_reverse_string import Solution


def test_reverse_string():
    s = ["h", "e", "l", "l", "o"]
    Solution.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]
    s = ["H", "a", "n", "n", "a", "h"]
    Solution.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
