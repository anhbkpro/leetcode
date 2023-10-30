from lc_1356_sort_integers_by_the_number_of_1_bits import Solution


def test_sort_by_bits():
    assert Solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
