from .most_beautiful_item_for_each_query import Solution


def test_most_beautiful_item_for_each_query():
    assert Solution().maximumBeauty(
        items=[[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], queries=[1, 2, 3, 4, 5, 6]
    ) == [2, 4, 5, 5, 6, 6]
