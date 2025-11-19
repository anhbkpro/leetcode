import pytest
from .longest_repeating_substring import Solution, SolutionDynamicProgramming


@pytest.fixture
def solution():
    return Solution()


@pytest.fixture
def solution_dynamic_programming():
    return SolutionDynamicProgramming()


def test_example_1(solution, solution_dynamic_programming):
    """Test example case with multiple repeating substrings"""
    s = "abbaba"
    assert solution.longestRepeatingSubstring(s) == 2  # "ab" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 2
    )  # "ab" repeats


def test_example_2(solution, solution_dynamic_programming):
    """Test example case with longer repeating substring"""
    s = "aabcaabdaab"
    assert solution.longestRepeatingSubstring(s) == 3  # "aab" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 3
    )  # "aab" repeats


def test_no_repeating_substring(solution, solution_dynamic_programming):
    """Test when there is no repeating substring"""
    s = "abcd"
    assert solution.longestRepeatingSubstring(s) == 0
    assert solution_dynamic_programming.longestRepeatingSubstring(s) == 0


def test_all_same_characters(solution, solution_dynamic_programming):
    """Test when all characters are the same"""
    s = "aaaa"
    assert solution.longestRepeatingSubstring(s) == 3  # "aaa" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 3
    )  # "aaa" repeats


def test_overlapping_substrings(solution, solution_dynamic_programming):
    """Test with overlapping repeating substrings"""
    s = "aabaabaa"
    assert solution.longestRepeatingSubstring(s) == 5  # "aabaa" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 5
    )  # "aabaa" repeats


def test_empty_string(solution, solution_dynamic_programming):
    """Test with empty string"""
    s = ""
    assert solution.longestRepeatingSubstring(s) == 0
    assert solution_dynamic_programming.longestRepeatingSubstring(s) == 0


def test_single_character(solution, solution_dynamic_programming):
    """Test with single character"""
    s = "a"
    assert solution.longestRepeatingSubstring(s) == 0
    assert solution_dynamic_programming.longestRepeatingSubstring(s) == 0


def test_two_characters(solution, solution_dynamic_programming):
    """Test with two characters"""
    s = "aa"
    assert solution.longestRepeatingSubstring(s) == 1  # "a" repeats
    assert solution_dynamic_programming.longestRepeatingSubstring(s) == 1  # "a" repeats


def test_multiple_possible_substrings(solution, solution_dynamic_programming):
    """Test with multiple possible repeating substrings of different lengths"""
    s = "ababab"
    assert solution.longestRepeatingSubstring(s) == 4  # "abab" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 4
    )  # "abab" repeats


def test_case_sensitive(solution, solution_dynamic_programming):
    """Test that the search is case-sensitive"""
    s = "aAaA"
    assert solution.longestRepeatingSubstring(s) == 2  # "aA" repeats
    assert (
        solution_dynamic_programming.longestRepeatingSubstring(s) == 2
    )  # "aA" repeats
