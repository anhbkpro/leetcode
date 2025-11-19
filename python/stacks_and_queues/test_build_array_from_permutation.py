import pytest
from stacks_and_queues.build_array_from_permutation import Solution


@pytest.mark.parametrize(
    "nums, expected_output",
    [
        ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
        ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
        ([0], [0]),
        ([1, 0], [0, 1]),
        ([2, 0, 1], [1, 2, 0]),
        ([3, 2, 1, 0], [0, 1, 2, 3]),
        ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]),
        ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
    ],
)
def test_build_array(nums, expected_output):
    solution = Solution()
    actual_output = solution.buildArray(nums)
    assert actual_output == expected_output
