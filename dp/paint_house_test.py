from .paint_house import Solution


def test_minCost():
    assert Solution().minCost(costs = [[17,2,17],[16,16,5],[14,3,19]]) == 10
    assert Solution().minCost(costs = [[7,6,2]]) == 2
