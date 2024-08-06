from .minimum_number_of_pushes_to_type_word_ii import Solution


def test_minimum_pushes():
    solution = Solution()
    assert solution.minimum_pushes_sort(word = "abcde") == 5
    assert solution.minimum_pushes_sort(word = "xyzxyzxyzxyz") == 12
    assert solution.minimum_pushes_sort(word = "aabbccddeeffgghhiiiiii") == 24
    assert solution.minimum_pushes_heap(word = "abcde") == 5
    assert solution.minimum_pushes_heap(word = "xyzxyzxyzxyz") == 12
    assert solution.minimum_pushes_heap(word = "aabbccddeeffgghhiiiiii") == 24
