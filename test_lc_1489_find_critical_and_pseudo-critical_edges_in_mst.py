

def test_find_critical_and_pseudo_critical_edges():
    assert Solution().findCriticalAndPseudoCriticalEdges(
        n=5,
        edges=[
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 2],
            [0, 3, 2],
            [0, 4, 3],
            [3, 4, 3],
            [1, 4, 6],
        ],
    ) == [[0, 1], [2, 3, 4, 5]]
