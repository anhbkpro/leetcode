import pytest

from .longest_palindromic_subsequence import (
    DynamicProgrammingWithSpaceOptimization,
    IterativeDynamicProgramming,
    RecursiveDynamicProgramming,
)


@pytest.fixture
def recursive_solution():
    return RecursiveDynamicProgramming()


@pytest.fixture
def iterative_solution():
    return IterativeDynamicProgramming()


@pytest.fixture
def space_optimized_solution():
    return DynamicProgrammingWithSpaceOptimization()


def test_example_1(recursive_solution, iterative_solution, space_optimized_solution):
    """Test example case with string 'bbbab'"""
    s = "bbbab"
    assert recursive_solution.longestPalindromeSubseq(s) == 4  # "bbbb"
    assert iterative_solution.longestPalindromeSubseq(s) == 4  # "bbbb"
    assert space_optimized_solution.longestPalindromeSubseq(s) == 4  # "bbbb"


def test_example_2(recursive_solution, iterative_solution, space_optimized_solution):
    """Test example case with string 'cbbd'"""
    s = "cbbd"
    assert recursive_solution.longestPalindromeSubseq(s) == 2  # "bb"
    assert iterative_solution.longestPalindromeSubseq(s) == 2  # "bb"
    assert space_optimized_solution.longestPalindromeSubseq(s) == 2  # "bb"


def test_empty_string(recursive_solution, iterative_solution, space_optimized_solution):
    """Test with empty string"""
    s = ""
    assert recursive_solution.longestPalindromeSubseq(s) == 0
    assert iterative_solution.longestPalindromeSubseq(s) == 0
    assert space_optimized_solution.longestPalindromeSubseq(s) == 0


def test_single_character(
    recursive_solution, iterative_solution, space_optimized_solution
):
    """Test with single character"""
    s = "a"
    assert recursive_solution.longestPalindromeSubseq(s) == 1
    assert iterative_solution.longestPalindromeSubseq(s) == 1
    assert space_optimized_solution.longestPalindromeSubseq(s) == 1


def test_all_same_characters(
    recursive_solution, iterative_solution, space_optimized_solution
):
    """Test when all characters are the same"""
    s = "aaaa"
    assert recursive_solution.longestPalindromeSubseq(s) == 4
    assert iterative_solution.longestPalindromeSubseq(s) == 4
    assert space_optimized_solution.longestPalindromeSubseq(s) == 4


def test_no_palindrome(
    recursive_solution, iterative_solution, space_optimized_solution
):
    """Test when there is no palindrome longer than 1"""
    s = "abcd"
    assert recursive_solution.longestPalindromeSubseq(s) == 1
    assert iterative_solution.longestPalindromeSubseq(s) == 1
    assert space_optimized_solution.longestPalindromeSubseq(s) == 1


def test_case_sensitive(
    recursive_solution, iterative_solution, space_optimized_solution
):
    """Test that the search is case-sensitive"""
    s = "aAaA"
    assert recursive_solution.longestPalindromeSubseq(s) == 3  # "aAa"
    assert iterative_solution.longestPalindromeSubseq(s) == 3  # "aAa"
    assert space_optimized_solution.longestPalindromeSubseq(s) == 3  # "aAa"


def test_longer_sequence(
    recursive_solution, iterative_solution, space_optimized_solution
):
    """Test with a longer sequence that has multiple palindromic subsequences"""
    s = "character"
    assert recursive_solution.longestPalindromeSubseq(s) == 5  # "carac"
    assert iterative_solution.longestPalindromeSubseq(s) == 5  # "carac"
    assert space_optimized_solution.longestPalindromeSubseq(s) == 5  # "carac"
