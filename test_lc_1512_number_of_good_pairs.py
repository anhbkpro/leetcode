from lc_1512_number_of_good_pairs import Solution


def test_num_identical_pairs():
    assert Solution.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]) == 4
    assert Solution.numIdenticalPairs(nums=[1, 1, 1, 1]) == 6
