from dp.n_th_tribonacci_number import Solution


def test_tribonacci():
    assert Solution().tribonacci(4) == 4
    assert Solution().tribonacci(25) == 1389537
