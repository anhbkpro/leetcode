import pytest

from .longest_substring_without_repeating_characters import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    test_cases = [
        ("abcabcbb", 3),  # Basic case with repeating characters
        ("bbbbb", 1),  # All same characters
        ("pwwkew", 3),  # Multiple distinct substrings
        ("dvdf", 3),  # Overlapping substrings
    ]
    for s, expected in test_cases:
        assert solution.lengthOfLongestSubstring(s) == expected


def test_edge_cases(solution):
    test_cases = [
        ("", 0),  # Empty string
        (" ", 1),  # Single space
        ("a", 1),  # Single character
        ("  ", 1),  # Multiple spaces
    ]
    for s, expected in test_cases:
        assert solution.lengthOfLongestSubstring(s) == expected


def test_special_cases(solution):
    test_cases = [
        ("aab", 2),  # Repeating at start
        ("abb", 2),  # Repeating at end
        ("abba", 2),  # Palindrome
        ("tmmzuxt", 5),  # Multiple repeating chars
    ]
    for s, expected in test_cases:
        assert solution.lengthOfLongestSubstring(s) == expected


def test_input_variations(solution):
    test_cases = [
        ("!@#$%^&*()", 10),  # Special characters
        ("12345", 5),  # Numbers only
        ("abc123!@#", 9),  # Mixed characters
        ("abcABC123", 9),  # Case sensitivity
    ]
    for s, expected in test_cases:
        assert solution.lengthOfLongestSubstring(s) == expected


def test_sliding_window_specific(solution):
    """Test cases specifically designed for sliding window edge cases"""
    test_cases = [
        ("abcdefghijklmnopqrstuvwxyz", 26),  # All unique chars
        ("aaabbbccc", 2),  # Groups of repeating chars
        ("abcdeafbcdef", 6),  # Multiple overlapping substrings
        ("abcabcdbb", 4),  # Nested repeating patterns
        ("aaaaabcdef", 6),  # Long repeating prefix
        ("abcdeeeeee", 5),  # Long repeating suffix
    ]
    for s, expected in test_cases:
        assert solution.lengthOfLongestSubstring(s) == expected
