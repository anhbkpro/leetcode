import pytest

from arraystrings.check_if_strings_can_be_made_equal_with_operations_i import Solution


@pytest.fixture
def equal_solution() -> Solution:
    return Solution()


def test_can_be_equal_with_identical_strings(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "abcd"
    expected_result: bool = True
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_with_swapped_even_indices(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "cbad"
    expected_result: bool = True
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_with_swapped_odd_indices(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "adcb"
    expected_result: bool = True
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_with_both_swaps(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "cdab"
    expected_result: bool = True
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_returns_false_when_impossible(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "dacb"
    expected_result: bool = False
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_returns_false_with_different_characters(
    equal_solution: Solution,
) -> None:
    # Arrange
    input_s1: str = "abcd"
    input_s2: str = "abce"
    expected_result: bool = False
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_with_all_same_characters(equal_solution: Solution) -> None:
    # Arrange
    input_s1: str = "aaaa"
    input_s2: str = "aaaa"
    expected_result: bool = True
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result


def test_can_be_equal_returns_false_with_adjacent_swap(
    equal_solution: Solution,
) -> None:
    # Arrange — adjacent swap (indices 0,1) is not a valid operation
    input_s1: str = "abcd"
    input_s2: str = "bacd"
    expected_result: bool = False
    # Act
    actual_result: bool = equal_solution.canBeEqual(input_s1, input_s2)
    # Assert
    assert actual_result == expected_result
