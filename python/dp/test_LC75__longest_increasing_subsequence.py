from typing import List

import pytest

from dp.LC75__longest_increasing_subsequence import Solution


@pytest.fixture
def lis_solution() -> Solution:
    return Solution()


def test_calculate_lis_with_standard_sequence(lis_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_length: int = 4  # [2, 5, 7, 101] or [2, 5, 7, 18]

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_strictly_increasing_sequence(
    lis_solution: Solution,
) -> None:
    # Arrange
    input_nums: List[int] = [1, 2, 3, 4, 5]
    expected_length: int = 5  # Entire sequence is increasing

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_strictly_decreasing_sequence(
    lis_solution: Solution,
) -> None:
    # Arrange
    input_nums: List[int] = [5, 4, 3, 2, 1]
    expected_length: int = 1  # No increasing subsequence longer than 1

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_single_element(lis_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [42]
    expected_length: int = 1  # Single element is a subsequence

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_duplicate_elements(lis_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 1, 1, 1]
    expected_length: int = 1  # No strictly increasing subsequence longer than 1

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_alternating_sequence(lis_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [1, 3, 2, 4, 3, 5]
    expected_length: int = 4  # [1, 2, 4, 5] or [1, 3, 4, 5]

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length


def test_calculate_lis_with_negative_numbers(lis_solution: Solution) -> None:
    # Arrange
    input_nums: List[int] = [-2, -1, -3, 0, 1]
    expected_length: int = 4  # [-2, -1, 0, 1]

    # Act
    actual_length: int = lis_solution.lengthOfLIS(input_nums)

    # Assert
    assert actual_length == expected_length
