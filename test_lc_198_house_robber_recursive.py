from lc_198_house_robber_recursive import Solution

solution = Solution()


def test_rob():
    assert solution.rob([1, 2, 3, 1]) == 4
    assert solution.rob([2, 7, 9, 3, 1]) == 12
