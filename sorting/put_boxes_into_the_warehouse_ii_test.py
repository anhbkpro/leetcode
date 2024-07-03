from .put_boxes_into_the_warehouse_ii import Solution


def test_max_boxes_in_warehouse():
    assert Solution().maxBoxesInWarehouse([4, 3, 4, 1], [5, 3, 3, 4, 1]) == 3
