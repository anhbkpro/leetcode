from lc_1921_eliminate_maximum_number_of_monsters import Solution


def test_eliminate_maximum():
    assert Solution.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]) == 3
    assert Solution.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]) == 1
