from first_missing_positive import Solution


def test_firstMissingPositive():
    sol = Solution()
    assert sol.firstMissingPositive([1, 2, 0]) == 3
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
    assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert sol.firstMissingPositive([1]) == 2
    assert sol.firstMissingPositive([1, 2, 3]) == 4
