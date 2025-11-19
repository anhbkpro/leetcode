from hashing.missing_number import Solution


def test_missingNumber():
    assert Solution().missingNumber([3, 0, 1]) == 2
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution().missingNumber([0]) == 1
