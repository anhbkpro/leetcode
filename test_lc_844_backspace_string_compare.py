from lc_844_backspace_string_compare import Solution

solution = Solution()


def test_backspace_compare():
    assert solution.backspaceCompare(s="ab#c", t="ad#c") is True
    assert solution.backspaceCompare(s="ab##", t="c#d#") is True
    assert solution.backspaceCompare(s="a#c", t="b") is False
