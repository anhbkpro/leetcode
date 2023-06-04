from lc_547_number_of_provinces import findCircleNum


def test_find_circle_num():
    assert findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
