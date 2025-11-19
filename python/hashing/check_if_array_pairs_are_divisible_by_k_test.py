from .check_if_array_pairs_are_divisible_by_k import Solution


def test_can_arrange():
    assert Solution().canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5) is True
    assert Solution().canArrange([1, 2, 3, 4, 5, 6], 7) is True
    assert Solution().canArrange([1, 2, 3, 4, 5, 6], 10) is False
