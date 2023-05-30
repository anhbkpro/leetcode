from lc_705_design_hashset import MyHashSet


def test_hashset():
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    assert obj.contains(1) == True
    assert obj.contains(3) == False
    obj.add(2)
    assert obj.contains(2) == True
    obj.remove(2)
    assert obj.contains(2) == False
