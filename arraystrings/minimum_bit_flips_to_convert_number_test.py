from .minimum_bit_flips_to_convert_number import Solution


def test_min_bit_flips():
    assert Solution().minBitFlips(start = 10, goal = 7) == 3
    assert Solution().minBitFlips(start = 3, goal = 4) == 3
