from .find_kth_bit_in_nth_binary_string import Solution


def test_find_kth_bit_in_nth_binary_string():
    assert Solution().findKthBit(n=3, k=1) == "0"
    assert Solution().findKthBit(n=4, k=11) == "1"
