import pytest

from greedy.LC75__can_place_flowers import Solution


@pytest.mark.parametrize(
    "flowerbed, n, expected_output",
    [
        ([0, 0, 0, 0], 3, False),
        ([0, 0, 1, 0, 0], 2, True),
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 0, 1, 0, 0], 2, True),
        ([0], 1, True),
        ([1], 1, False),
        ([0, 0, 0, 0, 0], 3, True),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([0, 0, 1, 0, 1], 1, True),
        ([0, 0, 1, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 0, 1], 2, True),
        ([1, 0, 0, 0, 0, 0, 1], 3, False),
        ([0, 0, 0, 0, 1, 0, 0, 0, 0], 3, True),
        ([0, 0, 1, 0, 0, 1, 0, 0], 2, True),
        ([0, 0, 1, 0, 0, 1, 0, 0], 3, False),
        ([0], 0, True),
        ([1], 0, True),
        ([], 0, True),
        ([], 1, False),
    ],
)
def test_can_place_flowers(flowerbed, n, expected_output):
    solution = Solution()
    actual_output = solution.can_place_flowers(
        flowerbed[:], n
    )  # use a copy to avoid mutation
    assert actual_output == expected_output
