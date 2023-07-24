from lc_50_pow_x_n import Solution
s = Solution()


def test_binary_exp():
    assert s.binary_exp(2, 0) == 1
    assert s.binary_exp(2, 1) == 2
    assert s.binary_exp(2, 2) == 4
    assert s.binary_exp(2, -2) == 0.25

