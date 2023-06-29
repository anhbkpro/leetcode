from lc_864_shortest_path_to_get_all_keys import shortestPathAllKeys


def test_shortest_path_all_keys():
    assert shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"]) == 8
    assert shortestPathAllKeys(["@..aA", "..B#.", "....b"]) == 6
