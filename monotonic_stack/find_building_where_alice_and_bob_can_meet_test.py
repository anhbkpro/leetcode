from .find_building_where_alice_and_bob_can_meet import Solution


def test_leftmost_building_queries():
    assert Solution().leftmostBuildingQueries(
        heights=[6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    ) == [2, 5, -1, 5, 2]
    assert Solution().leftmostBuildingQueries(
        heights=[5, 3, 8, 2, 6, 1, 4, 6],
        queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
    ) == [7, 6, -1, 4, 6]
