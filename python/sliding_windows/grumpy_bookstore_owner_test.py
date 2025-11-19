from .grumpy_bookstore_owner import Solution


def test_grumpy_bookstore_owner():
    assert (
        Solution().maxSatisfied(
            customers=[1, 0, 1, 2, 1, 1, 7, 5],
            grumpy=[0, 1, 0, 1, 0, 1, 0, 1],
            minutes=3,
        )
        == 16
    )
    assert (
        Solution().maxSatisfied(customers=[4, 10, 10], grumpy=[1, 1, 0], minutes=2)
        == 24
    )
