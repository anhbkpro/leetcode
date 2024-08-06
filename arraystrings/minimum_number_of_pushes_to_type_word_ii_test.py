from .minimum_number_of_pushes_to_type_word_ii import Solution


def test_minimum_pushes():
    solution = Solution()
    assert solution.minimumPushes(word = "abcde") == 5
    assert solution.minimumPushes(word = "xyzxyzxyzxyz") == 12
    assert solution.minimumPushes(word = "aabbccddeeffgghhiiiiii") == 24
