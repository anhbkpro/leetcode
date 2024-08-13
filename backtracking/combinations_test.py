from .combinations import Solution


def test_combine():
    # Input: n = 1, k = 1
    # Output: [[1]]
    solution = Solution()
    n = 1
    k = 1
    expected = [[1]]
    assert solution.combine(n, k) == expected
