from hash_table.first_missing_positive import Solution


def test_firstMissingPositive():
    assert Solution.first_missing_positive([1, 2, 0]) == 3
    assert Solution.first_missing_positive([3, 4, -1, 1]) == 2
    assert Solution.first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert Solution.first_missing_positive([1]) == 2
    assert Solution.first_missing_positive([1, 2, 3]) == 4
