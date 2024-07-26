from .find_the_city_with_the_smallest_number_of_neighbors_at_a_threshold_distance import Solution


def test_find_the_city():
    assert (
        Solution().findTheCity(
            4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4
        )
        == 3
    )
