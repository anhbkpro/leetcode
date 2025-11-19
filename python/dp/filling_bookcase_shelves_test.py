from .filling_bookcase_shelves import Solution


def test_min_height_shelves():
    assert (
        Solution().minHeightShelves(
            [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
        )
        == 6
    )
