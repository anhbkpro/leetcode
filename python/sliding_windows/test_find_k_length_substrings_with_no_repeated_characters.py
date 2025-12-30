import pytest

from .find_k_length_substrings_with_no_repeated_characters import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_case(solution):
    assert solution.numKLenSubstrNoRepeats("havefunonleetcode", 5) == 6


def test_empty_string(solution):
    assert solution.numKLenSubstrNoRepeats("", 1) == 0


def test_k_greater_than_string_length(solution):
    assert solution.numKLenSubstrNoRepeats("abc", 4) == 0


def test_no_valid_substrings(solution):
    assert solution.numKLenSubstrNoRepeats("aaa", 2) == 0


def test_all_unique_characters(solution):
    assert solution.numKLenSubstrNoRepeats("abcde", 3) == 3


def test_single_character_k(solution):
    assert solution.numKLenSubstrNoRepeats("abcde", 1) == 5


def test_exactly_k_length_string(solution):
    assert solution.numKLenSubstrNoRepeats("abcde", 5) == 1


def test_mixed_case_string(solution):
    assert solution.numKLenSubstrNoRepeats("aAbBcC", 2) == 5
