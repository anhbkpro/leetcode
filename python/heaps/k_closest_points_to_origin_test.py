from heaps.k_closest_points_to_origin import Solution


def test_k_closest_points_to_origin():
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
