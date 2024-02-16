from lc_1481_least_number_of_unique_integers_after_k_removals import Solution


def test_find_least_num_of_unique_ints():
    assert Solution.find_least_num_of_unique_ints(arr=[5, 5, 4], k=1) == 1
    assert Solution.find_least_num_of_unique_ints(arr=[4, 3, 1, 1, 3, 3, 2], k=3) == 2
