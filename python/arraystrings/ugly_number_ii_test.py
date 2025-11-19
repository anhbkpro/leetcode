from .ugly_number_ii import Solution


def test_ugly_number():
    assert Solution().nthUglyNumber(10) == 12
    assert Solution().nthUglyNumber(1) == 1
    assert Solution().nthUglyNumber(2) == 2
    assert Solution().nthUglyNumber(3) == 3
    assert Solution().nthUglyNumber(4) == 4
    assert Solution().nthUglyNumber(5) == 5
    assert Solution().nthUglyNumber(6) == 6
    assert Solution().nthUglyNumber(7) == 8
    assert Solution().nthUglyNumber(8) == 9
    assert Solution().nthUglyNumber(9) == 10
