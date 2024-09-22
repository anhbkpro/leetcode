from .k_th_smallest_in_lexicographical_order import Solution


def test_k_th_smallest_in_lexicographical_order():
    assert Solution().findKthNumber(13, 2) == 10
    assert Solution().findKthNumber(13, 5) == 13
