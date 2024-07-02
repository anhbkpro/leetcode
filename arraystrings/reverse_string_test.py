from .reverse_string import Solution


def test_reverse_string():
    input = ["h", "e", "l", "l", "o"]
    Solution().reverseString(input)
    assert input == ["o", "l", "l", "e", "h"]
