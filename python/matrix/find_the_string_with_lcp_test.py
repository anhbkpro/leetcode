from typing import List

import pytest

from matrix.find_the_string_with_lcp import Solution


@pytest.fixture
def lcp_solution() -> Solution:
    return Solution()


def test_find_the_string_with_valid_lcp_matrix(lcp_solution: Solution) -> None:
    # Arrange
    input_lcp: List[List[int]] = [
        [4, 0, 2, 0],
        [0, 3, 0, 1],
        [2, 0, 2, 0],
        [0, 1, 0, 1],
    ]
    expected_word: str = "abab"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_with_single_character(lcp_solution: Solution) -> None:
    # Arrange
    input_lcp: List[List[int]] = [[1]]
    expected_word: str = "a"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_with_all_same_characters(lcp_solution: Solution) -> None:
    # Arrange
    input_lcp: List[List[int]] = [
        [3, 2, 1],
        [2, 2, 1],
        [1, 1, 1],
    ]
    expected_word: str = "aaa"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_with_all_distinct_characters(lcp_solution: Solution) -> None:
    # Arrange
    input_lcp: List[List[int]] = [
        [3, 0, 0],
        [0, 2, 0],
        [0, 0, 1],
    ]
    expected_word: str = "abc"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_returns_empty_for_invalid_matrix(
    lcp_solution: Solution,
) -> None:
    # Arrange — lcp[0][1] claims shared prefix of 2, but lcp[1][0] is 0 (asymmetric)
    input_lcp: List[List[int]] = [
        [2, 2],
        [0, 1],
    ]
    expected_word: str = ""
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_returns_empty_when_too_many_chars_needed(
    lcp_solution: Solution,
) -> None:
    # Arrange — 27 distinct characters needed exceeds 'a'-'z'
    n: int = 27
    input_lcp: List[List[int]] = [[0] * n for _ in range(n)]
    for i in range(n):
        input_lcp[i][i] = 1
    expected_word: str = ""
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_returns_empty_for_inconsistent_lcp(
    lcp_solution: Solution,
) -> None:
    # Arrange — lcp[0][1] says shared prefix but characters would differ
    input_lcp: List[List[int]] = [
        [2, 1],
        [1, 1],
    ]
    expected_word: str = "aa"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_with_two_distinct_characters(
    lcp_solution: Solution,
) -> None:
    # Arrange
    input_lcp: List[List[int]] = [
        [2, 0],
        [0, 1],
    ]
    expected_word: str = "ab"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_returns_empty_for_wrong_diagonal(
    lcp_solution: Solution,
) -> None:
    # Arrange — diagonal must equal n-i for position i
    input_lcp: List[List[int]] = [
        [2, 0],
        [0, 2],
    ]
    expected_word: str = ""
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word


def test_find_the_string_with_repeating_pattern(lcp_solution: Solution) -> None:
    # Arrange — "abcabc"
    input_lcp: List[List[int]] = [
        [6, 0, 0, 3, 0, 0],
        [0, 5, 0, 0, 2, 0],
        [0, 0, 4, 0, 0, 1],
        [3, 0, 0, 3, 0, 0],
        [0, 2, 0, 0, 2, 0],
        [0, 0, 1, 0, 0, 1],
    ]
    expected_word: str = "abcabc"
    # Act
    actual_word: str = lcp_solution.findTheString(input_lcp)
    # Assert
    assert actual_word == expected_word
