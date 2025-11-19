from .shortest_distance_after_road_addition_queries_i import Solution


def test_shortest_distance_after_queries():
    assert Solution().shortestDistanceAfterQueries(
        n=5, queries=[[2, 4], [0, 2], [0, 4]]
    ) == [3, 2, 1]
    assert Solution().shortestDistanceAfterQueries(n=4, queries=[[0, 3], [0, 2]]) == [
        1,
        1,
    ]
