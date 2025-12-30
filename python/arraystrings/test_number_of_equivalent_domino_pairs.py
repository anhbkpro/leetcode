import pytest

from arraystrings.number_of_equivalent_domino_pairs import Solution


@pytest.mark.parametrize(
    "input_dominoes, expected_output",
    [
        ([[1, 2], [2, 1], [3, 4], [5, 6]], 1),  # One pair
        ([[1, 2], [1, 2], [1, 2]], 3),  # Three pairs (all the same)
        ([[1, 2], [2, 1], [1, 2], [2, 1]], 6),  # All equivalent, 4 choose 2 = 6
        ([[1, 2], [3, 4], [5, 6]], 0),  # No pairs
        ([[1, 1], [1, 1], [1, 1], [1, 1]], 6),  # All the same, 4 choose 2 = 6
        ([], 0),  # Empty input
        ([[1, 2]], 0),  # Single domino
        ([[1, 2], [2, 1], [1, 2], [2, 1], [3, 4]], 6),  # Four equivalent, one unique
    ],
)
def test_num_equiv_domino_pairs(input_dominoes, expected_output):
    solution = Solution()
    actual_output = solution.num_equiv_domino_pairs(input_dominoes)
    assert actual_output == expected_output
