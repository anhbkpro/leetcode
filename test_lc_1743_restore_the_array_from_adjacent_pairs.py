from lc_1743_restore_the_array_from_adjacent_pairs import Solution


def test_restore_array():
    assert Solution.restoreArray([[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4]
    assert Solution.restoreArray([[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3]
