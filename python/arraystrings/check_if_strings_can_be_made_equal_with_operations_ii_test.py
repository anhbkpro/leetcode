import pytest

from arraystrings.check_if_strings_can_be_made_equal_with_operations_ii import Solution


@pytest.fixture
def check_solution() -> Solution:
    return Solution()


def test_check_strings_with_identical_strings(check_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcdba"
    input_s2: str = "abcdba"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_with_swapped_even_indices(check_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "cbad"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_with_swapped_odd_indices(check_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "adcb"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_with_both_parity_swaps(check_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "cdab"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_returns_false_cross_parity_swap(
    check_solution: Solution,
) -> None:
    # Arrange — 'a' at even index can't move to odd index
    input_s1: str = "abcd"
    input_s2: str = "badc"
    expected_result: bool = False
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_returns_false_with_different_characters(
    check_solution: Solution,
) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "abce"
    expected_result: bool = False
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_with_all_same_characters(check_solution: Solution) -> None:
    # Arrange
    input_s1: str = "aaaa"
    input_s2: str = "aaaa"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_with_longer_rearranged_even_positions(
    check_solution: Solution,
) -> None:
    # Arrange — even positions: s1="ace", s2="eca"; odd positions: s1="bdf", s2="bdf"
    input_s1: str = "abcdef"
    input_s2: str = "ebcdaf"
    expected_result: bool = True
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_check_strings_returns_false_with_mismatched_frequencies(
    check_solution: Solution,
) -> None:
    # Arrange — even positions have different character frequencies
    input_s1: str = "aabc"
    input_s2: str = "abac"
    expected_result: bool = False
    # Act
    actual_result: bool = check_solution.checkStrings(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result
