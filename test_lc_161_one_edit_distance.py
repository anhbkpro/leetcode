from lc_161_one_edit_distance import Solution
solution = Solution()


def test_is_one_edit_distance():
    assert solution.is_one_edit_distance("ab", "acb") == True
