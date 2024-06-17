from .sum_of_square_numbers import Solution


def test_sum_of_square_numbers():
    assert Solution().judgeSquareSum(5) == True
    assert Solution().judgeSquareSum(3) == False
    assert Solution().judgeSquareSum(4) == True
    assert Solution().judgeSquareSum(2) == True
