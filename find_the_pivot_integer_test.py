from find_the_pivot_integer import Solution


def test_pivot_integer():
    assert Solution().pivotInteger(n=8) == 6
    assert Solution().pivotInteger(n=1) == 1
    assert Solution().pivotInteger(n=4) == -1
