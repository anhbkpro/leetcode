from lc_1578_minimum_time_to_make_rope_colorful import Solution


def test_min_cost():
    assert Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3
    assert Solution().minCost(colors="abc", neededTime=[1, 2, 3]) == 0
    assert Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2
