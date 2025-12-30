import pytest

from .number_of_substrings_containing_all_three_characters import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_functionality(solution):
    assert solution.numberOfSubstrings("abcabc") == 10
    assert solution.numberOfSubstrings("abc") == 1
    assert solution.numberOfSubstrings("abcabcabc") == 28


def test_edge_cases(solution):
    # Minimum length string containing all characters
    assert solution.numberOfSubstrings("cab") == 1
    # String with exactly 3 characters, one of each
    assert solution.numberOfSubstrings("bac") == 1


def test_special_cases(solution):
    # All characters at the end
    assert solution.numberOfSubstrings("aaabbbccc") == 9
    # All characters at the beginning
    assert solution.numberOfSubstrings("abcaaa") == 7
    # Multiple occurrences with gaps
    assert solution.numberOfSubstrings("aaacbbabc") == 21


def test_input_variations(solution):
    # Different character orders
    assert solution.numberOfSubstrings("acb") == 1
    assert solution.numberOfSubstrings("bca") == 1
    # Repeated characters
    assert solution.numberOfSubstrings("abcabc") == 10
    # Characters with gaps
    assert solution.numberOfSubstrings("aaaabc") == 4
