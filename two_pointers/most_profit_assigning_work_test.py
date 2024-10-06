from .most_profit_assigning_work import Solution


def test_most_profit_assigning_work():
    assert (
        Solution().maxProfitAssignment(
            difficulty=[2, 4, 6, 8, 10],
            profit=[10, 20, 30, 40, 50],
            worker=[4, 5, 6, 7],
        )
        == 100
    )
