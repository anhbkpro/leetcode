from .remove_max_number_of_edges_to_keep_graph_fully_traversable import Solution


def test_max_num_edges_to_remove():
    assert (
        Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]])
        == 2
    )
