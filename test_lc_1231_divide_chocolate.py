from lc_1231_divide_chocolate import maximizeSweetness


def test_maximize_sweetness():
    assert maximizeSweetness(sweetness=[1, 2, 3, 4, 5, 6, 7, 8, 9], k=5) == 6
    assert maximizeSweetness(sweetness=[5, 6, 7, 8, 9, 1, 2, 3, 4], k=8) == 1
    assert maximizeSweetness(sweetness=[1, 2, 2, 1, 2, 2, 1, 2, 2], k=2) == 5
