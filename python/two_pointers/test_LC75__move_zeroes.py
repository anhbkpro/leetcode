import pytest

from two_pointers.LC75__move_zeroes import Solution


@pytest.mark.parametrize(
    "input_nums, expected_output",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [1, 1, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0], [0]),
        ([1], [1]),
        ([], []),
        ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
        ([0, 1, 0, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0, 0]),
    ],
)
def test_move_zeroes(input_nums, expected_output):
    solution = Solution()
    nums = input_nums[:]
    solution.moveZeroes(nums)
    assert nums == expected_output
