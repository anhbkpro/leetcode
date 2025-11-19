from .maximum_number_of_points_with_cost import Solution


def test_max_points():
    assert Solution().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]) == 9
