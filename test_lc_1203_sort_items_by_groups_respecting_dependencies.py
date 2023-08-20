from lc_1203_sort_items_by_groups_respecting_dependencies import Solution


def test_sort_items():
    assert Solution.sortItems(
        n=8,
        m=2,
        group=[-1, -1, 1, 0, 0, 1, 0, -1],
        beforeItems=[[],
                     [6],
                     [5],
                     [6],
                     [3, 6],
                     [],
                     [],
                     []]
    ) == [7, 0, 5, 2, 6, 3, 4, 1]
