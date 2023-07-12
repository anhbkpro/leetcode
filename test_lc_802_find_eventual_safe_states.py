from lc_802_find_eventual_safe_states import eventualSafeNodes


def test_eventual_safe_nodes():
    assert eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
