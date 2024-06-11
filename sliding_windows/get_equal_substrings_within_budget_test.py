from .get_equal_substrings_within_budget import Solution


def test_equal_substrings():
    assert Solution().equalSubstring("abcd", "bcdf", 3) == 3
