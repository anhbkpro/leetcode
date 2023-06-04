from lc_1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero import minReorder


def test_min_reorder():
    assert minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert minReorder(n=3, connections=[[1, 0], [2, 0]]) == 0
