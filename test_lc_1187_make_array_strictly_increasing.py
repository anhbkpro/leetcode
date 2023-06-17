from lc_1187_make_array_strictly_increasing import make_array_increasing


def test_make_array_increasing():
    assert make_array_increasing([1, 5, 3, 6, 7], [1, 3, 2, 4]) == 1
    assert make_array_increasing([1, 5, 3, 6, 7], [4, 3, 1]) == 2
