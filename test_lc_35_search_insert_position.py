from lc_35_search_insert_position import Solution


def test_search_insert():
    assert Solution.search_insert(nums=[1, 3, 5, 6], target=5) == 2
    assert Solution.search_insert(nums=[1, 3, 5, 6], target=2) == 1
