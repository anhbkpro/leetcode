import pytest

from two_pointers.is_subsequence import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("abc", "ahbgdc", True),  # Basic case where s is a subsequence
        ("axc", "ahbgdc", False),  # Basic case where s is not a subsequence
        ("", "ahbgdc", True),  # Empty string is always a subsequence
        ("abc", "", False),  # Non-empty string is not a subsequence of empty string
        ("", "", True),  # Empty string is a subsequence of empty string
        ("abc", "abc", True),  # Exact match
        ("abc", "abcd", True),  # Subsequence at the start
        ("bcd", "abcd", True),  # Subsequence at the end
        ("b", "abc", True),  # Single character subsequence
        ("bb", "bbb", True),  # Multiple same characters
        ("aaaaaa", "bbaaaa", False),  # Not enough characters in t
    ],
)
def test_is_subsequence(solution, s: str, t: str, expected: bool):
    """Test checking if s is a subsequence of t"""
    assert solution.isSubsequence(s, t) == expected
