from hashing.largest_unique_number import Solution


def test_largest_unique_number():
    assert Solution().largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1]) == 8
    assert Solution().largestUniqueNumber([9, 9, 8, 8]) == -1
