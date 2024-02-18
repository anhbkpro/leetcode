from lc_506_relative_ranks import Solution


def test_find_relative_ranks():
    assert Solution.find_relative_ranks(score=[5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert Solution.find_relative_ranks(score=[10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
