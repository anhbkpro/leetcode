from .maximum_number_of_k_divisible_components import Solution


def test_max_k_divisible_components():
    assert (
        Solution().maxKDivisibleComponents(
            n=5, edges=[[0, 2], [1, 2], [1, 3], [2, 4]], values=[1, 8, 1, 4, 4], k=6
        )
        == 2
    )
    assert (
        Solution().maxKDivisibleComponents(
            n=7,
            edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
            values=[3, 0, 6, 1, 5, 2, 1],
            k=3,
        )
        == 3
    )
