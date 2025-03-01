from .apply_operations_to_an_array import Solution


def test_apply_operations():
    # Test case 1: Basic case with adjacent equal elements
    assert Solution().applyOperations([1, 1, 2, 2, 1]) == [2, 4, 1, 0, 0]

    # Test case 2: Array with no adjacent equal elements
    assert Solution().applyOperations([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test case 3: Array with zeros
    assert Solution().applyOperations([1, 0, 2, 0, 2]) == [1, 2, 2, 0, 0]

    # Test case 4: Empty array
    assert Solution().applyOperations([]) == []

    # Test case 5: Array with all equal elements
    assert Solution().applyOperations([2, 2, 2, 2]) == [4, 4, 0, 0]
