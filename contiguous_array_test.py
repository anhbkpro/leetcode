from contiguous_array import Solution


def test_find_max_length():
    Solution().findMaxLength([0, 1]) == 2
    Solution().findMaxLength([0, 1, 0]) == 2
    Solution().findMaxLength([0, 1, 0, 1]) == 4
    Solution().findMaxLength([0, 1, 0, 1, 0]) == 4
    Solution().findMaxLength([0, 1, 0, 0, 0, 1, 1, 1]) == 6
