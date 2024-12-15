import math
from .maximum_average_pass_ratio import Solution


def test_max_average_ratio():
    # Define tolerance for floating point comparison
    EPSILON = 1e-5

    # Get actual result
    actual = Solution().maxAverageRatio(
        classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2
    )

    # Expected result
    expected = 0.78333

    # Assert using absolute difference comparison
    assert math.isclose(
        actual, expected, abs_tol=EPSILON
    ), f"Expected {expected}, but got {actual}"
