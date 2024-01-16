from lc_380_insert_delete_getrandom_o1 import RandomizedSet

r = RandomizedSet()


def test_insert():
    r.insert(1)
    assert r.getRandom() == 1
    r.remove(2)
    r.insert(2)
    assert r.getRandom() in [1, 2]
    r.remove(1)
    r.insert(2)
    assert r.getRandom() == 2
