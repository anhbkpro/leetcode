import pytest

from stacks_and_queues.LC75__asteroid_collision import Solution


@pytest.mark.parametrize(
    "asteroids, expected_output",
    [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([1, -1, -2, 2], [-2, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
        ([1], [1]),
        ([], []),
        ([2, -2, 1, -1], []),
        ([10, -10, 10, -10], []),
        ([1, 2, -2, -1], []),
        ([3, 2, -2, -3], []),
    ],
)
def test_asteroid_collision(asteroids, expected_output):
    solution = Solution()
    actual_output = solution.asteroidCollision(asteroids)
    assert actual_output == expected_output
