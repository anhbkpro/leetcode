import math

from .maximum_average_pass_ratio import Solution


def test_max_average_ratio_example1():
    """Test Example 1: classes = [[1,2],[3,5],[2,2]], extraStudents = 2"""
    # Define tolerance for floating point comparison
    EPSILON = 1e-5

    # Get actual result
    actual = Solution().maxAverageRatio(
        classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2
    )

    # Expected result
    expected = 0.78333

    # Assert using absolute difference comparison
    assert math.isclose(actual, expected, abs_tol=EPSILON), (
        f"Expected {expected}, but got {actual}"
    )


def test_max_average_ratio_example2():
    """Test Example 2: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4"""
    # Define tolerance for floating point comparison
    EPSILON = 1e-5

    # Get actual result
    actual = Solution().maxAverageRatio(
        classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4
    )

    # Expected result
    expected = 0.53485

    # Assert using absolute difference comparison
    assert math.isclose(actual, expected, abs_tol=EPSILON), (
        f"Expected {expected}, but got {actual}"
    )


def test_max_average_ratio_edge_cases():
    """Test edge cases"""
    EPSILON = 1e-5

    # Test with no extra students
    actual = Solution().maxAverageRatio(classes=[[1, 2], [3, 5]], extraStudents=0)
    expected = (1 / 2 + 3 / 5) / 2
    assert math.isclose(actual, expected, abs_tol=EPSILON)

    # Test with single class
    actual = Solution().maxAverageRatio(classes=[[1, 3]], extraStudents=2)
    expected = 3 / 5
    assert math.isclose(actual, expected, abs_tol=EPSILON)
