from hashing.counting_elements import Solution


def test_counting_elements():
    assert Solution().countElements([1, 2, 3]) == 2
    assert Solution().countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
