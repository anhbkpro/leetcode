from lc_1611_minimum_one_bit_operations_to_make_integers_zero import Solution


def test_minimum_one_bit_operations():
    s = Solution()
    assert s.minimumOneBitOperations(n=3) == 2
    assert s.minimumOneBitOperations(n=6) == 4
