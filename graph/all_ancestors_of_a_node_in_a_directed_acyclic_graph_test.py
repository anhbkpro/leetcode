from .all_ancestors_of_a_node_in_a_directed_acyclic_graph import Solution


def test_get_ancestors():
    assert Solution().getAncestors(3, [[0, 1], [1, 2], [2, 0]]) == [
        [1, 2],
        [0, 2],
        [0, 1],
    ]
