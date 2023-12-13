from lc_1582_special_positions_in_a_binary_matrix import Solution


def test_num_special():
    assert Solution.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
    assert Solution.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
