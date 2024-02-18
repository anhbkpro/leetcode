from lc_658_find_k_closest_elements import Solution


def test_find_closest_elements():
    assert Solution.find_closest_elements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert Solution.find_closest_elements(arr=[1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]
