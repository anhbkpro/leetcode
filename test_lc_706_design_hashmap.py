from lc_706_design_hashmap import MyHashMap


def test_hashmap():
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    assert obj.get(3) == -1
    obj.put(2, 1)
    assert obj.get(2) == 1
    obj.remove(2)
    assert obj.get(2) == -1
