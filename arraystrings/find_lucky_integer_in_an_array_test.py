import pytest
from typing import List
from arraystrings.find_lucky_integer_in_an_array import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "arr,expected",
    [
        ([2, 2, 3, 4], 2),  # 2 appears 2 times
        ([1, 2, 2, 3, 3, 3], 3),  # 3 appears 3 times (larger than 2)
        ([2, 2, 2, 3, 3], -1),  # No lucky numbers
        ([1], 1),  # Single element that is lucky
        ([2], -1),  # Single element that is not lucky
        ([5, 5, 5, 5, 5], 5),  # 5 appears 5 times and is lucky
        ([], -1),  # Empty array
        ([1, 1, 1, 1], -1),  # 1 appears 4 times, not 1 time
        ([3, 3, 3], 3),  # 3 appears 3 times
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4),  # Multiple lucky numbers, return largest
    ],
)
def test_parametrized_cases(solution: Solution, arr: List[int], expected: int) -> None:
    # Act
    actual: int = solution.findLucky(arr)

    # Assert
    assert actual == expected
