from .combination_sum_ii import Solution


def test_combination_sum2():
    # Input: candidates = [10,1,2,7,6,1,5], target = 8
    # Output:
    # [
    # [1,1,6],
    # [1,2,5],
    # [1,7],
    # [2,6]
    # ]
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert solution.combinationSum2(candidates, target) == expected
