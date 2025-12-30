from .sum_of_square_numbers import Solution


def test_sum_of_square_numbers():
    assert Solution().judgeSquareSum(5)
    assert not Solution().judgeSquareSum(3)
    assert Solution().judgeSquareSum(4)
    assert Solution().judgeSquareSum(2)
