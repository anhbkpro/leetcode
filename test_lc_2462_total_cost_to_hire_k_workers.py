from lc_2462_total_cost_to_hire_k_workers import totalCost


def test_total_cost():
    assert totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4) == 11
    assert totalCost(costs=[1, 2, 4, 1], k=3, candidates=3) == 4
