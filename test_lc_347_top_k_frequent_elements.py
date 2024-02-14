from lc_347_top_k_frequent_elements import Solution


def test_top_k_frequent():
    assert Solution.top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert Solution.top_k_frequent(nums=[1], k=1) == [1]
