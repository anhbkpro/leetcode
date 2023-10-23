from lc_342_power_of_four import Solution

solution = Solution()


def test_is_power_of_four():
    assert solution.isPowerOfFour(num=16) is True
    assert solution.isPowerOfFour(num=5) is False
    assert solution.isPowerOfFour(num=1) is True
