from typing import List

import pytest

from arraystrings.count_the_hidden_sequences import Solution


@pytest.fixture
def sequence_solution() -> Solution:
    return Solution()


def test_count_sequences_with_standard_case(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [1, -3, 4]
    input_lower: int = 1
    input_upper: int = 6
    expected_count: int = 2  # Possible arrays: [3,4,1,5], [4,5,2,6]

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_no_possible_array(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [3, -4, 5, 1, -2]
    input_lower: int = 1
    input_upper: int = 4
    expected_count: int = 0  # Range too small for differences

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_single_difference(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [1]
    input_lower: int = 1
    input_upper: int = 5
    expected_count: int = 4  # Multiple possible starting points

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_all_positive_differences(
    sequence_solution: Solution,
) -> None:
    # Arrange
    input_differences: List[int] = [1, 2, 3]
    input_lower: int = 0
    input_upper: int = 10
    expected_count: int = 5  # Sequence steadily increases

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_all_negative_differences(
    sequence_solution: Solution,
) -> None:
    # Arrange
    input_differences: List[int] = [-1, -2, -1]
    input_lower: int = 0
    input_upper: int = 10
    expected_count: int = 7  # Sequence steadily decreases

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_zero_differences(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [0, 0, 0]
    input_lower: int = 1
    input_upper: int = 5
    expected_count: int = 5  # All elements must be equal

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_tight_bounds(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [1, -1]
    input_lower: int = 1
    input_upper: int = 2
    expected_count: int = 1  # Minimal valid range

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count


def test_count_sequences_with_large_range(sequence_solution: Solution) -> None:
    # Arrange
    input_differences: List[int] = [1, 1]
    input_lower: int = 1
    input_upper: int = 1000000
    expected_count: int = 999998  # Very wide range of possibilities

    # Act
    actual_count: int = sequence_solution.numberOfArrays(
        input_differences, input_lower, input_upper
    )

    # Assert
    assert actual_count == expected_count
