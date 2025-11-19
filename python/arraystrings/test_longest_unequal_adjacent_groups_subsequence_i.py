import pytest
from arraystrings.longest_unequal_adjacent_groups_subsequence_i import Solution


def test_get_longest_subsequence_empty_input():
    solution = Solution()
    assert solution.getLongestSubsequence([], []) == []


def test_get_longest_subsequence_single_element():
    solution = Solution()
    assert solution.getLongestSubsequence(["a"], [1]) == ["a"]
    assert solution.getLongestSubsequence(["b"], [0]) == ["b"]


def test_get_longest_subsequence_all_same_group():
    solution = Solution()
    words = ["a", "b", "c", "d"]
    groups = [1, 1, 1, 1]
    assert solution.getLongestSubsequence(words, groups) == ["a"]


def test_get_longest_subsequence_alternating_groups():
    solution = Solution()
    words = ["a", "b", "c", "d", "e"]
    groups = [0, 1, 0, 1, 0]
    assert solution.getLongestSubsequence(words, groups) == ["a", "b", "c", "d", "e"]


def test_get_longest_subsequence_typical_case():
    solution = Solution()
    words = ["a", "b", "c", "d", "e", "f"]
    groups = [1, 1, 0, 0, 1, 1]
    assert solution.getLongestSubsequence(words, groups) == ["a", "c", "e"]


def test_get_longest_subsequence_consecutive_same_groups():
    solution = Solution()
    words = ["a", "b", "c", "d", "e"]
    groups = [1, 1, 1, 0, 0]
    assert solution.getLongestSubsequence(words, groups) == ["a", "d"]


def test_get_longest_subsequence_multiple_groups():
    solution = Solution()
    words = ["a", "b", "c", "d", "e", "f", "g"]
    groups = [0, 1, 2, 0, 1, 2, 0]
    assert solution.getLongestSubsequence(words, groups) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
    ]


def test_get_longest_subsequence_complex_case():
    solution = Solution()
    words = ["a", "b", "c", "d", "e", "f", "g", "h"]
    groups = [1, 1, 0, 0, 1, 1, 0, 0]
    assert solution.getLongestSubsequence(words, groups) == ["a", "c", "e", "g"]


def test_get_longest_subsequence_leetcode_example():
    solution = Solution()
    words = ["a", "b", "c", "d"]
    groups = [1, 0, 1, 1]
    assert solution.getLongestSubsequence(words, groups) == ["a", "b", "c"]
