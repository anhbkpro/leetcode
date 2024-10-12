from heaps.kth_largest_element_in_a_stream import KthLargest


def test_kth_largest_element():
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
