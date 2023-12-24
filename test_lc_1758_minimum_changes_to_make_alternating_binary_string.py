from lc_1758_minimum_changes_to_make_alternating_binary_string import Solution

s = Solution()


def test_min_operations():
    assert s.minOperations(s="0100") == 1
    assert s.minOperations(s="10") == 0
    assert s.minOperations(s="1111") == 2
