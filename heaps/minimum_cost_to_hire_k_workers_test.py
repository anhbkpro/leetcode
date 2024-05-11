from heaps.minimum_cost_to_hire_k_workers import Solution


def test_minimum_cost_to_hire_k_workers():
    assert Solution().mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2) == 105.0
    rv = Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3)
    # round to 3 decimal places
    assert round(rv, 3) == 30.667
