import pytest
from .LC75__string_compression import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_array(solution):
    chars = []
    assert solution.compress(chars) == 0
    assert chars == []


def test_single_character(solution):
    chars = ["a"]
    assert solution.compress(chars) == 1
    assert chars[:1] == ["a"]


def test_no_compression_needed(solution):
    chars = ["a", "b", "c"]
    assert solution.compress(chars) == 3
    assert chars[:3] == ["a", "b", "c"]


def test_simple_compression(solution):
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert solution.compress(chars) == 6
    assert chars[:6] == ["a", "2", "b", "2", "c", "3"]


def test_leetcode_example_1(solution):
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert solution.compress(chars) == 6
    assert chars[:6] == ["a", "2", "b", "2", "c", "3"]


def test_leetcode_example_2(solution):
    chars = ["a"]
    assert solution.compress(chars) == 1
    assert chars[:1] == ["a"]


def test_leetcode_example_3(solution):
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert solution.compress(chars) == 4
    assert chars[:4] == ["a", "b", "1", "2"]


def test_multiple_groups(solution):
    chars = ["a", "a", "a", "b", "b", "a", "a"]
    assert solution.compress(chars) == 6
    assert chars[:6] == ["a", "3", "b", "2", "a", "2"]


def test_single_character_repeated(solution):
    chars = ["a", "a", "a", "a", "a", "a"]
    assert solution.compress(chars) == 2
    assert chars[:2] == ["a", "6"]


def test_mixed_length_groups(solution):
    chars = ["a", "a", "a", "b", "b", "b", "b", "c", "c"]
    assert solution.compress(chars) == 6
    assert chars[:6] == ["a", "3", "b", "4", "c", "2"]


def test_no_consecutive_chars(solution):
    chars = ["a", "b", "c", "d", "e"]
    assert solution.compress(chars) == 5
    assert chars[:5] == ["a", "b", "c", "d", "e"]


def test_large_repetition(solution):
    chars = ["a"] * 100
    assert solution.compress(chars) == 4
    assert chars[:4] == ["a", "1", "0", "0"]


def test_mixed_case(solution):
    chars = ["a", "A", "A", "A", "b", "b", "b", "b"]
    assert solution.compress(chars) == 5
    assert chars[:5] == ["a", "A", "3", "b", "4"]
