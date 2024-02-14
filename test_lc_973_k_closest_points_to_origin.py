from lc_973_k_closest_points_to_origin import Solution


def test_k_closest():
    assert (
            Solution.k_closest(
                points=[[1, 3], [-2, 2]],
                k=1
            ) == [[-2, 2]]
    )
    assert (
            Solution.k_closest(
                points=[[3, 3], [5, -1], [-2, 4]],
                k=2
            ) == [[3, 3], [-2, 4]]
    )
