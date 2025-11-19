from .minimum_number_of_k_consecutive_bit_flips import Solution


def test_min_k_bit_flips():
    assert Solution().minKBitFlips([0, 1, 0], 1) == 2
    assert Solution().minKBitFlips([1, 1, 0], 2) == -1
