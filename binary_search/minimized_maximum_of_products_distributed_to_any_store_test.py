from .minimized_maximum_of_products_distributed_to_any_store import Solution


def test_minimized_maximum_of_products_distributed_to_any_store():
    assert Solution().minimizedMaximum(n=6, quantities=[11, 6]) == 3
    assert Solution().minimizedMaximum(n=7, quantities=[15, 10, 10]) == 5
