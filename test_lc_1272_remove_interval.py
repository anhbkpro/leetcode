from lc_1272_remove_interval import removeInterval


def test_remove_interval():
    assert removeInterval([[0, 2], [3, 4], [5, 7]], [1, 6]) == [[0, 1], [6, 7]]
    assert removeInterval([[0, 5]], [2, 3]) == [[0, 2], [3, 5]]
