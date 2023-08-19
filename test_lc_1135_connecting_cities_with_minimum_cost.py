from lc_1135_connecting_cities_with_minimum_cost import Solution


def test_minimum_cost():
    assert Solution.minimum_cost(
        n=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    ) == 6
    assert (
        Solution.minimum_cost(
            n=4, connections=[[1, 2, 3], [3, 4, 4]]
        )
        == -1
    )
