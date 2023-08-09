from lc_2616_minimize_the_maximum_difference_of_pairs import Solution


def test_minimize_max():
    assert Solution.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2) == 1
    assert Solution.minimizeMax(nums=[4, 2, 1, 2], p=1) == 0
