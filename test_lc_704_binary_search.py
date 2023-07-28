from lc_704_binary_search import Solution


def test_search():
    assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
