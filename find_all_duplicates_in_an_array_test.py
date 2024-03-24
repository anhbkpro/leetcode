from find_all_duplicates_in_an_array import Solution


def test_find_all_duplicates():
    s = Solution()
    assert s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert s.findDuplicates([1, 1, 2]) == [1]
    assert s.findDuplicates([1, 1]) == [1]
    assert s.findDuplicates([3, 1, 3, 4, 2]) == [3]
    assert s.findDuplicates([1, 3, 4, 2, 2]) == [2]
