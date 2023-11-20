from lc_2391_minimum_amount_of_time_to_collect_garbage import Solution


def test_garbage_collection():
    assert Solution.garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]) == 21
    assert Solution.garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10]) == 37
