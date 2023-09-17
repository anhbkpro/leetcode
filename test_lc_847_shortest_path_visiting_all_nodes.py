from lc_847_shortest_path_visiting_all_nodes import Solution


def test_shortest_path_length():
    assert Solution.shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]]) == 4
    assert (
        Solution.shortestPathLength(graph=[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
        == 4
    )
