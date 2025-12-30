import pytest

from greedy.minimum_domino_rotations_for_equal_row import Solution


@pytest.mark.parametrize(
    "input_a, input_b, expected_output",
    [
        ([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2], 2),  # Typical case
        ([3, 5, 1, 2, 3], [3, 6, 3, 3, 4], -1),  # No solution
        ([1, 1, 1, 1], [1, 1, 1, 1], 0),  # Already equal
        ([1], [2], 0),  # Single domino, can rotate to either
        (
            [1, 2, 1, 1, 1, 2, 2, 2],
            [2, 1, 2, 2, 2, 2, 2, 2],
            1,
        ),  # Only one rotation needed
        ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], -1),  # No solution, all different
        ([2, 2, 2, 2], [2, 2, 2, 2], 0),  # All dominos already equal
    ],
)
def test_min_domino_rotations(input_a, input_b, expected_output):
    solution = Solution()
    actual_output = solution.min_domino_rotations(input_a, input_b)
    assert actual_output == expected_output
