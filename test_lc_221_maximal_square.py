from lc_221_maximal_square import Solution


def test_maximal_square():
    assert Solution.maximal_square(matrix=[['1', '0', '1', '0', '0'],
                                           ['1', '0', '1', '1', '1'],
                                           ['1', '1', '1', '1', '1'],
                                           ['1', '0', '0', '1', '0']]) == 4
    assert Solution.maximal_square(matrix=[['0', '1'],
                                           ['1', '0']]) == 1
