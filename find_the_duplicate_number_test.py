from find_the_duplicate_number import Solution


def test_findDuplicate():
    s = Solution()
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicate([1, 1]) == 1
    assert s.findDuplicate([1, 1, 2]) == 1
