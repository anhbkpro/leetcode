from lc_1091_shortest_path_in_binary_matrix import shortestPathBinaryMatrix


def test_shortest_path_binary_matrix():
    assert shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
