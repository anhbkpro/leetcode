from lc_269_alien_dictionary import alienOrder


def test_alien_order():
    assert alienOrder(["abc", "ab"]) == ""
    assert alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert alienOrder(["z", "x"]) == "zx"
    assert alienOrder(["z", "x", "z"]) == ""
